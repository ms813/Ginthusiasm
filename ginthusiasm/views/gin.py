from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from ginthusiasm.models import Gin, TasteTag, Distillery, Review
from ginthusiasm.forms import GinSearchForm, AddGinForm, ReviewForm
from django.db.models import Q


from haystack.query import SearchQuerySet, SQ
from ginthusiasm_project.GoogleMapsAuth import api_keys
import shlex, json

# View for the main gin page
def show_gin(request, gin_name_slug):
    context_dict = {}

    try:
        # Try to find the gin name slug with the given name.
        gin = Gin.objects.get(slug=gin_name_slug)

        # Add the gin object to the context dictionary.
        context_dict['gin'] = gin

        # Grab the reviews on this gin
        reviews = gin.reviews.all()

        #### Map parameters ####
        if reviews:
            # 1 or more reviews, so create a list of coordinates
            coords = [{ 'lat' : r.lat, 'lng' : r.long } for r in reviews]
        else:
            # 0 reviews, so center map on distillery
            distillery = gin.distillery
            if distillery:
                coords = [{'lat': distillery.lat, 'lng': distillery.long}]
            else:
                # 0 reviews and 0 distilleries, use coords for the whole world
                coords = [
                    {'lat': 85, 'lng': -180},
                    {'lat': -85, 'lng': 180}
                ]

        # set the zoom level - if more than one marker the map script scales the map dynamically anyways
        context_dict['zoom'] = 16

        # coords must be well formed JSON so encode here
        context_dict['coords'] = json.dumps(coords)

        # Get reviews from the DB split by review type, so they will
        # be accessible in the template
        expert_reviews = reviews.filter(review_type=Review.EXPERT)
        user_reviews = reviews.filter(review_type=Review.BASIC)
        context_dict['expert_reviews'] = expert_reviews
        context_dict['other_reviews'] = user_reviews
        # print context_dict['expert_reviews']
        # print context_dict['other_reviews']

        if api_keys:
            context_dict['js_api_key'] = api_keys[0]

    except Gin.DoesNotExist:
        context_dict['gin'] = None

    if request.user.is_authenticated:
        context_dict['form'] = ReviewForm()
        add_review(request, gin_name_slug)


    # Render the response and return it to the client
    return render(request, 'ginthusiasm/gin_page.html', context=context_dict)


# View for adding a gin to the database
def add_gin(request, distillery_name_slug):
    try:
        distillery = Distillery.objects.get(slug=distillery_name_slug)
    except Distillery.DoesNotExist:
        distillery = None

    form = AddGinForm()

    if request.method == 'POST':
        form = AddGinForm(request.POST)
        if form.is_valid():
            if distillery:
                gin = form.save(commit=False)
                gin.distillery = distillery
                gin.average_rating = 0

                if 'image' in request.FILES:
                    gin.image = request.FILES['image']

                gin.save()
                form.save_m2m()
                return redirect('show_distillery', distillery_name_slug)
        else:
            print(form.errors)

    context_dict = {'add_gin_form': form, 'distillery': distillery}
    return render(request, 'ginthusiasm/add_gin_page.html', context=context_dict)



def rate_gin(request, gin_name_slug):
    if not request.user.is_anonymous():
        if request.method == 'POST':
            user_rating = request.POST.get('rating')
            if user_rating > 0 or user_rating <= 5:

                gin = Gin.objects.get(slug=gin_name_slug)
                userprofile = request.user.userprofile

                review, created = Review.objects.get_or_create(user=userprofile, gin=gin)

                review.rating = user_rating
                review.save()

                return HttpResponse('rated')
    else:
        return HttpResponse('unauthenticated')

    return HttpResponse('not rated')

# View for the gin search page
def gin_search_results(request):
    query_dict = request.GET
    gin_list = []

    # order by user defined ordering
    order_by = 'relevance'
    # if order_by is invalid default to ordering by gin name
    if query_dict.get('order_by') in dict(GinSearchForm.ORDER_BY_CHOICES):
        order_by = query_dict.get('order_by')

    # Execute filter query
    if query_dict.get('distillery') or query_dict.get('tags') or not query_dict.get('keywords'):
        gin_list = Gin.objects.filter(create_gin_query(query_dict))
    else:
        gin_list = gin_keyword_filter(query_dict.get('keywords'))
        gin_list = gin_list.filter(create_gin_query(query_dict))

    # Order search results
    if order_by != "relevance":
        gin_list = gin_list.order_by(order_by)

    # If there is only one result returned then redirect straight to that page
    if len(gin_list) == 1:
        return redirect('show_gin', gin_list[0].slug)

    # Remember values of form fields
    form = GinSearchForm(initial={
        'keywords': query_dict.get('keywords'),
        'min_price': query_dict.get('min_price'),
        'max_price': query_dict.get('max_price'),
        'min_rating': query_dict.get('min_rating'),
        'max_rating': query_dict.get('max_rating'),
        'order_by': query_dict.get('order_by'),
        'order': query_dict.get('order'),
    })

    if request.user.is_authenticated():
        for gin in gin_list:
            gin = add_user_ratings_to_gin(request.user, gin)

    context_dict = {'gins': gin_list, 'advanced_search_form': form}
    return render(request, 'ginthusiasm/gin_search_page.html', context=context_dict)

def add_user_ratings_to_gin(user, gin):

    user_review = gin.reviews.filter(user=user.userprofile)

    if len(user_review) > 0:
        gin.user_rating = user_review[0].rating
    else:
        gin.user_rating = 0

    print gin.user_rating

    return gin


# Function for generating a gin search query (Q() object) from a query dictionary
def create_gin_query(query_dict):
    queries = Q()

    # filter by price
    if query_dict.get('max_price'):
        queries.add(
            ~Q(price__gt=query_dict.get('max_price'))
            , Q.AND
        )
    if query_dict.get('min_price'):
        queries.add(
            ~Q(price__lt=query_dict.get('min_price'))
            , Q.AND
        )

    # filter by rating
    if query_dict.get('max_rating'):
        queries.add(
            ~Q(average_rating__gt=query_dict.get('max_rating'))
            , Q.AND
        )
    if query_dict.get('min_rating'):
        queries.add(
            ~Q(average_rating__lt=query_dict.get('min_rating'))
            , Q.AND
        )

    # filter by tag
    if query_dict.get('tags'):
        tags = shlex.split(query_dict.get('tags'))
        print tags
        tags_query = Q()
        for tag in tags:
            tags_query.add (
                Q(taste_tags__name__iexact=tag)
                , Q.OR
            )
        queries.add(tags_query, Q.AND)

    # filter by distillery
    if query_dict.get('distillery'):
        distilleries = shlex.split(query_dict.get('distillery').replace("+", " "))
        distilleries_query = Q()
        for distillery in distilleries:
            distilleries_query.add(
                Q(distillery__name__icontains=distillery)
                , Q.OR
            )
        queries.add(distilleries_query, Q.AND)

    return queries

# Filters gins by keywords, returns a QuerySet that can be further filtered
def gin_keyword_filter(search_text):
    if search_text:
        sqs = SearchQuerySet().models(Gin).auto_query(search_text)
    else:
        sqs = SearchQuerySet().models(Gin).all()

    primary_keys = []
    for gin in sqs:
        primary_keys.append(gin.pk)

    # From: codybonney.com/creating-a-queryset-from-a-list-while-presevering-order-using-django
    clauses = ' '.join(['WHEN id=%s THEN %s' % (pk, i) for i, pk in enumerate(primary_keys)])
    ordering = 'CASE %s END' % clauses

    return Gin.objects.filter(pk__in=primary_keys).extra(select={'ordering': ordering}, order_by=('ordering',))

def gin_keyword_filter_autocomplete(request):
    if request.method == 'POST':
        print request.POST
        search_text = request.POST.get('search_text')

        gins = SearchQuerySet().autocomplete(content_auto=search_text)[:5]

        context_dict = {'gins': gins}
        return render_to_response('ginthusiasm/ajax_search.html', context=context_dict)
    else:
        return redirect('gin_search_results')


def add_review(request, gin_name_slug):

    gin = Gin.objects.get(slug=gin_name_slug)
    author = request.user.userprofile

    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(data=request.POST)
        response_data={}

        if form.is_valid():
            if gin:
                if author:
                    review = form.save(commit=False)
                    review.gin = gin
                    review.user = author
                    review.review_type = author.user_type
                    review.save()

                    response_data['result'] = 'Create post successful'
                    return HttpResponse(
                        json.dumps(response_data),
                        content_type="application/json"
                    )

        else:
            print(form.errors)

    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
        
    return render_to_response('ginthusiasm/add_review_widget.html', {'form':form, 'gin':gin })

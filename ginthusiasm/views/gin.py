from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ginthusiasm.models import Gin, Distillery, Review, UserProfile
from ginthusiasm.forms import GinSearchForm, AddGinForm, ReviewForm
from distillery import show_distillery
from django.db.models import Q
from haystack.query import SearchQuerySet
from ginthusiasm_project.GoogleMapsAuth import api_keys
from map_helper import MapHelper
import json
import shlex

"""
This file handles creating, displaying and rating the Gin model
"""


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

        # Map parameters
        if reviews:
            # 1 or more reviews, so create a list of coordinates
            coords = [{'lat': r.lat, 'lng': r.lng} for r in reviews]
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
        # an expert is anyone that is not a BASIC user
        context_dict['expert_reviews'] = reviews.filter(~Q(user__user_type=UserProfile.BASIC))
        context_dict['other_reviews'] = reviews.filter(user__user_type=UserProfile.BASIC)

        if api_keys:
            context_dict['js_api_key'] = api_keys[0]

    except Gin.DoesNotExist:
        context_dict['gin'] = None

    # Add the review form to the template if the user is logged in
    if request.user.is_authenticated:
        # check if the user has already written a review and populate the form with it
        review = gin.reviews.filter(user=request.user.userprofile).first()
        if review:
            initial_data = {
                "date": review.date,
                "rating": review.rating,
                "content": review.content,
                "lat": review.lat,
                "lng": review.lng,
            }
            context_dict['form'] = ReviewForm(initial=initial_data)
        else:
            context_dict['form'] = ReviewForm()

        add_review(request, gin_name_slug)

    # Render the response and return it to the client
    return render(request, 'ginthusiasm/gin_page.html', context=context_dict)


# View for adding a gin to the database
@login_required
def add_gin(request, distillery_name_slug):
    try:
        distillery = Distillery.objects.get(slug=distillery_name_slug)
    except Distillery.DoesNotExist:
        distillery = None

    form = AddGinForm()

    # Check that the user is logged in, send them to the distillery page
    if request.user.is_anonymous():
        return show_distillery(request, distillery_name_slug)

    # and is either the distillery owner or an admin
    is_admin = request.user.userprofile.user_type == UserProfile.ADMIN
    owns_distillery = request.user.userprofile == distillery.owner

    # if the user doesnt have privileges, send them to the distillery page
    if not (is_admin or owns_distillery):
        return show_distillery(request, distillery_name_slug)

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
    return render(request, 'ginthusiasm/add_gin_page.html',
                  context=context_dict)


# Creates or updates a review for the specified gin with a user rating
# Note this view should be called using AJAX, so it passes back a status string as a HttpResponse
def rate_gin(request, gin_name_slug):
    # check the user is logged in
    if not request.user.is_anonymous():
        if request.method == 'POST':

            # grab the user rating from the POST data
            user_rating = request.POST.get('rating')

            # check the rating is within the allowed bounds (1-5)
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
# Returns a list of all gins by default
def gin_search_results(request):
    query_dict = request.GET

    # order by user defined ordering, default = relevance
    order_by = GinSearchForm.RELEVANCE

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

    # attach the user's saved ratings to each gin to be displayed
    if request.user.is_authenticated():
        for gin in gin_list:
            add_user_ratings_to_gin(request.user, gin)

    context_dict = {'gins': gin_list, 'advanced_search_form': form}
    return render(request, 'ginthusiasm/gin_search_page.html', context=context_dict)


# helper function that gets the user's stored rating for a gin if it exists
def add_user_ratings_to_gin(user, gin):
    user_review = gin.reviews.filter(user=user.userprofile)

    if len(user_review) > 0:
        gin.user_rating = user_review[0].rating
    else:
        gin.user_rating = 0

    return gin


# Function for generating a gin search query (Q() object) from a query dictionary
def create_gin_query(query_dict):
    queries = Q()

    # filter by price
    if query_dict.get('max_price'):
        queries.add(
            ~Q(price__gt=query_dict.get('max_price')),
            Q.AND
        )
    if query_dict.get('min_price'):
        queries.add(
            ~Q(price__lt=query_dict.get('min_price')),
            Q.AND
        )

    # filter by rating
    if query_dict.get('max_rating'):
        queries.add(
            ~Q(average_rating__gt=query_dict.get('max_rating')),
            Q.AND
        )
    if query_dict.get('min_rating'):
        queries.add(
            ~Q(average_rating__lt=query_dict.get('min_rating')),
            Q.AND
        )

    # filter by tag
    if query_dict.get('tags'):
        tags = shlex.split(query_dict.get('tags'))
        tags_query = Q()
        for tag in tags:
            tags_query.add(
                Q(taste_tags__name__iexact=tag),
                Q.OR
            )
        queries.add(tags_query, Q.AND)

    # filter by distillery
    if query_dict.get('distillery'):
        distilleries = query_dict.get('distillery').replace("+", " ").split()
        distilleries_query = Q()
        for distillery in distilleries:
            distilleries_query.add(
                Q(distillery__name__icontains=distillery),
                Q.OR
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


# Filters gin by keyword, auto-completing via AJAX as the user types
def gin_keyword_filter_autocomplete(request):
    if request.method == 'POST':
        search_text = request.POST.get('search_text')

        # get the top 5 matching gins
        gins = SearchQuerySet().autocomplete(content_auto=search_text)[:5]

        context_dict = {
            'results': [{
                'name': gin.object.name,
                'slug': gin.object.slug,
            } for gin in gins],
            'show_url': 'show_gin'
        }
        return render_to_response('ginthusiasm/ajax_search.html', context=context_dict)
    else:
        return redirect('gin_search_results')


@login_required
def add_review(request, gin_name_slug):
    gin = Gin.objects.get(slug=gin_name_slug)
    author = request.user.userprofile

    if request.method == 'POST':
        form = ReviewForm(data=request.POST)
        response_data = {}

        ## Catherine - add postcode from review form here
        #postcode = "G117PY"
        #mh = MapHelper()
        #geodata = mh.postcodeToLatLng(postcode)
        # {'lat' : x, 'lng' : y}

        if form.is_valid():
            if gin and author:
                # Get or create the review for this gin-author pair
                review, created = Review.objects.get_or_create(user=author, gin=gin)
                review.gin = gin
                review.user = author
                review.content = form.cleaned_data.get('content')
                review.rating = form.cleaned_data.get('rating')
                review.review_type = author.user_type
                review.date = form.cleaned_data.get('date')
                review.lat = form.cleaned_data.get('lat')
                review.lng = form.cleaned_data.get('lng')

                if form.cleaned_data.get('postcode') == "":
                    print("The postcode is empty")
                    review.lat = form.cleaned_data.get('lat')
                    review.lng = form.cleaned_data.get('lng')

                else:
                    print("The postcode is not empty")
                    print(form.cleaned_data.get('postcode'))
                    review.postcode = form.cleaned_data.get('postcode')
                    mh = MapHelper()
                    geodata = mh.postcodeToLatLng(review.postcode)
                    review.lng = geodata.get('lng')
                    review.lat = geodata.get('lat')



                review.save()
                response_data['result'] = 'Create review successful'
                return HttpResponse(
                    json.dumps(response_data),
                    content_type="application/json"
                )

        else:
            print(form.errors)

    else:
        # GET request, probably when rendering a Gin large page
        pass
        #return render(request, 'ginthusiasm/add_review_widget.html', {'form': form, 'gin': gin})

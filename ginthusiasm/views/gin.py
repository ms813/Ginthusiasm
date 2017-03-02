from django.shortcuts import render, redirect
from django.http import HttpResponse
from ginthusiasm.models import Gin, TasteTag, Distillery, Review
from ginthusiasm.forms import GinSearchForm, AddGinForm
from django.db.models import Q
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
        user_reviews = reviews.filter(review_type=Review.USER)
        context_dict['expert_reviews'] = expert_reviews
        context_dict['other_reviews'] = user_reviews
        # print context_dict['expert_reviews']
        # print context_dict['other_reviews']

        if api_keys:
            context_dict['js_api_key'] = api_keys[0]

    except Gin.DoesNotExist:
        context_dict['gin'] = None

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


# View for the gin search page
def gin_search_results(request):
    query_dict = request.GET

    # order by user defined ordering
    order_by = 'name'
    # if order_by is invalid default to ordering by gin name
    if query_dict.get('order_by') in dict(GinSearchForm.ORDER_BY_CHOICES):
        order_by = query_dict.get('order_by')

    # The order defaults to ascending
    if query_dict.get('order') == 'DESC':
        order_by = '-' + order_by

    # Execute filter query
    gin_list = Gin.objects.filter(create_gin_query(query_dict)).distinct().order_by(order_by)

    # If there is only one result returned then redirect straight to that page
    if len(gin_list) == 1:
        return redirect('show_gin', gin_list[0].slug)

    # Remember values of form fields
    form = GinSearchForm(initial={
        'keywords': query_dict.get('keywords'),
        'distillery': query_dict.get('distillery'),
        'min_price': query_dict.get('min_price'),
        'max_price': query_dict.get('max_price'),
        'min_rating': query_dict.get('min_rating'),
        'max_rating': query_dict.get('max_rating'),
        'order_by': query_dict.get('order_by'),
        'order': query_dict.get('order'),
    })

    context_dict = {'gins': gin_list, 'advanced_search_form': form}
    return render(request, 'ginthusiasm/gin_search_page.html', context=context_dict)


# Function for generating a gin search query (Q() object) from a query dictionary
def create_gin_query(query_dict):
    queries = Q()

    # filter by keywords
    if query_dict.get('keywords'):
        keywords = shlex.split(query_dict.get('keywords').replace("+", " "))
        keyword_query = Q()
        for keyword in keywords:
            keyword_query.add(
                Q(name__icontains=keyword) |
                Q(short_description__icontains=keyword) |
                Q(long_description__icontains=keyword) |
                Q(taste_tags__name__icontains=keyword) |
                Q(distillery__name__icontains=keyword)
                , Q.OR
            )
        queries.add(keyword_query, Q.AND)

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
        tags = shlex.split(query_dict.get('tags').replace("+", " "))
        tags_query = Q()
        for tag in tags:
            tags_query.add(
                Q(taste_tags__name__icontains=tag)
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

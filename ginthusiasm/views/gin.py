from django.shortcuts import render, redirect
from django.http import HttpResponse
from ginthusiasm.models import Gin, TasteTag, Distillery
from ginthusiasm.forms import GinSearchForm, AddGinForm
from django.db.models import Q
from haystack.query import SearchQuerySet, SQ
import shlex

# View for the main gin page
def show_gin(request, gin_name_slug):
    context_dict = {}

    try:
        # Try to find the gin name slug with the given name.
        gin = Gin.objects.get(slug=gin_name_slug)

        # Add the gin object to the context dictionary.
        context_dict['gin'] = gin
        context_dict['expert_reviews'] = ['expert_reviews']
        context_dict['other_reviews'] = ['other_reviews']

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

    # Execute filter query
    gin_list = gin_keyword_filter(query_dict.get('keywords'))
    gin_list = gin_list.filter(create_gin_query(query_dict))#.order_by(order_by)

    # If there is only one result returned then redirect straight to that page
    if gin_list.count() == 1:
        return redirect('show_gin', gin_list[0].object.slug)

    # Remember values of form fields
    form = GinSearchForm(initial={
        'keywords' : query_dict.get('keywords'),
        'distillery' : query_dict.get('distillery'),
        'min_price' : query_dict.get('min_price'),
        'max_price' : query_dict.get('max_price'),
        'min_rating' : query_dict.get('min_rating'),
        'max_rating' : query_dict.get('max_rating'),
        'order_by' : query_dict.get('order_by'),
        'order' : query_dict.get('order'),
    })

    context_dict = {'gins': gin_list, 'advanced_search_form': form}
    return render(request, 'ginthusiasm/gin_search_page.html', context=context_dict)

# Function for generating a gin search query (Q() object) from a query dictionary
def create_gin_query(query_dict):
    queries = SQ()

    # filter by price
    if query_dict.get('max_price'):
        queries.add (
            ~SQ(price__gt=query_dict.get('max_price'))
            , SQ.AND
        )
    if query_dict.get('min_price'):
        queries.add (
            ~SQ(price__lt=query_dict.get('min_price'))
            , SQ.AND
        )

    # filter by rating
    if query_dict.get('max_rating'):
        queries.add (
            ~SQ(average_rating__gt=query_dict.get('max_rating'))
            , SQ.AND
        )
    if query_dict.get('min_rating'):
        queries.add (
            ~SQ(average_rating__lt=query_dict.get('min_rating'))
            , SQ.AND
        )

    # filter by tag
    if query_dict.get('tags'):
        tags = shlex.split(query_dict.get('tags'))
        print tags
        tags_query = SQ()
        for tag in tags:
            tags_query.add (
                SQ(taste_tags__name__iexact=tag)
                , SQ.OR
            )
        queries.add(tags_query, Q.AND)

    # filter by distillery
    if query_dict.get('distillery'):
        distilleries = shlex.split(query_dict.get('distillery').replace("+", " "))
        distilleries_query = SQ()
        for distillery in distilleries:
            distilleries_query.add (
                SQ(distillery__name__icontains=distillery)
                , SQ.OR
            )
        queries.add(distilleries_query, Q.AND)

    print queries
    return queries

def gin_keyword_filter(search_text):
    if search_text:
        sqs = SearchQuerySet().models(Gin).auto_query(search_text)
    else:
        sqs = SearchQuerySet().models(Gin).all()

    return sqs

def gin_keyword_filter_autocomplete(request):
    print nothing

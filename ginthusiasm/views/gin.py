from django.shortcuts import render, redirect
from django.http import HttpResponse
from ginthusiasm.models import Gin, TasteTag
from ginthusiasm.forms import AdvancedSearchForm
from django.db.models import Q

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

# View for the gin search page
def gin_search_results(request):
    query_dict = request.GET

    print query_dict
    queries = Q()

    # Build filter query
    if query_dict.get('keywords'):
        print ("Keywords")
        queries.add (
            Q(name__icontains=query_dict.get('keywords')) |
            Q(short_description__icontains=query_dict.get('keywords')) |
            Q(long_description__icontains=query_dict.get('keywords')) |
            Q(taste_tags__name__icontains=query_dict.get('tags'))
            , Q.AND
        )
    if query_dict.get('max_price'):
        print ("Max Price")
        queries.add (
            ~Q(price__gt=query_dict.get('max_price'))
            , Q.AND
        )
    if query_dict.get('min_price'):
        print ("Min Price")
        queries.add (
            ~Q(price__lt=query_dict.get('min_price'))
            , Q.AND
        )
    if query_dict.get('max_rating'):
        print ("Max Rating")
        queries.add (
            ~Q(average_rating__gt=query_dict.get('max_rating'))
            , Q.AND
        )
    if query_dict.get('min_rating'):
        print ("Min Rating")
        queries.add (
            ~Q(average_rating__lt=query_dict.get('min_rating'))
            , Q.AND
        )
    if query_dict.get('tags'):
        print ("Tags")
        queries.add (
            Q(taste_tags__name__icontains=query_dict.get('tags'))
            , Q.AND
        )

    print queries
    # order by user defined ordering
    order_by = 'name'
    # if order_by is invalid default to ordering by gin name
    if query_dict.get('order_by') in dict(AdvancedSearchForm.ORDER_BY_CHOICES):
        order_by = query_dict.get('order_by')

    # The order defaults to ascending
    if query_dict.get('order') == 'DESC':
        order_by = '-' + order_by


    # Execute filter query
    gin_list = Gin.objects.filter(queries).order_by(order_by)

    # If there is only one result returned then redirect straight to that page
    if len(gin_list) == 1:
        return redirect('show_gin', gin_list[0].slug)

    context_dict = {'gins': gin_list, 'advanced_search_form': AdvancedSearchForm()}

    return render(request, 'ginthusiasm/gin_search_page.html', context=context_dict)

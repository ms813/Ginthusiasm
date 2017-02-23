from django.shortcuts import render
from django.http import HttpResponse
from ginthusiasm.models import Gin
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

    except Gin.DoesNotExist:
        context_dict['gin'] = None

    # Render the response and return it to the client
    return render(request, 'ginthusiasm/gin_page.html', context=context_dict)

def gin_search_results(request):
    query_dict = request.GET

    print query_dict
    queries = Q()

    # Build filter query
    if query_dict.get('keywords'):
        queries.add
        (
            (
                Q(name__icontains=query_dict.get('keywords')) |
                Q(short_description__icontains=query_dict.get('keywords')) |
                Q(long_description__icontains=query_dict.get('keywords'))
            ), Q.AND
        )
    if query_dict.get('max_price'):
        queries.add
        (
            (
                Q(price__lt=query_dict.get('max_price')) |
                Q(price=query_dict.get('max_price'))
            ), Q.AND
        )
    if query_dict.get('min_price'):
        queries.add
        (
            (
                Q(price__gt=query_dict.get('min_price')) |
                Q(price=query_dict.get('min_price'))
            ), Q.AND
        )

    order_by = ''
    # The order defaults to ascending
    if query_dict.get('order') == 'DESC':
        order_by = '-'

    if query_dict.get('order_by'):
        order_by += query_dict.get('order_by')

    # Execute filter query
    gin_list = Gin.objects.filter(queries).order_by(order_by)

    context_dict = {'gins': gin_list, 'advanced_search_form': AdvancedSearchForm()}

    return render(request, 'ginthusiasm/gin_search_page.html', context=context_dict)

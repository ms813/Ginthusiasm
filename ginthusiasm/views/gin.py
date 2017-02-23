from django.shortcuts import render
from django.http import HttpResponse
from ginthusiasm.models import Gin
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

    query = Q(price__gt=30.00)

    gin_list = Gin.objects.filter(query).order_by('-average_rating')

    context_dict = {'gins': gin_list}

    return render(request, 'ginthusiasm/gin_search_page.html', context=context_dict)

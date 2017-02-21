from django.shortcuts import render
from django.http import HttpResponse
from ginthusiasm.models import Gin

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
    return HttpResponse("Gin page loaded. " + gin.name)

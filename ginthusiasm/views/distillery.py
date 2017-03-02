from django.shortcuts import render, redirect
from ginthusiasm.models import Distillery
from ginthusiasm.forms import DistillerySearchForm
from django.db.models import Q
from ginthusiasm.views import MapHelper

from ginthusiasm_project.GoogleMapsAuth import api_keys

# MS - to encode map coords
import json

# View for the main distillery page
def show_distillery(request, distillery_name_slug):
    # Dictionary for key & value pairs, which are then passed to the HTML template
    # by the render function.
    context_dict = {}

    try:
        # Find the distillery by querying the DB with the name slug. As
        # slug is unique, should only return one distillery.
        distillery = Distillery.objects.get(slug=distillery_name_slug)

        # Add the found distillery object to the context dictionary.
        # 'distillery' = key, distillery = found distillery object.
        context_dict['distillery'] = distillery

        # MS - interactive map code
        #########################################################
        # add the map parameters to the context dictionary
        coords = { 'lat' : distillery.lat, 'lng' : distillery.long }

        # note the coords must be well formed json to be correctly interpreted on the client slide
        # hence the need to json encode here
        context_dict['coords'] = json.JSONEncoder().encode(coords)
        context_dict['zoom'] = 16

        # grab our Google maps API key and pass it along with the context
        # add the api key if we have one
        if len(api_keys) > 0:
            context_dict['js_api_key'] = api_keys[0]
        #########################################################

    except Distillery.DoesNotExist:
        context_dict['distillery'] = None

    # Render the response and return it to the client
    return render(request, 'ginthusiasm/distillery_page.html', context=context_dict)

def distillery_search_results(request):
    query_dict = request.GET
    print query_dict

    # Execute query
    distillery_list=[]
    if query_dict.get('distillery_name'):
        distillery_list = Distillery.objects.filter(name__icontains=query_dict['distillery_name'])
        print distillery_list

    # If there is only one result returned then redirect straight to that page
    if len(distillery_list) == 1:
        return redirect('show_distillery', distillery_list[0].slug)

    context_dict = {'distilleries': distillery_list, 'advanced_search_form': DistillerySearchForm()}

    return render(request, 'ginthusiasm/distillery_search_page.html', context=context_dict)

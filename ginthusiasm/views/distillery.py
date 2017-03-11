from django.shortcuts import render, redirect
from ginthusiasm.models import Distillery
from ginthusiasm.forms import DistillerySearchForm

from ginthusiasm_project.GoogleMapsAuth import api_keys

import json

"""
This file contains views related to the Distillery model, including searching by distillery
"""


# View for the main distillery page
def show_distillery(request, distillery_name_slug):
    context_dict = {}

    try:
        # Find the distillery by querying the DB with the name slug. As
        # slug is unique, should only return one distillery.
        distillery = Distillery.objects.get(slug=distillery_name_slug)

        # Add the found distillery object to the context dictionary.
        # 'distillery' = key, distillery = found distillery object.
        context_dict['distillery'] = distillery

        # add the map parameters to the context dictionary
        coords = {'lat': distillery.lat, 'lng': distillery.long}

        # note the coords must be well formed json to be correctly interpreted on the client slide
        context_dict['coords'] = json.dumps(coords)
        context_dict['zoom'] = 16

        # add the api key if we have one
        if len(api_keys) > 0:
            context_dict['js_api_key'] = api_keys[0]

    except Distillery.DoesNotExist:
        context_dict['distillery'] = None

    # Render the response and return it to the client
    return render(request, 'ginthusiasm/distillery_page.html', context=context_dict)


# handles searching for distilleries from the main search widget
def distillery_search_results(request):
    query_dict = request.GET

    # Execute query
    distillery_list = []
    if query_dict.get('distillery_name'):
        distillery_list = Distillery.objects.filter(name__icontains=query_dict['distillery_name'])
    else:
        distillery_list = Distillery.objects.all()

    # If there is only one result returned then redirect straight to that page
    if len(distillery_list) == 1:
        return redirect('show_distillery', distillery_list[0].slug)

    context_dict = {'distilleries': distillery_list, 'advanced_search_form': DistillerySearchForm()}

    return render(request, 'ginthusiasm/distillery_search_page.html', context=context_dict)

from django.shortcuts import render
from ginthusiasm.views import MapHelper
from ginthusiasm_project.GoogleMapsAuth import api_keys

# to encode map coords
import json

def maptest(request):
    mh = MapHelper()
    lat = 55.871873
    lng = -4.288336
    zoom = 16
    coords = { 'lat' : lat, 'lng' : lng }
    single_marker_url = mh.getStaticMapUrl(coords=coords, zoom=zoom)

    multi_coords = [
        { 'lat' : lat, 'lng' : lng },
        { 'lat' : lat + 0.01, 'lng' : lng + 0.01},
        { 'lat' : lat - 0.015, 'lng' : lng + 0.04},
    ]

    multi_marker_url = mh.getStaticMapUrl(coords=multi_coords)

    context = {
        # for the static map
        'single_marker_map_url' : single_marker_url,
        'multi_marker_map_url' : multi_marker_url,

        # params for the dynamic js map
        'coords' : json.JSONEncoder().encode(multi_coords),
        'zoom' : zoom,
    }

    # add the api key if we have one
    if len(api_keys ) > 0:
        context['js_api_key'] = api_keys[0]

    return render(request, 'ginthusiasm/maptest.html', context)

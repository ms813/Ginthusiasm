from django.shortcuts import render
from ginthusiasm.views import MapHelper
from ginthusiasm_project.GoogleMapsAuth import api_keys

def maptest(request):
    mh = MapHelper()
    lat = 55.871873
    lng = -4.288336
    zoom = 16
    url = mh.getStaticMapUrl(lat, lng, zoom=zoom)

    context = {
        # for the static map
        'map_url' : url,

        # params for the dynamic js map
        'lat' : lat,
        'lng' : lng,
        'zoom' : zoom,
    }

    # add the api key if we have one
    if len(api_keys ) > 0:
        context['js_api_key'] = api_keys[0]

    return render(request, 'ginthusiasm/maptest.html', context)

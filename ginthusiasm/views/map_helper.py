from ginthusiasm_project.GoogleMapsAuth import api_keys
import requests

"""
Helper class to build static Google Maps urls

Glasgow Uni main building: 55.871873, -4.288336, zoom 16 is good
"""
class MapHelper:

    def __init__(self):
        self.urls = {
            'static' : 'https://maps.googleapis.com/maps/api/staticmap',
            'geodata' : 'http://maps.googleapis.com/maps/api/geocode/',
        }

        # See https://developers.google.com/maps/documentation/static-maps/intro
        # for a full list of params
        params = {
            # zoom factor:
                # 7 ~ whole of Scotland
                # 13 ~ whole of Glasgow
                # 18 ~ main building of Glasgow Uni
            'zoom' : '16',

            'size' : '640x640',      # size takes the form '{width}x{height}' in px
            'scale' : 1,         # set as 2 for higher resolution
            'maptype' : 'hybrid'    # roadmap | satellite | hybrid | terrain
        }

        self.default_params = params

    # coords should be either a single {lat, lng} pair, or a list of [{lat, lng}] pairs
    def getStaticMapUrl(self, coords, **kwargs):

        map_url = self.urls['static']+ '?'

        # copy the default parameters
        map_params = self.default_params.copy()

        # build the markers part of the url
        markers = "markers="
        if isinstance(coords, dict):
            # only one set of coords specified
            markers = markers + str(coords.get('lat'))+ ',' + str(coords.get('lng')) + '&'
        else:
            # multiple markers, separated by |
            del map_params['zoom']
            for p in coords:
                markers = markers + str(p.get('lat'))+ ',' + str(p.get('lng')) + '|'
            markers = markers + '&'

        map_url = map_url + markers

        # update or add any values passed as optional kwargs
        if kwargs is not None:
            for k,v in kwargs.iteritems():
                map_params[k] = v

        # build the URL by concatenating key-value pairs
        for k,v in map_params.iteritems():
            map_url = map_url + k + '=' + str(v) + '&'

        # add the API key if we have one
        if len(api_keys) > 0:
            map_url = map_url + "key=" + api_keys[0]
        else:
            # if no api key, trim the trailing ampersand
            map_url = map_url[:-1]

        return map_url

    # Get the center lat and long from a postcode using google geocoding
    def postcodeToLatLng(self, postcode):
        # see https://developers.google.com/maps/documentation/geocoding/intro
        postcode = postcode.replace(" ", "")
        url = self.urls['geodata'] + 'json?address=' + postcode;        

        response = requests.get(url).json()

        results = response['results']
        for r in results:
            check_postcode = r.get('address_components')[0].get('long_name').replace(" ", "")
            if check_postcode == postcode:
                bounds = r.get('geometry').get('bounds')
                print(bounds)

                ne = bounds.get('northeast')
                sw = bounds.get('southwest')

                mid = {
                    'lat' : (ne['lat'] - sw['lat']) / 2 + sw['lat'],
                    'lng' : (ne['lng'] - sw['lng']) / 2 + sw['lng']
                }

                return mid
        return None


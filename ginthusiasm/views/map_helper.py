from ginthusiasm_project.GoogleMapsAuth import api_keys

# Glasgow Uni main building: 55.871873, -4.288336, zoom 16 is good

class MapHelper:

    def __init__(self):
        self.urls = {
            'static' : 'https://maps.googleapis.com/maps/api/staticmap'
        }

        # See https://developers.google.com/maps/documentation/static-maps/intro
        # for a full list of params
        params = {
            # zoom factor:
                # 7 ~ whole of Scotland
                # 13 ~ whole of Glasgow
                # 18 ~ main building of Glasgow Uni
            'zoom' : '16',

            'width' : 640,      # width in px
            'height' : 640,     # height in px
            'scale' : 1,         # set as 2 for higher resolution
            'maptype' : 'hybrid'    # roadmap | satellite | hybrid | terrain
        }

        # size takes the form '{width}x{height}'
        params['size'] = str(params['width']) + 'x' + str(params['height'])
        self.default_params = params

    def getStaticMapUrl(self, lat, lng, **kwargs):
        # set the center of the map to lat,lng
        center_coords = str(lat)+ ',' + str(lng)
        map_url = self.urls['static'] + '?center=' + center_coords +'&'

        # copy the default parameters
        map_params = self.default_params.copy()

        #place a marker, with custom attributes if specified, or default red if not
        marker = kwargs.get('marker')
        if marker:
            c = marker.get('color') # named color or hex 0x######
            size = marker.get('size') # tiny | mid | small

            # remove the marker from the args list so it isnt added again
            del kwargs['marker']
        else:
            c = 'red'
            size = ''
        map_url = map_url + 'markers=color:' + c + '%7Csize:' + size + '%7C' + center_coords + '&'

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

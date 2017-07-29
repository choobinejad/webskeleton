import googlemaps
from webskeleton.connections.serializers import echo_serializer as serializer


class GoogleMaps(object):

    def __init__(self, config, api_key_file):

        with open(api_key_file, 'r') as key:
            self.gmaps = googlemaps.Client(key=key.read()[:-1])
        self.config = config

    def geocode_query(self, text):
        return self.gmaps.geocode(text)

    def places_nearby(self, location):
        return self.gmaps.places_nearby(location)

    def run(self):
        results = dict()
        results['geocode'] = self.geocode_query()
        results['places_nearby'] = self.places_nearby()
        return serializer(results)

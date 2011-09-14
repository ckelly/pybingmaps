import unittest
import random
from time import sleep
import os

from bingmaps import *

class BingMapsTestError(Exception):
    """Bing Maps test exception"""

    def __init__(self, reason):
        self.reason = unicode(reason)

    def __str__(self):
        return self.reason

# TODO: enter your key for testing
api_key = ''

class DirectionsTests(unittest.TestCase):
    def setUp(self):
        self.api = BingMapsAPI(api_key=api_key)
        
    def testBasicNav(self):
        # start - 717 Market St
        # end  - Ferry Plaza, San Francisco, CA
        
        # we shrunk the precision to match return values for easier comparison
        start_lat = "37.786861"
        start_lon = "-122.403689"
        end_lat = "37.795556"
        end_lon = "-122.392124"
        
        start = start_lat+","+start_lon
        end = end_lat+","+end_lon
        
        ret = self.api.routes(waypoints=[start, end])
        
        # verify start and end points are reflected in response
        self.assertNotEqual(ret, {})
        estimated_total = ret['resourceSets'][0]['estimatedTotal']
        
        self.assertEqual(estimated_total, 1)

        routeLegs = ret['resourceSets'][0]['resources'][0]['routeLegs']
        self.assertEqual(len(routeLegs), 1)
        
        itinerary_items = routeLegs[0]['itineraryItems']
        self.assertNotEqual(itinerary_items, [])

        # skip the last step, as it doesn't have a transport Mode
        for i in itinerary_items:
            self.assertEqual(i['details'][0]['mode'], 'Driving')

        
    def testPedestrianNav(self):
        start_lat = "37.7868609332517"
        start_lon = "-122.403689949149"
        end_lat = "37.795556930015"
        end_lon = "-122.392124051039"

        start = start_lat+","+start_lon
        end = end_lat+","+end_lon

        ret = self.api.routes(waypoints=[start,end], travelMode='Walking')
        self.assertNotEqual(ret, {})
        
        legs = ret['resourceSets'][0]['resources'][0]['routeLegs']
        self.assertNotEqual(legs, [])
        
        legs = legs[0]
        
        itinerary_items = legs['itineraryItems']
        self.assertNotEqual(itinerary_items, [])
        
        # skip the last step, as it doesn't have a transport Mode
        for i in itinerary_items:
            self.assertEqual(i['details'][0]['mode'], 'Walking')
        
if __name__ == '__main__':
    unittest.main()
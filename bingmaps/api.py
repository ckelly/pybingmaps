# Pybingmaps
# Copyright 2011 Lumatic, Inc
# See LICENSE for details.

import os

from bingmaps.binder import bind_api
from bingmaps.parsers import JSONParser
from bingmaps.utils import import_simplejson
from bingmaps.auth import KeyAuthHandler
json = import_simplejson()


class BingMapsAPI(object):
    '''Bing Maps API'''
    
    def __init__(self,
            host='dev.virtualearth.net', api_key=None,
            retry_count=0, retry_errors=None, retry_delay=0,
            parser=None):
            # short circuit this for now, change if we need Oauth, etc later
        self.host = host
        self.retry_count = retry_count
        self.retry_delay = retry_delay
        self.retry_errors = retry_errors
        self.parser = parser or JSONParser()
        self.api_key = api_key

        # no need to have user init this separately, so do it for them
        if self.api_key:
            self.auth = KeyAuthHandler(api_key=self.api_key)
        else:
            self.auth = None

    # Bing Maps method calls

    # directions
    # from is a reserved word, but we need to pass it in. This should do it
    def routes(self, waypoints, travelMode='Driving', version='v1', *args, **kargs):
        # update routes to waypoint values
        for count in xrange(0, len(waypoints)):
            kargs['wp.%d' % count] = waypoints[count]

        # we're excluding format as we're only handling JSON
        return bind_api(
        path = '/REST/{version}/Routes/{travelMode}',
        allowed_param = ['avoid', 'distanceBeforeFirstTurn', 'heading', 'optimize',
         'routePathOutput', 'tolerances', 'distanceUnit', 'dateTime', 
         'timeType', 'maxSolutions', 'suppressStatus', 'jsonp', 'output',
         'jsonso', 'culture', 'mapView', 'userLocation', 'userIp'] + ["wp.%d" % x for x in xrange(0,25)]
    )(self, version=version, travelMode=travelMode, output='json', *args, **kargs)


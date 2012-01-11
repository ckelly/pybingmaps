# Pybingmaps
# Copyright 2011 Lumatic, Inc
# See LICENSE for details.


class BingMapsError(Exception):
    """Bing Maps exception"""

    def __init__(self, reason, response=None):
        self.reason = unicode(reason)
        self.response = response

    def __str__(self):
        return self.reason

# Pybingmaps
# Copyright 2014 Chris Kelly
# See LICENSE for details.

import six

class BingMapsError(Exception):
    """Bing Maps exception"""

    def __init__(self, reason, response=None):
        self.reason = six.text_type(reason)
        self.response = response
        Exception.__init__(self, reason)

    def __str__(self):
        return self.reason

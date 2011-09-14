# Pybingmaps
# Copyright 2011 Lumatic, Inc
# See LICENSE for details.

"""
Pybingmaps Bing Maps API library
"""
__version__ = '0.1.0'
__author__ = 'Lumatic'
__license__ = 'MIT'

from bingmaps.error import BingMapsError
from bingmaps.api import BingMapsAPI

def debug(enable=True, level=1):
    
    import httplib
    httplib.HTTPConnection.debuglevel = level
# Pybingmaps
# Copyright 2014 Chris Kelly
# See LICENSE for details.

"""
Pybingmaps Bing Maps API library
"""
__version__ = '0.5.0'
__author__ = 'Chris Kelly'
__license__ = 'MIT'

from bingmaps.error import BingMapsError
from bingmaps.api import BingMapsAPI

# Global, unauthenitcated instance of API
api = BingMapsAPI()

def debug(enable=True, level=1):
    import logging
    urllib3_logger = logging.getLogger('urllib3')
    urllib3_logger.setLevel(level)

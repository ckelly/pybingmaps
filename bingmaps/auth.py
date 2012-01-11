# Pybingmaps
# Copyright 2011 Lumatic, Inc
# See LICENSE for details.


class AuthHandler(object):

    def apply_auth(self, url, method, headers, parameters):
        """Apply authentication headers to request"""
        raise NotImplementedError

    def append_auth(self, url, method, headers, parameters):
        """Apply certain authentication to url as params"""
        raise NotImplementedError

    def get_account_key(self):
        """Return the account_key of the authenticated user"""
        raise NotImplementedError


class KeyAuthHandler(AuthHandler):

    def __init__(self, api_key):
        self.api_key = api_key

    def append_auth(self, url, method, headers, parameters):
        parameters['key'] = self.api_key

    def apply_auth(self, url, method, headers, parameters):
        pass

    def get_api_key(self):
        return self.api_key

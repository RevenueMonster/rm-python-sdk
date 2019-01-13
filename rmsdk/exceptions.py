#!/usr/bin/python3

class RMSDKException(Exception):

    @property
    def message(self):
        return self.__dict__.get('message', None) or getattr(self, 'args')[0]


class RMSDKAPIException(Exception):

    @property
    def message(self):
        return self.__dict__.get('message', None) or getattr(self, 'args')[0]
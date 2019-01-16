#!/usr/bin/python3

import json
from .model import RMSDKModel
from .utils import getB64String
from .request import Request
from .exceptions import RMSDKException

check_keys = ["clientID", "clientSecret", "privateKey"]

class Auth(RMSDKModel):

    def __init__(self, configs):
        super(Auth, self).__init__(configs)

        for key in check_keys:
            self.checkConfigs(configs, key)

        self.defaults = {
            "clientID": configs["clientID"],
            "clientSecret": configs["clientSecret"],
            "privateKey": configs["privateKey"],
            "environment": configs["environment"],
            "accessToken": None,
            "refreshToken": None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, configs.get(param, default))


    def __str__(self):
        return "Auth(accessToken={}refreshToken={})".format(
                self.accessToken, self.refreshToken)

    
    def checkConfigs(self, configs, key):
        try:
            _ = configs[key]
        except KeyError:
            raise RMSDKException("{} is required!".format(key))


    def getHeader(self):
        credentials = self.clientID + ":" + self.clientSecret
        header = {
            "Authorization": "Basic {}".format(getB64String(credentials))
        }
        return header


    def clientCredentials(self):
        payload = json.dumps({
            "grantType": "client_credentials"
        })
        request = Request(environment=self.environment, auth="oauth", endpoint="v1/token")
        response = request.doPost(self.getHeader(), data=payload)
        self.accessToken, self.refreshToken = response["accessToken"], response["refreshToken"]
        return self.accessToken, self.refreshToken


    def getRefreshToken(self, refreshToken):
        payload = json.dumps({
            "grantType": "refresh_token",
            "refreshToken": refreshToken
        })
        request = Request(environment=self.environment, auth="oauth", endpoint="v1/token")
        response = request.doPost(self.getHeader(), data=payload)
        self.accessToken, self.refreshToken = response["accessToken"], response["refreshToken"]
        return self.accessToken, self.refreshToken
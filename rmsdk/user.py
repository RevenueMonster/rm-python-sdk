#!/usr/bin/python3

from .model import RMSDKModel
from .request import Request

class User(RMSDKModel):

    def __init__(self, configs={}):
        super(User, self).__init__(configs)
        self.defaults = {
            "environment": configs["environment"],
            "privateKey": configs["privateKey"],
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, configs.get(param, default))
    
    def getUserProfile(self, accessToken):
        request = Request(environment=self.environment, endpoint="v3/user")
        headers, _ = self.getHeadersAndData(accessToken=accessToken, data=None, requestUrl=request.baseUrl, method="get")
        response = request.doGet(headers=headers)
        return response
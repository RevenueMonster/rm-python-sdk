#!/usr/bin/python3

from .model import RMSDKModel
from .request import Request

class Merchant(RMSDKModel):

    def __init__(self, configs):
        super(Merchant, self).__init__(configs)
        self.defaults = {
            "environment": configs["environment"],
            "privateKey": configs["privateKey"],
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, configs.get(param, default))
    
    def getMerchantProfile(self, accessToken):
        request = Request(environment=self.environment, endpoint="v3/merchant")
        headers, _ = self.getHeadersAndData(accessToken=accessToken, data=None, requestUrl=request.baseUrl, method="get")
        response = request.doGet(headers=headers)
        return response

    def getMerchantSubcriptions(self, accessToken):
        request = Request(environment=self.environment, endpoint="v3/merchant/subscriptions")
        headers, _ = self.getHeadersAndData(accessToken=accessToken, data=None, requestUrl=request.baseUrl, method="get")
        response = request.doGet(headers=headers)
        return response
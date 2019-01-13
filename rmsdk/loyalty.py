#!/usr/bin/python3

from .model import RMSDKModel
from .request import Request

class Loyalty(RMSDKModel):

    def __init__(self, configs={}):
        super(Loyalty, self).__init__(configs)
        self.defaults = {
            "environment": configs["environment"],
            "privateKey": configs["privateKey"],
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, configs.get(param, default))
    
    def giveLoyaltyPoint(self, accessToken, data):
        request = Request(environment=self.environment, endpoint="v3/loyalty/reward")
        headers, data = self.getHeadersAndData(accessToken=accessToken, data=data, requestUrl=request.baseUrl)
        response = request.doPost(headers=headers, data=data)
        return response

    def getLoyaltyMember(self, accessToken, memberID):
        request = Request(environment=self.environment, endpoint="v3/loyalty/member/{}".format(memberID))
        headers, _ = self.getHeadersAndData(accessToken=accessToken, data=None, requestUrl=request.baseUrl, method="get")
        response = request.doGet(headers=headers)
        return response

    def getLoyaltyMembers(self, accessToken):
        request = Request(environment=self.environment, endpoint="v3/loyalty/members")
        headers, _ = self.getHeadersAndData(accessToken=accessToken, data=None, requestUrl=request.baseUrl, method="get")
        response = request.doGet(headers=headers)
        return response

    def getLoyaltyMemberPointHistory(self, accessToken, memberID):
        request = Request(environment=self.environment, endpoint="v3/loyalty/member/{}/history".format(memberID))
        headers, _ = self.getHeadersAndData(accessToken=accessToken, data=None, requestUrl=request.baseUrl, method="get")
        response = request.doGet(headers=headers)
        return response
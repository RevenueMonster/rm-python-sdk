#!/usr/bin/python3

from .model import RMSDKModel
from .request import Request

class Store(RMSDKModel):

    def __init__(self, configs):
        super(Store, self).__init__(configs)
        self.defaults = {
            "environment": configs["environment"],
            "privateKey": configs["privateKey"],
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, configs.get(param, default))

    def getStores(self, accessToken):
        request = Request(environment=self.environment, endpoint="v3/stores")
        headers, _ = self.getHeadersAndData(accessToken=accessToken, data=None, requestUrl=request.baseUrl, method="get")
        response = request.doGet(headers=headers)
        return response

    def getStoreByID(self, accessToken, storeID):
        request = Request(environment=self.environment, endpoint="v3/store/{}".format(storeID))
        headers, _ = self.getHeadersAndData(accessToken=accessToken, data=None, requestUrl=request.baseUrl, method="get")
        response = request.doGet(headers=headers)
        return response

    def createStore(self, accessToken, data):
        request = Request(environment=self.environment, endpoint="v3/store")
        headers, data = self.getHeadersAndData(accessToken=accessToken, data=data, requestUrl=request.baseUrl)
        response = request.doPost(headers=headers, data=data)
        return response

    def updateStore(self, accessToken, storeID, data):
        request = Request(environment=self.environment, endpoint="v3/store/{}".format(storeID))
        headers, data = self.getHeadersAndData(accessToken=accessToken, data=data, requestUrl=request.baseUrl, method="patch")
        response = request.doPatch(headers=headers, data=data)
        return response

    def deleteStore(self, accessToken, storeID):
        request = Request(environment=self.environment, endpoint="v3/store/{}".format(storeID))
        headers, _ = self.getHeadersAndData(accessToken=accessToken, data=None, requestUrl=request.baseUrl, method="delete")
        response = request.doDelete(headers=headers)
        return response
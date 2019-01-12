#!/usr/bin/python3

import json
from time import time
from rm import RMSDKModel
from rm.utils import Request

class Transaction(RMSDKModel):

    def __init__(self, configs):
        super(Transaction, self).__init__(configs)
        self.defaults = {
            "environment": configs["environment"],
            "privateKey": configs["privateKey"],
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, configs.get(param, default))
    
    def createTransaction(self, accessToken, data):
        request = Request(environment=self.environment, endpoint="v3/payment/transaction/qrcode")
        headers, data = self.getHeadersAndData(accessToken=accessToken, data=data, requestUrl=request.baseUrl)
        response = request.doPost(headers=headers, data=data)
        return response

    def getTransaction(self, accessToken):
        request = Request(environment=self.environment, endpoint="v3/payment/transaction/qrcodes")
        headers, _ = self.getHeadersAndData(accessToken=accessToken, data=None, requestUrl=request.baseUrl, method="get")
        response = request.doGet(headers=headers)
        return response

    def getTransactionByCode(self, accessToken, code):
        request = Request(environment=self.environment, endpoint="v3/payment/transaction/qrcode/{}".format(code))
        headers, _ = self.getHeadersAndData(accessToken=accessToken, data=None, requestUrl=request.baseUrl, method="get")
        response = request.doGet(headers=headers)
        return response

    def getTransactionsByCode(self, accessToken, code):
        request = Request(environment=self.environment, endpoint="v3/payment/transaction/qrcode/{}/transactions".format(code))
        headers, _ = self.getHeadersAndData(accessToken=accessToken, data=None, requestUrl=request.baseUrl, method="get")
        response = request.doGet(headers=headers)
        return response
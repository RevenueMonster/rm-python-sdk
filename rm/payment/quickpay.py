#!/usr/bin/python3

import json
from time import time
from rm import RMSDKModel
from rm.utils import Request


class QuickPay(RMSDKModel):

    def __init__(self, configs):
        super(QuickPay, self).__init__(configs)
        self.defaults = {
            "environment": configs["environment"],
            "privateKey": configs["privateKey"],
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, configs.get(param, default))

    def quickPay(self, accessToken, data):
        request = Request(environment=self.environment, endpoint="v3/payment/quickpay")
        headers, data = self.getHeadersAndData(accessToken=accessToken, data=data, requestUrl=request.baseUrl)
        response = request.doPost(headers=headers, data=data)
        return response
        
    def refund(self, accessToken, data):
        request = Request(environment=self.environment, endpoint="v3/payment/refund")
        headers, data = self.getHeadersAndData(accessToken=accessToken, data=data, requestUrl=request.baseUrl)
        response = request.doPost(headers=headers, data=data)
        return response

    def reverse(self, accessToken, data):
        request = Request(environment=self.environment, endpoint="v3/payment/reverse")
        headers, data = self.getHeadersAndData(accessToken=accessToken, data=data, requestUrl=request.baseUrl)
        response = request.doPost(headers=headers, data=data)
        return response
    
    def getAllTransactions(self, accessToken):
        request = Request(environment=self.environment, endpoint="v3/payment/transactions")
        headers, _ = self.getHeadersAndData(accessToken=accessToken, data=None, requestUrl=request.baseUrl, method="get")
        response = request.doGet(headers=headers)
        return response

    def getTransactionByID(self, accessToken, transactionID):
        request = Request(environment=self.environment, endpoint="v3/payment/transaction/{}".format(transactionID))
        headers, _ = self.getHeadersAndData(accessToken=accessToken, data=None, requestUrl=request.baseUrl, method="get")
        response = request.doGet(headers=headers)
        return response

    def getTransactionByOrder(self, accessToken, transactionID):
        request = Request(environment=self.environment, endpoint="v3/payment/transaction/order/{}".format(transactionID))
        headers, _ = self.getHeadersAndData(accessToken=accessToken, data=None, requestUrl=request.baseUrl, method="get")
        response = request.doGet(headers=headers)
        return response

    def dailySettlementReport(self, accessToken, data) -> list:
        request = Request(environment=self.environment, endpoint="v3/payment/settlement/csv")
        headers, data = self.getHeadersAndData(accessToken=accessToken, data=data, requestUrl=request.baseUrl)
        response = request.doPost(headers=headers, data=data)
        return response
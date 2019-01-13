#!/usr/bin/python3

from .model import RMSDKModel
from .request import Request

class Voucher(RMSDKModel):

    def __init__(self, configs={}):
        super(Voucher, self).__init__(configs)
        self.defaults = {
            "environment": configs["environment"],
            "privateKey": configs["privateKey"],
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, configs.get(param, default))
    
    def issueVoucher(self, accessToken, batchKey):
        request = Request(environment=self.environment, endpoint="v3/voucher-batch/{}/issue".format(batchKey))
        headers, _ = self.getHeadersAndData(accessToken=accessToken, data=None, requestUrl=request.baseUrl)
        response = request.doPost(headers=headers, data=None)
        return response

    def voidVoucher(self, accessToken, voucherCode):
        request = Request(environment=self.environment, endpoint="v3/voucher/{}/void".format(voucherCode))
        headers, _ = self.getHeadersAndData(accessToken=accessToken, data=None, requestUrl=request.baseUrl)
        response = request.doPost(headers=headers, data=None)
        return response

    def getVoucherByCode(self, accessToken, voucherCode):
        request = Request(environment=self.environment, endpoint="v3/voucher/{}".format(voucherCode))
        headers, _ = self.getHeadersAndData(accessToken=accessToken, data=None, requestUrl=request.baseUrl, method="get")
        response = request.doGet(headers=headers)
        return response

    def getVoucherBatches(self, accessToken):
        request = Request(environment=self.environment, endpoint="v3/voucher-batches")
        headers, _ = self.getHeadersAndData(accessToken=accessToken, data=None, requestUrl=request.baseUrl, method="get")
        response = request.doGet(headers=headers)
        return response

    def getVoucherBatchByKey(self, accessToken, batchKey):
        request = Request(environment=self.environment, endpoint="v3/voucher-batch/{}".format(batchKey))
        headers, _ = self.getHeadersAndData(accessToken=accessToken, data=None, requestUrl=request.baseUrl, method="get")
        response = request.doGet(headers=headers)
        return response
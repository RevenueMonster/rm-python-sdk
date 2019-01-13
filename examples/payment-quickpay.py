#!/usr/bin/python3

from rmsdk import RMSDK
from configs import configs

quickpay_payload = {
    "authCode": "1234567890",
    "order": {
        "amount": 100,
        "currencyType":"MYR",
        "id":"joker123",
        "title":"title",
        "detail":"desc",
        "additonalData":"API Test"
   },
    "ipAddress": "8.8.8.8",
    "terminalId": "19382734937293999",
    "storeId": "6170506694335521334"
}

refund_payload = {
    "transactionId": "190109042809010428940037",
    "refund": {
        "type": "FULL",
        "currencyType": "MYR",
        "amount": 100,
    },
    "reason": "test"
}

reverse_payload = {
    "orderId": "111222333"
}

dailySettlementReport_payload = {
    "date": "2019-01-09",
    "method": "WECHATPAY",
    "region": "MALAYSIA",
    "sequence": 1
}

# client_credentials
client = RMSDK(configs=configs)
accessToken, pay = client.accessToken, client.quickPay

# print(pay.quickPay(accessToken, quickpay_payload))
# print(pay.refund(accessToken, refund_payload))
# print(pay.reverse(accessToken, reverse_payload))
# print(pay.getAllTransactions(accessToken))
# print(pay.getTransactionByID(accessToken, "190109063931010426123307"))
# print(pay.getTransactionByOrder(accessToken, "wedsddr"))
# print(pay.dailySettlementReport(accessToken, dailySettlementReport_payload))
#!/usr/bin/python3

import rm
from configs import configs

create_transaction_payload = {
    "amount": 100,
    "currencyType": "MYR",
    "expiry": {
        "type": "PERMANENT"
    },
    "isPreFillAmount": True,
    "method": ['WECHATPAY'],
    "order": {
        "details": "Test",
        "title": "Title"
    },
    "redirectUrl": 'https://www.google.com',
    "storeId": '1981039839353524638',
    "type": 'DYNAMIC',
}

# client_credentials
client = rm.RMSDK(configs=configs)
accessToken, pay = client.accessToken, client.transaction

print(pay.createTransaction(accessToken, data=create_transaction_payload)) 
# print(pay.getTransaction(accessToken)) 
# print(pay.getTransactionByCode(accessToken, "c72cc63701e07d097669dcd7d4809140"))
# print(pay.getTransactionsByCode(accessToken, "c72cc63701e07d097669dcd7d4809140"))
#!/usr/bin/python3

from rmsdk.utils import generateSignature

data = {
    "name": "REVENUE MONSTER",
    "addressLine1": "B-5-30, 5th Floor, Block Bougainvillea",
    "addressLine2": "PJU 6A, Lebuhraya SPRINT, 10 Boulevard,",
    "postCode": "47400",
    "city": "Petaling Jaya",
    "state": "Selangor",
    "country": "Malaysia",
    "countryCode": "60",
    "phoneNumber": "377334080"
}

payload = {
    "authCode": "134850717797247290",
    "order": {
        "amount":1,
        "currencyType":"MYR",
        "id":"1234433332332323414",
        "title":"title",
        "detail":"desc",
        "additonalData":"API Test"
   },
    "ipAddress": "8.8.8.8",
    "terminalId": "19382734937293",
    "storeId": "6170506694335521334"
}

signature = generateSignature(
                data=payload, 
                method="post", 
                nonceStr="3df7053d698040e3a9d1c47dbe0156c5eaeb57c0131311e9915ea860b635ee61", 
                requestUrl="https://sb-open.revenuemonster.my/v3/payment/quickpay", 
                signType="sha256", 
                timestamp="1546931187.8109288", 
                privateKeyDest="/workspace/rm-python-sdk/keys/private_key.pem")

print(signature)
#!/usr/bin/python3

from rmsdk import RMSDK
from configs import configs

create_store_payload_valid = {
    "name": "Test store",
    "addressLine1": "Earth",
    "addressLine2": "Mars",
    "postCode": "10001",
    "city": "Petaling Jaya",
    "state": "Selangor",
    "country": "Malaysia",
    "countryCode": "60",
    "phoneNumber": "377334080"
}

create_store_payload_invalid = {
    "name": "Test store",
    "addressLine1": "Earth",
    "addressLine2": "Mars",
    "postCode": "10001",
    "city": "Johor",
    "state": "Pahang",
    "country": "60",
    "phoneNumber": "377334080"
}

client = RMSDK(configs=configs)
accessToken, store = client.accessToken, client.store

# print(store.getStores(accessToken))
# print(store.getStoreByID(accessToken, "1547113463894433307"))
# print(store.createStore(accessToken, create_store_payload_valid))
# print(store.updateStore(accessToken, "1547113463894433307", create_store_payload_valid))
# print(store.deleteStore(accessToken, "1547113463894433307"))
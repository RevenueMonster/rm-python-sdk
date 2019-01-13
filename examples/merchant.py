#!/usr/bin/python3

from rmsdk import RMSDK
from configs import configs

client = RMSDK(configs=configs)

# print(client.merchant.getMerchantProfile(client.accessToken))
# print(client.merchant.getMerchantSubcriptions(client.accessToken))
#!/usr/bin/python3

import rm
from configs import configs

client = rm.RMSDK(configs=configs)

# print(client.merchant.getMerchantProfile(client.accessToken))
# print(client.merchant.getMerchantSubcriptions(client.accessToken))
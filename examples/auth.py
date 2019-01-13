#!/usr/bin/python3

from rmsdk import RMSDK
from configs import configs

client = RMSDK(configs=configs)

print("Access token: \n{}\n".format(client.accessToken))
print("Refresh token: \n{}".format(client.refreshToken))
#!/usr/bin/python3

import rm
from configs import configs

client = rm.RMSDK(configs=configs)

print("Access token: \n{}\n".format(client.accessToken))
print("Refresh token: \n{}".format(client.refreshToken))
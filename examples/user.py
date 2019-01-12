#!/usr/bin/python3

import rm
from configs import configs

client = rm.RMSDK(configs=configs)
accessToken, user = client.accessToken, client.user

print(user.getUserProfile(accessToken))
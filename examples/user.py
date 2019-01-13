#!/usr/bin/python3

from rmsdk import RMSDK
from configs import configs

client = RMSDK(configs=configs)
accessToken, user = client.accessToken, client.user

print(user.getUserProfile(accessToken))
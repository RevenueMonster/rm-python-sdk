#!/usr/bin/python3

import rm
from configs import configs

give_loyalty_point_payload = {
    "point": 100,
    "type": "ID",
    "memberId": "7765269777796630408",
    "countryCode": "60",
    "phoneNumber": "172826990"
}

client = rm.RMSDK(configs=configs)
accessToken, loyalty = client.accessToken, client.loyalty

# print(loyalty.giveLoyaltyPoint(accessToken, give_loyalty_point_payload))
# print(loyalty.getLoyaltyMember(accessToken, "7765269777796630408"))
# print(loyalty.getLoyaltyMembers(accessToken))
# print(loyalty.getLoyaltyMemberPointHistory(accessToken, "7765269777796630408"))
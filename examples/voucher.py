#!/usr/bin/python3

from rmsdk import RMSDK
from configs import configs


client = RMSDK(configs=configs)
accessToken, voucher = client.accessToken, client.voucher

# print(voucher.issueVoucher(accessToken, "EhQKCE1lcmNoYW50EJXVzd3wraqTORIYCgxWb3VjaGVyQmF0Y2gQkvnGweaB2uQg"))
# print(voucher.voidVoucher(accessToken, "EhQKCE1lcmNoYW50EJXVzd3wraqTORIYCgxWb3VjaGVyQmF0Y2gQkvnGweaB2uQg"))
# print(voucher.getVoucherByCode(accessToken, "EhQKCE1lcmNoYW50EJXVzd3wraqTORIYCgxWb3VjaGVyQmF0Y2gQkvnGweaB2uQg"))
# print(voucher.getVoucherBatches(accessToken))
print(voucher.getVoucherBatchByKey(accessToken, "EhQKCE1lcmNoYW50EJXVzd3wraqTORIYCgxWb3VjaGVyQmF0Y2gQkvnGweaB2uQg"))
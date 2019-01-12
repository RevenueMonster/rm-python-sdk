#!/usr/bin/python3

import rm
from configs import configs


client = rm.RMSDK(configs=configs)
accessToken, voucher = client.accessToken, client.voucher

# print(voucher.issueVoucher(accessToken, "EhQKCE1lcmNoYW50EJXVzd3wraqTORIYCgxWb3VjaGVyQmF0Y2gQkvnGweaB2uQg"))
# print(voucher.voidVoucher(accessToken, "EhQKCE1lcmNoYW50EJXVzd3wraqTORIYCgxWb3VjaGVyQmF0Y2gQkvnGweaB2uQg"))
# print(voucher.getVoucherByCode(accessToken, "EhQKCE1lcmNoYW50EJXVzd3wraqTORIYCgxWb3VjaGVyQmF0Y2gQkvnGweaB2uQg"))
# print(voucher.getVoucherBatches(accessToken))
print(voucher.getVoucherBatchByKey(accessToken, "EhQKCE1lcmNoYW50EJXVzd3wraqTORIYCgxWb3VjaGVyQmF0Y2gQkvnGweaB2uQg"))
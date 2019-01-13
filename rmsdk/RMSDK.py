#!/usr/bin/python3

from rmsdk import (
    Auth,
    Loyalty,
    Merchant,
    QuickPay, 
    Store,
    Transaction,
    User,
    Voucher
)

class RMSDK(object):

    def __init__(self, configs={}):
        self.auth = Auth(configs)

        # authenticate when instance is first created
        self.auth.clientCredentials()
        for k, v in vars(self.auth).items():
            if not k.startswith("_") and k != "defaults":
                setattr(self, k, v)
        
        self.loyalty = Loyalty(configs)
        self.merchant = Merchant(configs)
        self.quickPay = QuickPay(configs)
        self.store = Store(configs)
        self.transaction = Transaction(configs)
        self.user = User(configs)
        self.voucher = Voucher(configs)
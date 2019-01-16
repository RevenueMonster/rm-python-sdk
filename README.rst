RM-API-SDK-Python
=================

|image0| |image1| |image2|

This is an Python SDK that maps some of the RESTful methods of Open API
that are documented at `Revenue Monster Open API
Documentation <doc.revenuemonster.my>`__.

Getting Started
---------------

Installation
~~~~~~~~~~~~

::

   pip3 install rmsdk

Prerequisite
~~~~~~~~~~~~

Before using the SDK, users must obtain credentials from merchant portal
first. Click
`here <https://github.com/RevenueMonster/RM-API-SDK-Python/blob/master/docs/merchant-portal.md>`__
for tutorial.

Supported APIs
--------------

-  Client Credentials (Authentication)

   -  `Generate Client Credentials <#generate-client-credentials>`__
   -  `Generate Refresh Token <#generate-refresh-token>`__

-  Merchant Related APIs

   -  `Get Merchant Profile <#get-merchant-profile>`__
   -  `Get Merchant Subscriptions <#get-merchant-subscriptions>`__

-  Store

   -  `Get Store List <#get-store-list>`__
   -  `Get Store By ID <#get-store-by-id>`__
   -  `Create Store <#create-store>`__
   -  `Update Store <#update-store>`__
   -  `Delete Store <#delete-store>`__

-  User

   -  `Get User Profile <#get-user-profile>`__

-  Payment (Quickpay QR)

   -  `QuickPay <#quickpay>`__
   -  `Refund <#refund>`__
   -  `Reverse <#reverse>`__
   -  `Get All Transactions <#get-all-transactions>`__
   -  `Get Transaction By ID <#get-transaction-by-id>`__
   -  `Get Transaction By Order ID <#get-transaction-by-order-id>`__
   -  `Get Daily Settlement Report <#get-daily-settlement-report>`__

-  Payment (Transaction QR)

   -  `Create Transaction <#create-transaction>`__
   -  `Get Transaction <#get-transaction>`__
   -  `Get Transaction By Code <#get-transaction-by-code>`__
   -  `Get List of Transactions By
      Code <#get-list-of-transaction-by-code>`__

-  Loyalty

   -  `Give Loyalty Point <#give-loyalty-point>`__
   -  `Get Loyalty Member <#get-loyalty-member>`__
   -  `Get List of Loyalty Members <#get-list-of-loyalty-members>`__
   -  `Get Point History <#get-point-history>`__

-  Voucher

   -  `Issue Voucher <#issue-voucher>`__
   -  `Void Voucher <#void-voucher>`__
   -  `Get Voucher By Code <#get-voucher-by-code>`__
   -  `Get Voucher Batches <#get-voucher-batches>`__
   -  `Get Voucher Batches By Batch
      Key <#get-voucher-batches-by-batch-key>`__

Usage
-----

This section explains the basic usage of the SDK. Detail usage for
individual modules are prepared in the
`examples <https://github.com/RevenueMonster/RM-API-SDK-Python/tree/master/examples>`__
folder.

A ``dictionary`` that contains ``clientID``, ``clientSecret``,
``environment`` and ``privateKey`` (path to private key) is expected to
passed in as argument. An object of the ``RMSDK`` class will be
instantiated. All modules covered in this SDK will be available under
the instantiated object.

For instance, to use the store module, simply,

::

   response = client.module.methodName(*args)

Authentication
--------------

Authenticate SDK
~~~~~~~~~~~~~~~~

::

   from rmsdk import RMSDK

   client = RMSDK(configs={
       "environment": "sandbox", # or production
       "clientID": "client-id",
       "clientSecret": "client-secret",
       "privateKey": "path-to-private-key"
   })

   accessToken, refreshToken = client.accessToken, client.refreshToken

Generate Client Credentials
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To get refresh token and access token(expired after 2 hours) with using
provided clientID and clientSecret.

::

   client = Auth({
       "environment": "sandbox", # or production
       "clientID": "client-id",
       "clientSecret": "client-secret",
       "privateKey": "path-to-private-key"
   })

   accessToken, refreshToken = client.clientCredentials()

Generate Refresh Token
~~~~~~~~~~~~~~~~~~~~~~

To get new access token(expired after 2 hours) with using provided
clientId and clientSecret (recommended to schedule to run this fucntion
on every less than 2 hours) in order to avoid expired access token
error.

::

   accessToken, refreshToken = client.getRefreshToken(refreshToken)

Merchant
--------

Get Merchant Profile
~~~~~~~~~~~~~~~~~~~~

::

   result = client.merchant.getMerchantProfile(accessToken)

Get Merchant Subscriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   result = client.merchant.getMerchantSubcriptions(accessToken)

Store
-----

Get Store List
~~~~~~~~~~~~~~

::

   result = client.store.getStores(accessToken)

Get Store By ID
~~~~~~~~~~~~~~~

::

   result = client.store.getStoreByID(accessToken, storeID)

Create Store
~~~~~~~~~~~~

::

   result = client.store.createStore(accessToken, {
       "name": "Test store",
       "addressLine1": "Earth",
       "addressLine2": "Mars",
       "postCode": "10001",
       "city": "Petaling Jaya",
       "state": "Selangor",
       "country": "Malaysia",
       "countryCode": "60",
       "phoneNumber": "377334080"
   })

Update Store
~~~~~~~~~~~~

::

   result = client.store.updateStore(accessToken, storeID, {
       "name": "Test store",
       "addressLine1": "Earth",
       "addressLine2": "Mars",
       "postCode": "10001",
       "city": "Petaling Jaya",
       "state": "Selangor",
       "country": "Malaysia",
       "countryCode": "60",
       "phoneNumber": "377334080"
   })

Delete Store
~~~~~~~~~~~~

::

   result = client.store.deleteStore(accessToken, storeID)

User
----

Get User Profile
~~~~~~~~~~~~~~~~

::

   result = client.user.getUserProfile(accessToken)

Payment (Quickpay QR)
---------------------

QuickPay
~~~~~~~~

::

   result = client.quickPay.quickPay(accessToken, {
       "authCode": "1234567890",
       "order": {
           "amount": 100,
           "currencyType":"MYR",
           "id":"1312331232",
           "title":"title",
           "detail":"desc",
           "additonalData":"API Test"
      },
       "ipAddress": "8.8.8.8",
       "terminalId": "19382734937293999",
       "storeId": "6170506694335521334"
   })

Refund
~~~~~~

::

   result = client.quickPay.refund(accessToken, {
       "transactionId": "190109042809010428940037",
       "refund": {
           "type": "FULL",
           "currencyType": "MYR",
           "amount": 100,
       },
       "reason": "test"
   })

Reverse
~~~~~~~

::

   result = client.quickPay.reverse(accessToken, {
       "orderId": "111222333"
   })

Get All Transactions
~~~~~~~~~~~~~~~~~~~~

::

   result = client.quickPay.getAllTransactions(accessToken)

Get Transaction By ID
~~~~~~~~~~~~~~~~~~~~~

::

   result = client.quickPay.getTransactionByID(accessToken, transactionID)

Get Transaction By Order ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   result = client.quickPay.getTransactionByOrder(accessToken, orderID)

Get Daily Settlement Report
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   result = client.quickPay.dailySettlementReport(accessToken, {
       "date": "2019-01-09",
       "method": "WECHATPAY",
       "region": "MALAYSIA",
       "sequence": 1
   })

Payment (Transaction QR)
------------------------

Create Transaction
~~~~~~~~~~~~~~~~~~

::

   result = client.transaction.createTransaction(accessToken, {
       "amount": 100,
       "currencyType": "MYR",
       "expiry": {
           "type": "PERMANENT"
       },
       "isPreFillAmount": True,
       "method": ['WECHATPAY'],
       "order": {
           "details": "Test",
           "title": "Title"
       },
       "redirectUrl": 'https://www.revenuemonster.com',
       "storeId": '1981039839353524638',
       "type": 'DYNAMIC',
   })

Get Transaction
~~~~~~~~~~~~~~~

::

   result = client.transaction.getTransaction(accessToken)

Get Transaction By Code
~~~~~~~~~~~~~~~~~~~~~~~

::

   result = client.transaction.getTransactionByCode(accessToken, qrCode)

Get List of Transactions By Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   result = client.transaction.getTransactionByCode(accessToken, qrCode)

Loyalty
-------

Give Loyalty Point
~~~~~~~~~~~~~~~~~~

::

   result = client.loyalty.giveLoyaltyPoint(accessToken, {
       "point": 100,
       "type": "ID",
       "memberId": "7765269777796630408",
       "countryCode": "60",
       "phoneNumber": "172826990"
   })

Get Loyalty Member
~~~~~~~~~~~~~~~~~~

::

   result = client.loyalty.getLoyaltyMember(accessToken, memberID)

Get List of Loyalty Members
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   result = client.loyalty.getLoyaltyMembers(accessToken)

Get Point History
~~~~~~~~~~~~~~~~~

Get Loyalty point history of a member

::

   result = client.loyalty.getLoyaltyMemberPointHistory(accessToken, memberID)

Voucher
-------

Issue Voucher
~~~~~~~~~~~~~

::

   result = client.voucher.issueVoucher(accessToken, batchKey)

Void Voucher
~~~~~~~~~~~~

::

   result = client.voucher.voidVoucher(accessToken, voucherCode)

Get Voucher By Code
~~~~~~~~~~~~~~~~~~~

::

   result = client.voucher.getVoucherByCode(accessToken, voucherCode)

Get Voucher Batches
~~~~~~~~~~~~~~~~~~~

::

   result = client.voucher.getVoucherBatches(accessToken)

Get Voucher Batches By Batch Key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   result = client.voucher.getVoucherBatchByKey(accessToken, batchKey)

Detail examples can be found at
`examples <https://github.com/RevenueMonster/RM-API-SDK-Python/tree/master/examples>`__.

.. |image0| image:: https://img.shields.io/pypi/pyversions/rmsdk.svg
   :target: https://pypi.org/project/rmsdk/
.. |image1| image:: https://img.shields.io/pypi/v/nine.svg
   :target: https://pypi.org/project/rmsdk/
.. |image2| image:: https://img.shields.io/pypi/l/rmsdk.svg
   :target: https://pypi.org/project/rmsdk/

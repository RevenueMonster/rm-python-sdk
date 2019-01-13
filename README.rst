RM-API-SDK-Python
=================

This is an Python SDK that maps some of the RESTful methods of Open API
that are documented at `Revenue Monster Open API
Documentation <doc.revenuemonster.my>`__.

Getting Started
---------------

Installation
~~~~~~~~~~~~

::

   pip3 install rmsdk

Registration and obtain credentials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before using the SDK, users must obtain credentials from merchant portal
first. Click
`here <https://github.com/RevenueMonster/RM-API-SDK-Python/blob/master/docs/merchant-portal.md>`__
for tutorial.

Usage Examples
--------------

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

   response = client.store.methodName(*args)

For full parameter, please refer `Revenue Monster Open API
Documentation <doc.revenuemonster.my>`__.

Authentication
~~~~~~~~~~~~~~

::

   from rmsdk import RMSDK

   client = RMSDK(configs={
       "environment": "sandbox", # or production
       "clientID": "client-id",
       "clientSecret": "client-secret",
       "privateKey": "path-to-private-key"
   })

   accessToken, refreshToken = client.accessToken, client.refreshToken

Payment
~~~~~~~

::

   quickpay_payload = {
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
   }

   response = client.quickPay.quickPay(accessToken, quickpay_payload)

For full examples, please visit the
`examples <https://github.com/RevenueMonster/RM-API-SDK-Python/tree/master/examples>`__
folder

Covered Functions
-----------------

-  [x] Client Credentials (Authentication)
-  [x] Refresh Token (Authentication)
-  [x] Get Merchant Profile
-  [x] Get Merchant Subscriptions
-  [x] Get Stores
-  [x] Get Stores By ID
-  [x] Create Store
-  [x] Update Store
-  [x] Delete Store
-  [x] Get User Profile
-  [x] Payment (Transaction QR) - Create Transaction QRCode/URL
-  [x] Payment (Transaction QR) - Get Transaction QRCode/URL
-  [x] Payment (Transaction QR) - Get Transaction QRCode/URL By Code
-  [x] Payment (Transaction QR) - Get Transactions By Code
-  [x] Payment (Quick Pay) - Payment
-  [x] Payment (Quick Pay) - Refund
-  [x] Payment (Quick Pay) - Reverse
-  [x] Payment (Quick Pay) - Get All Payment Transactions
-  [x] Payment (Quick Pay) - Get All Payment Transaction By ID
-  [x] Payment (Quick Pay) - Daily Settlement Report
-  [x] Give Loyalty Point
-  [x] Get Loyalty Members
-  [x] Get Loyalty Member
-  [x] Get Loyalty Member Point History
-  [x] Issue Voucher
-  [x] Void Voucher
-  [x] Get Voucher By Code
-  [x] Get Voucher Batches
-  [x] Get Voucher Batch By Key
-  [ ] Send Notification (Merchant)
-  [ ] Send Notification (Store)
-  [ ] Send Notification (User)

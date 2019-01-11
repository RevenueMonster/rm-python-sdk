import os
import json
from base64 import b64encode
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

from rm import RMSDKException
from rm.utils.helper import orderDict


def generateSignature(
        data, 
        method: str,
        nonceStr: str,
        requestUrl: str, 
        signType: str, 
        timestamp: str,
        privateKeyDest: str) -> str:

    if not os.path.exists(privateKeyDest):
        raise RMSDKException("Private Key File not found")

    # deep sort payload data if it is a dict
    if isinstance(data, dict) and data is not None:
        # deep sort and encode to base64
        data = json.dumps(orderDict(data), separators=(',', ':'))

    data = b64encode(s=data.encode(encoding="utf-8")).decode() if data is not None else data

    # format message according to documents
    data = "" if data is None else "data={}&".format(data)
    message =  data + \
              "method=" + method + \
              "&nonceStr=" + nonceStr + \
              "&requestUrl=" + requestUrl + \
              "&signType=" + signType + \
              "&timestamp=" + timestamp
    message = bytes(message, "utf-8")

    key = RSA.import_key(open(privateKeyDest).read())
    hash = SHA256.new(message)
    signature = pkcs1_15.new(key).sign(hash)
    
    return b64encode(signature).decode("utf-8")
#!/usr/bin/python3

import os
import uuid
import json
from base64 import b64encode
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from .exceptions import RMSDKException

def orderDict(d: dict):
    """Deep sort dictionary by keys
    
    Args:
        d (dict): unsorted dictionary
    
    Returns:
        [dict]: Sorted dictionary
    """

    return {k: orderDict(v) if isinstance(v, dict) else v for k, v in sorted(d.items())}


def getNonce():
    return str(uuid.uuid4().hex + uuid.uuid1().hex)


def getB64String(s: str, encoding="utf-8") -> str:
    """Returns an encoded base64 string
    
    Args:
        s (str): Raw string
        encoding (str, optional): Defaults to "utf-8".
    
    Returns:
        [str]: Encoded base64 string
    """

    return b64encode(s.encode(encoding)).decode(encoding)

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
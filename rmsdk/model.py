#!/usr/bin/python3

import json
import requests
from time import time
from .utils import generateSignature, getNonce, orderDict

class RMSDKModel(object):
    """The base RM SDK Model all other models will inherit.
    
    Args:
        object ([dict]): A dictionary containing the attributes for the Model.
    """

    def __init__(self, configs: dict):
        """Create an instance of the base RMSDKModel"""

        self.defaults = {
            '_raw_json': None
        }

        setattr(self, '_raw_json', configs)

    def __str__(self):
        """Return a string representation of the RMSDKModel. By default this
        is the same as asJsonString().
        
        Returns:
            [str]: Model Representation in string.
        """

        return self.asJsonString()

    def asJsonString(self):
        """Return a JSON string of the RMSDKModel based on key/value pairs
        returned from the asDict() function.
        
        Returns:
            [str]: Model Representation in string.
        """

        return json.dumps(
            self.asDict(),
            sort_keys=True,
            separators=(',', ':'),
            indent=4
        )

    def asDict(self):
        """Return a dictionary representation of the RMSDKModel.
        
        Returns:
            [dict]: Model Representation
        """

        data = {}

        for (key, value) in self._raw_json.items():
            if isinstance(self._raw_json.get(key, None), (list, tuple, set)):
                data[key] = list()
                for subobj in self._raw_json.get(key, None):
                    data[key].append(subobj)

            elif self._raw_json.get(key, None):
                data[key] = self._raw_json.get(key, None)

        return data

    def request(self, url, headers, data):
        try:
            response = requests.post(url, headers, data)
            return json.loads(response.text)
        except requests.HTTPError as err:
            return err

    def getHeader(self, accessToken, signature, nonceStr, timestamp):
        """Default request headers in this SDK.
        
        Args:
            accessToken (str): Access token need to access Revenue Monster APIs
            signature (str): Signature algorithm is used to sign your payment API request 
                                with a private key to obtain additional security
            nonceStr (str): Nonce string
            timestamp (str): Request time stamp
        
        Returns:
            [dict]: Request header
        """

        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'X-Signature': 'sha256 ' + signature,
            'X-Nonce-Str': nonceStr,
            'X-Timestamp': timestamp
        }
        return headers

    def getSignature(self, data, method, nonceStr, requestUrl, timestamp):
        signature = generateSignature(
            data=data, 
            method=method, 
            nonceStr=nonceStr, 
            requestUrl=requestUrl,
            signType="sha256",
            timestamp=timestamp, 
            privateKeyDest=self.privateKey)
        return signature

    def getHeadersAndData(self, accessToken, requestUrl, method="post", data=None):
        nonceStr = getNonce()
        timestamp = str(time())

        if data is not None:
            data = json.dumps(orderDict(data), separators=(',', ':'))

        signature = self.getSignature(data, method, nonceStr, requestUrl, timestamp)
        headers = self.getHeader(accessToken, signature, nonceStr, timestamp)

        return headers, data
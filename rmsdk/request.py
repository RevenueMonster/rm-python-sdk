#!/usr/bin/python3

import json
import requests
from typing import Union
from .exceptions import RMSDKAPIException, RMSDKException

class Request(object):

    def __init__(self, environment, endpoint, auth="open"):
        self.baseUrl = self.formatUrl(environment, auth, endpoint)
        self.baseHeader = {
            "User-Agent": "RM API Client Python",
            "Content-Type": "application/json",
        }
        defaultSession = requests.Session()
        defaultSession.headers = self.baseHeader
        self.session = defaultSession

    def combineDict(self, a, b):
        return dict(a, **b)

    def formatUrl(self, environment, auth, endpoint):
        return "https://{}{}.revenuemonster.my/{}".format("sb-" if environment == "sandbox" else "", auth, endpoint)

    def loadResponse(self, s: str) -> Union[dict, list]:
        try:
            return json.loads(s)
        except ValueError as ve:
            return s.splitlines()

    def makeRequest(self, method=None, url=None, data=None, headers=None, params=None):
        try:
            if data is not None and not json.loads(data):
                raise RMSDKException("Payload data cannot be empty")

            response = self.session.request(
                method=method,
                url=url,
                data=data,
                headers=headers,
                params=params,
                timeout=2000
            )
            
            content = self.loadResponse(response.text)

            if response.status_code != 200:
                raise RMSDKAPIException(content)

            return content
        except requests.HTTPError as err:
            return err

    def doGet(self, headers):
        return self.makeRequest(
            method="GET",
            url=self.baseUrl,
            headers=headers
        )

    def doPost(self, headers, data):
        return self.makeRequest(
            method="POST",
            url=self.baseUrl,
            data=data,
            headers=self.combineDict(self.session.headers, headers)
        )

    def doPatch(self, headers, data):
        return self.makeRequest(
            method="PATCH",
            url=self.baseUrl,
            data=data,
            headers=self.combineDict(self.session.headers, headers)
        )

    def doDelete(self, headers):
        return self.makeRequest(
            method="DELETE",
            url=self.baseUrl,
            headers=self.combineDict(self.session.headers, headers)
        )
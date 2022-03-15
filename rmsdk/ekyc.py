import json
from .model import RMSDKModel
from .request import Request

class EKYC(RMSDKModel):
    def __init__(self, configs):
        super(EKYC, self).__init__(configs)
        self.defaults = {
            "environment": configs["environment"],
            "privateKey": configs["privateKey"],
        }
        
        for (param, default) in self.defaults.items():
            setattr(self, param, configs.get(param, default))
            
        self.payload = {
            "service": "ekyc",
            "version": "v1",
        }
            
    def mykad_recog(self, accessToken: str, data: dict) -> dict:
        """
        Function to make http request to get recognize mykad
        
        args:
            accessToken (str): Access Token to allow open api to get user
            data (dict): Data to send to open api server
            
        returns:
            dict: dict containing only id for mykad recog result (require to parse the results via different route)
        """
        request = Request(environment=self.defaults['environment'], endpoint='v3/service')
        self.payload['function'] = 'id-mykad'
        self.payload['request']  = data
        
        headers, data = self.getHeadersAndData(accessToken=accessToken, data=self.payload, requestUrl=request.baseUrl)
        response = request.doPost(headers=headers, data=data)
        return response
    
    def face_verification(self, accessToken: str, data: dict) -> dict:
        """
        Funtion to get the similarity between two faces
        
        args:
            accessToken (str): Access Token to allow open api to get user
            data (dict): Data to send to open api server
            
        returns:
            dict: Results if the two faces are similar or not 
        """
        request = Request(environment=self.defaults['environment'], endpoint='v3/service')
        self.payload['function'] = 'face-compare'
        self.payload['request']  = data
        
        headers, data = self.getHeadersAndData(accessToken=accessToken, data=self.payload, requestUrl=request.baseUrl)
        
        response = request.doPost(headers=headers, data=data)
        return response
    
    def get_mykad_results(self, accessToken: str, data: dict) -> dict:
        """
        Function to get the results from the recognized mykad
        
        args:
            accessToken (str): Access Token to allow open api to get user
            data (dict): Data to send to open api server
            
        returns:
            dict: Results containing the recognize mykad
        """
        self.payload['function'] = "get-mykad-result"
        self.payload['request']  = data
        request = Request(environment=self.defaults['environment'], endpoint='v3/service')
        headers, data = self.getHeadersAndData(accessToken=accessToken, data=self.payload, requestUrl=request.baseUrl)
        
        response = request.doPost(headers=headers, data=data)
        return response
    
    def get_ekyc_results(self, accessToken: str, data: dict) -> dict:
        """
        Function to get the end to end ekyc results
        
        args:
            accessToken (str): Access Token to allow open api to get user
            data (dict): Data to send to open api server
            
        returns:
            dict: Results containing the end to end including face and mykad results
        """
        request = Request(environment=self.defaults['environment'], endpoint='v3/service')
        self.payload['function'] = "get-ekyc-result"
        self.payload['request']  = data
        headers, data = self.getHeadersAndData(accessToken=accessToken, data=self.payload, requestUrl=request.baseUrl)
        
        response = request.doPost(headers=headers, data=data)
        return response
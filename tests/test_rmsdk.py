import unittest
import base64
import requests
from rmsdk import RMSDK
from examples.configs import configs

class TestEKYCSDK(unittest.TestCase):
    def setUp(self):
        self.client = RMSDK(configs=configs)
        self.accessToken = self.client.accessToken
    
    def to_b64(self, img_url: str):
        img_byte = requests.get(img_url).content
        img_b64 = base64.b64encode(img_byte)
        
        return img_b64
    
    def test_mykad_recog(self):
        img_url = 'https://buletinonlines.net/v7/wp-content/uploads/2016/06/Mykad-penghuni-puan-Noraini-2.jpg'
        img_b64 = self.to_b64(img_url)
        
        mykad_payload = {
            "service": "ekyc",
            "version": "v1",
            "function": "id-mykad",
            "request": {
                "notify_url": "https://aifire.com/ekyc/result",
                "query_image_content": img_b64.decode('utf-8')
            }
        }
        
        results = self.client.ekyc.mykad_recog(self.accessToken, mykad_payload)
        get_result_mykad_payload = {
            "service": "ekyc",
            "version": "v1",
            "function": "get-mykad-result",
            "request": {
                'id': results['item']['requestID']
                # "id": "62201d48a694817dede84b35"
            }
        }

        mykad_results = self.client.ekyc.get_mykad_results(self.accessToken, get_result_mykad_payload)
        self.assertIn('item', mykad_results)
            
    def test_face_verfication(self):
        face_img_url = 'https://media.glamour.com/photos/5a425fd3b6bcee68da9f86f8/master/pass/best-face-oil.png'
        img_b64 = self.to_b64(face_img_url)
        
        face_verification_payload = {
            "service": "ekyc",
            "version": "v1",
            "function": "face-compare",
            "request": {
                "query_image_content_1": img_b64.decode('utf-8'),
                "query_image_content_2": img_b64.decode('utf-8')
            }
        }
        face_verification_results = self.client.ekyc.face_verification(self.accessToken, face_verification_payload)
        self.assertIn('item', face_verification_results)
        
        self.assertIn('similarity', face_verification_results['item'])
        self.assertEqual(face_verification_results['item']['isSamePerson'], True)
        
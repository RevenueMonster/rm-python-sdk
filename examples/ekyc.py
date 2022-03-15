from rmsdk import RMSDK
from configs import configs
from pprint import pprint
import requests
import base64

def url_to_b64(img_url: str):
    img_byte = requests.get(img_url).content
    img_b64 = base64.b64encode(img_byte)
    
    return img_b64

if __name__ == '__main__':
    # Init client
    client = RMSDK(configs=configs)
    accessToken = client.accessToken

    # Recognize mykad
    img_url = 'https://buletinonlines.net/v7/wp-content/uploads/2016/06/Mykad-penghuni-puan-Noraini-2.jpg'
    mykad_payload = {
        "request": {
            "notify_url": "https://aifire.com/ekyc/result",
            "query_image_content": url_to_b64(img_url).decode('utf-8')
        }
    }

    results = client.ekyc.mykad_recog(accessToken, mykad_payload)
    pprint(results)

    # Get mykad results
    get_result_mykad_payload = {
        "request": {
        'id': results['item']['requestID']
        # "id": "62201d48a694817dede84b35"
    }}

    mykad_results = client.ekyc.get_mykad_results(accessToken, get_result_mykad_payload)
    pprint(mykad_results)

    # Face verification
    face_img_url = 'https://media.glamour.com/photos/5a425fd3b6bcee68da9f86f8/master/pass/best-face-oil.png'
    img_b64 = url_to_b64(face_img_url)

    face_verification_payload = {
        "request": {
            "query_image_content_1": img_b64.decode('utf-8'),
            "query_image_content_2": img_b64.decode('utf-8'),
        }
    }
    face_verification_results = client.ekyc.face_verification(accessToken, face_verification_payload)
    pprint(face_verification_results)

    # Get EKYC Results
    ekyc_payload = {
        "request": {
            "id": "62201d48a694817dede84b35"
        }
    }
    ekyc_results = client.ekyc.get_ekyc_results(accessToken, ekyc_payload)
    pprint(ekyc_results)
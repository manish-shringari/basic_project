from pyzbar import pyzbar
import cv2
import glob, os, sys
import requests
import json

api_key = 'CJzxYTdrGnS0qK6xdFIfCiV6qBjBiwVA'
def get_data(vin):
    li = glob.glob('*.jpg')
    if li:
        img = cv2.imread(li[-1])
        barcode = pyzbar.decode(img)
        # cmd = 'rm *.jpg'
        cmd = 'del *.jpg'
        os.system(cmd)
        vin = barcode[0][0][1:]
        res = decode_vin(vin=vin)
        return res
    elif vin:
        res = decode_vin(vin=vin)
        return res
    else:
        return 'no barcode uploaded'


def decode_vin(vin):
    # end_point = 'http://api.marketcheck.com/v1/vin/{}/specs?api_key={}'.format(vin, api_key)
    end_point = 'https://marketcheck-prod.apigee.net/v1/vin/{}/specs?api_key={}'.format(vin, api_key)
    try:
        response = requests.get(end_point)
        # print response
        data = response.content
        # print data
        result = json.loads(data)
        return result
    except Exception as e:
        return e

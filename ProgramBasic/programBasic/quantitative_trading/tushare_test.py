import requests
import json
import datetime
import time

base_url = "http://api.tushare.pro"
api_name = "stock_basic"

token = 'e409da......'

t = datetime.datetime.now()
payload_nonce = str(int(time.mktime(t.timetuple())*1000))

payload = {
   "api_name": api_name,
   "token": token,
   "params": {"list_state": "L"},
   "fields": "",
}

encoded_payload = json.dumps(payload).encode('utf-8')

request_headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache"
}

response = requests.post(base_url,
                         data=encoded_payload,
                         headers=request_headers)

new_order = response.json()
print(new_order)

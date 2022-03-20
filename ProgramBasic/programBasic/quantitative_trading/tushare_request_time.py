import json
import requests
import timeit


base_url = "http://api.tushare.pro"
api_name = "stock_basic"


def get_order():
    token = 'e409da15543a996941da34cb9093a98e53970f0dde745143818b4093'

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
    return response


n = 10
latency = timeit.timeit('get_order', setup='from __main__ import get_order', number=n) * 1.0 / n
print('Latency is {} ms'.format(latency * 1000))

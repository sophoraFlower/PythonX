# -*- coding:utf-8 -*-

import requests


url = 'https://apis.zhanqi.tv/static/v2.1/game/live/6/1/1.json'

r = requests.post(url)
response = r.json()

print(r.status_code)
print(response['data']['rooms'][0])



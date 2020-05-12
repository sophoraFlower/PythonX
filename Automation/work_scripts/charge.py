# coding:utf-8

import requests
import time

page_start = 0
page_end = 1085
other = 2700

url = 'https://er.zhanqi.tv/proxy/funds.bullet_log_list'
cookies = dict(PHPSESSID='9639bkednnjj6ctgak717okt76',
               gid='1697940447', ZQ_GUID='86307684-2654-36D3-185F-A2B802020B70', tj_uid='111369973')
count = 0
for j in range(1085):
    r_all = requests.post(url, data={'action': -1, 'channel': 177, 'nickname': None,
                                     'startTime': '2019-05-22 00:00:00',
                                     'endTime': '2019-05-30 23:59:59',
                                     'page': j}, cookies=cookies)
    j += 1
    time.sleep(1)
    for i in range(10):
        count += int(r_all.json()["data"]["list"][i]["count"])
    print(count)
print(count)
count = count + other
print("all zidan:" + str(count))

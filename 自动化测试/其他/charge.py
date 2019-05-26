# coding:utf-8

import requests

url = 'https://beta.zhanqi.tv/api/user/charge/order'
cookies = dict(PHPSESSID='4vjbsbbs4e91j64uu3153k39q8',
               gid='1800728418', ZQ_GUID='B3CA2DA2-06AD-5689-6ECD-04A9700F3413', tj_uid='104265993',
               taskTipCookie108474804='2019-03-18', cookie_ip='1944858858%2C1944858858')
r_all = requests.post(url, data={'amount': 1000, }, cookies=cookies)
string = str(r_all.content, 'utf-8')
print(string)
# print(r_all.headers)


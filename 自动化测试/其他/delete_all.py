# coding:utf-8

import requests

url = 'http://beta.monkey.zhanqi.tv/proxy/badword.list'
url_del = 'http://beta.monkey.zhanqi.tv/proxy/badword.del'
# url_list = 'http://beta.monkey.zhanqi.tv/proxy/badword.list'
cookies = dict(PHPSESSID='tmcn7o3jh0gpb5ugi1gvd7l003', ZQ_GUID='62699101-171A-9DFE-FBB9-6AE39538D6E8',
               gid='1744965237', tj_uid='111369985')
r_all = requests.post(url, data={'page': 1, 'type': 0, 'txt': None, 'flag': None}, cookies=cookies)
badword_length = int(r_all.json()['data']['pagination']['pageTotal'])
print(badword_length)
for j in range(badword_length):
    r = requests.post(url, data={'page': 1, 'type': 0, 'txt': None, 'flag': None}, cookies=cookies)
    badword_list = r.json()['data']['list']
    for i in range(len(badword_list)):
        print('delete badword id: ' + badword_list[i]['id'])
        r_delete = requests.post(url_del, data={'id': int(badword_list[i]['id'])}, cookies=cookies)
        print(r_delete.content)


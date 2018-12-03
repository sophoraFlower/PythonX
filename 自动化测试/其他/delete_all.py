# coding:utf-8

import requests

url = 'http://beta.monkey.zhanqi.tv/proxy/badword.list'
url_del = 'http://beta.monkey.zhanqi.tv/proxy/badword.del'
# url_list = 'http://beta.monkey.zhanqi.tv/proxy/badword.list'
cookies = dict(PHPSESSID='a7v56me8l5hjf70bsdm8d96si2', ZQ_GUID='C3900FA5-88AA-4E6F-7251-B24DAA32D86E',
               gid='1779337236', tj_uid='51')
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


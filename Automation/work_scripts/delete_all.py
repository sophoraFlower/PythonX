# coding:utf-8

import requests

url = 'http://er.zhanqi.tv/proxy/badword.list'
url_del = 'http://er.zhanqi.tv/proxy/badword.del'
# url_list = 'http://beta.monkey.zhanqi.tv/proxy/badword.list'
cookies = dict(PHPSESSID='p1ecj44rqjn8hn38nuc0or1c54',
               gid='1845039736', loginType='%22TOKEN%22')
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


# coding:utf-8

import requests

url = 'http://beta.monkey.zhanqi.tv/proxy/badword.list'
url_del = 'http://beta.monkey.zhanqi.tv/proxy/badword.del'
# url_list = 'http://beta.monkey.zhanqi.tv/proxy/badword.list'
cookies = dict(PHPSESSID='v35gabu31hsrfk7t8s1ivgi416', ZQ_GUID='B75351F9-C8FA-3167-5CF2-5FF642772363',
               gid='1759383513', tj_uid='111369984')

for j in range(300):
    r = requests.post(url, data={'page': 1, 'type': 0, 'txt': None, 'flag': None}, cookies=cookies)
    badword_list = r.json()['data']['list']
    for i in range(len(badword_list)):
        print('delete badword id: ' + badword_list[i]['id'])
        r_delete = requests.post(url_del, data={'id': int(badword_list[i]['id'])}, cookies=cookies)
        print(r_delete.content)


# coding:utf-8

import requests

url = 'http://beta.monkey.zhanqi.tv/proxy/site.badword_list'
url_del = 'http://beta.monkey.zhanqi.tv/proxy/site.del_keywords'
cookies = dict(PHPSESSID='sj03fghh5auhc3al79pgtdso62', ZQ_GUID='AD4FC9AD-6A12-964D-5CCF-D6148F630051',
               gid='1759383513', tj_uid='111437877')

for j in range(500):
    # 国家敏感词
    # r = requests.post(url, data={'page': 1, 'search': None, 'type[]': 0}, cookies=cookies)
    # 运营敏感词
    # r = requests.post(url, data={'page': 1, 'search': None, 'type[]': 1}, cookies=cookies)
    # 广告敏感词
    # r = requests.post(url, data={'page': 1, 'search': None, 'type[]': 2}, cookies=cookies)
    # 版权敏感词
    r = requests.post(url, data={'page': 1, 'search': None, 'type[]': 3}, cookies=cookies)
    print(r.content.decode(encoding='utf-8'))
    badword_list = r.json()['data']['list']
    for i in range(len(badword_list)):
        print('delete badword id: ' + badword_list[i]['id'])
        r_delete = requests.post(url_del, data={'id': int(badword_list[i]['id'])}, cookies=cookies)
        print(r_delete.content)


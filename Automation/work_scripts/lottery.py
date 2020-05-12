# coding:utf-8

import requests

url = 'https://beta.zhanqi.tv/api/actives/end2018/lottery'

cookies = dict(PHPSESSID='qqs13fh7gsbqbqhbnv2lvkm1hc', ZQ_GUID='2321D35B-F057-0275-F3DB-B404BCF1687A',
               gid='1683694764', tj_uid='111316848')

lottery_length = 1000
for j in range(lottery_length):
    r = requests.post(url, data={'bless': 10}, cookies=cookies)
    badword_list = r.json()['data']['gift']
    print(badword_list)


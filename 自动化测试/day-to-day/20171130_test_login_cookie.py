# coding=utf-8
import requests

'''
# 接口: 获取我的关注的主播列表接口
# 接口地址：http://www.zhanqi.tv/api/user/follow.listsbypage
# module: xxx
# author: caofei@bianfeng.com 2017/11/30
# update: xxx@bianfeng.com 2017/11/30
#         xxx@bianfeng.com 2017/12/01
#         xxx@bianfeng.com 2017/12/09
'''

url = 'http://www.zhanqi.tv/api/user/follow.listsbypage'
payload = {'page': '2', 'num': '8', '_v': '25200430'}
data = {'account': '15068899860', 'password': 'zqcf666'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Content-Length': '195',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'www.zhanqi.tv',
    'Referer': 'https://www.zhanqi.tv/',
    'X-Requested-With': 'XMLHttpRequest'
    }
cookies = dict(PHPSESSID='h4opsotoe8qv112qgb6q4geaf4',
               gid='1777701824', tj_uid='108474802',
               cookie_ip='1944858858,1944858858',
               Hm_lvt_299cfc89fdba155674e083d478408f29='1511863182,1511944454,1512004316',
               zq_check_account='M8899860_o65Gsb',
               Hm_lvt_103ebb1b832fa07afa5ac4eb9d827ce0='1511935372',
               Hm_lpvt_299cfc89fdba155674e083d478408f29='1512021686',
               ZQ_GUID='6BDC0C4B-A1D9-7501-77F6-15418CFA3DDD'
               )
req = requests.post(url, params=payload, data=data, headers=headers, cookies=cookies)
response = req.json()
print(response['code'])
print(response['message'])

followLists = response['data']['list']
listLength = len(followLists)

for i in range(listLength):
    follow = followLists[i]['nickname']
    if follow:
        print(follow)

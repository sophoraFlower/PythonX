# coding: UTF-8

import requests
import re


# 将cookies转换成字典形式，zhihu_cookie为保存的cookie文件，跟程序处在同一路径
# def get_cookie():
#     with open('zhihu_cookie', 'r') as f:
#         cookies = {}
#         for line in f.read().split(';'):
#             name, value = line.strip().split('=', 1)  # 1代表只分割一次
#             cookies[name] = value
#         return cookies

Cookie = {
    'PHPSESSID': 'mc53sgl5d34d0b4pe020qu5n67',
    'gid': '1616550938',
    'cookie_ip': '%2C1944858858',
    'Hm_lvt_299cfc89fdba155674e083d478408f29': '1510904173',
    'Hm_lpvt_299cfc89fdba155674e083d478408f29': '1510905008',
    'top_animate_guide': '1',
    'myLocationCacheKey': '%u6D59%u6C5F%u676D%u5DDE',
    'myIpCacheKey': '115.236.48.234',
    'myIspCacheKey': '%u7535%u4FE1%u5BBD%u5E26',
    'myContryCacheKey': '%u4E2D%u56FD'
    }


s = requests.Session()
url = 'https://apis.zhanqi.tv/auth/user.login'
headers = {
    'User-Agent': 'Mozilla/5.0 Gecko/20100101 Firefox/57.0',
    'Accept': 'application/json, text/javascript, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': ' https://www.zhanqi.tv/'
    }
req2 = s.get(url, headers=headers, cookies=Cookie, verify=False)
html = req2.content


# 将获取到的页面源码写入zhihu.html文件中
with open('zhihu.html', 'w') as fl:
    fl.write(html)


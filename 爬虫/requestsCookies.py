# coding:utf-8
import requests

headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Content-Length": "195",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "www.zhanqi.tv",
        "Referer": "https://www.zhanqi.tv/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
        "X-Requested-With": "XMLHttpRequest",
        }
form_data = {
      'account': '15068899860',
      'password': 'zqcf666',
      'geetest_challenge': '68883d35ca323a7eec984444b9cf52eb',
      'geetest_validate': 'd9495ff3c3a5030952cf9cf0a5ebee96',
      'geetest_seccode': 'd9495ff3c3a5030952cf9cf0a5ebee96%7Cjordan',
     }
req = requests.post('https://www.zhanqi.tv/api/auth/user.login?geetest_ver=3.0&os=0&platform=1', data=form_data, headers=headers)
# get_cookies = []
# for item in req.cookies:
#     print(item)
load_cookies = requests.utils.dict_from_cookiejar(req.cookies)
print(load_cookies)

wait(10000000000000000000000)
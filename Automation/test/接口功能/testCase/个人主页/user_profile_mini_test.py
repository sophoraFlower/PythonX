# -*- coding: utf-8 -*-

import requests
import unittest
import os
import sys
import json
from commentClass import readConfigFile
from commentClass.logger import Logger

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

config = readConfigFile.ReadConfig()
my_log = Logger(logger="UserProfileMini").getlog()

'''
#    -----------------------------------------------------------------------------------------
#    Type：Online
#    Module: 个人主页
#    Interface: https://www.zhanqi.tv/api/user/profile/mini
#    Description: 用户mini信息接口
#    Author: Written by caofei@bianfeng.com
#    Date: 2017/12/19
#    Update: 
#    -----------------------------------------------------------------------------------------
'''


class UserProfileMini(unittest.TestCase):
    """ 用户mini信息接口 """

    def setUp(self):
        self.base = config.get_http_pc(name="base_url")
        self.url = self.base + 'api/user/profile/mini'
        my_log.info('**** ' + self.url + ' ****')

    def test_user_profile_mini_success(self):
        """ 获取成功 """
        self.data = {'uid': 80414943}
        my_log.info("获取成功")
        r = requests.post(self.url, data=self.data)
        self.response_data = r.json()
        self.assertEqual(self.response_data['code'], 0, msg='ERROR: 获取失败')
        self.assertEqual(self.response_data['message'], 'SUCCESS', msg='ERROR: 返回值错误')
        my_log.info(json.dumps(self.response_data, ensure_ascii=False, indent=4))
        print(json.dumps(self.response_data, ensure_ascii=False, indent=4))

    def test_user_profile_mini_all_null(self):
        """ 参数为空 """
        # self.data = {'uid': ''}
        my_log.info("参数为空")
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertEqual(self.response_data['code'], 1001, msg='ERROR: 返回异常值')
        self.assertEqual(self.response_data['message'], '访问对象(UID)错误', msg='ERROR: 返回异常值')
        my_log.info(json.dumps(self.response_data, ensure_ascii=False, indent=4))
        print(json.dumps(self.response_data, ensure_ascii=False, indent=4))

    def tearDown(self):
        my_log.info("--------------------------------------------------------------")


if __name__ == "__main__":
    unittest.main()
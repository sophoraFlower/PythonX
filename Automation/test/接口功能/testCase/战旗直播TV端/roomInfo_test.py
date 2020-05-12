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
my_log = Logger(logger="RoomInfo").getlog()

'''
#    -----------------------------------------------------------------------------------------
#    Type：Online
#    Module: TV
#    Interface: https://apis.zhanqi.tv/static/v2.1/room/{roomid}.json
#    Description: 根据房间ID获取直播间信息
#    Author: Written by caofei@bianfeng.com
#    Date: 2017/10/10
#    Update: 2017/12/19
#    -----------------------------------------------------------------------------------------
'''


class RoomInfo(unittest.TestCase):
    """ 根据房间ID获取直播间信息 """

    def setUp(self):
        self.base = config.get_http_mobile(name="mobile_base_url")
        self.url = self.base + 'static/v2.1/room/'
        my_log.info('**** ' + self.url + ' ****')

    def test_roomInfo_success(self):
        """ 获取成功 """
        self.roomid = '40145'
        my_log.info("获取成功")
        r = requests.post(self.url + self.roomid + '.json')
        self.response_data = r.json()
        self.assertEqual(self.response_data['code'], 0, msg='ERROR:获取失败')
        self.assertEqual(self.response_data['message'], 'OK', msg='ERROR:返回值错误')
        my_log.info(json.dumps(self.response_data, ensure_ascii=False, indent=4))
        print(json.dumps(self.response_data, ensure_ascii=False, indent=4))

    def tearDown(self):
        my_log.info("--------------------------------------------------------------")


if __name__ == '__main__':
    unittest.main()

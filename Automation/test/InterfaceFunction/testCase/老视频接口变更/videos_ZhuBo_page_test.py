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
my_log = Logger(logger="VideosZhuBoPage").getlog()

'''
#    -----------------------------------------------------------------------------------------
#    Type：Online
#    Module: 老视频接口变更
#    Interface: https://www.zhanqi.tv/api/static/v2.2/video/recommend/{uid}/{gameId}/{page}/{nums}.json
#    Description: PC主播页面底部视频接口
#    Author: Written by caofei@bianfeng.com
#    Date: 2017/10/10
#    Update: 2017/12/19
#    -----------------------------------------------------------------------------------------
'''


class VideosZhuBoPage(unittest.TestCase):
    """ PC主播页面底部视频接口 """

    def setUp(self):
        #  https://www.zhanqi.tv/api/static/v2.2/video/recommend/{uid}/{gameId}/{page}/{nums}.json
        self.base = config.get_http_pc(name="base_url")
        self.url = self.base + 'api/static/v2.2/video/recommend/'
        my_log.info('**** ' + self.url + ' ****')

    def test_videosZhuBoPage_success(self):
        """ 获取成功 """
        self.data = {'uid': 100015330, 'gameId': 6, 'page': 1, 'nums': 8}
        uid = str(self.data['uid'])
        game_id = str(self.data['gameId'])
        page = str(self.data['page'])
        nums = str(self.data['nums'])
        my_log.info("获取成功")
        r = requests.post(self.url + uid + '/' + game_id + '/' + page + '/' + nums + '.json')
        self.response_data = r.json()
        self.assertEqual(self.response_data['code'], 0, msg='ERROR:获取失败')
        self.assertEqual(self.response_data['message'], 'SUCCESS', msg='ERROR:返回值错误')
        my_log.info(json.dumps(self.response_data, ensure_ascii=False, indent=4))
        print(json.dumps(self.response_data, ensure_ascii=False, indent=4))

    def tearDown(self):
        my_log.info("--------------------------------------------------------------")


if __name__ == '__main__':
    unittest.main()

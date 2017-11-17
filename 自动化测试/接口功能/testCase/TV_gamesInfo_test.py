# coding: UTF-8

import requests
import unittest
import os
import sys
from framework import readConfigFile
from framework.logger import Logger

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

config = readConfigFile.ReadConfig()
mylog = Logger(logger="GamesInfo").getlog()


class GamesInfo(unittest.TestCase):
    ''' 获取游戏列表 '''

    # https://apis.zhanqi.tv/static/v2.2/tv/games.json
    def setUp(self):
        self.url = 'https://apis.zhanqi.tv/static/v2.2/tv/games.json'
        mylog.info("接口:获取游戏列表，测试开始")

    def tearDown(self):
        mylog.info("接口:获取游戏列表，测试完成")

    def test_gamesInfo_success(self):
        ''' 获取成功 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertEqual(self.response_data['code'], 0, msg='ERROR:获取失败')
        self.assertEqual(self.response_data['message'], 'OK', msg='ERROR:返回值错误')
        print(self.response_data)

    def test_roomInfo_games(self):
        ''' 直播间列表 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertTrue(isinstance(self.response_data['data'], list), msg='ERROR:返回数据类型错误')
        print(self.response_data['data'])
    
    # 直播间列表 - game结构
    def test_roomInfo_img(self):
        ''' 游戏图 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data'][0]['img'], msg='ERROR:游戏图为空')
        print(self.response_data['data'][0])

    def test_roomInfo_id(self):
        ''' 游戏唯一ID '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data'][0]['id'], msg='ERROR:游戏唯一ID错误')
        print(self.response_data['data'][0])

    def test_roomInfo_name(self):
        ''' 游戏名字 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data'][0]['name'], msg='ERROR:游戏名字为空')
        print(self.response_data['data'][0])


if __name__ == '__main__':
    unittest.main()

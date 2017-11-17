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
mylog = Logger(logger="IndexInfo").getlog()


class IndexInfo(unittest.TestCase):
    ''' 首屏数据获取 '''

    # https://apis.zhanqi.tv/static/v2.2/tv/index.json
    def setUp(self):
        self.url = 'https://apis.zhanqi.tv/static/v2.2/tv/index.json'
        mylog.info("接口:首屏数据获取，测试开始")

    def tearDown(self):
        mylog.info("接口:首屏数据获取，测试完成")

    def test_indexInfo_success(self):
        ''' 获取成功 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertEqual(self.response_data['code'], 0, msg='ERROR:获取失败')
        self.assertEqual(self.response_data['message'], 'OK', msg='ERROR:返回值错误')
        print(self.response_data)

    def test_indexInfo_img(self):
        ''' 大背景图片 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['img'], msg='ERROR:大背景图片为空')
        print(self.response_data['data']['img'])

    def test_indexInfo_live(self):
        ''' 主页默认播放直播间 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.response_data_live = self.response_data['data']['live']
        self.rType = isinstance(self.response_data_live, dict)
        self.assertTrue(self.rType, msg='ERROR:返回数据类型错误')
        print(self.response_data['data']['live'])

    def test_indexInfo_gamer(self):
        ''' 百变主页推荐数据 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertTrue(isinstance(self.response_data['data']['gamer'][0], dict), msg='ERROR:返回数据类型错误')
        print(self.response_data['data']['gamer'][0])

    def test_indexInfo_index(self):
        ''' 主页轮播推荐数据 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertTrue(isinstance(self.response_data['data']['index'][0], dict), msg='ERROR:返回数据类型错误')
        print(self.response_data['data']['index'][0])
    
    # 测试百变主页推荐数据
    def test_indexInfo_gamers_id(self):
        ''' 当前直播间ID '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['gamer'][0]['id'], msg='ERROR:直播间ID为空')
        print(self.response_data['data']['gamer'][0]['id'])

    def test_indexInfo_gamers_img(self):
        ''' 当前直播间配图 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['gamer'][0]['img'], msg='ERROR:直播间配图为空')
        print(self.response_data['data']['gamer'][0]['img'])

    def test_indexInfo_gamers_title(self):
        ''' 直播间标题 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['gamer'][0]['title'], msg='ERROR:直播间标题为空')
        print(self.response_data['data']['gamer'][0]['title'])

    def test_indexInfo_gamers_nickname(self):
        ''' 当主播昵称 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['gamer'][0]['nickname'], msg='ERROR:主播昵称为空')
        print(self.response_data['data']['gamer'][0]['nickname'])

    def test_indexInfo_gamers_cdns(self):
        ''' 直播间拉流线路信息 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['gamer'][0]['line'], msg='ERROR:直播间拉流线路信息为空')
        print(self.response_data['data']['gamer'][0]['line'])

    def test_indexInfo_gamers_online(self):
        ''' 直播间在线人数 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['gamer'][0]['online'], msg='ERROR:直播间在线人数为空')
        print(self.response_data['data']['gamer'][0]['online'])

    def test_indexInfo_gamers_status(self):
        ''' 直播状态 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertEqual(self.response_data['data']['gamer'][0]['status'], 4, msg='ERROR:开播状态错误')
        print(self.response_data['data']['gamer'][0]['status'])
    
    # 测试主页轮播推荐数据
    def test_indexInfo_index_id(self):
        ''' 当前直播间ID '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['index'][0]['id'], msg='ERROR:直播间ID为空')
        print(self.response_data['data']['index'][0]['id'])

    def test_indexInfo_index_img(self):
        ''' 当前直播间配图 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['index'][0]['img'], msg='ERROR:直播间配图为空')
        print(self.response_data['data']['index'][0]['img'])

    def test_indexInfo_index_title(self):
        ''' 直播间标题 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['index'][0]['title'], msg='ERROR:直播间标题为空')
        print(self.response_data['data']['index'][0]['title'])

    def test_indexInfo_index_nickname(self):
        ''' 当主播昵称 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['index'][0]['nickname'], msg='ERROR:主播昵称为空')
        print(self.response_data['data']['index'][0]['nickname'])

    def test_indexInfo_index_cdns(self):
        ''' 直播间拉流线路信息 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['index'][0]['line'], msg='ERROR:直播间拉流线路信息为空')
        print(self.response_data['data']['index'][0]['line'])

    def test_indexInfo_index_online(self):
        ''' 直播间在线人数 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['index'][0]['online'], msg='ERROR:直播间在线人数为空')
        print(self.response_data['data']['index'][0]['online'])

    def test_indexInfo_index_status(self):
        ''' 直播状态 '''
        r = requests.get(self.url)
        self.response_data = r.json()
        self.assertEqual(self.response_data['data']['index'][0]['status'], 4, msg='ERROR:开播状态错误')
        print(self.response_data['data']['index'][0]['status'])


if __name__ == '__main__':
    unittest.main()

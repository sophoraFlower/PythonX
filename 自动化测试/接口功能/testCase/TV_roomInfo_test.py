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
mylog = Logger(logger="RoomInfo").getlog()

# roomid 直播间id


class RoomInfo(unittest.TestCase):
    ''' 根据房间ID获取直播间信息 '''

    # https://apis.zhanqi.tv/static/v2.1/room/{roomid}.json
    def setUp(self):
        self.roomid = '40145'
        self.url = 'https://apis.zhanqi.tv/static/v2.1/room/' + self.roomid + '.json'
        mylog.info("接口:根据房间ID获取直播间信息，测试开始")

    def tearDown(self):
        mylog.info("接口:根据房间ID获取直播间信息，测试完成")

    def test_roomInfo_success(self):
        ''' 获取成功 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.assertEqual(self.response_data['code'], 0, msg='ERROR:获取失败')
        self.assertEqual(self.response_data['message'], 'OK', msg='ERROR:返回值错误')
        print(self.response_data)

    def test_roomInfo_id(self):
        ''' 直播间id '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.assertEqual(self.response_data['data']['id'], '40145', msg='ERROR:直播间id返回值为空')
        print(self.response_data['data']['id'])

    def test_roomInfo_uid(self):
        ''' 主播id '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.assertEqual(self.response_data['data']['uid'], '104814802', msg='ERROR:主播id返回值为空')
        print(self.response_data['data']['uid'])

    def test_roomInfo_nickname(self):
        ''' 主播昵称 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.assertEqual(self.response_data['data']['nickname'], '死亡宣告丶vasilii', msg='ERROR:主播昵称错误')
        print(self.response_data['data']['nickname'])

    def test_roomInfo_gender(self):
        ''' 主播性别（1，女；2，男） '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.assertEqual(self.response_data['data']['gender'], '2', msg='ERROR:主播性别错误')
        print(self.response_data['data']['gender'])

    def test_roomInfo_avatar(self):
        ''' 主播头像地址 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['avatar'], msg='ERROR:头像地址为空')
        print(self.response_data['data']['avatar'])

    def test_roomInfo_url(self):
        ''' 房间地址 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.assertEqual(self.response_data['data']['url'], '/1145620', msg='ERROR:主播房间地址错误')
        print(self.response_data['data']['url'])

    def test_roomInfo_title(self):
        ''' 房间标题 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['title'], msg='ERROR:房间标题不存在')
        print(self.response_data['data']['title'])

    def test_roomInfo_gameId(self):
        ''' 游戏id '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.assertEqual(self.response_data['data']['gameId'], '6', msg='ERROR:游戏id错误')
        print(self.response_data['data']['gameId'])

    def test_roomInfo_videoId(self):
        ''' 流名 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.assertEqual(self.response_data['data']['videoId'], '40145_cWcrH', msg='ERROR:流名错误')
        print(self.response_data['data']['videoId'])

    def test_roomInfo_spic(self):
        ''' 直播截图小图 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['spic'], msg='ERROR:直播截图小图不存在')
        print(self.response_data['data']['spic'])

    def test_roomInfo_bpic(self):
        ''' 直播截图大图 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['bpic'], msg='ERROR:直播截图大图不存在')
        print(self.response_data['data']['bpic'])

    def test_roomInfo_online(self):
        ''' 在线人数 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['online'], msg='ERROR:在线人数异常')
        print(self.response_data['data']['online'])

    def test_roomInfo_status(self):
        ''' 直播间状态（4:直播,其他:休息） '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.assertEqual(self.response_data['data']['status'], '0', msg='ERROR:直播状态错误')
        print(self.response_data['data']['status'])

    def test_roomInfo_gameName(self):
        ''' 游戏名 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.assertEqual(self.response_data['data']['gameName'], '英雄联盟', msg='ERROR:游戏名错误')
        print(self.response_data['data']['gameName'])

    def test_roomInfo_gameUrl(self):
        ''' 游戏分类URL '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.assertEqual(self.response_data['data']['gameUrl'], '/games/lol', msg='ERROR:游戏分类URL错误')
        print(self.response_data['data']['gameUrl'])

    def test_roomInfo_gameInco(self):
        ''' 游戏Icon '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['gameIcon'], msg='ERROR:游戏Icon不存在')
        print(self.response_data['data']['gameIcon'])

    def test_roomInfo_follows(self):
        ''' 订阅数 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['follows'], msg="ERROR:订阅数据异常")
        print(self.response_data['data']['follows'])


if __name__ == '__main__':
    unittest.main()

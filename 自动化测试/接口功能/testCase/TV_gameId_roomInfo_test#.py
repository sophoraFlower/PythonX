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
mylog = Logger(logger="GameIdRoomInfo").getlog()

# roomid 直播间id


class GameIdRoomInfo(unittest.TestCase):
    ''' 获取具体某个游戏下的直播间列表 '''

    # https://apis.zhanqi.tv/static/v2.1/game/live/{gameid}/{nums}/{page}.json
    def setUp(self):
        self.gameId = 6
        self.nums = 1
        self.page = 1
        self.url = 'https://apis.zhanqi.tv/static/v2.1/game/live/' + 'gamId/' + 'nums/' + 'page' + '.json'
        mylog.info("接口:获取具体某个游戏下的直播间列表，测试开始")

    def tearDown(self):
        mylog.info("接口:获取具体某个游戏下的直播间列表，测试完成")

    def test_gameIdRoomInfo_success(self):
        ''' 获取成功 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.assertEqual(self.response_data['code'], 0)
        self.assertEqual(self.response_data['message'], 'OK')
        print(self.response_data)

    def test_gameIdRoomInfo_id(self):
        ''' 直播间id '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.roomInfo = self.response_data['data']['rooms'][0]
        self.assertTrue(self.roomInfo['id'], msg="ERROR:XXX")
        print(self.roomInfo['id'])

    def test_gameIdRoomInfo_uid(self):
        ''' 主播id '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.roomInfo = self.response_data['data']['rooms'][0]
        self.assertTrue(self.roomInfo['uid'], msg="ERROR:XXX")
        print(self.roomInfo['uid'])

    def test_gameIdRoomInfo_nickname(self):
        ''' 主播昵称 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.roomInfo = self.response_data['data']['rooms'][0]
        self.assertTrue(self.roomInfo['nickname'], msg="ERROR:XXX")
        print(self.roomInfo['nickname'])

    def test_gameIdRoomInfo_gender(self):
        ''' 主播性别（1，女；2，男） '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.roomInfo = self.response_data['data']['rooms'][0]
        self.assertTrue(self.roomInfo['gender'], msg="ERROR:XXX")
        print(self.roomInfo['gender'])

    def test_gameIdRoomInfo_avatar(self):
        ''' 主播头像地址 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.roomInfo = self.response_data['data']['rooms'][0]
        self.assertTrue(self.roomInfo['avatar'], msg="ERROR:XXX")
        print(self.roomInfo['avatar'])

    def test_gameIdRoomInfo_url(self):
        ''' 房间地址 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.roomInfo = self.response_data['data']['rooms'][0]
        self.assertTrue(self.roomInfo['url'], msg="ERROR:XXX")
        print(self.roomInfo['url'])

    def test_gameIdRoomInfo_title(self):
        ''' 房间标题 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.roomInfo = self.response_data['data']['rooms'][0]
        self.assertTrue(self.roomInfo['title'], msg="ERROR:XXX")
        print(self.roomInfo['title'])

    def test_gameIdRoomInfo_gameId(self):
        ''' 游戏id '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.roomInfo = self.response_data['data']['rooms'][0]
        self.assertTrue(self.roomInfo['gameId'], msg="ERROR:XXX")
        print(self.roomInfo['gameId'])

    def test_gameIdRoomInfo_videoId(self):
        ''' 流名 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.roomInfo = self.response_data['data']['rooms'][0]
        self.assertTrue(self.roomInfo['videoId'], '40145_cWcrH')
        print(self.roomInfo['videoId'])

    def test_gameIdRoomInfo_spic(self):
        ''' 直播截图小图 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.roomInfo = self.response_data['data']['rooms'][0]
        self.assertTrue(self.roomInfo['spic'], msg="ERROR:XXX")
        print(self.roomInfo['spic'])

    def test_gameIdRoomInfo_bpic(self):
        ''' 直播截图大图 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.assertTrue(self.response_data['data']['rooms']['bpic'], msg="ERROR:XXX")
        print(self.roomInfo['bpic'])

    def test_gameIdRoomInfo_online(self):
        ''' 在线人数 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.roomInfo = self.response_data['data']['rooms'][0]
        self.assertTrue(self.roomInfo['online'], msg="ERROR:XXX")
        print(self.roomInfo['online'])

    def test_gameIdRoomInfo_status(self):
        ''' 直播间状态（4:直播,其他:休息） '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.roomInfo = self.response_data['data']['rooms'][0]
        self.assertTrue(self.roomInfo['status'], msg="ERROR:XXX")
        print(self.roomInfo['status'])

    def test_gameIdRoomInfo_gameName(self):
        ''' 游戏名 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.roomInfo = self.response_data['data']['rooms'][0]
        self.assertTrue(self.roomInfo['gameName'], msg="ERROR:XXX")
        print(self.roomInfo['gameName'])

    def test_gameIdRoomInfo_gameUrl(self):
        ''' 游戏分类URL '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.roomInfo = self.response_data['data']['rooms'][0]
        self.assertTrue(self.roomInfo['gameUrl'], msg="ERROR:XXX")
        print(self.roomInfo['gameUrl'])

    def test_gameIdRoomInfo_gameInco(self):
        ''' 游戏Icon '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.roomInfo = self.response_data['data']['rooms'][0]
        self.assertTrue(self.roomInfo['gameIcon'], msg='ERROR:游戏Icon不存在')
        print(self.roomInfo['gameIcon'])

    def test_gameIdRoomInfo_follows(self):
        ''' 订阅数 '''
        r = requests.post(self.url)
        self.response_data = r.json()
        self.roomInfo = self.response_data['data']['rooms'][0]
        self.assertTrue(self.roomInfo['follows'], msg="ERROR:订阅数据异常")
        print(self.roomInfo['follows'])


if __name__ == '__main__':
    unittest.main()

# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time

'''
##########################################################
#    module:  
#    abstract: 
#    description:
#    ----------------------------------------------------
#    依赖：已登录
#        1.打开战旗直播首页
#        2.选择第一个推荐位直播间，并进入
#        3.打开背包
#        4.查找打call礼物，存在就发送*30;不存在就关闭背包
#        5.关闭浏览器（可选）
#    ----------------------------------------------------
#    author: Written by caofei@bianfeng.com
#    date: 2017/12/21
#    update:
##########################################################
'''


class BagsPropsSendCall(unittest.TestCase):

    def setUp(self):
        self.driverOptions = webdriver.ChromeOptions()
        # 浏览器本地存储数据地址:cookie等信息
        # home chrome
        # self.driverOptions.add_argument(r"user-data-dir=C:\Users\Houle\AppData\Local\Google\Chrome\User Data")
        # work chrome
        self.driverOptions.add_argument(r"user-data-dir=C:\Users\caofei\AppData\Local\Google\Chrome\User Data")
        self.browser = webdriver.Chrome('chromedriver', 0, self.driverOptions)
        self.browser.maximize_window()
        self.browser.implicitly_wait(3)

    def test_bagsPropsSendCall(self):
        self.browser.get('https://www.zhanqi.tv/')

        # 选定首页推荐位第一个直播间
        self.browser.find_element_by_xpath('//*[@id="video_carousel"]/li[1]').click()
        time.sleep(4)

        # 进入该直播间
        self.browser.find_element_by_xpath('//*[@id="BFPlayerID"]').click()
        print('pass: into BroadcastRoom!')
        self.browser.implicitly_wait(6)

        # 关掉引导提示，无的话直接进入下一步
        room_guide = self.browser.find_elements_by_class_name('im—room-guide')
        if len(room_guide) != 0:
            self.browser.find_element_by_xpath('//*[@id="js-right-chat-panel"]/div[2]/div[2]/a').click()
        else:
            pass
        time.sleep(2)

        # 打开背包
        self.browser.find_element_by_xpath('//*[@id="js-room-gift-area"]/div/ul').click()

        # 查找打call礼物，存在就发送*30;不存在就关闭背包
        props = self.browser.find_elements_by_class_name('js-prop-item')
        for i in range(0, len(props)):
            # 鼠标移到悬停元素上
            ActionChains(self.browser).move_to_element(props[i]).perform()
            time.sleep(3)
            prop_name = self.browser.find_element_by_class_name('js-prop-name').text
            if prop_name == '打call':
                prop_num = int(self.browser.find_element_by_class_name('js-prop-use-cnt-txt').text)
                for j in range(0, prop_num):
                    self.browser.find_element_by_class_name('js-use-btn').click()
                    print("send gift is success! 0" + str(j))
                    time.sleep(4)
                    ActionChains(self.browser).move_to_element(props[i]).perform()
                    if j == 30:
                        break
                    else:
                        continue
            else:
                pass
        self.browser.implicitly_wait(3)
        self.browser.find_element_by_xpath('//*[@id="js-room-gift-area"]/div/ul').click()
        time.sleep(2)

    def tearDown(self):

        # 关闭窗口和浏览器
        self.browser.close()
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()


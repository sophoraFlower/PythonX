# coding=utf-8
from selenium import webdriver
import unittest
import time

'''
##########################################################
#    module:  
#    abstract: barrage hot-word 
#    description:
#    ----------------------------------------------------
#    依赖：需要先执行thirdParty_sign_on_by_wb_UItest.py
#        1.打开战旗直播首页
#        2.进入指定直播间直播间，并进入
#        3.关掉引导提示（无的话直接进行下一步）
#        4.发送弹幕-逐一发送热词
#        5.判断热词弹幕是否发送成功
#        6.关闭浏览器
#    ----------------------------------------------------
#    author: Written by caofei@bianfeng.com
#    date: 2018/04/02
#    update:
##########################################################
'''


class SendBarrageByHotWord(unittest.TestCase):

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

    def test_SendBarrageByHotWord(self):

        self.browser.get('http://beta.zhanqi.tv/11134')
        time.sleep(8)

        e_window = self.browser.find_element_by_xpath('/html/body/div[15]/a')
        try:
            e_window.click()
            print('pass: @@@@@@@@@@@@@@@@@ !')
        except Exception as e:
            print('Exception found:', format(e))
        time.sleep(4)
        # 打开热词弹窗，逐一发送弹幕热词，时间间隔2s
        hw_window = self.browser.find_element_by_xpath('//*[@id="js-chat-control-panel"]/div[3]/div[1]/a')
        try:
            hw_window.click()
            print('pass: open hot-word window success!')
        except Exception as e:
            print('Exception found:', format(e))

        hot_word_lists = self.browser.find_elements_by_class_name('js-hot-word-item')
        hw_lists_length = len(hot_word_lists)
        for hot_word in hot_word_lists:
            print(hot_word.text)
        time.sleep(2)
        hw_window.click()
        print('打印热词列表长度！' + str(hw_lists_length))

        for i in range(0, hw_lists_length):
            print('########### start send hot word ! ###########')
            hw_window.click()
            time.sleep(2)
            hot_word_lists = self.browser.find_elements_by_class_name('js-hot-word-item')
            hot_word_lists[i].click()
            time.sleep(2)

        time.sleep(4)
        for i in range(0, 1000):
            print('########### start send hot word ! ###########')
            hw_window.click()
            time.sleep(2)
            hot_word_lists = self.browser.find_elements_by_class_name('js-hot-word-item')
            hot_word_lists[2].click()
            time.sleep(2)

    def tearDown(self):

        wb_title = self.browser.title
        print('**********' + wb_title + '**********')
        time.sleep(5)

        # 关闭窗口和浏览器
        self.browser.close()
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()


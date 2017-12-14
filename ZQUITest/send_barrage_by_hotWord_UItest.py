# coding=utf-8
from selenium import webdriver
import unittest
import time

'''
    1.打开战旗直播首页
    2.选择第一个推荐位直播间，并进入
    3.关掉引导提示（无的话直接进行下一步）
    4.发送弹幕-逐一发送热词
    5.判断热词弹幕是否发送成功
    6.关闭浏览器
'''


class SendBarrageByHotWord(unittest.TestCase):

    def setUp(self):
        self.driverOptions = webdriver.ChromeOptions()
        # home
        # self.driverOptions.add_argument(r"user-data-dir=C:\Users\Houle\AppData\Local\Google\Chrome\User Data")
        # work
        self.driverOptions.add_argument(r"user-data-dir=C:\Users\caofei\AppData\Local\Google\Chrome\User Data")
        self.browser = webdriver.Chrome('chromedriver', 0, self.driverOptions)
        self.browser.maximize_window()
        self.browser.implicitly_wait(3)

    def test_signOnByWB(self):
        self.browser.get('https://www.zhanqi.tv/')

        # 选定首页推荐位第一个直播间
        try:
            self.browser.find_element_by_xpath('//*[@id="video_carousel"]/li[1]').click()
            print('pass: select first BroadcastRoom success!')
        except Exception as e:
            print('Exception found:', format(e))
        time.sleep(2)

        # 进入该直播间
        try:
            self.browser.find_element_by_xpath('//*[@id="BFPlayerID"]').click()
            print('pass: into BroadcastRoom success!')
        except Exception as e:
            print('Exception found:', format(e))
        self.browser.implicitly_wait(6)

        # 关掉引导提示，无的话直接进入下一步
        room_guide = self.browser.find_elements_by_class_name('im—room-guide')
        if len(room_guide) != 0:
            self.browser.find_element_by_xpath('//*[@id="js-right-chat-panel"]/div[2]/div[2]/a').click()
        else:
            pass
        time.sleep(2)

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

        # 判断热词弹幕是否发送成功
        # myself_barrage_lists = self.browser.find_elements_by_class_name('js-chat-list-li myself')
        # mbr_lists_length = len(myself_barrage_lists)
        # for i in range(0, mbr_lists_length):
        #     print(myself_barrage_lists[i].text)

    def tearDown(self):

        wb_title = self.browser.title
        print('**********' + wb_title + '**********')
        time.sleep(5)

        # 关闭窗口和浏览器
        self.browser.close()
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()


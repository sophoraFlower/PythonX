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
#        4.查找“每日初级日常礼盒”、“中级日常礼盒”、“高级日常礼盒”
#        5.打开对于的礼盒
#        6.汇总当前背包中各类礼物
#        7.关闭浏览器
#    ----------------------------------------------------
#    author: Written by caofei@bianfeng.com
#    date: 2017/12/22
#    update:
##########################################################
'''


class OpenBagsGifts(unittest.TestCase):

    def setUp(self):
        self.driverOptions = webdriver.ChromeOptions()
        # 浏览器本地存储数据地址:cookie等信息
        # home chrome
        self.driverOptions.add_argument(r"user-data-dir=C:\Users\Houle\AppData\Local\Google\Chrome\User Data")
        # work chrome
        # self.driverOptions.add_argument(r"user-data-dir=C:\Users\caofei\AppData\Local\Google\Chrome\User Data")
        self.browser = webdriver.Chrome('chromedriver', 0, self.driverOptions)
        self.browser.maximize_window()
        self.browser.implicitly_wait(3)

    def test_openBagsGifts(self):
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

        # 查找“每日初级日常礼盒”、“中级日常礼盒”、“高级日常礼盒”
        props = self.browser.find_elements_by_class_name('js-prop-item')
        self.day_gift = False
        for i in range(0, len(props)):
            if self.day_gift:
                # 鼠标移到悬停元素上
                ActionChains(self.browser).move_to_element(props[i-1]).perform()
            else:
                ActionChains(self.browser).move_to_element(props[i]).perform()
            time.sleep(3)
            prop_name = self.browser.find_element_by_class_name('js-prop-name').text
            prop_num = self.browser.find_element_by_class_name('js-prop-use-cnt-txt').text
            print("***** " + prop_name + " ****** " + prop_num)

            # 此处需要优化，打开日常礼盒后，顺序发生变化，待修改
            if prop_name in ['初级日常礼盒', '中级日常礼盒', '高级日常礼盒']:
                self.day_gift = True
                self.browser.find_element_by_class_name('js-use-btn').click()
                ibox_window = self.browser.find_element_by_class_name('iboxMsg')

                # 鼠标移到悬停元素上
                ActionChains(self.browser).move_to_element(ibox_window).perform()
                ibox_message = ibox_window.find_element_by_tag_name('p').text
                print(ibox_message)
                ibox_window.find_element_by_class_name('btn').click()
                print("open 初级日常礼盒 is success!")
                time.sleep(2)
            else:
                self.day_gift = False
                pass
        self.browser.implicitly_wait(3)

    def tearDown(self):

        # 关闭窗口和浏览器
        self.browser.close()
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()


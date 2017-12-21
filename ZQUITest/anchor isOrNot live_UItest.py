# coding=utf-8
from selenium import webdriver
import unittest
import time

'''
##########################################################
#    module:  myFocus 小乌云丶
#    abstract:
#    description:
#    ----------------------------------------------------
#    依赖/前置条件：已登录
#        1.进入战旗首页
#        2.进入个人中心 > 我的关注 
#        3.找到已关注主播（小乌云丶）
#        4.获取主播头像
#        5.截取当前主播头像
#        6.截图对比，判断主播是否在直播
#        7.直播状态，进入该直播间；未直播，默认直接进入“我的关注”第一个直播间
#        8.退出登录（可选），并关闭浏览器
#    ----------------------------------------------------
#    author: Written by caofei@bianfeng.com
#    date: 2017/12/21
#    update:
##########################################################
'''


class AnchorIsOrNotLive(unittest.TestCase):

    def setUp(self):
        self.driverOptions = webdriver.ChromeOptions()
        # 浏览器本地存储数据地址
        # home
        # self.driverOptions.add_argument(r"user-data-dir=C:\Users\Houle\AppData\Local\Google\Chrome\User Data")
        # work
        self.driverOptions.add_argument(r"user-data-dir=C:\Users\caofei\AppData\Local\Google\Chrome\User Data")
        self.browser = webdriver.Chrome('chromedriver', 0, self.driverOptions)
        self.browser.maximize_window()
        self.browser.implicitly_wait(3)

    def test_anchorIsOrNotLive(self):
        # 进入战旗首页
        self.browser.get('https://www.zhanqi.tv/')

        # 进入我的关注
        print('sign in my focus')
        self.browser.find_element_by_link_text('关注').click()
        time.sleep(2)

        # 清除浏览记录
        print('clear watch record!')
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.browser.find_element_by_link_text('清除全部').click()
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/div[6]/div[2]/button[1]').click()
        time.sleep(3)
        self.browser.refresh()
        time.sleep(3)

        # 找到小乌云主播
        self.browser.execute_script("window.scrollTo(0, -200);")
        self.isExist = False
        my_focus_lists_page = self.browser.find_elements_by_class_name('pageItem')
        mf_lists_length = len(my_focus_lists_page)
        for i in range(1, mf_lists_length-1):
            time.sleep(3)
            my_focus_lists_page[i].click()
            xiao_wu_yun = self.browser.find_elements_by_link_text('小乌云丶')
            if len(xiao_wu_yun):
                self.isExist = True
                print('pass: I find xiaowuyun!')
                break
            else:
                continue

        # 查看直播间状态
        if self.isExist:
            pass
            my_focus_lists = self.browser.find_elements_by_class_name('js-follow-item')
            my_focus_live_lists = self.browser.find_elements_by_class_name('done-play')
            mf_lists_length = len(my_focus_lists)
            mf_live_lists_length = len(my_focus_live_lists)
            self.list_index = 0
            self.live_list_index = 0
            for i in range(0, mf_lists_length):
                time.sleep(2)
                xiao_wu_yun = my_focus_lists[i].find_elements_by_link_text('小乌云丶')
                if len(xiao_wu_yun):
                    self.list_index = i
                else:
                    pass
            for j in range(0, mf_live_lists_length):
                time.sleep(2)
                xiao_wu_yun_live = my_focus_lists[j].find_elements_by_link_text('小乌云丶')
                if len(xiao_wu_yun_live):
                    self.live_list_index = j
                else:
                    pass

            if self.list_index == self.live_list_index:
                self.browser.find_element_by_link_text('小乌云丶').click()
                print("小乌云在直播啦！快去观看吧！")
            else:
                pass
                print("小乌云不在直播！换别家吧！")
                # 默认直接进入“我的关注”第一个直播间，一般为直播
                self.browser.refresh()
                self.browser.find_elements_by_class_name('js-follow-item')[0].click()

        else:
            pass

    def tearDown(self):
        self.browser.execute_script("window.scrollTo(document.body.scrollWidth, 0);")
        self.browser.refresh()
        time.sleep(3)

        # 获取当前浏览器所有的窗口
        handles = self.browser.window_handles

        # 依次关闭所有打开页面
        for i in range(len(handles)):
            self.browser.switch_to.window(handles[i])
            self.browser.close()


if __name__ == "__main__":
    unittest.main()
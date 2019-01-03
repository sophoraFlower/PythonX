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
#        4.进入直播直播间
#        5.退出登录（可选），并关闭浏览器
#    ----------------------------------------------------
#    author: Written by caofei@bianfeng.com
#    date: 2017/12/18
#    update:
##########################################################
'''


class MyFocusWUYUN(unittest.TestCase):

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

    def test_myFocusWUYUN(self):
        # 进入战旗首页
        self.browser.get('https://www.zhanqi.tv/')

        # 进入我的关注
        try:
            self.browser.find_element_by_link_text('关注').click()
            print('pass: sign in my focus is success!')
        except Exception as e:
            print('Exception found:', format(e))
        time.sleep(2)

        # 清除浏览记录
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        try:
            self.browser.find_element_by_link_text('清除全部').click()
            print('pass: start clear watch record!')
        except Exception as e:
            print('Exception found:', format(e))
        time.sleep(3)

        try:
            self.browser.find_element_by_xpath('/html/body/div[6]/div[2]/button[1]').click()
            print('pass: clearing watch record!')
        except Exception as e:
            print('Exception found:', format(e))
        time.sleep(3)
        self.browser.refresh()
        time.sleep(3)

        watch_record = self.browser.find_element_by_xpath('//*[@id="js-history-panel"]/div[2]/div[2]/span')
        if watch_record:
            print('pass: clear record is success!')
            time.sleep(2)
        else:
            pass
        time.sleep(3)

        # 找到小乌云主播,并进入直播间(关注列表里确定要有该主播，负责直接报error)
        self.browser.execute_script("window.scrollTo(0, -200);")
        my_focus_lists = self.browser.find_elements_by_class_name('pageItem')
        mf_lists_length = len(my_focus_lists)
        for i in range(1, mf_lists_length-1):
            time.sleep(3)
            my_focus_lists[i].click()
            xiao_wu_yun = self.browser.find_elements_by_link_text('小乌云丶')
            if len(xiao_wu_yun):
                xiao_wu_yun[0].click()
                print('pass: I find xiaowuyun!')
                break
            else:
                continue

        # 查看直播间状态

    def tearDown(self):
        self.browser.execute_script("window.scrollTo(document.body.scrollWidth, 0);")
        self.browser.refresh()
        time.sleep(3)

        # 获取当前浏览器所有的窗口
        handles = self.browser.window_handles

        # 切换回最初打开的窗口
        self.browser.switch_to.window(handles[0])
        self.browser.close()

        # 窗口切换，切换为新打开的窗口
        self.browser.switch_to.window(handles[-1])
        self.browser.close()

        # 关闭所有窗口
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
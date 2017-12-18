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
            self.browser.find_elements_by_link_text('关注').click()
            print('pass: sign in my focus is success!')
            self.assertTrue(len(login_ele), msg='登录失败')
        except Exception as e:
            print('Exception found:', format(e))
        time.sleep(2)
        
        # 跳转第三方-微博账号登录窗口
        try:
            self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/div[2]/div/div/ul/li[3]/a/i[1]').click()
            print('pass: wb login window success!')
        except Exception as e:
            print('Exception found:', format(e))
        time.sleep(10)

        # 获取所有窗口句柄
        all_handles = self.browser.window_handles

        for handle in all_handles:
            if handle == self.now_handle:
                # 切换页面
                self.browser.switch_to.window(handle)
                # 输入微博账号和密码
                try:
                    # 使用会员账号(zhanqitv2017@sina.com 2017@zhanqiTV)
                    self.browser.find_element_by_xpath('//*[@id="userId"]').send_keys('zhanqitv2017@sina.com')
                    print('pass: input account success!')
                except Exception as e:
                    print('Exception found:', format(e))
                time.sleep(2)

                try:
                    self.browser.find_element_by_xpath('//*[@id="passwd"]').send_keys('2017@zhanqiTV')
                    print('pass: input password success!')
                except Exception as e:
                    print('Exception found:', format(e))
                time.sleep(2)

                '''是否进入战旗主页'''
                try:
                    self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div/div[2]/div/p/a[1]').click(
                    )
                    print('pass: into zhanqiTV page is success!')
                    title = self.browser.title
                    self.assertEqual(title, '网站连接 - 战旗直播平台', msg='第三方登陆失败!')
                except Exception as e:
                    print('Exception found:', format(e))
                time.sleep(1)

                '''是否登陆成功'''
                try:
                    login_ele = self.browser.find_elements_by_link_text('账号')
                    print('pass: sign on zhanqiTV is success!')
                    self.assertTrue(len(login_ele), msg='登录失败')
                except Exception as e:
                    print('Exception found:', format(e))
                time.sleep(3)

    def tearDown(self):

        self.browser.refresh()
        time.sleep(2)

        # 关闭窗口和浏览器
        self.browser.close()
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
# coding=utf-8
from selenium import webdriver
import unittest
import time

'''
############################################################################################
#    module:  
#    abstract: third-party sign-on weibo
#    description:
#    -------------------------------------------------------------------------------------
#        依赖/前置条件：当前chrome浏览器未登录展期，第三方登录（微博）账号为新浪邮箱，且已绑定战旗手机账号
#        账号信息： 微博账号：account：zhanqitv2017@sina.com passwd: 2017@zhanqiTV 15068890000
#        1.打开战旗直播首页（未登录）
#        2.使用第三方登录-微博账号登录（微博账号推荐新浪邮箱注册的账号，并绑定对应战旗账号）
#        3.登陆成功
#        4.可进入战旗首页，做任意操作(UI测试)
#        5.可进去新浪微博首页，做任意操作(不可频繁登录，微博这边容易封IP)
#        6.关闭浏览器
#    -------------------------------------------------------------------------------------
#    author: Written by caofei@bianfeng.com
#    date: 2017/12/14
#    update:
############################################################################################
'''


class ThirdPartySignOnByWB(unittest.TestCase):

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

    def test_signOnByWB(self):
        self.browser.get('https://www.zhanqi.tv/')

        # 获取当前窗口句柄
        self.now_handle = self.browser.current_window_handle

        # 获得cookie信息
        # cookie = self.browser.get_cookies()
        # print(cookie)

        # 遍历打印cookies中的name和value信息
        # for cookie in browser.get_cookies():
        #    print("%s -> %s" % (cookie['name'], cookie['value']))

        # 打开登录窗口
        try:
            self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[1]/ul/li[1]/a/span').click()
            print('pass: login window success!')
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

        # 进入新浪微博首页
        # self.browser.implicitly_wait(3)
        # self.browser.get('https://weibo.com/')
        # wb_title = self.browser.title
        # print('**********' + wb_title + '**********')

        # 关闭窗口和浏览器
        self.browser.close()
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
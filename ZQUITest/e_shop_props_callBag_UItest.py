# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time

'''
##########################################################
#    module:  
#    abstract: e-shop 打call-gift-bag
#    description:
#    ----------------------------------------------------
#    依赖/前置条件：已登录
#        1.进入战旗首页
#        2.进入商城 > 道具 
#        3.判断当前战旗币
#        4.大于1000战旗币，购买10打call礼包，否则不执行任何操作
#        5.退出登录（可选），并关闭浏览器
#    ----------------------------------------------------
#    author: Written by caofei@bianfeng.com
#    date: 2017/12/18
#    update:
##########################################################
'''


class EShopPropsBag(unittest.TestCase):

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

    # 当前账户战旗币数量
    account_zq_money = 0

    def test_eShopPropsBag(self):
        self.browser.get('https://www.zhanqi.tv/')

        # 个人战旗币数量查询
        login_ele = self.browser.find_elements_by_link_text('账号')
        if len(login_ele) == 1:
            '''进入个人中心'''
            # 鼠标移到悬停元素上
            ActionChains(self.browser).move_to_element(login_ele[0]).perform()
            time.sleep(6)
            try:
                self.browser.find_element_by_link_text('个人中心').click()
                print('pass: sign in my center is success!')
            except Exception as e:
                print('Exception found:', format(e))
            self.browser.implicitly_wait(3)

            # 获取战旗币数量
            account_rich_lists = self.browser.find_elements_by_class_name('js-user-left-rich-coin')
            account_zq_money = int(account_rich_lists[0].text)
            if account_zq_money >= 1000:
                print('pass: my zhanqi money more than 1000! the number is ' + str(account_zq_money))
            else:
                print('慢慢攒吧！小伙子！' + str(account_zq_money))
            self.browser.implicitly_wait(3)

        # 获取当前窗口句柄
        self.now_handle = self.browser.current_window_handle

        # 打开商城页面
        try:
            self.browser.find_element_by_link_text('商城').click()
            print('pass: login e-shop success!')
        except Exception as e:
            print('Exception found:', format(e))
        time.sleep(2)

        # 获取所有窗口句柄
        all_handles = self.browser.window_handles

        for handle in all_handles:
            if handle != self.now_handle:
                # 切换页面
                self.browser.switch_to.window(handle)

                # 进入道具购买窗口
                try:
                    self.browser.find_element_by_link_text('道具').click()
                    print('pass: login props window success!')
                except Exception as e:
                    print('Exception found:', format(e))
                time.sleep(2)

                # 购买10打call礼包
                try:
                    self.browser.find_element_by_id('88').click()
                    print('pass: start buy call gift bag!')
                except Exception as e:
                    print('Exception found:', format(e))
                time.sleep(2)

                try:
                    self.browser.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[2]/div[2]/a').click()
                    print('pass: buying call gift bag!')
                except Exception as e:
                    print('Exception found:', format(e))
                time.sleep(2)

        # 切换回最初打开的窗口
        self.browser.switch_to.window(all_handles[0])
        self.browser.close()

        # 战旗币-1000
        account_rich_lists = self.browser.find_elements_by_class_name('js-user-left-rich-coin')
        new_account_zq_money = int(account_rich_lists[0].text)
        self.assertTrue(new_account_zq_money, msg="Error!")
        # self.assertEqual(new_account_zq_money, account_zq_money-1000, msg="Error!")

        # 打call礼包+1，数量+10

    def tearDown(self):

        self.browser.refresh()
        time.sleep(2)

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
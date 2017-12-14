# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time


class ThirdPartySignOnByWB(unittest.TestCase):

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

        # 获取当前窗口句柄
        self.now_handle = self.browser.current_window_handle

        # 获得cookie信息
        # cookie = self.browser.get_cookies()
        # print(cookie)

        # 遍历打印cookies中的name和value信息
        # for cookie in browser.get_cookies():
        #    print("%s -> %s" % (cookie['name'], cookie['value']))

        try:
            self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[1]/ul/li[1]/a/span').click()
            print('pass: login window success!')
        except Exception as e:
            print('Exception found:', format(e))
        time.sleep(2)

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

                try:
                    self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div/div[2]/div/p/a[1]').click(
                    )
                    print('pass: third-party sign on is success!')
                    title = self.browser.title
                    self.assertEqual(title, '网站连接 - 战旗直播平台', msg='第三方登陆失败!')
                except Exception as e:
                    print('Exception found:', format(e))
                time.sleep(6)

    def tearDown(self):
        # 退出登录（可封装成公共方法）
        ele = self.browser.find_element_by_link_text('账号')

        # 鼠标移到悬停元素上
        ActionChains(self.browser).move_to_element(ele).perform()
        time.sleep(6)
        try:
            self.browser.find_element_by_xpath('//*[@id="yp-btnLogout"]').click()
            print('pass: sign out window success!')
        except Exception as e:
            print('Exception found:', format(e))
        self.browser.implicitly_wait(3)
        try:
            self.browser.find_element_by_xpath('/html/body/div[6]/div[2]/button[1]').click()
            print('pass: sign out zhanqiTV success!')
        except Exception as e:
            print('Exception found:', format(e))
        time.sleep(1)
        self.browser.refresh()
        time.sleep(2)

        self.browser.implicitly_wait(3)

        self.browser.implicitly_wait(3)
        self.browser.get('https://weibo.com/')
        wb_title = self.browser.title
        print('**********' + wb_title + '**********')
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time

'''
    依赖/前置条件：无
    1.打开战旗直播首页（未登录/登录）
    2.如果已登录,退出登录，关闭浏览器
    3.当前未登录,刷新页面，关闭浏览器
    4.验证当前是否登录
    5.验证是否成功退出登录（已登录）
'''


class SignOut(unittest.TestCase):

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

    def test_signOut(self):
        self.browser.get('https://www.zhanqi.tv/')

        # 判断‘账号’按钮是否存在
        login_ele = self.browser.find_elements_by_link_text('账号')
        if len(login_ele) == 1:
            # print(len(login_ele))
            '''退出登录'''
            # 鼠标移到悬停元素上
            ActionChains(self.browser).move_to_element(login_ele[0]).perform()
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
            login_ele_isExist = self.browser.find_elements_by_link_text('账号')
            self.assertFalse(len(login_ele_isExist), msg='退出登录失败')
        else:
            pass
            print('当前账号处于未登录状态！')

    def tearDown(self):

        self.browser.refresh()
        time.sleep(2)

        # 关闭窗口和浏览器
        self.browser.close()
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
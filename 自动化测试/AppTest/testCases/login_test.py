# coding=utf-8

import unittest
import time
import os
import sys
from base import readConfig
from base.logger import Logger
from appium import webdriver

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

config = readConfig.ReadConfig()
log = Logger(logger="Login").getlog()


class Login(unittest.TestCase):
    def setUp(self):
        self.udid = config.get_device_info("udid")
        self.platformName = config.get_device_info("platformName")
        self.platformVersion = config.get_device_info("platformVersion")
        self.deviceName = config.get_device_info("deviceName")
        self.appPackage = config.get_device_info("appPackage")
        self.appActivity = config.get_device_info("appActivity")
        self.noReset = config.get_device_info("noReset")
        self.unicodeKeyboard = config.get_device_info("unicodeKeyboard")
        self.resetKeyboard = config.get_device_info("resetKeyboard")

        desired_caps = dict()
        desired_caps.update({
            "udid": self.udid,
            "platformName": self.platformName,
            "platformVersion": self.platformVersion,
            "deviceName": self.deviceName,
            "appPackage": self.appPackage,
            "appActivity": self.appActivity,
            "noReset": self.noReset,
            "unicodeKeyboard": self.unicodeKeyboard,
            "resetKeyboard": self.resetKeyboard
        })
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(10)  # app启动后等待8秒，方便元素加载完成

    def test_login(self):
        self.account = "15068899860"
        self.password = "zqcf666"
        log.info("test login")
        # 关闭广告
        if self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/ib_close"):
            self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/ib_close").click()
        else:
            pass
        time.sleep(1)

        # 点击头像icon
        if self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/main_entry_mine_btn"):
            self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/main_entry_mine_btn").click()
        else:
            pass
        time.sleep(1)

        # 进行登录操作
        if self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/fi_user_avatar"):
            self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/fi_user_avatar").click()
        else:
            pass
        time.sleep(1)
        self.driver.find_elements_by_id("com.gameabc.zhanqiAndroid:id/code_edit")[0].send_keys(self.account)
        self.driver.find_elements_by_id("com.gameabc.zhanqiAndroid:id/code_edit")[1].send_keys(self.password)
        self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/login_submit").click()
        time.sleep(1)
        self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/tv_entry_home_page").click()
        time.sleep(1)
        # 截图
        img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
        now_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_save_path = img_folder + now_time + '.png'
        self.driver.get_screenshot_as_file(screen_save_path)
        log.info("save screenshot is success!")
        self.assertTrue("true", msg="###")
        time.sleep(3)
        self.driver.quit()

    def tearDown(self):
        log.info("--------------------------------------------")
        log.info("login test is end!")


if __name__ == '__main__':
    unittest.main()


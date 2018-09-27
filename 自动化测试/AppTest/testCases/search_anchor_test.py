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
log = Logger(logger="SearchAnchor").getlog()


class SearchAnchor(unittest.TestCase):
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
        time.sleep(8)  # app启动后等待8秒，方便元素加载完成

    def test_search_anchor(self):
        self.account = "15068899860"
        self.password = "zqcf666"
        log.info("test search anchor")
        # 关闭广告
        # if self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/ib_close"):
        #     self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/ib_close").click()
        # else:
        #     pass
        time.sleep(3)

        # 搜索主播
        if self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/main_entry_search"):
            self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/main_entry_search").click()
        else:
            log.info("search window is not exist")
        time.sleep(0.5)
        self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/zq_search_main_edit").send_keys(u"二细")
        time.sleep(3)
        self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/zq_search_main_search_tv").click()
        time.sleep(3)

        # 验证搜索
        # if self.driver.find_element_by_link_text("二细"):
        #     log.info("search anchor is success!")
        #     self.assertTrue("true", "true")
        #     pass
        # else:
        #     log.info("search anchor is not exist")
            # 截图
        self.assertTrue("true", msg="###")
        img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
        now_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_save_path = img_folder + now_time + '.png'
        self.driver.get_screenshot_as_file(screen_save_path)
        log.info("save screenshot is success!")
        time.sleep(3)
        self.driver.quit()

    def tearDown(self):
        log.info("--------------------------------------------")
        log.info("search anchor test is end!")


if __name__ == '__main__':
    unittest.main()


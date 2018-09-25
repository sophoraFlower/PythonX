# !/usr/bin/env python
# coding=utf-8

import unittest
# import selenium
import time
import warnings  # 忽略ResourceWarning
from appium import webdriver
from base import readConfigFile

config = readConfigFile.ReadConfig()


class MainTest(unittest.TestCase):
    """ygn_test.py"""

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略ResourceWarning
        cls.udid = config.get_one_plus_5t("udid")
        cls.platformName = config.get_one_plus_5t("platformName")
        cls.platformVersion = config.get_one_plus_5t("platformVersion")
        cls.deviceName = config.get_one_plus_5t("deviceName")
        cls.appPackage = config.get_one_plus_5t("appPackage")
        cls.appActivity = config.get_one_plus_5t("appActivity")
        cls.noReset = config.get_one_plus_5t("noReset")
        cls.unicodeKeyboard = config.get_one_plus_5t("unicodeKeyboard")
        cls.resetKeyboard = config.get_one_plus_5t("resetKeyboard")

        desired_caps = dict()
        desired_caps.update({
            "udid": cls.udid,
            "platformName": cls.platformName,
            "platformVersion": cls.platformVersion,
            "deviceName": cls.deviceName,
            "appPackage": cls.appPackage,
            "appActivity": cls.appActivity,
            "noReset": cls.noReset,
            "unicodeKeyboard": cls.unicodeKeyboard,
            "resetKeyboard": cls.resetKeyboard
        })

        print("Desired_Caps:".format(desired_caps))
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        print('tear down-------------')
        # cls.driver.quit()

    # @unittest.skip("I don't want to run this case")
    def test_adoff(self):  # 关闭霸屏广告
        """test case adoff"""
        time.sleep(1)
        if self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/ib_close"):
            self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/ib_close").click()
        else:
            pass

    # @unittest.skip("I don't want to run this case")
    def test_center(self):  # 首页个人中心入口
        """test case center"""
        self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/main_entry_mine_btn").click()
        time.sleep(1)
        self.driver.open_notifications()
        time.sleep(1)
        self.driver.press_keycode(4)
        time.sleep(0.5)
        self.driver.press_keycode(4)

    # @unittest.skip("I don't want to run this case")
    def test_search(self):  # 搜索
        """test case search"""
        self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/main_entry_search").click()
        time.sleep(0.5)
        self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/zq_search_main_edit").send_keys(u"文森特")
        time.sleep(0.5)
        self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/zq_search_main_search_tv").click()

    # @unittest.skip("I don't want to run this case")
    def test_login(self):  # login->logout
        """test case login"""
        self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/main_entry_mine_btn").click()
        time.sleep(0.5)
        self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/fi_user_avatar").click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android."
                                          "widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget."
                                          "LinearLayout/android.widget.EditText").send_keys("ygn1992")
        time.sleep(0.5)
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android."
                                          "widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget."
                                          "LinearLayout/android.widget.EditText").send_keys("ygn1992")
        time.sleep(0.5)
        self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/login_submit").click()
        time.sleep(0.8)
        self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/fi_user_avatar").click()
        time.sleep(0.5)
        self.driver.find_element_by_id("com.gameabc.zhanqiAndroid:id/user_main_logout").click()
        time.sleep(0.5)
        self.driver.press_keycode(4)


if __name__ == '__main__':
    unittest.main(verbosity=2)

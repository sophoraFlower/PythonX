# coding=utf-8

import unittest
import os
import time
from base import readConfig
from appium import webdriver

config = readConfig.ReadConfig()
# 启动appium服务
os.system('start startAppiumServer.bat')
# 等待appium服务启动完毕
time.sleep(8)


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.udid = config.get_device_info("udid")
        cls.platformName = config.get_device_info("platformName")
        cls.platformVersion = config.get_device_info("platformVersion")
        cls.deviceName = config.get_device_info("deviceName")
        cls.appPackage = config.get_device_info("appPackage")
        cls.appActivity = config.get_device_info("appActivity")
        cls.noReset = config.get_device_info("noReset")
        cls.unicodeKeyboard = config.get_device_info("unicodeKeyboard")
        cls.resetKeyboard = config.get_device_info("resetKeyboard")

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
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_login(self):
        self.account = "15068899860"
        self.password = "zqcf666"
        print("########################")

    @classmethod
    def tearDownClass(cls):
        print("test is success!")


if __name__ == '__main__':
    unittest.main(verbosity=2)


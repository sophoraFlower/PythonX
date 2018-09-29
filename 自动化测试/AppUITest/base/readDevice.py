# coding=utf-8

import os
import configparser

'''
    读取设备信息，并将当前设备信息输出到config文件夹
'''

device = os.popen('adb devices').read()
# 处理空行和多余的字符串
udid = device.split("\n")[1]
tIndex = udid.index("\t")
platformVersion = os.popen('adb shell getprop ro.build.version.release').read().split("\n")[0]
deviceName = os.popen('adb shell getprop ro.product.model').read().split("\n")[0]

config = configparser.ConfigParser()
config['TestDeviceInfo'] = dict()
config['TestDeviceInfo'].update({
    "udid": udid[0:tIndex],
    "platformName": 'Android',
    "platformVersion": platformVersion,
    "deviceName": deviceName,
    "appPackage": 'com.gameabc.zhanqiAndroid',
    "appActivity": 'com.gameabc.zhanqiAndroid.Activty.MainActivity',
    "noReset": 'true',
    "unicodeKeyboard": 'true',
    "resetKeyboard": 'true'
})
with open('../config/config_Device.ini', 'w') as configfile:
    config.write(configfile)

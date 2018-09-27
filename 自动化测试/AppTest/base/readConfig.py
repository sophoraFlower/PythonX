# coding=utf-8
import os
import configparser

# configPath = os.path.abspath(os.path.dirname(os.getcwd())) + '\\config\\config_Device.ini'
configPath = os.path.abspath(os.curdir) + '\\config\\config_Device.ini'


class ReadConfig:

    # 构造函数，读取配置文件(config_Device.ini等文件)
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(configPath)

    def get_device_info(self, name):
        value = self.config.get("TestDeviceInfo", name)
        return value

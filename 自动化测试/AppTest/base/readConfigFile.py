# coding=utf-8
import os
import configparser

configPath = os.path.abspath(os.curdir) + '\\config\\config_OnePlus5T.ini'
print(os.path.abspath(os.curdir))


class ReadConfig:

    # 构造函数，读取配置文件(config.ini)
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(configPath)

    def get_one_plus_5t(self, name):
        value = self.config.get("OnePlus5T", name)
        return value

    # 邮件信息
    # def get_email(self, name):
    #     value = self.config.get("EMAIL", name)
    #     return value

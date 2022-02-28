# coding=utf-8
import os
import configparser

configPath = os.path.abspath(os.curdir) + '\\testConfig\\config.ini'

class ReadConfig:

    # 构造函数，读取配置文件(config.ini)
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(configPath)

    def get_http_pc(self, name):
        value = self.config.get("HTTP_PC", name)
        return value

    def get_http_beta(self, name):
        value = self.config.get("HTTP_Beta", name)
        return value

    def get_http_mobile(self, name):
        value = self.config.get("HTTP_Mobile", name)
        return value

    # 邮件信息
    # def get_email(self, name):
    #     value = self.config.get("EMAIL", name)
    #     return value
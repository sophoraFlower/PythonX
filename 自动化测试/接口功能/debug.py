# -*- coding: utf-8 -*-

from commentClass import readConfigFile

config = readConfigFile.ReadConfig()
test = config.get_http_pc(name="base_url")
print(test)
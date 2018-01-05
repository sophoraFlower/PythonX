# coding=utf-8

from selenium import webdriver
import time
import os
import re
import datetime

driverOptions = webdriver.ChromeOptions()
driverOptions.add_argument(r"user-data-dir=C:\Users\caofei\AppData\Local\Google\Chrome\User Data")
browser = webdriver.Chrome('chromedriver', 0, driverOptions)
browser.maximize_window()
browser.implicitly_wait(3)

path = 'C:\\Users\\caofei\\Desktop\\screenshots\\'
if not os.path.exists(path):
    os.makedirs(path)
else:
    pass

browser.get("https://www.zhanqi.tv/games/pubg")
browser.implicitly_wait(3)
for i in range(0, 180):
    browser.implicitly_wait(2)
    filename = path + re.sub(r'[^0-9]', '', str(datetime.datetime.now())) + '.png'
    browser.get_screenshot_as_file(filename)
    time.sleep(20)
    browser.refresh()

browser.quit()

filePath = 'C:\\Users\\caofei\\Desktop\\screenshots\\'
for parent, dirs, files in os.walk(filePath):
    fileSize = 0
    for file in files:
        currentPath = os.path.join(parent, file)
        newFileSize = int(str(os.path.getsize(currentPath))[0:3])
        if newFileSize != fileSize:
            localTimeDay = str(file)[0:4] + '-' + str(file)[4:6] + '-' + str(file)[6:8]
            localTimeHour = str(file)[8:10] + ':' + str(file)[10:12] + ':' + str(file)[12:14]
            localTime = localTimeDay + ' ' + localTimeHour
            with open(filePath + 'result.txt', "a+") as f:
                print(localTime)
        else:
            pass
        fileSize = newFileSize

# coding=utf-8
from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.maximize_window()
time.sleep(3)

browser.get('https://www.baidu.com')
try:
    browser.find_element_by_link_text('新闻')
    print('pass: success! text')
except Exception as e:
    print('Exception found:', format(e))

time.sleep(2)

# try:
#     browser.find_element_by_partial_link_text('主页').click()
#     print('pass: success! partial text')
# except Exception as e:
#     print('Exception found:', format(e))
#
# time.sleep(2)

browser.find_element_by_id("kw").send_keys("Selenium")
time.sleep(2)
try:
    # <span style="font-family:Microsoft YaHei;">调用clear()方法去清除</span>
    browser.find_element_by_id("kw").clear()
    print('test pass: clean successful')
except Exception as e:
    print("Exception found", format(e))

browser.refresh()
time.sleep(4)
browser.quit()
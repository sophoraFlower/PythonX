# coding=utf-8
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()
time.sleep(6)

browser.get('https://www.zhanqi.tv/')

# 获取当前窗口句柄
now_handle = browser.current_window_handle
print('@@@@@@@ ' + now_handle)

# 获得cookie信息
# cookie = browser.get_cookies()
# print(cookie)

# 遍历打印cookies中的name和value信息
for cookie in browser.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))

try:
    browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[1]/ul/li[1]/a/span').click()
    print('pass: login window success!')
except Exception as e:
    print('Exception found:', format(e))
time.sleep(2)

# try:
#     browser.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/div[2]/form/div[1]/div[2]/input').send_keys('15068899860')
#     print('pass: input account success!')
# except Exception as e:
#     print('Exception found:', format(e))
#
# time.sleep(2)
#
# try:
#     browser.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/div[2]/form/div[2]/div[2]/input').send_keys('zqcf666'
#                                                                                                                )
#     print('pass: input password success!')
# except Exception as e:
#     print('Exception found:', format(e))
#
# time.sleep(2)

try:
    browser.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/div[2]/div/div/ul/li[3]/a/i[1]').click()
    print('pass: wb login window success!')
except Exception as e:
    print('Exception found:', format(e))
time.sleep(10)

# 获取所有窗口句柄
all_handles = browser.window_handles

for handle in all_handles:
    if handle == now_handle:
        # 输出待选择的窗口句柄
        print(handle)
        browser.switch_to.window(handle)
        # browser.find_element_by_xpath("//*[@id='menu_projects']/a").click()
        try:
            browser.find_element_by_xpath('//*[@id="userId"]').send_keys('zjdxm@sina.cn')
            print('pass: input account success!')
        except Exception as e:
            print('Exception found:', format(e))
        time.sleep(2)

        try:
            browser.find_element_by_xpath('//*[@id="passwd"]').send_keys('**lwx520zjdxm**')
            print('pass: input password success!')
        except Exception as e:
            print('Exception found:', format(e))
        time.sleep(2)

        try:
            browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div/div[2]/div/p/a[1]').click()
            print('pass: login success!')
        except Exception as e:
            print('Exception found:', format(e))
        time.sleep(5)

        # flash设置
        browser.get('chrome://settings/content/siteDetails?site=https://www.zhanqi.tv')
        browser.find_element_by_xpath('//*[@id="permission"]').click()
        browser.find_element_by_xpath('//*[@id="allow"]').click()

        # 关闭当前窗口
        # browser.close()
        # time.sleep(3)
        # # 输出主窗口句柄
        # print(now_handle)
        # # 返回主窗口
        # browser.switch_to.window(now_handle)
        # time.sleep(2)


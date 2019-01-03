# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
import time

'''
##########################################################
#    module:  
#    abstract: 
#    description:
#    ----------------------------------------------------
#        1.打开知乎登录页：https://www.zhihu.com/signup
#        2.使用第三方登录：微博
#        3.我关注的问题页面
#        4.取关问题-遍历
#        5.关闭浏览器（可选）
#    ----------------------------------------------------
#    author: Written by caofei@bianfeng.com
#    date: 2019/01/03
#    update:
##########################################################
'''

driverOptions = webdriver.ChromeOptions()
# 浏览器本地存储数据地址
# home
# self.driverOptions.add_argument(r"user-data-dir=C:\Users\Houle\AppData\Local\Google\Chrome\User Data")
# work
driverOptions.add_argument(r"user-data-dir=C:\Users\Houle\AppData\Local\Google\Chrome\User Data")
driver = webdriver.Chrome('chromedriver', 0, driverOptions)
driver.maximize_window()
driver.implicitly_wait(3)

# 登录知乎
'''
driver.get('https://www.zhihu.com/')
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span').click()
driver.find_element_by_class_name('Login-socialLogin').click()
weibo_login = driver.find_element_by_class_name('Icon--weibo')
ActionChains(driver).move_to_element(weibo_login).perform()
time.sleep(2)
weibo_login.click()
# 输入微博账号和密码
driver.find_element_by_xpath('//*[@id="userId"]').send_keys('xxxx@xxxx.cn')
print('input account success!')
driver.find_element_by_xpath('//*[@id="passwd"]').send_keys('xxxxxxx')
print('input password success!')
driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]').click()
print('login start ...')
try:
    driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]').click()
    print('login start ...')
except Exception as e:
    print('Exception found:', format(e))
try:
    driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]').click()
    print('login start ...')
except Exception as e:
    print('Exception found:', format(e))
time.sleep(6)

allow = driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/div/div[2]/div[2]/p/a[1]')
ActionChains(driver).move_to_element(allow).perform()
driver.implicitly_wait(3)
allow.click()
driver.implicitly_wait(3)

driver.execute_script("window.scrollTo(0, 66);")
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[2]/div/div/div[4]/ul/li[2]/a/span[1]').click()

windows = driver.window_handles
driver.switch_to.window(windows[1])
'''
driver.get('https://www.zhihu.com/people/Houlelord/following/questions')
# for i in range(753):
# driver.execute_script("window.scrollTo(0, 66);")
driver.find_elements_by_class_name('QuestionItem-title')[0].find_element_by_tag_name('a').click()
time.sleep(6)
windows_new = driver.window_handles
driver.switch_to.window(windows_new[1])
cancel_follow = driver.find_elements_by_class_name('FollowButton')
print(cancel_follow[0].is_displayed())
print(cancel_follow[1].is_displayed())
time.sleep(6)
ActionChains(driver).move_to_element(cancel_follow[1]).perform()
time.sleep(6)
cancel_follow = driver.find_elements_by_class_name('FollowButton')
print(cancel_follow[0].is_displayed())
print(cancel_follow[1].is_displayed())
# driver.delete_cookie('l_n_c')
# driver.delete_cookie('n_c')
cancel_follow[1].click()
print(driver.get_cookies())
time.sleep(6)
# if cancel_follow.is_displayed():
#     driver.find_element_by_class_name('Button--grey').click()
# driver.find_element_by_class_name('Button--primary').click()
# js = 'document.querySelectorAll("button")[0].style.display = "block";'
# driver.execute_script(js)
# cancel_follow = driver.find_element_by_class_name('FollowButton')
# driver.execute_script('arguments[0].click();', cancel_follow)
# ActionChains(driver).move_to_element(cancel_follow).perform()
# time.sleep(4)
# cancel_follow.send_keys(Keys.ENTER)
# driver.refresh()
# time.sleep(1)
# driver.close()
# driver.switch_to.window(windows_new[1])
# driver.refresh()
# time.sleep(1)
# print('delete the ' + str(i) + ' page')





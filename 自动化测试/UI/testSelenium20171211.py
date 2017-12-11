from selenium import webdriver
import time

browser = webdriver.Firefox()
# browser = webdriver.Chrome()

# 最大化浏览器
browser.maximize_window()
# 设置隐式时间等待
browser.implicitly_wait(8)

browser.get('https://www.zhanqi.tv')

assert '战旗直播_Live For Gamers丨天生爱玩,游戏至上！- zhanqi.tv' in browser.title

elem = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/input")
elem.send_keys("EDG")
time.sleep(3)
browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/i").click()
time.sleep(5)

browser.quit()
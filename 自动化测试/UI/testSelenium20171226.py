# coding=utf-8
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(6)
#
# driver.get("http://www.baidu.com/")
# # ctrl+T
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')


# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://news.baidu.com')
# driver.implicitly_wait(8)
#
# for i in driver.find_elements_by_xpath("//*/input[@type='radio']"):
#     i.click()
#     time.sleep(3)

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://www.baidu.com')
# time.sleep(2)
#
# element = driver.find_element_by_xpath("//*[@id='lg']/img")
# actionChains = ActionChains(driver)
# actionChains.context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(6)
# driver.get("https://tieba.baidu.com/index.html")
# time.sleep(1)
#
# target_elem = driver.find_element_by_link_text("地区")
# 用目标元素参考去拖动
# driver.execute_script("return arguments[0].scrollIntoView();", target_elem)


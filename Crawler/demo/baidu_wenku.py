# coding=utf-8
from selenium import webdriver
import time
import requests

driverOptions = webdriver.ChromeOptions()

# 浏览器本地信息
driverOptions.add_argument(r"user-data-dir=C:\Users\caofei\AppData\Local\Google\Chrome\User Data")
browser = webdriver.Chrome('chromedriver', 0, driverOptions)
browser.maximize_window()
browser.implicitly_wait(3)

# 获取文档对应的地址：https://wenku.baidu.com/view/d907f3ebb8f67c1cfad6b8f5.html
browser.get('https://wenku.baidu.com/view/d907f3ebb8f67c1cfad6b8f5.html')
time.sleep(1)
# web_height = browser.get_window_size()['height']
# web_height = document.body.scrollHeight/2

browser.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
more_page = browser.find_element_by_xpath('//*[@id="html-reader-go-more"]/div[1]/span[1]/span')
time.sleep(1)
more_page.click()
time.sleep(1)

mum_string = browser.find_element_by_class_name('page-count').text
page_num = int(mum_string[1:3])

# 记录下载过的图片地址，避免重复下载
img_url_dic = {}
# 图片编号
m = 0
# 按实际页面大小定义滑动初始高度
web_height = 2130
for i in range(1, page_num+1):
    if i == 4:
        continue
    if i >= 3:
        print("####### " + str(web_height))
        browser.execute_script("window.scrollTo(0, " + str(web_height) + ");")
        web_height += 666
    time.sleep(2)
    print('########### start get ' + str(i) + ' page ###########')
    bd_element_id = '//*[@id="flow-ppt-wrap"]/div/div/div[' + str(i) + ']/div/img'
    bd_element = browser.find_element_by_xpath(bd_element_id)
    img_url = bd_element.get_attribute('src')
    if img_url != None:
        print("@@@@@@@@@@@ " + img_url + "@@@@@@@@@@")
    time.sleep(2)
    # 保存图片到指定路径
    if img_url != None and not img_url in img_url_dic:
        img_url_dic[img_url] = ''
        m += 1
        ext = img_url.split('.')[-1]
        filename = str(m) + '.' + ext
        # 保存图片数据
        html = requests.get(img_url)
        with open('./baiduwenku/' + str(m) + '.' + 'jpg', 'wb') as file:
            file.write(html.content)
            file.close()


# 关闭窗口和浏览器
browser.close()
browser.quit()





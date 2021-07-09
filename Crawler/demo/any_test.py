# coding=utf-8

import requests
import os
import re
from bs4 import BeautifulSoup
from datetime import datetime

# 获取当前文件所在路径
file_path = os.getcwd()

# 创建存放爬取结果的文件夹
result_path = file_path + '\\results'
if not os.path.exists(result_path):
    os.makedirs(result_path)
else:
    pass

# 网站url
url = 'http://www.myaidoctor.com/recruit?language=1'
# 获取页面html
response_data = requests.get(url)
# print(response_data.text)

# 解析HTML内容
soup = BeautifulSoup(response_data.text, 'lxml')
# 匹配中文字符
pattern = re.compile(u"[\u4e00-\u9fa5]+")
# 招聘岗位-大类
work_type = soup.find_all('div', class_='research-r')

# 招聘岗位-具体
work_list = soup.find_all('div', class_='reach-inHead')

# 招聘岗位-岗位职责和任职要求
work_content = soup.find_all('div', class_='reachleft')

# 结果文件以当前时间点命名
with open(result_path + '\\' + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+'.txt', "a+") as f:
    # 写入岗位分类
    f.write('当前有如下岗位分类:')
    for item in work_type:
        item_cn = re.findall(pattern, item.string)
        f.write(' ' + item_cn[0])
    f.write('\n')

    # 写入具体岗位
    f.write('\n')
    f.write('当前有如下具体岗位:')
    for item in work_list:
        f.write("\n" + item.find_all('span')[0].string)
    f.write('\n')

    # 岗位职责和任职要求
    f.write('\n')
    f.write('各岗位职责和任职要求如下:')
    f.write('\n'+'--------------------------------------------------' + '\n')
    for item in work_content:
        # 岗位名称
        f.write('**' + item.find_all('span')[0].string + '**')
        # 岗位职责
        f.write('\n' + item.find_all('p')[0].string)
        for item_p in item.find_all('p')[1].find_all(text=True):
            f.write('\n' + item_p.string)
        f.write('\n')

        # 任职要求
        f.write('\n' + item.find_all('p')[2].string)
        for item_p in item.find_all('p')[3].find_all(text=True):
            f.write('\n' + item_p.string)
        f.write('\n')
        f.write('--------------------------------------------------' + '\n')






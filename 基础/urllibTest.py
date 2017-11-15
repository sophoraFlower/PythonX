# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup as bs
from urllib import request


# 分析网页函数
def getLatestBook_list():
    resp = request.urlopen('https://book.douban.com/')
    html_data = resp.read().decode('utf-8')

    soup = bs(html_data, 'lxml')
    # latest_book = soup.find_all('div', class_='carousel')
    # latest_book_list = latest_book[0].find_all('div', class_='more-meta')
    #
    # latest_list = []
    # for tag_book_item in latest_book_list:
    #     latest_dict = {}
    #     latest_dict['book_name'] = tag_book_item.find_all('h4', class_='title')[0].string.strip()
    #     latest_dict['author'] = tag_book_item.find_all('span', class_='author')[0].string.strip()
    #     latest_list.append(latest_dict)
    # return latest_list
    children_list = soup.html.children
    for child in children_list:
        print(child)
    # return soup.html.contents[]


NowLatestBook_list = getLatestBook_list()
print(NowLatestBook_list)
# coding=utf-8

import re


# 读取文件内容
f = open('redata.txt', 'r')
content = f.readlines()
for line in content:
    print(line.strip())

"""1-19 提取每行中完整的时间戳"""
patt19 = '^[A-Z][a-z]{2}\s[A-Z][a-z]{2}\s\s?\d{1,2}\s\d{2}:\d{2}:\d{2}\s\d{4}'
for line in content:
    print(re.match(patt19, line.strip()).group())

"""1-20 提取每行中完整的电子邮件地址"""
patt20 = '[a-z]+@[a-z]+\.[a-z]+'
for line in content:
    print(re.search(patt20, line.strip()).group())

"""1-21 仅仅提取时间戳中的月份"""
patt21 = '[A-Z][a-z]{2}\s\s?\d{1,2}'
for line in content:
    print(re.search(patt21, line.strip()).group())

"""1-22 仅仅提取时间戳中的年份"""
patt22 = '\d{4}'
for line in content:
    print(re.search(patt22, line.strip()).group())

"""1-23 仅仅提取时间戳中的时间（HH:MM:SS）"""
patt23 = '\d{2}:\d{2}:\d{2}'
for line in content:
    print(re.search(patt23, line.strip()).group())

"""1-24 仅仅从电子邮件地址中提取登录名和域名（包括主域名和高级域名一起提取）"""
patt24 = '([a-z]+)@([a-z]+\.[a-z]+)'
for line in content:
    print(re.search(patt24, line.strip()).group(1))
    print(re.search(patt24, line.strip()).group(2))

"""1-25 仅仅从电子邮件地址中提取登录名和域名（包括主域名和高级域名）"""
patt25 = '([a-z]+)@([a-z]+)\.([a-z]+)'
for line in content:
    print(re.search(patt25, line.strip()).group(1))
    print(re.search(patt25, line.strip()).group(2))
    print(re.search(patt25, line.strip()).group(3))

"""1-26 使用你的电子邮件地址替换每一行数据中的电子邮件地址"""
patt26 = '[a-z]+@[a-z]+\.[a-z]+'
for line in content:
    print(re.sub(patt26, 'houle.cf@foxmail.com', line.strip()))

"""1-27 从时间戳中提取月、日和年，然后以“月，日，年”的格式，每一行仅仅迭代一次。
处理电话号码。对于练习 1-28 和 1-29，回顾 1.2 节介绍的正则表达式\d{3}-\d{3}-\d{4}，
它匹配电话号码，但是允许可选的区号作为前缀。更新正则表达式，使它满足以下条件"""
patt27 = '(^[A-Z][a-z]{2})\s([A-Z][a-z]{2})\s(\s?\d{1,2})'
for line in content:
    print(re.search(patt27, line.strip()).group(1))
    print(re.search(patt27, line.strip()).group(2))
    print(re.search(patt27, line.strip()).group(3))

"""1-28 区号（三个整数集合中的第一部分和后面的连字符）是可选的，也就是说，正则
表达式应当匹配 800-555-1212，也能匹配 555-1212"""
patt28 = '(\d{9,10}-)?\d{1}-\d{1,2}$'
for line in content:
    print(re.search(patt28, line.strip()).group())

"""1-29 支持使用圆括号或者连字符连接的区号（更不用说是可选的内容）使正则表达式
匹配 800-555-1212、555-1212 以及（800）555-1212"""
patt29 = '\(?(\d{9,10})?\)?-?\d{1}-\d{1,2}$'
for line in content:
    print(re.search(patt29, line.strip()).group())

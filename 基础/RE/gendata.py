# coding=utf-8
import re

from random import randrange, choice
from string import ascii_lowercase as lc
# from sys import int
from time import ctime
"""1-16 为 gendata.py 更新代码，使数据直接输出到 redata.txt 而不是屏幕"""
"""1-17 判断在 redata.txt 中一周的每一天出现的次数（换句话说，读者也可以计算所选择
的年份中每个月中出现的次数）"""
"""1-18 通过确认整数字段中的第一个整数匹配在每个输出行起始部分的时间戳，确保在
redata.txt 中没有数据损坏"""

tlds = ('com', 'edu', 'net', 'org', 'gov')
week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
week_days = [0, 0, 0, 0, 0, 0, 0]
f = open('redata.txt', 'w')
# randrange() 方法返回指定递增基数集合中的一个随机数，基数缺省值为1
# ctime() 函数把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式,如：Tue Feb 17 10:00:18 2013
# choice() 方法返回一个列表，元组或字符串的随机项
for i in range(randrange(5, 11)):
    dtint = randrange(2**32)    # pick date
    dtstr = ctime(dtint)        # date string
    llen = randrange(4, 8)      # login is shorter
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)  # domain is longer
    dom = ''.join(choice(lc) for j in range(dlen))
    data = ('%s::%s@%s.%s::%d-%d-%d\n' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen))
    week_day = dtstr[0:3]
    pattTime = '^[A-Z][a-z]{2}\s[A-Z][a-z]{2}\s'   # '(^[A-Z][a-z]{2}\s){2}\s\s?(\d{2}:){3}\s[a-z]{4}::[a-z]+@[a-z]+\.[a-z]+::\d+-\d-\d'
    print("###: " + data)
    print("@@@: " + str(re.search(pattTime, data)))
    for m in range(6):
        if week_day == week[m]:
            week_days[m] = week_days[m]+1
    f.write(data)
f.close()
for day in week_days:
    print(day)



# coding=utf-8

import requests
import time

'''
    因为无法修改服务器时间
    也不能修改代码时间（这很容易导致上线时时间没写正确造成BUG）
    所以采取一种新的机制来模拟活动时间

    如果redis有设置当前时间
        则代码中的当前时间=  redis中的当前时间
    如果redis中没有设置当前时间， 或者当前时间=0
        则代码中的当前时间 = 真正的当前时间
'''
# 设置当前时间为 2018-11-06 18:59:00
# url = 'http://beta.zhanqi.tv/api/actives/double11/setTime?datetime=2018-11-08%2018:59:00'

start_time = '18:28:00'
end_time = '20:00:00'
url = 'http://beta.zhanqi.tv/api/actives/double11/setTime?datetime=2018-11-08%20'

for i in range(0, 3000):

    m_time = 29
    s_time = 0
    h_time = 18
    while int(h_time) < 24:
        while int(m_time) < 60:
            # 秒时间
            for k in range(60):
                if int(k) < 10:
                    s_time = '0' + str(k)
                else:
                    s_time = str(k)
                    print(url + str(h_time) + ':' + str(m_time) + ':' + str(s_time))
                requests.get(url + str(h_time) + ':' + str(m_time) + ':' + str(s_time))
                time.sleep(1)
                print(requests.get('http://beta.zhanqi.tv/api/actives/double11/getTime').text)
            m_time = int(m_time)
            m_time += 1
            if int(m_time) < 10:
                m_time = '0' + str(m_time)
            else:
                m_time = str(m_time)
            if int(m_time) == 59:
                m_time = 0
        h_time += 1

# 清除设置的当前时间， 恢复成系统时间
requests.get('http://beta.zhanqi.tv/api/actives/double11/setTime')





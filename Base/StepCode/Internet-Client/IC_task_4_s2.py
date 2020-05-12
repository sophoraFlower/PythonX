# coding=utf-8

from socket import *
from time import ctime

'''2-4 客户端
    更新 TCP（tsTclnt.py）和 UDP（tsUclnt.py）客户端，以使得服务器名称
    无须硬编码到应用程序中。此外，应该允许用户指定主机名和端口号，且如果二者
    中任何一个或者全部参数丢失，那么应该使用默认值。
'''

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


tcpSerSock = socket(AF_INET, SOCK_STREAM)   # 定义socket类型，网络通信，TCP
tcpSerSock.bind(ADDR)  # 套接字绑定的IP与端口
tcpSerSock.listen(5)         # 开始TCP监听,监听1个请求
while True:
    print("waiting for connect...")
    tcpCliSock, addr = tcpSerSock.accept()   # 接受TCP连接，并返回新的套接字与IP地址
    print('...Connected by:', addr)  # 输出客户端的IP地址

    while True:
        data = tcpCliSock.recv(BUFSIZ)    # 把接收的数据实例化
        if not data:
            break
        # tcpCliSock.send('[%s] %s' % (bytes(ctime(), 'utf-8'), data))
        tcpCliSock.send(('[%s] %s:miaomiao' % (bytes(ctime(), 'utf-8'), data)).encode())
    tcpCliSock.close()
# tcpSerSock.close()

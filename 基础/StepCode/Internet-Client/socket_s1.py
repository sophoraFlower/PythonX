# coding=utf-8

from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)   # 定义socket类型，网络通信，TCP
tcpSerSock.bind(ADDR)   # 套接字绑定的IP与端口
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




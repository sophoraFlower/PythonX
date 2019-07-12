# coding=utf-8

from socket import *
from time import ctime
import os

'''
        实现 Python 库参考文档中关于 socket 模块中的 TCP 客户端/
    服务器程序示例，并使其能够正常工作。首先运行服务器，然后启动客户端。也可
    以在 http://docs.python.org/library/socket#example 网址中找到在线源码。
    如果你觉得示例中服务器的功能太单调，那么可以更新服务器代码，以使它具有更
    多功能，令其能够识别以下命令。
    date 服务器将返回其当前日期/时间戳，即 time.ctime()。
    os 获取操作系统信息（os.name）。
    ls 列出当前目录文件清单（提示：os.listdir()列出一个目录，os.curdir 是当前目
    录）。选做题：接受 ls dir 命令，返回 dir 目录中的文件清单。
    你不需要一个网络来完成这个任务，因为你的计算机可以与自己通信。请注意，
    在服务器退出之后，在再次运行它之前必须清除它的绑定。否则，可能会遇到“端
    口已绑定”的错误提示。此外，操作系统通常会在 5 分钟内清除绑定，所以请耐
    心等待。
'''
HOST = '127.0.0.1'
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
        handle = data.decode()
        print("######### " + handle)
        if handle == 'data':
            tcpCliSock.send(('data: %s' % (bytes(ctime(), 'utf-8'))).encode())
        elif handle == 'os':
            tcpCliSock.send(('os: %s' % (bytes(os.name, 'utf-8'))).encode())
        elif handle == 'ls':
            tcpCliSock.send(('ls: %s' % (bytes(str(os.listdir(os.curdir)), 'utf-8'))).encode())
        else:
            tcpCliSock.send(('#########: %s' % (bytes(handle, 'utf-8'))).encode())
    tcpCliSock.close()
# tcpSerSock.close()

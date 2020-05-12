# coding=utf-8

from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpCliSok = socket(AF_INET, SOCK_STREAM)      # 定义socket类型，网络通信，TCP
tcpCliSok.connect(ADDR)       # 要连接的IP与端口
while True:
    data = input('>')       # 与人交互，输入命令
    if not data:
        break
    tcpCliSok.sendall(data.encode())      # 把命令发送给对端
    data = tcpCliSok.recv(BUFSIZ).decode()   # 把接收的数据定义为变量
    if not data:
        break
    print(data)       # 输出变量
tcpCliSok.close()   # 关闭连接

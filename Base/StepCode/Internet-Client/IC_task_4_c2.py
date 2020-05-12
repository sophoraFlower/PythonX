# coding=utf-8

from socket import *
import getopt
import sys

'''2-4 客户端
    更新 TCP（tsTclnt.py）和 UDP（tsUclnt.py）客户端，以使得服务器名称
    无须硬编码到应用程序中。此外，应该允许用户指定主机名和端口号，且如果二者
    中任何一个或者全部参数丢失，那么应该使用默认值。
'''

# 默认HOST和PORT
DefaultHOST = '127.0.0.1'
DefaultPORT = 21567
BUFSIZ = 1024

HOST = ''
PORT = 0
try:
    opts, args = getopt.getopt(sys.argv[1:], '', ['host=', 'port='])
    for op, value in opts:
        if op == '--host':
            HOST = value
        elif op == '--port':
            PORT = int(value)
except getopt.GetoptError:
    sys.exit()
# 判断
ADDR = ()
if HOST == '':
    ADDR = (DefaultHOST, PORT)
elif PORT == '':
    PADDR = (HOST, DefaultPORT)
elif HOST == '' and PORT == '':
    ADDR = (DefaultHOST, DefaultPORT)
else:
    ADDR = (HOST, PORT)

tcpCliSok = socket(AF_INET, SOCK_STREAM)      # 定义socket类型，网络通信，TCP
tcpCliSok.connect(ADDR)

while True:
    data = input("> ")       # 与人交互，输入命令
    if not data:
        break
    tcpCliSok.sendall(data.encode())      # 把命令发送给对端
    data = tcpCliSok.recv(BUFSIZ).decode()   # 把接收的数据定义为变量
    if not data:
        break
    print(data)       # 输出变量
tcpCliSok.close()   # 关闭连接

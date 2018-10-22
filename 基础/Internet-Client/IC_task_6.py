# coding=utf-8
from socket import *
from time import ctime
'''
    使用 socket.getservbyname()来确定使用 UDP 协议的“daytime”服
    务的端口号。检查 getservbyname()的文档以获得其准确的使用语法（即 socket. 
    getservbyname._ doc_）。那么，现在编写一个应用程序，使该应用程序能够通过网
    络发送一条虚拟消息，然后等待服务器回复。一旦你收到服务器的回复，就将其显
    示到屏幕上
'''

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('wating for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto(('[%s] %s' % (bytes(ctime(), 'utf-8'), data)).encode(), addr)
    print('...received from and returned to:', addr)
# udpSerSock.close()

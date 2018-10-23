# coding=utf-8

from socket import *

'''2-7 半双工聊天
    半双工聊天。创建一个简单的半双工聊天程序。指定半双工，我们的意思就是，当建
    立一个连接且服务开始后，只有一个人能打字，而另一个参与者在得到输入消息提示
    之前必须等待消息。并且，一旦发送者发送了一条消息，在他能够再次发送消息之前，
    必须等待对方回复。其中，一位参与者将在服务器一侧，而另一位在客户端一侧。
'''

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
while True:
    data = input('> ')
    if not data:
        break
    elif data == 'Q':
        break
    else:
        tcpCliSock.sendall(data.encode())
    print("####-1 clent send:" + data)
    data = tcpCliSock.recv(BUFSIZ).decode()
    print("####-4 client recv" + data)
    if not data:
        break
    print('tcpCliSock.getpeername(): ' + str(tcpCliSock.getpeername()))
tcpCliSock.close()

# coding=utf-8

from socket import *
# import sys

# host = sys.argv[1]
# textport = sys.argv[2]
#
# s = socket(AF_INET, SOCK_DGRAM)
# try:
#     port = int(textport)
# except ValueError:
#     port = getservbyname(textport, 'udp')
#
# s.connect((host, port))
# print("Enter data to transmit:")
# data = sys.stdin.readline().strip()
# s.sendall(data)
# print("Looking for replies; press Ctrl-C or Ctrl-Break to stop.")
# while 1:
#     buf = s.recv(2048)
#     if not len(buf):
#         break
#     sys.stdout.write(buf)

'''
    使用 socket.getservbyname()来确定使用 UDP 协议的“daytime”服
    务的端口号。检查 getservbyname()的文档以获得其准确的使用语法（即 socket. 
    getservbyname._ doc_）。那么，现在编写一个应用程序，使该应用程序能够通过网
    络发送一条虚拟消息，然后等待服务器回复。一旦你收到服务器的回复，就将其显
    示到屏幕上
'''

port = getservbyname("daytime", "UDP")
print("####### " + str(port))
addr = ("127.0.0.1", port)
conn = socket(AF_INET, SOCK_DGRAM)
conn.sendto("something".encode(), addr)
data, addr = conn.recvfrom(1024)
if data:
    print(data)

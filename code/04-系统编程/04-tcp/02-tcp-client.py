#coding=utf-8
from socket import *

# 创建socket
tcpClientSocket = socket(AF_INET, SOCK_STREAM)

# 链接服务器
srvAddr = ("192.168.33.144", 8899)
tcpClientSocket.connect(srvAddr)

# 提示用户输入数据
sendData = input("请输入您要发送的数据:")
sendData = sendData.encode()

tcpClientSocket.send(sendData)

# 接受对方发送过来的数据,最大接受1024个字节
recvData = tcpClientSocket.recv(1024)
print("接受到的数据为:%s"%recvData)

# 关闭套接字
tcpClientSocket.close()
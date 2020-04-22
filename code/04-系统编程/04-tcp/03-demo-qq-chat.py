#!/usr/bin/python3
#coding=utf-8
from socket import *

# 创建socket
tcpSrvSocket = socket(AF_INET, SOCK_STREAM)

# 绑定本地信息
address = ('', 7788)
tcpSrvSocket.bind(address)

# 使用socket创建的套接字默认的属性是主动的,使用listen将其变为被动等待接收别人的链接
tcpSrvSocket.listen(5)

while True:

    # 如果有新的客户端来链接服务器,那么就产生一个新型的套接字专门为这个客户端服务器
    # newSocket用来为这个客户端服务
    # tcpSrvSocket 就可以省下来专门等待其他新客户端的链接
    newSocket, clientAddr = tcpSrvSocket.accept()

    while True:

        # 接收对方发送过来的数据,最大接受1024个字节
        recvData = newSocket.recv(1024)
        recvData = recvData.decode(encoding="utf-8")

        # 如果接受的数据的长度为0,则意味着客户端关闭了链接
        if len(recvData)>0:
            print('recv:%s'%recvData)
        else:
            break

        # 发送一些数据到客户端
        sendData = input("send:")
        sendData = sendData.encode()
        newSocket.send(sendData)

    # 关闭这个客户端服务器的套接字,只要关闭了,就意味着为不能再为这个客户端服务了,如果还需要服务,只能重新运行程序
    newSocket.close()


# 关闭监听套接字,只要这个套接字关闭了,就意味着整个程序不再接受任何新的客户端连接
tcpSrvSocket.close()





#coding=utf-8

from socket import *

# 创建Socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# 绑定
serverSocket.bind((("", 8899)))

# listen,数字"5"表示已建立和未建立的队列总长度
serverSocket.listen(5)

# clientSocket表示新的客户端, clientInfo表示新的客户端的ip以及短裤
clientSocket, clientInfo = serverSocket.accept()

# 接受数据,最大字节数为1024
recvData = clientSocket.recv(1024)

# 打印
print("%s:%s"%(str(clientInfo), recvData))

# 关闭套接字
clientSocket.close()
serverSocket.close()
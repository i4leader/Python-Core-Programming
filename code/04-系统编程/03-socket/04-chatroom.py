#coding=utf-8

from socket import *

def main():
    udpSocket = socket(AF_INET, SOCK_DGRAM)

    udpSocket.bind(("", 6789))


    # 收到数据就打印
    while True:
        recvInfo = udpSocket.recvfrom(1024)
        print('[%s]:%s'%(str(recvInfo[1]), recvInfo[0].decode('utf-8')))

if __name__ == "__main__":
    main()




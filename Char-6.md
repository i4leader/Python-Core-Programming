# 1. 网络概述-udp
*** 
## 1.1.网络通信概述


## 1.2.tcp/ip 简介
### 1. 什么是协议
有的人说英语,有的人说中文,有的说德语,说同一种语言的可以交流,不同的语言之间就不行了.
为了解决不同族人之间的语言沟通障碍,规定了国际通用语言是英语,这时一个规定,这就是协议.   
   
### 2. 计算机网络沟通用什么
现在的生活中,不同的计算机只需要能够联网(有线无线都可以)那么就可以相互进行传递数据      
   
那么不同种类之间的计算机到底是怎么进行数据传递的呢?   
   
就像说不同语言的人沟通一样,只要有一种大家都认可都遵守的协议即可,那么这个计算机都遵守的网络通信协议叫做TCP/IP协议.
   
### 3. TCP/IP 协议(族)
早期的计算机网络,都是由各厂商自己规定一套协议,IBM,Apple和Microsoft都有各自的网路协议,互相兼容   
为了把全世界的所有不同类型的计算机都连接起来,就必须规定一套全球通用的协议,所以,大家把互联网的协议简称为TCP/IP协议.   
   
常用的网络协议如下图所示:
![tcpip](images/6-1.jpg)    
            
## 1.3.端口
### 1.什么是端口
那么TCP/IP协议中的端口指的是什么呢?   
端口就好比一个房子的门,是出入这间房子的必经之路.   
   
如果一个进程需要收发网络数据,那么就需要有这样的端口      
在linux系统中,端口可以有65536(2的16次方)个之多!   
既然有这么多,操作系统为了统一管理,所以进行了编号,这就是端口号.   
   
### 2. 端口号
端口是通过端口号来标记的,端口号只有整数,范围是从0到65535
   
### 3. 端口是怎样分配的   
端口号不是随意使用的,而是按照一定的规定进行分配.   
端口的分类标准有好几种,我们这里不做详细讲解,只介绍一下知名端口和动态端口.      
   
#### 3.1 知名端口(Well Known Ports)
知名端口是众所周知的端口号,范围从0到1023
```
80端口分配给HTTP服务
21端口分配给FTP服务
```
   
可以理解为,一些常用的功能使用的号码是估计的,好比 电话号码110,120,114一样      
   
#### 3.2 动态端口(Dynamic Ports)
动态端口的范围是从1024到65535   
之所以称为动态端口,是因为它一般不固定分配某种服务,而是动态分配.   
动态分配是指当一个系统进程或应用程序进程需要网络通信时,它向主机申请一个端口,主机从可用的端口号中分配一个供它使用.   
当这个进程关闭时,同时也就释放了所占用的端口号.      
   
#### 3.3 怎样查看端口?
用"netstat -an" 查看端口状态   
   
### 4.小总结   
端口有什么用呢? 我们知道,一台拥有IP地址的主机可以提供许多服务,比如HTTP(万维网服务),FTP(文件传输),SMTP(电子邮件)等,
这些服务完全可以通过1个IP地址来实现,那么,主机是怎样区分不同的网络服务呢?显然不能只靠IP地址,因为IP地址与网络服务的关系
是一对多的关系.实际上是通过"IP地址+端口号"来区分不同的服务的.需要注意的是,端口并不是一一对应的.比如你的电脑
作为客户机访问一台WWW服务器时,WWW服务器使用"80"端口与你的电脑通信,但你的电脑则可能使用"3457"这样的端口.      
   
## 1.4.ip地址
### 1. IP地址的作用
用来标识设备地址
   
### 2. IP地址的分类
每一个IP地址包括两部分:网络地址和主机地址   
   
### 2.1 A类IP地址

   
### 2.2 B类IP地址     
    
   
### 2.3 C类IP地址   
   
   
c类网路可达2097152个,每个网路能容纳254个主机   
   
### 2.4 D类地址用于多点广播
D类IP地址第一个字节以'1110'开始,它是一个专门保留的地址.   
它并不指向特定的网络,目前这一类地址被用在多点广播(Multicast)中   
多点广播地址用来一次寻址一组计算机  
地址范围:224.0.0.1-239.255.255.254


### 2.5 E类IP地址
以"1111"开始,为将来使用保留   
E类地址保留,仅做实验和开发用   
   
### 2.6 私有IP   
这么多网络ip中,国际规定有一部分IP地址是用于我们的局域网使用,也就是属于私网IP,不在公网中使用,他们的范围是:   
```
10.0.0.0 ~ 10.255.255.255
172.16.0.0 ~ 172.31.255.255
192.168.0.0 ~ 192.168.255.255

```   
   
### 2.7 注意
IP地址127.0.0.1~127.255.255.255 用于回路测试.   
如: 127.0.0.1可以代表本机IP地址,用http://127.0.0.1 就可以测试本机中配置的Web服务器.      
   
   
## 1.5.子网掩码


## 1.6.socket简介
### 1.本地的进程间通信(IPC)有很多种方式,例如
* 队列
* 同步(互斥锁,条件变量等)
以上通信方式都是在一台机器上不同进程之间的通信方式,那么问题来了   
网络中进程之间如何通信?      
   
### 2. 网络中进程之间如何通信
首要解决的问题是如何唯一标识一个进程,否则通信无从谈起!   
在本地可以通过进程PID来唯一标识一个进程,但是在网络中这是行不通的.   
其实TCP/IP协议族已经帮我们解决了这个问题,网络层的"IP地址"可以唯一标识网络中的主机,而传输层的"协议+端口"可以唯一
标识主机中的应用程序(进程).   
这样利用 ip地址,协议,端口就可以标识网络的进程了,网络中的进程通信就可以利用这个标志与其他进程进行交互.   

### 3. 什么是socket
socket(简称 套接字)是进程间通信的一种方式, 它与其他进程间通信的一个主要不同是:   
它能实现不同主机间的进程间通信,我们网络上各种各样的服务大多是基于socket来完成通信的,例如我们每天浏览网页,QQ聊天,收发email等等  
   
### 4. 创建socket
在Python中使用socket模块的函数,socket就可以完成:   
```
socket.socket(AddressFamily, Type)
```   
   
#### 说明:   
函数socket.socket 创建一个socket,返回该socket的描述符,该函数带有两个参数:
* Address Family:可以选择 AF_INET (用于Internet进程间通信)或者AF_UNIX(用于同一台机器进程间通信),
实际工作常用AF_INET
* Type:套接字类型,可以是SOCK_STREAM(流式套接字,主要用于TCP协议)或者SOCK_DGRAM(数据报套接字,主要用于UDP协议)     
   
创建一个tcp socket(tcp 套接字)   
```
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('TCP Socket Created')
```   
   
创建一个udp socket(udp套接字)
```
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('UDP Socket Created')
```   
   
   
   
## 1.7.udp介绍


## 1.8.udp网络程序-发送数据
创建一个udp客户端程序的流程是简单的,具体步骤如下:
1. 创建客户端套接字
2. 发送/接受数据
3. 关闭套接字

代码如下:
```
#coding=utf-8

from socket import *

#1. 创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

#2. 准备接收方的地址
sendAddr = ('192.168.33.144', 8080)

#3. 从键盘获取数据
sendData = input('请输入要发送的数据:')
sendData = sendData.encode()

#4. 发送数据到指定的电脑上
udpSocket.sendto(sendData, sendAddr)

#5. 关闭套接字
udpSocket.close()

```
   
运行结果:   
![socket](images/6-2-1.png)      
   
![socket-server](images/6-2-2.png)    
   
## 1.9.udp网络程序-发送,接收数据


## 1.10.udp网络程序-端口问题


## 1.11.udp绑定信息
### 1. 绑定信息
还记得在上一节课中,如果一个网络程序在每次运行的时候端口是随机变化的么?
   
一般情况下,在一天电脑上运行的网络程序有很多,而各自用的端口号很多情况下不知道,为了不与其他的网络程序占用同一个端口号,
往往在编程中,udp的端口号一般不绑定  
   
但是如果需要做成一个服务器端的程序的话,是需要绑定的,想想看这又是为什么呢?         
   
### 2. 绑定示例
```
#coding=utf-8

from socket import *

#1. 创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

#2. 绑定本地的相关信息,如果一个网络程序不绑定,则系统会随机分配
bindAddr = ('', 7788) #ip地址和端口号,ip一般不用写,表示本地的任何一个ip
udpSocket.bind(bindAddr)

#3. 等待接收对方发送的数据
recvData = udpSocket.recvfrom(1024)  # 1024表示本次接收的最大字节数

#4. 显示接收到的数据
print(recvData)

#5. 关闭套接字
udpSocket.close()
```   
   
运行结果：   
![socket-bind-recv](images/6-3.png)
   

## 1.12.udp网路通信过程


## 1.13.udp应用:模拟QQ聊天
代码演示:
```
#coding=utf-8

from threading import Thread
from socket import *

#1.收数据,然后打印
def recvData():
    while True:
        recvInfo = udpSocket.recvfrom(1024)
        print(">>%s:%s"%(str(recvInfo[1]), recvInfo[0]))

#2. 检测键盘,发数据
def sendData():
    while True:
        sendInfo = input("<<")
        udpSocket.sendto(sendInfo.encode("gb2312"), (destIp, destPort))


udpSocket = None
destIp = ''
destPort = 0

def main():

    global udpSocket
    global destIp
    global destPort

    destIp = input('对方的IP:')
    destPort = int(input('对方的端口:'))

    udpSocket = socket(AF_INET, SOCK_DGRAM)
    sendAddr = ('',4567)
    udpSocket.bind(sendAddr)

    tr = Thread(target=recvData)
    ts = Thread(target=sendData)

    tr.start()
    ts.start()

    tr.join()
    ts.join()

if __name__ == '__main__':
    main()
``` 



## 1.14.udp应用:聊天室
```
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
```
   
运行结果:   
![chatroom](images/6-5.png)   
   
   
   
## 1.15.udp总结


## 1.16.udp综合作业

# 2.TFTP项目-TCP编程
## 2.1 wireshark抓包工具使用


## 2.2 TFTP下载演示


## 2.3 应用:TFTP客户端


## 2.4 udp广播



## 2.5 tcp相关介绍



## 2.6 tcp服务器



## 2.7 tcp客户端


## 2.8 应用:模拟qq聊天 






# 3.网络
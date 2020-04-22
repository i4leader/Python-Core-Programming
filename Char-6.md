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
1. TFTP:
     TFTP（Trivial File Transfer Protocol,简单文件传输协议）是TCP/IP协议族中的一个用来在客户机与服务器之间进行简单文件传输的协议，基于UDP实现。提供不复杂、开销不大的文件传输服务。端口号为69。
2. TFTP的报文格式，如图所示
![tftp](images/6-5.png) 

图中显示了5种TFTP报文格式（操作码1和2的报文使用相同的格式）。   
   
TFTP报文的头两个字节表示操作码，对于读请求和写请求（WRQ)，文件名字段说明客户要读或写的位于服务器上的文件。模式字段是一个ASCII码串netascii或octet   
* netascii表示数据是以成行的ascii码字符组成，以两个字节\r \n作为行结束符
* octet则将数据看做8bit一组的字节流而不作任何解释。
   
最后一种TFTP报文类型是差错报文，它的操作码为5.它用于服务器不能处理读请求或者写请求的情况。在文件传输的过程中的读和写也会导致传送这种报文，接着停止传输。
3. TFTP的工作过程
     TFTP的工作过程很像停止等待协议，发送完一个文件块后就等待对方的确认，确认时应指明所确认的块号。发送万数据后在规定时间内收不到确认就要重发数据PDU，发送确认PDU的一方弱在规定时间内收不到下一个文件块，也要重发确认PDU。这样保证文件的传送不致因某一个数据报的丢失而告失败。
     
## 2.3 应用:TFTP客户端
```
#coding=utf-8
 
#导包
import sys
import struct
from socket import *
 
#全局变量
g_server_ip = ''
g_downloadFileName = ''
 
#运行程序格式不正确
def run_test():
	"判断运行程序传入参数是否有错"
	global g_server_ip
	global g_downloadFileName
	
	if len(sys.argv) != 3:
		print("运行程序格式不正确")
		print('-'*30)
		print("tips:")
		print("python3 tftp_download.py 192.168.1.1 test.jpg")
		print('-'*30)
		exit()
	else:
		g_server_ip = sys.argv[1]
		g_downloadFileName = sys.argv[2]
 
		#print(g_server_ip, g_downloadFileName)
 
#主程序
def main():
	run_test()
 
	# 打包
	sendDataFirst = struct.pack('!H%dsb5sb'%len(g_downloadFileName), 1, g_downloadFileName.encode('gb2312'), 0, 'octet'.encode('gb2312'), 0)
 
	# 创建UDP套接字
	s = socket(AF_INET, SOCK_DGRAM)
 
	# 发送下载文件请求数据到指定服务器
	s.sendto(sendDataFirst, (g_server_ip, 69)) #第一次发送, 连接tftp服务器
 
	downloadFlag = True #表示能够下载数据，即不擅长，如果是false那么就删除
	fileNum = 0 #表示接收文件的序号
 
	# 以二进制格式创建新文件
	f = open(g_downloadFileName, 'wb')
 
	while True:
	#3. 接收服务发送回来的应答数据
		responseData = s.recvfrom(1024)
 
		#print(responseData)
		
		recvData, serverInfo = responseData
 
		# 解包
		packetOpt = struct.unpack("!H", recvData[:2])  #操作码
		packetNum = struct.unpack("!H", recvData[2:4]) #块编号
 
		#print(packetOpt, packetNum)
 
		# 接收到数据包
		if packetOpt[0] == 3: #optNum是一个元组(3,)
			# 计算出这次文件的序号，是上一次接收到的+1。
			fileNum += 1
 
			# 文件超过了65535 那么就又从0开始计数。
			if fileNum == 65536:
				fileNum = 0
 
			# 包编号是否和上次相等
			if fileNum == packetNum[0]:
				f.write(recvData[4:]) #写入文件
				fileNum = packetNum[0]
 
			# 整理ACK的数据包
			ackData = struct.pack("!HH", 4, packetNum[0])
			s.sendto(ackData, serverInfo)
 
		# 错误应答
		elif packetOpt[0] == 5:
			print("sorry，没有这个文件!")
			downloadFlag = False
			break
 
		else:
			print(packetOpt[0])
			break
 
		# 接收完成，退出程序。
		if len(recvData) < 516:
			downloadFlag = True
			print("%s文件下载完毕!"%g_downloadFileName)
			break
 
	if downloadFlag == True:
		f.close()
	else:
		os.unlink(g_downloadFileName) #没有下载的文件，就删除刚创建的文件。
 
 
#调用main函数
if __name__ == '__main__':
	main()

```
   
运行结果:   
![tftp](images/6-6.png)   
   
## 2.4 udp广播
### 网络编程中的广播
```
#coding=utf-8

import socket, sys

dest = ('<broadcast>', 7788)

# 创建udp套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 对这个需要发送广播数据的套接字进行修改设置,否则不能发送广播数据
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)

# 以广播的形式发送数据到本网络的所有电脑中
s.sendto("Hi", dest)

print("等待对方回复(按CTRL+C退出)")

while True:
    (buf, address) = s.recvfrom(2048)
    print("Received from %s: %s"%(adress, buf))
```


## 2.5 tcp(传输控制协议)相关介绍
### udp(用户数据包协议)通信模型
udp通信模型中,在通信开始之前,不需要建立相关的链接,只需要发送数据即可,类似于生活中"写信"   
tcp特点:
   
* 稳定
* 相对于udp而言,要慢一点
* web服务器都是用的tcp
   
udp特点   
* 不稳定
* 适当比tcp要快一些
   
![udp模型](images/6-7.png)     
   
### tcp通信模型
udp通信模型中,在通信开始之前,一定要建立相关的链接,才能发送数据,类似于生活中的"打电话"   
![tcp模型](images/6-8.png)   
   
   
   
   
   
## 2.6 tcp服务器
如果上面的电话机过程一样,在程序中,如果想要完成一个tcp服务器的功能,
1. socket创建一个套接字
2. bind绑定ip和port
3. listen 是套接字变为可以被动链接
4. accept等待客户端的链接
5. recv/send 接受发送数据
   
一个很简单的tcp服务器如下:   
   
```
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
```
   
运行结果:   
![tcpsrv](images/6-9.png)   
   

## 2.7 tcp客户端
tcp客户端,并不是像之前一个段子:一个顾客去饭馆吃饭,这个顾客要加菜,就问服务员咱们饭店有客户端吗,然后这个服务员非常客气的说道:先生,我们饭店不用客户端,我们直接送到您的餐桌上.   
如果,不学习网络的知识是不是说不定也会发生那样的笑话.  
   
所谓的服务器端:就是提供服务的一方,而客户端,就是需要被服务的一方   
   
### tcp客户端构建流程
tcp的客户端要比服务器端简单很多,如果说服务器端是需要自己买手机,插手机卡,设置铃声,等待别人打电话流程的话,那么客户端就只需要找一个电话亭,拿起电话拨打即可,流程要少很多   
   
示例代码:      
```
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
```   
   
运行结果:   
![tcpclient](images/6-10.png)   
   
![tcpcli1](images/6-10-1.png)   
     
   
## 2.8 应用:模拟qq聊天 
代码如下:
```
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

```
   
运行结果:
![client](images/6-11-1.png)   
   
![server](images/6-11-2.png)   

# 3.网络通信过程详解
## 3.1 Packet Tracer网络通信过程
Packet Tracer 是由Cisco(著名网络公司,思科)公司发布的一个辅助学习工具,
为学习思科网络课程的初学者去设计,配置,排除网络故障提供了网络模拟环境.
用户可以在软件的图形界面上直接使用拖拽方法建立网络拓扑,并可提供数据包在网络中进行详细的处理过程,观察网络实时运行情况.   


## 3.2 2台电脑组网



## 3.3 通过集线器组网



## 3.4 通过交换机组网



## 3.5 通过路由器组网



## 3.6 交换机,路由器,服务器组网



## 3.7 tcp三次握手



## 3.8 tcp四次握手



## 3.9 tcp十种状态



## 3.10 tcp的2MSL问题



## 3.11 tcp长连接和短连接



## 3.12 listen的队列长度



## 3.13 手动配置IP



## 3.14 常见网络攻击案例



## 3.14 家庭上网解析




# 1. 进程
# 2. 线程
***
## 2.1 多线程-threading
python 的thread模块是比较底层的模块,python的threading模块是对tread做了一些包装,可以更加方便的被使用   
   
### 1.使用threading模块
**单线程执行**
```
#coding=utf-8
import time

def saySorry():
    print("亲爱的,我错了,我能吃饭了吗?")
    time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        saySorry()
```     
   
运行结果:   
![singlethread](images/5-1.png)
   
**多线程执行**
```
#coding=utf-8
import threading
import time

def saySorry():
    print("亲爱的,我错了,我能吃饭了吗?")
    time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=saySorry())
        t.start() #启动线程,即让线程开始执行
```   
   
运行结果:   
![multithread](images/5-1.png)   
   
#### 说明
1. 可以明显看出使用了多线程并发的操作,花费的时间短很多
2. 创建好的线程,需要调用start()方法来启动   
   
   
## 2.2 threading 注意点


## 2.3 多线程-共享全局变量


## 2.4 进程,线程对比
### 功能
* 进程,能够完成多任务,比如在一台电脑上能够同时运行多个QQ
* 线程,能够完成多个任务,比如一个QQ中的多个聊天窗口
   
   
   
   
## 2.5 同步的概念


## 2.6 互斥锁


## 2.7 多线程-非共享数据


## 2.8 死锁


## 2.9 同步应用


## 2.10 条件变量


## 2.11 生产者与消费者-条件变量
### 线程同步之条件变量
互斥锁是最简单的线程同步机制,Python提供的Condition对象提供了对复杂线程同步问题的支持.   
Condition被称为条件变量,除了提供与Lock类似的acquire和release方法外,还提供了wait和notify方法.   
线程首先acquire一个条件变量,然后判断一些条件.   
* 如果条件不满足则wait;
* 如果条件满足,进行一些处理改变条件后,通过notify方法通知其他线程,其他处于wait状态的线程接到通知后会
重新判断条件.不断的重复这一过程,从而解决复杂的同步问题.   
   
示例如下:   
```

```   
    
运行结果:   

   
可以认为Condition对象维护了一个锁(Lock/RLock)和一个waiting池,线程通过acquire获得Condition对象,
当调用方法时,线程会释放Condition内部的锁并进入blocked状态,同时在waiting池中记录这个线程.当调用notify
方法时,Condition对象会从waiting池中挑选一个线程,通知其调用acquire方法尝试取到锁.   
Condition对象的构造函数可以接受一个Lock/Rlock对象作为参数,如果没有指定,则Condition对象会在内部自行创建一个RLock.   
除了notify方法外,Condition对象还提供了notifyAll方法,可以通过waiting池中的所有线程尝试acquire内部锁.
由于上述机制,处于waiting 状态的线程只能通过notify方法唤醒,所以notifyAll的作用在于防止有线程永远处于沉默状态.   
   
### 生产者与消费者-条件变量
演示条件变量同步的经典问题是生产者与消费者的问题: 假设有一群生产者(Producer)和一群消费者(Consumer) 通过
一个市场来交互产品. 生产者的"策略"是如果市场上剩余产品的数量多余100个,那么就消费3个产品.用Condition解决生产者与消费者问题的代码如下:   
```




```   
   
   
   
   
   
   
   
## 2.12 生产者与消费者-队列
前面介绍了互斥锁和条件变量解决线程间的同步问题,并使用条件变量同步机制解决了生产者与消费者问题.   
让我们考虑更复杂的一种场景: 产品是各不相同的. 这时只记录一个数量就不够了,还需要记录每个产品的细节.
很容易想到需要用一个容器将这些产品记录下来.   

### 1. 队列
先进先出   

先进后出
   
Python的Queue模块中提供了同步的,线程安全的队列类,包括FIFO(先入先出)队列Queue, LIFO(后入先出) 队列LifoQueue,
和优先级队列PriorityQueue. 这些队列都实现了锁原语 (可以理解为原子操作,即要么不做,要么就做完), 能够在多线程中直接使用.
可以使用队列来实现线程间的同步.   
用FIFO队列实现上述生产者与消费者问题的代码如下:   
```


```   
   
   
   

## 2.13 ThreadLocal



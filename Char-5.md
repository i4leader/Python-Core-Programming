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
### 2.2.1 线程执行代码的
通过上一小节,能够看出,通过使用threading 模块能够完成多任务的程序开发,为了让每个线程的封装性更完美,所以使用threading模块时,
往往会定义一个新的子类class,只要继承threading.Tread就可以了,然后重写run方法   
示例如下:   
```
#coding=utf-8
import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name+ ' @ '+str(i) #name属性中保存的是当前线程的名字
            print(msg)


if __name__=='__main__':
    t = MyThread()
    t.start()

```   
运行结果:   
![thread](images/5-2.png)      
   
#### 说明
*   python的threading.Thread 类有一个方法,用于定义线程的功能函数,可以在自己的线程类中覆盖该方法,而创建自己的线程实例后,
通过Thread类的start方法,可以启动该线程,交给python虚拟机进行调查,当该线程获得执行的机会时,就会调用run方法执行线程.   
   
### 2.2.2 线程的执行顺序  
``` 
#coding=utf-8
import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name+ ' @ '+str(i) #name属性中保存的是当前线程的名字
            print(msg)

def test():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == "__main__":
    test()

```   
运行结果:      
![threadorder](images/5-3.png)   
   
#### 说明
从代码和执行这里我们可以看出,多线程程序的执行顺序是不确定的.当执行到sleep语句时, 线程将被阻塞(Blocked),到sleep结束后,
线程进入就绪(Runnable)状态,等待调度.而线程调度将自行选择一个线程执行,上面的代码中只能保证每个线程都运行完整个run函数,
但是线程的启动顺序,run函数中每次循环的执行顺序都不能确定.     
   
### 2.2.3. 总结
1. 每个线程一定会有一个名字,尽管上面的例子中没有指定线程对象的name,但是python会自动为线程指定一个名字.   
2. 当线程的run()方法结束时该线程完成.   
3. 无法控制线程调度程序,但可以通过别的方式来影响线程调度的方式
4. 线程的几种状态      
   
## 2.3 多线程-共享全局变量
```
#coding=utf-8
from threading import Thread
import time

g_num = 100

def work1():
    global g_num
    for i in range(3):
        g_num += 1

    print("----in work1, g_num is %d----"%g_num)


def work2():
    global g_num
    print("----in work2, g_num is %d----"%g_num)

print("----线程创建之前g_num is %d----"%g_num)

t1 = Thread(target=work1)
t1.start()

# 超时一会,保证t1线程中的事情做完
time.sleep(1)

t2 = Thread(target=work2)
t2.start()

```   
运行结果:   
![线程间共享](images/5-4.png)   

### 共享全局变量的缺点
```
from threading import Thread
import time

g_num = 0

def test1():
    global g_num
    for i in range(1000000):
        g_num += 1

    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num
    for i in range(1000000):
        g_num += 1

    print("---test2---g_num=%d"%g_num)

p1 = Thread(target=test1)
p1.start()

time.sleep(3) #取消屏蔽之后 再次运行程序,结果会不一样,,,为啥呢?

p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)

```   
运行结果:   
![yessleep](images/5-5.png)      
   
![nosleep](images/5-6.png)  
   
### 列表当做实参传递到线程中
```
from threading import Thread
import time

def work1(nums):
    nums.append(44)
    print("----in work1----",nums)

def work2(nums):
    # 延时一会,保证t1线程中的事情做完
    time.sleep(1)
    print("---in work2---",nums)
    
g_nums = [11,22,33]

t1 = Thread(target=work1, args=(g_nums,))
t1.start()

t2 = Thread(target=work2, args=(g_nums,))
t2.start()
```     
   
运行结果:      
![list2parameter](images/5-7.png)    
  
#### 总结
* 在一个进程内的所有线程共享全局变量,能够在不适用其他方式的前提下完成多线程之间的数据共享(这点要比多进程要好)
* 缺点就是,线程是对全局变量随意篡改可能造成多线程之间对全局变量的混乱(即线程非安全)  
  
   
## 2.4 进程,线程对比
### 功能
* 进程,能够完成多任务,比如在一台电脑上能够同时运行多个QQ
* 线程,能够完成多个任务,比如一个QQ中的多个聊天窗口

   
   
   
   
## 2.5 同步的概念
### 2.5.1 多线程开发可能遇到的问题
假设两个线程11和12都要对num=0进行增1运算,11和12都会对num修改10次,num的最终的结果应该为20.   
但是由于是多线程访问,有可能出现下面的情况:   
在num=0时,t1取得num=0,此时系统把t1调度为"sleeping"状态,把t2转换为"running"状态,t2也获得num=0,然后t2对得到的值
进行加1并赋给num,使得num=1,然后系统又把t2调度为"sleeping",把t1转为"running",线程t1又把它之前得到的0加1后赋值给num.
这样,明明t1和t2都完成了1次加1工作,但结果仍然是num=1.   
   
```
from threading import Thread
import time

g_num = 0

def test1():
    global g_num
    for i in range(1000000):
        g_num += 1

    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num
    for i in range(1000000):
        g_num += 1

    print("---test2---g_num=%d"%g_num)

p1 = Thread(target=test1)
p1.start()

time.sleep(3) #取消屏蔽之后 再次运行程序,结果会不一样,,,为啥呢?

p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)

```   
   
运行结果(可能不一样,但是结果往往不是2000000):   
![yessleep](images/5-5.png)      
   
![nosleep](images/5-6.png)  
   
   

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



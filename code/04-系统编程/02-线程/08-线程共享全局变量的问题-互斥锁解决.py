from threading import Thread, Lock
import time

g_num = 0

def test1():
    global g_num
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()
    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()
    print("---test2---g_num=%d"%g_num)

# 创建一把互斥锁,这个锁默认是没有上锁的
mutex = Lock()



p1 = Thread(target=test1)
p1.start()

# time.sleep(3) #取消屏蔽之后 再次运行程序,结果会不一样,,,为啥呢?

p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)

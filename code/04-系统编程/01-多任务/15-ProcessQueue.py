#coding=utf-8
from multiprocessing import Queue
from multiprocessing import Process
import os, random, time

# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print("Put %s to queue..."%value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print("Get %s from queue."%value)
            time.sleep(random.random())
        else:
            break


if __name__=='__main__':
    # 父进程创建Queue,并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw,写入:
    pw.start()
    # waiting for pw end
    pw.join()
    # start sub_process pr, and read:
    pr.start()
    pr.join()
    # pr process is dead loop, cannot wait for it's ending
    print('')
    print("All data are write and read, Done!")



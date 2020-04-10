#coding=utf-8
from multiprocessing import Process
import os
from time import sleep

# 子进程要执行的代码
def run_proc(name, age, **kwargs):
    print('子进程运行中,name= %s, age=%d, pid=%d...'%(name, age, os.getpid()))
    print(kwargs)
    sleep(0.5)

if __name__=='__main__':
    print('父进程 %d.'%os.getpid())
    p = Process(target=run_proc, args=('test', 19), kwargs={'m':20})
    print('子进程将要执行')
    p.start()   # 让这个进程开始执行run_proc函数里的代码
    p.join() # 堵塞
    print('子进程已结束')
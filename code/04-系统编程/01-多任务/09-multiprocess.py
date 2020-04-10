#coding=utf-8
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('子进程运行中,name= %s,pid=%d...'%(name, os.getpid()))

if __name__=='__main__':
    print('父进程 %d.'%os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('子进程将要执行')
    p.start()   # 让这个进程开始执行run_proc函数里的代码
    p.join()
    print('子进程已结束')
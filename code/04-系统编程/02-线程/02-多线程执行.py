#coding=utf-8
from threading import Thread
import time
import os

def saySorry():
    print("亲爱的,我错了,我能吃饭了吗?")
    time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        t = Thread(target=saySorry())
        t.start() #启动线程,即让线程开始执行
       # print(t)
       # print(os.getpid())

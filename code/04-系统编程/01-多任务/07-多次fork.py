import os
import time

# 父进程
ret = os.fork()
if ret == 0:
    # 子进程
    print("--1--")
else:
    # 父进程
    print("--2--")

    # 父子进程
    ret = os.fork()
    if ret == 0:
        # 2儿子
        print('--11--')
    else:
        # 父进程
        print('--22--')


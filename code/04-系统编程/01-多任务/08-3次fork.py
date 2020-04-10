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
    print('--11--')
else:
    print('--22--')

# 父子进程
ret = os.fork()
if ret == 0:
    print('--111--')
else:
    print('--222--')

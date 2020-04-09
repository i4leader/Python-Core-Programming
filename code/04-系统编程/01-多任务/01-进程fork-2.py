import os
import time

# 注意,fork函数,只在Unix/Linux/Mac 上运行,Windows不可以
pid = os.fork()

if pid == 0:
    while True:
        print("哈哈1")
        time.sleep(1)

else:
    while True:
        print("哈哈2")
        time.sleep(1)


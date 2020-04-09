import os

# 注意,fork函数,只在Unix/Linux/Mac 上运行,Windows不可以
pid = os.fork()
print(pid)
if pid > 0:
    print("---父进程:%d---%d"%(pid, os.getpid()))

else:
    print("-"*50)
    print(pid)
    print("---子进程:%d---pid:%d---ppid:%d"%(pid, os.getpid(), os.getppid()))

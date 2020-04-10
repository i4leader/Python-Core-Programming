#coding=utf-8
from multiprocessing import Queue
q=Queue(3) #初始化一个Queue对象,最多可接受三条put消息
q.put("消息1")
q.put("消息2")
print(q.full()) #false
q.put("消息3")
print(q.full()) #true


## 1. 面向对象进阶

  

## 2. 其他知识点
### 2.1 import 导入模块
#### 1. 搜索路径
```
import sys
sys.path
```
![import](images/1-1.png)   

**路径搜索**  
* 从上面列出的目录中按照顺序搜索路径
* 如果路径不存在，可以使用sys.path.append 添加路径
* ‘’表示当前路径

#### 2. 重新导入模块
模块被导入之后，import module 不能重新导入模块，重新导入需要   
```
reload.模块文件名()
```   
![import](images/1-1.png)   
   
   
### 2.2 循环导入
#### 1. 什么是循环导入
a.py   
```
from b import b

print(“------This is module a.py------")
def a():
    print("hello, a")
    b()

a()
```   

b.py   
```
from a import a

print("---------This is module b.py----------")

def b():
    print("hello, b")

def c():
    a()
c()
~      
```   

不要在模块中相互调用，否则会出现问题。   


### 2.3 作用域
#### 什么是命名空间
> 比如有一个学校,有10个班级,在7班和8班中都有一个叫"小王"的同学,如果在学校的广播中呼叫'小王'时,7班和8班的
> 这两个人就纳闷了,你是喊谁呢!!! 如果是7班的小王的话,那么就很明确了,那么此时的7班就是小王所在的范围,即命名空间.
   
#### globals,locals
> 在之前学习变量的作用域时,经常会提到全局变量和局部变量,之所以称之为局部,全局.就是因为他们的自作用的区域不同,这就是作用域   
   
* locals
   
![locals](images/1-6.png)   
   
* globals
   
![locals](images/1-7.png)   
   
#### LEGB
Python 使用LEGB的顺序来查找一个符号对应的对象   
```
locals -> enclosing functions -> globals -> builtins
```   
   
* locals,当前所在命名空间(如函数,模块),函数的参数也属于命名空间内的变量  
* enclosing, 外部嵌套函数的命名空间(闭包中常见)
```
def fun1():
    a = 10
    def fun2():
        # a 位于外部嵌套函数的命名空间
        print(a)
```   
* globals,全局变量,函数定义所在模块的命名空间   
```
a = 1
def fun():
    # 需要通过 global 指令来声明全局变量
    global a
    # 修改全局变量,而不是创建一个新的 local 变量
    a = 2
```

### 2.4 == 、 is（重点）
![==is](images/1-3.png)   
   
#### 总结   
* is是比较两个引用是否指向了同一个对象（引用比较）
* == 是比较两个对象是否相等   

### 2.5 深拷贝、浅拷贝（重点）
#### 1. 浅拷贝
* 浅拷贝是对于一个对象的顶层拷贝   
   
通俗的理解是：拷贝了引用，并没有拷贝内容   
![qiancopy](images/1-4.png)   

#### 2. 深拷贝
* 深拷贝是对于一个对象的内容进行了拷贝   
   
```
import copy

a = [11,22,33]

b = copy.deepcopy(a)

id(a)

id(b)
```   
![deepcopy](images/1-5.png)   
   
Python的每个对象都分为可变和不可变，主要的核心类型中，数字、字符串、元组是不可变的，列表、字典是可变的。   

copy.copy()如果复制的不可变类型，那就是浅copy；如果复制的是可变类型，则第一层是深copy，第二层为浅copy。   

### 2.6 进制、位运算
看如下示例：   
> 如果有一个十进制数5，其二进制为: 0000 0101
> 把所有的数像左移一位，其结果为: 0000 1010
> 想一想：二进制 0000 1010 十进制是多少呢？？？ 其答案为10，有没有发现是5的2倍呢！
> 再假设有一个十进制数3，其二进制为： 0000 0011
> 把所有数像左移动一位，其结果为： 0000 0110
> 二进制0000 0110 的十进制为6，也正好是3的2倍
通过以上2个例子，能够看出，把一个数的各位整体向左移动一个位，就变成原来的2倍   
那么在python中，怎样实现向左移动呢？还有其他的吗？？？   
   
#### <1>位运算的介绍
* & 按位与
* | 按位或
* ^ 按位异或
* ~ 按位取反
* << 按位左移
* \>> 按位右移   
用途：直接操作二进制，省内存，效率高   

#### <2>位运算
##### 1) << 按位左移
```
各二进位全部左移n位，高位丢弃，低位补0   
```   
```
x << n 左移 x 的所有二进制位向左移动n位，移出位删掉，移进的位补0
```   
**【注意事项】**
* a 左移1位相当于乘以 2
* 用途，快速计算一个数乘以2的n次方（8<<3等同于8*2^3）
   
b. 左移可能会改变一个数的正负性   

##### 2）>> 按位右移
```
各二进位全部右移n位,保持符号位不变

x >> n x的所有二进位向右移动n位,移出的位删掉,移进的位补符号位,右移不会改变一个数的符号
```   
**[注意事项]** 
* 右移1位相当于除以2
* x 右移n位就相当于除以2的n次方  用途:快速计算一个数除以2的n次方(8>>3等同于8/2^3)   
   
##### 3) & 按位与
```
全1才1否则0: 只有对应的两个2进位均为1时,结果位才为1,否则为0  
用6和3这个例子,不要用9和13的例子
```   

##### 4) | 按位或
```
有1就1 只要对应的二个二进位有一个为1时,结果位就为1,否则为0
```   

##### 5) | 按位异或
```
不同为1 当对应的二进位相异(不相同)时,结果为1,否则为0
```   

##### 6) ~取反
```
很好哦理解,就是原来为0的变成1,原来1的变成0.
```  
~9 = -10

##### [扩展]
位运算优先级

### 2.7 私有化
* xx:公有变量
* _x:单前置下划线,私有化属性和方法, from somemodule import * 禁止导入,类对象和子类可以访问 
* __xx: 双前置下划线,避免与子类中的属性命名冲突,无法在外部直接访问(名字重整所以访问不到)
* \_\_xx__: 双前后下划线.用户名字空间的魔法对象和属性,例如:\_\_init__, __不要自己发明这样的名字
* xx_: 单后置下划线,用于避免与Python关键词的冲突  
    
通过name mangling (名字重整(目的就是以防子类意外重写基类的方法或者属性)如:_Class_object) 机制就可以访问private了.   
   
```
#coding=utf-8

class Person(object):
    def __init__(self, name, age, taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def showperson(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    def dowork(self):
        self._work()
        self.__away()

    def _work(self):
        print("my _work")

    def __away(self):


```   
   

### 2.8 属性property
#### 1. 私有属性添加getter 和setter 方法
```
class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error,不是整型数字")
```   

#### 2. 使用property升级getter 和setter 方法
```
class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error,不是整型数字")
    money = property(getMoney, setMoney)

```

## 3. 其他知识点



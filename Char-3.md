## 1. 面向对象进阶


## 2. 其他的知识点


## 3. 其他的知识点
### 3.1 垃圾回收(1)


### 3.2 垃圾回收(2)


### 3.3 垃圾回收(3)-gc模块


### 3.4 内建属性


### 3.5 内建函数


### 3.6 集合set


### 3.7 functools


### 3.8 模块


### 3.9 调试
#### pdb
pdb 是基于命令行的调试工具,非常类似gnu的gdb(调试c/c++).
   
|命令|简写命令|作用|
|:----|:----|:----|
|break|b|设置断点|
|continue|c|继续执行程序,遇到断点才会停|
|list|l|查看当前行的代码段|
|step|s|进入函数|
|return|r|执行代码直到从当前函数返回|
|quit|q|终止并退出|
|next|n|执行下一行|
|print|p|打印变量的值|
|help|h|帮助|
|args|a|查看传入参数|
| |回车|重复上一条命令|
|break|b|显示所有断点|
|break lineno|b lineno|在指定行设置断点|
|break file:lineno|b file:lineno|在指定文件的行设置断点|
|clear num| |删除指定断点|
|bt| |查看函数调用栈帧|
   
#### 执行时调试:
程序启动,停止在第一行等待单步调试.   
```
python3 -m pdb some.py
```  
   
#### 交互调试
进入python或ipython解释器   
```
import pdb
pdb.run('testfun(args)')  #此时会打开pdb调试,注意: 先使用s跳转到这个testfun函数中,然后就可以使用
```   
   
#### 程序里埋点
当程序执行到pdb.set_trace() 位置时停下来调试  
```
代码上下文
...

import pdb
pdb.set_trace()

...

```   

设置断点:   
```
b 7

```   
![breakpoint](images/3-1.png)   
   
删除断点   
```
clear 7
```   
![clearb](images/3-2.png)   
   
打印变量数据   
```
p 变量名

```   
![clearb](images/3-3.png)  
   
#### 日志调试   
##### Print 大法      
   
使用pdb调试5个demo   
##### demo 1
```
import pdb
a = "aaa"
pdb.set_trace()
b = "bbb"
c = "ccc"
final = a + b + c
print final

```

作业:   
```
#coding = utf-8
import pdb

def add3Nums(a1,a2,a3):
    result = a1+a2+a3
    return result

def get3NumsAvarage(s1,s2):
    s3 = s1 + s2 + s1
    result = 0
    result = add3Nums(s1,s2,s3)/3

if __name__ = '__main__':
    
    a = 11
    # pdb.set_trace()
    b = 12
    final = get3NumsAvarage(a,b)
    print(final)

```
   
pdb 调试有个缺陷就是对于多线程,远程调试支持不够好,同时没有直观的显示.      
   

### 3.10 编码风格
#### 错误认知
* 这很浪费时间
* 我是个艺术家
* 所有人都能穿的鞋不会合任何人的脚
* 我擅长指定编码规范
   
#### 正确认知
* 促进团队协作
* 减少bug处理
* 提高可读性,降低维护成本
* 有助于代码审查
* 养成习惯,有助于程序员自身的成长
   
#### pep8 编码规范
python Enhancement Proposals: Python 改进方案
https://www.python.org/dev/peps/
   
#### 每级缩进4个空格
括号中使用垂直隐式缩进或使用悬挂缩进.后者应该注意第一行要没有参数,后续行要有缩进.   
* Yes
   
```
# 对准左括号
foo = long_function_name(var_one, var_two, 
                         var_three, var_four)

# 不对准左括号,但多加一层缩进,以和后面内容区别.
def long_function_name(
        var_one, var_two, var_three, var_four):
    print(var_one)

# 悬挂缩进必须多加一层缩进.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```   
* No
   
```
# 不使用垂直对齐时,第一行不能有参数.
foo =  long_function_name(var_one, var_two, 
    var_three, var_four)

# 参数的缩进和后续内容缩进不能区别
def long_function_name(
    var_one, var_two, 
    var_three, var_four): 
    print(var_one)
```
   
#### 四个空格的规则是对续行可选的
```
# 悬挂缩进不一定是四个空格
foo = long_function_name(
  var_one, var_two, 
  var_three, var_four)
if 语句跨行时,两个字符关键字(比如if)加上一个空格,再加上左括号构成了很好的缩进.后续行暂时没有规定

# 没有额外缩进,不是很好看,不是很推荐
if (this_is_one_thing and 
    that_is_another_thing):
    do_something()

# 添加注释
if (this_is_one_thing and 
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate. 
    do_something()

# 额外添加缩进,推荐
# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing 
        and that_is_another_thing):
    do_something()

```

#### 左边括号也可以另起一行.有两种格式,建议第2中.
```
# 右括号不回退,个人不推荐
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )

# 右括号回退
my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```
   
#### 空格或Tab?
* 空格是首选的缩进方法.
* Tab仅仅在已经使用tab缩进的代码中为了保持一致性而使用.   
* Python3 中不允许混合使用Tab和空格缩进
* Python2 中包含空格与Tab和空格缩进的应该全部转为空格缩进.
   
#### 最大行宽
* 限制所有行的最大行宽为79字符
* 文本长块,比如文档字符串或注释,行长宽应限制为72字符.
   
#### 空行
* 两行空行分割顶层函数和类的定义
* 类的方法定义用单个空行分割
* 额外的空行可以必要的时候用于分割不同的函数组,但是要尽量节约使用
* 额外的空行可以必要的时候用于分割不同的逻辑块,但是要尽量节约使用.
      
#### 源文件编码
* 在核心Python发布的代码应该总是使用UTF-8(ASCII在Python2) .
* Python3(默认UTF-8)不应有编码声明.  
   

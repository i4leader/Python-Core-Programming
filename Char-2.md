## 面向对象进阶

### 1.1 元类


### 1.2 python是动态语言
#### 1.动态语言的定义
动态编程语言 是 高级程序设计语言 的一个类别,在计算机科学领域已被广泛应用,它是一类在 运行时可以改变其结构的语言:
例如新的函数,对象,甚至代码可以被引进,已有的函数可以被删除或是其他结构上的变化.动态语言目前非常有活力,例如JavaScript
便是一个动态语言,除此之外如PHP,Ruby,Python等也属于动态语言,而C,C++等语言则不属于动态语言.---来自维基百科
   
#### 2. 运行的过程中给对象绑定(添加)属性
```
class Person(object):
    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age


P = Person("小明","24")
```   
   
在这里,我们定义了1个类Person,在这个类里,定义了两个初始属性name和age,但是人还有性别啊!
如果这个类不是你写的是不是你会尝试访问性别这个属性呢?   
```
P.sex = 'male'
P.sex
```   
   
这时候就发现问题了,我们定义的类里面没有sex这个属性啊!怎么回事呢?这就是动态语言的魅力和坑!这里实际上就是动态给实例绑定属性!
   
#### 3. 运行的过程中给类绑定(添加)属性
```
class Person(object):
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge


laowang = Person("老王","30")
print(laowang.name)
print(laowang.age)

laowang.addr = "beijing"  # 给对象添加属性
print(laowang.addr)

laozhao = Person("laozhao", 18)
#print(laozhao.addr)

Person.num = 100    # 给类添加属性

print(laozhao.num)
print(laowang.num)
```   
   


### 1.3 __slots__
现在我们终于明白了,动态语言和静态语言的不同   
动态语言: 可以在运行的过程中修改代码   
静态语言: 编译时已经搞定好代码,运行过程中不能修改   
如果我们想要限制实例的属性怎么办? 比如,只允许对Person实例添加name和age属性.   
为了达到限制的目的,Python允许在定义class的时候,定义一个特殊的__slots__变量,来限制该实例能添加的属性:   
![slots](images/2-2.png)
   
#### 注意:
* 使用__slots__要注意,__slots__定义的属性仅对当前类实例起作用,对继承的子类是不起作用的
   



### 1.4 生成器
#### 1.什么是生成器
通过列表生成式,我们可以直接创建一个列表,但是,受到内存限制,列表的容量肯定是有限的.而且,创建一个包含100万
个元素的列表,不仅占用很大的存储空间,如果我们仅仅需要访问前面几个元素,那后面绝大多数元素占用的空间都白白
浪费了,所以,如果列表元素可以按照某种算法推算出来,那我们是否可以在循环的过程中不断推算出后续的元素呢?这样
就不必创建完整的list,从而节省大量的空间.**在Python中,这种一边循环一边计算的机制,称为:生成器 Generator**
   
#### 2.创建生成器方法1
要创建一个生成器,有很多种方法,第一种方法很简单,只要把一个列表生成式的[]改成()   
```
>>> L = [x*2 for x in range(5)]
>>> L
[0, 2, 4, 6, 8]
>>> G = ( x*2 for x in range(5))
>>> G
<generator object <genexpr> at 0x101633050>
>>> 

```   
   
创建 L 和 G 的区别在于最外层的[]和(), L 是一个列表, 而 G 是一个生成器. 我们可以直接打印出 L 的每一个元素,
但我们怎么打印出 G 的每一个元素呢? 如果要一个一个打印出来,可以通过next()函数获得生成器的下一个返回值:   
```
>>> G
<generator object <genexpr> at 0x101633050>
>>> next(G)
0
>>> next(G)
2
>>> next(G)
4
>>> next(G)
6
>>> next(G)
8
>>> next(G)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> 

```

#### 3. 创建生成器的方式2
generator非常强大.如果推算的算法比较复杂,用类似列表生成式的for 循环无法实现的时候,还可以用函数来实现.   
比如,著名的斐波拉契数列(Fibonacci), 除第一个和第二个数外,任意一个数都可由两个数相加得到:   
1,1,2,3,5,8,13,21,34,...   
斐波那契数列用列表生成式写不出来,但是,用函数把它打印出来却很容易:   
```
>>> def fib(times):
...     n = 0
...     a,b = 0,1
...     while n<times:
...         print(b)
...         a,b = b, a+b
...         n+=1
...     return 'done'
... 
>>> fib(5)
1
1
2
3
5
'done'

```   
```
def creatNum():
    print("-----start-----")
    a,b = 0,1
    for i in range(5):
        yield b     
        a,b = b,a+b
    print("----stop-----")

a = createNum()

# 方式一
for num in a:   #迭代器是可以用for循环来打印的.   
    print(num)

# 方式二
ret = a.__next__()
print(ret)

#注意:
#next(a)
#a.__next__()
#以上两种方式是一样的

```   
   
#### 4. send
例子: 执行到yield时,gen函数作用暂时保存,返回i的值; temp接受下次c.send("python"), send发送过来的值,
c.next()等价c.send(None)   
```
def gen():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i+=1
       
```   
   
**使用Next函数**
   
```
f = gen()
next(f)
0
next(f)
None
1
f.__next__()
None
2
f.send(None)
None
3
f.send(None)
None
4
```   
   
![send](images/2-3.png)      
   
   
   
   
### 1.5 迭代器
迭代是访问集合元素的一种方式,迭代器是一个记住遍历的位置的对象.迭代器对象从集合的第一个元素开始访问,直到,直到所有的元素被访问完结束.迭代器只能往前不能往后.
   
#### 1) 可迭代对象
以直接作用于for循环的数据类型有以下几种:   
一类是集合数据类型,如list, tuple, dict, set, str等;   
一类是generator,包括生成器和带yield的generator function,   
这些可以直接作用于for循环的对象统称为可迭代对象: Iterable .   

#### 2) 判断是否可以迭代
可以使用isinstance()判断一个对象是否是Iterable对象;   
![iterableobject](images/2-1.png)   

#### 3) 迭代器
可以被next()函数调用并不断返回下一个值得对象称为迭代器: Iterator.   

#### 4) iter()函数
生成器都是Iterator对象,但list, dict, str 虽然是Iterable, 却不是Iterator.   
把list, dict, str等Iterable 变成 Iterator 可以使用iter()函数:   
```
from collections import *
isinstance(iter([]), Iterator)
True
isinstance(iter('abc'), Iterator)
True
```   

#### 总结
* 凡是可作用于for循环的对象都是Iterable类型;
* 凡是可作用于next()函数的对象都是Iterator类型
* 集合数据类型如list, dict, str 等是iterable 但不是iterator,不过可以通过iter()函数获得一个iterator对象.
   
### 1.6 闭包
#### 1.函数引用
```
def test1():
    print("----in test1 func----")

# 调用函数
test1()

# 引用函数
ret = test1

print(id(ret))
print(id(test1))

# 通过引用调用函数
ret()

```   
运行结果:   
```
----in test1 func----
4404593936
4404593936
----in test1 func----
```    
   
#### 2. 什么是闭包
```
# 定义一个函数
def test(number):
     
    # 在函数内部再定义一个函数,并且这个函数用到了外边函数的变量,那么将这个函数以及用到一些变量称之为闭包
    def test_in(number_in):
        print("in test_in 函数, number_in is %d"%number_in)
        return number+number_in
    # 其实这里返回的就是闭包的结果
    return test_in

#给test函数赋值,这个20就是给参数number
ret = test(20)

#注意这里的100其实给参数number_in
print(ret(100))

#注意这里的200其实给参数number_in
print(ret(200))

```   
运行结果:   
```
in test_in 函数, number_in is 100
120
in test_in 函数, number_in is 200
220

```   

#### 4. 看一个闭包的实际例子:
```
def line_conf(a, b):
    def line(x):
        return a*x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5))
print(line2(5))

```
这个例子中,函数line与变量a,b 构成闭包.在创建闭包的时候,我们通过line_conf的参数a,b说明了这两个变量的取值,
这样,我们就确认了函数的最终形式(y = x + 1和y = 4x + 5).我们只需要变换参数a,b,就可以获得不同的直线表达函数.
由此,我们可以看到,闭包也具有提高代码可复用性的作用.  
如果没有闭包,我们需要每次创建直线函数的时候同时说明a,b,x.这样,我们就需要更多的参数传递,也减少了代码的可移植性.   
   
闭包思考:   
1. 闭包似优化了变量,原来需要类对象完成的工作,闭包也可以完成   
2. 由于闭包引用了外部函数的局部变量,则外部函数的局部变量没有及时释放,消耗内存   
   

### 1.7 装饰器
装饰器是程序开发中经常会用到的一个功能,用好了装饰器,开发效率如虎添翼,所以这也是Python面试中必问的问题,
但对于好多初次接触这个知识的人来讲,这个功能有点绕,自学时直接绕过去了,然后面试问到就挂了,因为装饰器是程序开发的基础知识,
这个都不会,别跟人家说你会Python,看了下面的文章,保证你学会装饰器.   
   
#### 1. 先明白这段代码
```
#### 第一波 ####
def foo():
    print('foo')

foo     # 表示是函数
foo()   # 表示执行foo函数

#### 第二波 ####
def foo():
    print('foo')

foo = lambda x:x + 1

foo()   # 执行下面的lambda表达式,而不再是原来的foo函数,因为foo这个名字被重新指向了另外一个匿名函数

```   
   
#### 2. 需求来了
初创公司有N个业务部门,1个基础平台部门,基础平台负责提供底层的功能.如: 数据库操作,redis调用,监控API等功能.
业务部门使用基础功能时,只需调用基础平台提供的功能即可.如下:   
```
####################### 基础平台提供的功能如下 #########################

def f1():
    print('f1')

def f2():
    print('f2')

def f3():
    print('f3')

def f4():
    print('f4')

####################### 业务部门A 调用基础平台提供的功能 #########################

f1()
f2()
f3()
f4()

####################### 业务部门B 调用基础平台提供的功能 #########################

f1()
f2()
f3()
f4()


```   
目前公司有条不紊的进行着,但是,以前基础平台的开发人员在写代码时候没有关注验证相关的问题,
即:基础平台提供的功能可以被任何人使用.现在需要对基础平台的所有功能进行重构,为平台提供的所有功能添加验证机制,
即:执行功能前,先进行验证.   
   
### 老大把工作交给Low B,他是这么做的:
> 跟每个业务部门交涉,每个业务部门自己写代码,调用基础平台的功能之前先验证.唉,这样一来基础平台就不需要做任何修改一了.
> 太棒了,有充足的时间泡妹子...
      
   当天Low B被开除了...

### 老大把工作交给Low BB,他是这么做的:
```
####################### 基础平台提供的功能如下 #########################

def f1():
    # 验证1
    # 验证2
    # 验证3
    print('f1')

def f2():
    # 验证1
    # 验证2
    # 验证3
    print('f2')

def f3():
    # 验证1
    # 验证2
    # 验证3
    print('f3')

def f4():
    # 验证1
    # 验证2
    # 验证3
    print('f4')

####################### 业务部门A 调用基础平台提供的功能 #########################

f1()
f2()
f3()
f4()

####################### 业务部门B 调用基础平台提供的功能 #########################

f1()
f2()
f3()
f4()

```   
过了一周Low BB被开除了...

### 老大把工作交给Low BBB,他是这么做的:
> 只对基础平台的代码进行重构,其他业务部门无需做任何修改
   
```
def checkLogin():
    # 验证1
    # 验证2
    # 验证3
    pass

def f1():
    checkLogin()
    print('f1')

def f2():
    checkLogin()
    print('f2')

def f3():
    checkLogin()
    print('f3')

def f4():
    checkLogin()
    print('f4')

####################### 业务部门A 调用基础平台提供的功能 #########################

f1()
f2()
f3()
f4()

####################### 业务部门B 调用基础平台提供的功能 #########################

f1()
f2()
f3()
f4()

```   
老大看了一下Low BBB的实现,嘴角露出了一丝的欣慰的笑,语重心长的跟Low BBB聊了个天:   
**老大说:**   
写代码要遵循开放封闭原则,虽然在这个原则是用面向对象开发,但是也适用于函数式编程,简单来说,
它规定已经实现的功能代码不允许被修改,但可以被扩展,即:   
* 封闭:已实现的功能代码块
* 开放:对扩展开发
   
如果将开放封闭的原则应用在上述需求中,那么就不允许在函数f1,f2,f3,f4的内部进行修改代码,老板就给了Low BBB一个实现方案:   
```
def w1(func):
    def inner():
        # 验证1
        # 验证2
        # 验证3
        func()
    return inner

@w1
def f1():
    print('f1')

@w1
def f2():
    print('f2')

@w1
def f3():
    print('f3')

@w1
def f4():
    print('f4')

```   
对于上述代码,也是仅仅对基础平台的代码进行修改,就可以实现在其他人调用函数f1 f2 f3 f4之前都进行[验证]操作,
并且其他业务部门无需做任何操作.   
Low BBB心惊胆战的问了下,这段代码的内部执行原理是什么呢?   
老大正要生气,突然Low BBB的手机掉到地上,恰巧屏保就是Low BBB的女友照片,老大一看一紧一抖,喜笑颜开,决定和Low BBB交个好朋友.
      
详细的开始讲解了:   
单独以f1为例:   
```
def w1(func):
    def inner():
        # 验证1
        # 验证2
        # 验证3
        func()
    return inner

@w1
def f1():
    print('f1')

```   
python 解释器就会从上到下解释代码,步骤如下:   
1. def w1(func): ==> 将w1函数加载到内存
2. @w1  
   
没错,从表面上看解释器仅仅会解释这两句代码,因为函数在没有被调用之前其内部代码不会被执行.   
从表面看解释器会执行这两句,但是@w1 这一句代码里却有大文章,@函数名 是python的一种语法糖.   
   
### 上例@w1内部会执行一下操作:
#### 执行w1函数
> 执行w1函数,并将 @w1 下面的函数作为w1函数的参数,即:@w1等价于w1(f1)所以,内部就会去执行:
> ```
> def inner():
>    # 验证1
>    # 验证2
>    # 验证3
>    f1()       # func是参数,此时 func 等于 f1
> return inner  # 返回的 inner, inner代表的是函数,非执行函数,其实就是将原来的 f1 函数塞进另外一个函数中
> ```   
   
#### w1的返回值
> 将执行完的w1函数返回值 赋值给 @w1 下面的函数的函数名f1 即将w1的返回值再重新赋值给 f1,即:
> ```
> 新f1 = def inner():
>             # 验证1
>             # 验证2
>             # 验证3 
>             原来f1()
>        return inner
> ```
> 所以,以后业务部门想要执行 f1 函数时,就会执行 新f1 函数,在新f1 函数内部先执行验证,再执行原来的f1函数,
> 然后将原来的f1 函数的返回值返回给业务调用者.
   
如此一来,即执行了验证的功能,又执行了原来f1函数的内容,并将原f1函数返回值 返回给业务调用者.   
   

### 3.再议装饰器
```
# 定义函数:完成包裹数据
def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

# 定义函数,完成包裹数据
def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makeBold
def test1():
    return "hello world-1"

@makeItalic
def test2():
    return "hello world-2"

@makeItalic
@makeBold
def test3():
    return "hello world-3"

a1 = test1()
print(a1)

a2 = test2()
print(a2)

a3 = test3()
print(a3)

```   
运行结果:   
```
<b>hello world-1</b>
<i>hello world-2</i>
<i><b>hello world-3</b></i>
```
   
#### 例1:无参数的函数
```
from time import ctime, sleep

def timefun(func):
    def wrappedfunc():
        print("%s called at %s"%(func.__name__, ctime()))
        func()
    return wrappedfunc

@timefun
def foo():
    print("I am foo")

foo()
sleep(2)
foo()

```   
上面代码理解装饰器执行行为可理解成   
```
foo = timefun(foo)
# foo 先作为参数赋值给func后,foo接受指向timefun返回的wrappedfunc
foo()
# 调用foo(),即等价调用wrappedfunc()
# 内部函数wrappedfunc被引用,所以外部函数的func变量(自由变量)并没有被释放
# func里保存的是原foo函数对象

```

#### 例5:装饰器带参数,在原有装饰器的基础上,设置外部变量
```
from time import ctime,sleep

def timefun_arg(pre='hello'):
    def timefun(func):
        def wrappedfunc():
            print('%s called at %s %s'%(func.__name__,ctime(),pre))
            return func()
        return wrappedfunc
    return timefun

@timefun_arg("itcast")
def foo():
    print("I am foo")

@timefun_arg("python")
def too():
    print("I am too")

foo()
sleep(2)
foo()
```

## 2.其他的知识点

## 3.其他的知识点


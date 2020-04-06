## 面向对象进阶

### 1.1 元类


### 1.2 python是动态语言


### 1.3 __slots__


### 1.4 生成器


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

```   

### 1.6 闭包


### 1.7 装饰器


## 2.其他的知识点

## 3.其他的知识点


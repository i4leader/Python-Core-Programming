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

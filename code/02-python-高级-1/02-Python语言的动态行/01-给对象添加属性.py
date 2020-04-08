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
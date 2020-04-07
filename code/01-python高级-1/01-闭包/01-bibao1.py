def test(number):

    print("-----1-----")

    def test_in(number2):   # 函数里面定义的函数不会被执行
        print("-----2-----")
        print(number+number2)

    print("-----3-----")
    return test_in  # 返回的是函数

ret = test(100)
print('-'*30)
ret(1)
ret(100)
ret(200)
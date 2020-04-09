def creatNum():
    print("-----start-----")
    a,b = 0,1
    for i in range(5):
        print("111111111")
        yield b
        print("222222222")
        a,b = b,a+b
        print("333333333")
    print("----stop-----")



a = creatNum()

for num in a:
    print(num)




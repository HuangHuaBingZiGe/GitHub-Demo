# global 关键字

print('-----------------------------------')
count = 5


def MyFun():
    count = 10
    print(count)


MyFun()
print(count)
print('-----------------------------------')


def MyFun():
    global count
    count = 10
    print(count)


MyFun()
print(count)
print('-----------------------------------')


def fun1():
    print('fun1()正在被调用...')
    
    def fun2():
        print('func2()正在被调用...')
    
    fun2()


fun1()
print('-----------------------------------')


def FunX(x):
    def FunY(y):
        return x * y
    
    return FunY


i = FunX(8)
print(i)
print(type(i))
print('-----------------------------------')
print(i(5))
print('-----------------------------------')
print(FunX(8)(5))
print('-----------------------------------')


def Fun1():
    x = [5]
    
    def Fun2():
        x[0] *= x[0]
        return x[0]
    
    return Fun2()


print(Fun1())
print('-----------------------------------')


def Fun1():
    x = 5
    
    def Fun2():
        nonlocal x
        x *= x
        return x
    
    return Fun2()


print(Fun1())
print('-----------------------------------')

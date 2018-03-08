"""
1.类继承：

class A(object):
    def show(self):
        print('base show')
        
class B(A):
    def show(self):
        print('derived show')
        
print('--------------------------------')
obj = B()
obj.show()
print('--------------------------------')
"""

"""
2.方法对象：

class A(object):
    def __init__(self,a,b):
        self.__a = a
        self.__b = b
        
    def myprint(self):
        print('a=',self.__a,'b=',self.__b)
        
    # 为了能让对象实例能被直接调用，需要实现__call__方法
    
    def __call__(self,num):
        print('call:',num+self.__a)

print('--------------------------------')
a1 = A(10,20)
a1.myprint()
print('--------------------------------')
a1(80)
print('--------------------------------')
"""

"""
3.new 和 init：

# 使用__new__方法，可以决定返回那个对象，也就是创建对象之前，这个可以用于设计模式的单例、工厂模式。__init__是创建对象时调用的

class B(object):
    def fn(self):
        print('B fn')
    def __init__(self):
        print("B INIT")
        
class A(object):
    def fn(self):
        print('A fn')
    def __new__(cls, a):
        print("New",a)
        if a > 10:
            return super(A,cls).__new__(cls)
        return B()
    def __init__(self,a):
        print("INIT",a)
    
a1 = A(5)
a1.fn()
a2 = A(20)
a2.fn()
"""

"""
4.Python list 和 dict 生成：

ls = [1,2,3,4]
list1 = [i for i in ls if i > 2]
print(list1)

list2 = [i*2 for i in ls if i > 2]
print(list2)

dic1 = {x : x ** 2 for x in (2,4,6)}
print(dic1)

dict2 = {x : 'item' + str(x ** 2) for x in (2,4,6)}
print(dict2)

set1 = {x for x in 'hello world' if x not in 'low level'}
print(set1)
"""

""""
5.全局变量 和  局部变量：

num = 9
def f1():
    num=20
def f2():
    print(num)

f2()
f1()
f2()

# 全局变量

num = 9
def f1():
    global num
    num = 20
def f2():
    print(num)
f2()
f1()
f2()
"""

"""
6.交换两个变量的值：

一行代码交换两个变量值

a=8
b=9
(a,b)=(b,a)
"""

"""
7.默认方法：

class A(object):
    def __init__(self,a,b):
        self.a1 = a
        self.b1 = b
        print('init')
    def mydefault(self):
        print('default')
    def __getattr__(self, name):
        return self.mydefault
    
print('------------------------------------')
a1 = A(10,20)
a1.fn1()
a1.fn2()
a1.fn3()
print('------------------------------------')

# 方法__getattr__只有当没有定义的方法调用时，才是调用他。当fn1方法传入参数时，我们可以给mydefault方法增加一个*args不定参数来兼容


class A(object):
    def __init__(self,a,b):
        self.a1 = a
        self.a2 = b
        print('init')
    def mydefault(self,*args):
        print('default:' + str(args[0]))
    def __getattr__(self, name):
        print("other fn:",name)
        return self.mydefault

print('------------------------------------')
a1 = A(10,20)
a1.fn1(33)
a1.fn2('hello')
a1.fn3(10)
print('------------------------------------')
"""

"""
8.包管理：

一个包里有三个模块，mod1.py, mod2.py, mod3.py，但使用from demopack import *导入模块时，如何保证只有mod1、mod3被导入了

增加__init__.py文件，并在文件中增加

__all__ = ['mod1','mod3']
"""

"""
9.闭包

写一个函数，接收整数参数n，返回一个函数，函数的功能是把函数的参数和n相乘并把结果返回

def mulby(num):
    def gn(val):
        return num * val
    return gn

zw = mulby(7)
print(zw(9))
"""

"""
10.性能

解析下面的代码慢在哪?????????????????

def strtest1(num):
    str = 'first'
    for i in range(num):
        str += "X"
    return str

python的str是个不可变对象，每次迭代，都会生成新的str对象来存储新的字符串，num越大，创建的str对象越多，内存消耗越大
"""

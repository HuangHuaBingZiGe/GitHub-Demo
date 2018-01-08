#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
50个话题
9章
1.课程简介
2.数据结构相关话题
3.迭代器与生成器相关话题
4.字符串处理相关话题
5.文件I/O操作相关话题
6.数据编码与处理相关话题
7.类与对象相关话题
8.多线程与多进程相关话题
9.装饰器相关话题
"""

"""
第1章 课程简介
    1-1 课程简介
    1-2 在线编码工具WebIDE使用指南

第2章 数据结构与算法进阶训练
    2-1 如何在列表, 字典, 集合中根据条件筛选数据
    2-2 如何为元组中的每个元素命名, 提高程序可读性
    2-3 如何统计序列中元素的出现频度
    2-4 如何根据字典中值的大小, 对字典中的项排序
    2-5 如何快速找到多个字典中的公共键(key)
    2-6 如何让字典保持有序
    2-7 如何实现用户的历史记录功能(最多n条)

第3章 对象迭代与反迭代技巧训练
    3-1 如何实现可迭代对象和迭代器对象(1)
    3-2 如何实现可迭代对象和迭代器对象(2)
    3-3 如何使用生成器函数实现可迭代对象
    3-4 如何进行反向迭代以及如何实现反向迭代
    3-5 如何对迭代器做切片操作
    3-6 如何在一个for语句中迭代多个可迭代对象

第4章 字符串处理技巧训练
    4-1 如何拆分含有多种分隔符的字符串
    4-2 如何判断字符串a是否以字符串b开头或结尾
    4-3 如何调整字符串中文本的格式
    4-4 如何将多个小字符串拼接成一个大的字符串
    4-5 如何对字符串进行左, 右, 居中对齐
    4-6 如何去掉字符串中不需要的字符

第5章 文件I/O高效处理技巧训练
    5-1 如何读写文本文件
    5-2 如何处理二进制文件
    5-3 如何设置文件的缓冲
    5-4 如何将文件映射到内存
    5-5 如何访问文件的状态
    5-6 如何使用临时文件

第6章 csv，json，xml,excel高效解析与构建技巧训练
    6-1 如何读写csv数据
    6-2 如何读写json数据
    6-3 如何解析简单的xml文档
    6-4 如何构建xml文档
    6-5 如何读写excel文件

第7章 类与对象深度技术进阶训练
    7-1 如何派生内置不可变类型并修改实例化行为
    7-2 如何为创建大量实例节省内存
    7-3 如何让对象支持上下文管理
    7-4 如何创建可管理的对象属性
    7-5 如何让类支持比较操作
    7-6 如何使用描述符对实例属性做类型检查
    7-7 如何在环状数据结构中管理内存
    7-8 如何通过实例方法名字的字符串调用方法

第8章 多线程编程核心技术应用进阶训练
    8-1 如何使用多线程
    8-2 如何线程间通信
    8-3 如何在线程间进行事件通知
    8-4 如何使用线程本地数据
    8-5 如何使用线程池
    8-6 如何使用多进程

第9章 装饰器使用技巧进阶训练
    9-1 如何使用函数装饰器
    9-2 如何为被装饰的函数保存元数据
    9-3 如何定义带参数的装饰器
    9-4 如何实现属性可修改的函数装饰器
    9-5 如何在类中定义装饰器

"""

"""
7-1 如何派生内置不可变类型并修改实例化行为

实际案例：
我们想自定义一种新类型的元组，对于传入的可迭代对象，我们只保留作其中int类型且大于0的元素，例如：
IntTuple([1,-1,'abc',6,['x','y'],3])=>(1,6,3)

要求IntTuple是内置tuple的子类，如何实现？

解决方案：
定义类IntTuple继承内置tuple，并实现__new__，修改实例化行为

"""

"""
class IntTuple(tuple):
    
    # new先于init方法创建执行
    def __new__(cls,iterable):
        g = (x for x in iterable if isinstance(x,int) and x > 0)
        print(g)
        return super(IntTuple,cls).__new__(cls,g)
    
    # 创建构造器
    def __init__(self,iterable):
        # before
        print(self)
        #super(IntTuple,self).__init__(iterable)
        # after
        
    
t = IntTuple([1,-1,'abc',6,['x','y'],3])
print(t)
"""

"""
7-2 如何为创建大量实例节省内存

实际案例：
    某网络游戏中，定义了玩家类Player（id，name，status，...）每有一个在线玩家，在服务器程序内则有一个Player的实例，当在线人数很多时，将产生大量实例（如百万级）
    
如何降低这些大量实例的内存开销？

解决方案：
    定义类的__slots__属性，它是用来声明实例属性名字的列表

"""

"""
class Player(object):
    def __init__(self,uid,name,status=0,level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level
    
class Player2(object):
    __slots__ = ['uid','name','status','level']
    def __init__(self,uid,name,status=0,level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level

p1 = Player('0001','Jim')
p2 = Player2('0001','Jim')

print(dir(p1))
print(dir(p2))

print(set(dir(p1)))
print(set(dir(p2)))

print(set(dir(p1)) - set(dir(p2)))

print(p1.__dict__)
p1.x = 123
print(p1.x)
print(p1.__dict__)
p1.__dict__['y'] = 99
print(p1.y)
print(p1.__dict__)

# __dict__ 占用内存
del p1.__dict__['x']
# print(p1.x)

print(sys.getsizeof(p1.__dict__)) # 这个字典占用了320个字节
# 关闭动态属性绑定，提前声明 __slots__ 有哪些空间保存哪些属性，阻止属性绑定
"""

"""
7-3 如何让对象支持上下文管理

with open('demo.txt','w') as f:
    f.write('abcdef')
    f.writelines(['wyz\n','123\n'])
# f.close()

实际案例：
    我们实现了一个telnet客户端的类TelnetClient，调用实例的start()方法启动客户端与服务器交互，交互完毕后需要调用cleanup()方法，关闭已连接的socket,以及将操作历史记录写入文件并关闭
    
    能否让TelnetClient的实例支持上下文管理协议，从而替代手工调用cleanup()方法
    
解决方案：
    实现上下文管理协议，需定义实现的__enter__，__exit__方法，它们分别在with开始和结束时被调用

"""

"""
from telnetlib import Telnet
from sys import stdin,stdout
from collections import deque

class TelnetClient(object):
    def __init__(self,addr,port=23):
        self.addr = addr
        self.port = port
        self.tn = None
    
    def start(self):
        self.tn = Telnet(self.addr,self.port)
        self.history = deque()
        
        # user
        t = self.tn.read_until('login: ')
        stdout.write(t)
        user = stdin.readline()
        self.tn.write(user)
        
        # password
        t = self.tn.read_until('Password: ')
        if t.startswith(user[:-1]):t = t[len(user) + 1:]
        stdout.write(t)
        self.tn.write(stdin.readline())
        
        t = self.tn.read_until('$ ')
        stdout.write(t)
        while True:
            uinput = stdin.readline()
            if not uinput:
                break
            self.history.append(uinput)
            self.tn.write(uinput)
            t = self.tn.read_until('$ ')
            stdout.write(t[len(uinput) + 1:])
            
    def cleanup(self):
        self.tn.close()
        self.tn = None
        with open(self.addr + '_history.txt','w') as f:
            f.writelines(self.history)
            
client = TelnetClient('192.168.179.128')
print('\nstart...')
client.start()
print('\ncleanup')
"""

"""
from telnetlib import Telnet
from sys import stdin, stdout
from collections import deque

class TelnetClient(object):
    def __init__(self, addr, port=23):
        self.addr = addr
        self.port = port
        self.tn = None
    
    def start(self):
        raise Exception('Test')
        # user
        t = self.tn.read_until('login: ')
        stdout.write(t)
        user = stdin.readline()
        self.tn.write(user)
        
        # password
        t = self.tn.read_until('Password: ')
        if t.startswith(user[:-1]): t = t[len(user) + 1:]
        stdout.write(t)
        self.tn.write(stdin.readline())
        
        t = self.tn.read_until('$ ')
        stdout.write(t)
        while True:
            uinput = stdin.readline()
            if not uinput:
                break
            self.history.append(uinput)
            self.tn.write(uinput)
            t = self.tn.read_until('$ ')
            stdout.write(t[len(uinput) + 1:])
    
    def cleanup(self):
        pass
            
    def __enter__(self):
        self.tn = Telnet(self.addr,self.port)
        self.history = deque()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('In __exit__')
        
        self.tn.close()
        self.tn = None
        with open(self.addr + '_history.txt', 'w') as f:
            f.writelines(self.history)
        return True
        
# 对这个对象使用with方法，会进入enter方法,enter需要返回值
with TelnetClient('127.0.0.1') as client:
    client.start()
print('End')
"""

"""
7-4 如何创建可管理的对象属性

实际案例：
    在面向对象编程中，我们把方法（函数）看作对象的接口，直接访问对象的属性可能是不安全的，或设计上不够灵活，但是使用调用方法在形式上不如访问属性简洁
    
circle.getRadius()
circle.setRadius(5.0) #繁

circle.radius
circle.radius = 5.0  #简

能否在形式上是属性访问，但实际上调用方法？

解决方案：
    使用property函数为类创建可管理属性，fget/fset/fdel对应相应属性访问

"""

"""
from math import pi

class Circle(object):
    def __init__(self,radius):
        self.radius = radius
        
    def getRadius(self):
        return round(self.radius,2)
    
    def setRadius(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError('wrong type')
        self.radius = float(value)
        
    def getArea(self):
        return self.radius ** 2 * pi
    
    R = property(getRadius,setRadius)
    
# 调用方法，比较灵活，只需要改方法返回值或者某些参数
c = Circle(3.2)
#c.getRadius()
print(c.R)
c.R = 5.9
print(c.R)

# 类型错误，无法识别
# c.radius = 'abc'
# d = c.radius * 2
# print(d)
"""

"""
7-5 如何让类支持比较操作

实际案例：
    有时我们希望自定义的类，实例间可以使用<,<=,>,>=,==,!=符号进行比较，我们自定义比较的行为，例如，有一个矩形的类，我们希望比较两个矩形的实例时，比较的是他们的面积

解决方案：
    比较符号运算符重载，需要实现一下方法：
    __lt__，__le__，__gt__，__ge__,__eq__,__ne__
    使用标准库下的functools下的类装饰器total_ordering可以简化此过程
    
    
"""

"""
from functools import total_ordering
from abc import ABCMeta,abstractmethod

@total_ordering
class  Shape(object):
    @abstractmethod
    def area(self):
        pass
    
    def __lt__(self, obj):
        print('in __lt__')
        if not isinstance(obj, Shape):
            raise TypeError('obj is not Shape')
        return self.area() < obj.area()
    
    def __eq__(self, obj):
        print('in __eq__')
        if not isinstance(obj, Shape):
            raise TypeError('obj is not Shape')
        return self.area() == obj.area()

class Rectangle(Shape):
    def __init__(self,w,h):
        self.w = w
        self.h = h
    
    def area(self):
        return self.w * self.h
    
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return self.r ** 2 * 3.14

'''
    def __le__(self, obj):
        return self < obj or self == obj
    
    def __gt__(self, obj):
        return not (self < obj or self == obj)
'''

r1 = Rectangle(5,3)
r2 = Rectangle(4,4)
c1 = Circle(3)

print(c1 <= r1 ) # r1.__lt__(r2)
print(r1 > c1 ) # r1.__lt__(r2)
print(r1 > 1)
"""

"""
7-6 如何使用描述符对实例属性做类型检查

实际案例：
    在某项目中，我们实现了一些类，并希望能像静态类型语言那样（C、C++、Java），对它们的实例属性做类型检查
p = Person()
p.name = 'Bob'    # 必须是str
p.age = 18        # 必须是int
p.height = 1.83   # 必须是float

要求：
    1.可以对实例变量名指定类型
    2.赋予不正确类型时抛出异常
    
解决方案：
    使用描述符来实现需要类型检查的属性，分别实现__get__、__set__、__delete__方法，在__set__内使用isinstance函数做类型检查

"""
'''
class Attr(object):
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_
    
    def __get__(self, instance, cls):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise TypeError('expected an %s' % self.type_)
        instance.__dict__[self.name] = value
    
    def __delete__(self, instance):
        del instance.__dict__[self.name]

class Person(object):
    name = Attr('name', str)
    age = Attr('age', int)
    height = Attr('height', float)
    
p = Person()
p.name = 'Bob'
print(p.name)
p.age = '17'
'''

"""
7-7 如何在环状数据结构中管理内存

实际案例：
    在python中，垃圾回收器通过引用计数来回收垃圾对象，但某些环状数据结构（树、图...），存在对象间的循环引用，比如树的父节点引用子节点，子节点也同时引用父节点，此时同时del掉引用父子节点，两个对象不能被立即回收
    
如何解决此类的内存管理问题？

解决方案：
    使用标准库weakref，它可以创建一种能访问对象但不增加引用计数的对象

"""

'''
class A(object):
    def __del__(self):
        print('in A.__del__')

a = A()
import sys
a2 = a
# 查看引用计数
print(sys.getrefcount(a) - 1)
del a2
print(sys.getrefcount(a) - 1)
a = 5 # 当计数变为0，调用__del__方法
'''

"""
class Data(object):
    def __init__(self, value, owner):
        self.owner = owner
        self.value = value
    def __str__(self):
        return "%s's data, value is %s" %(self.owner,self.value)
    def __del__(self):
        print('in Data.__del__')
        
class Node(object):
    def __int__(self,value):
        self.data = Data(value, self)
    def __del__(self):
        print('in node.__del__')
        
node = Node()
import gc
gc.collect()
input('wait....')
"""

'''
class A(object):
    def __del__(self):
        print('in A.__del__')
        
a = A()
import sys
print(sys.getrefcount(a) - 1)
import weakref
a_wref = weakref.ref(a)
a2 = a_wref()
print(a is a2)
print(sys.getrefcount(a) - 1)
del a
del a2
print(a_wref())
print(a_wref() is None)
'''

'''
import weakref
class Data(object):
    def __init__(self, value, owner):
        self.owner = weakref.ref(owner)
        self.value = value
    def __str__(self):
        return "%s's data, value is %s" % (self.owner(), self.value)
    def __del__(self):
        print('in Data.__del__')


class Node(object):
    def __int__(self, value):
        self.data = Data(value, self)
    def __del__(self):
        print('in node.__del__')

node = Node()
del node
input('wait...')
'''

'''
7-8 如何通过实例方法名字的字符串调用方法

实际案例：
    某项目中，我们的代码使用了3个不同库中的图形类：Circle、Triangle、Rectangle，他们都有一个获取图形面积的接口（方法），但接口名字不同，我们可以实现一个统一的获取面积的函数，使用每种方法名进行尝试，调用相应类的接口

解决方案：
    方法1：使用内置函数getattr，通过名字在实例上获取方法对象，然后调用
    方法2：使用标准库operator下的methodcaller函数调用

'''

'''
class Circle(object):
    def __init__(self,r):
        self.r = r
    def area(self):
        return self.r ** 2 * 3.14
    
class Rectangle(object):
    def __init__(self,w,h):
        self.w = w
        self.h = h
    def get_area(self):
        return self.w * self.h
    
class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
    def getArea(self):
        a, b, c = self.a,self.b,self.c
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c))  ** 0.5
        return area

def getArea(shape):
    for name in ('area','getArea','get_area'):
        f = getattr(shape, name, None)
        if f:
            return f()
        
shape1 = Circle(2)
shape2 = Triangle(3, 4, 5)
shape3 = Rectangle(6, 4)

shapes = [shape1,shape2,shape3]
print(map(getArea,shapes))
'''

"""
from operator import methodcaller
s = 'abc123abc456'
print(s.find('abc',4))
print(methodcaller('find','abc',4))
print(methodcaller('find','abc',4)(s))
"""

"""
OOP：面向对象编程
OOA：面向对象分析
OOD：面向对象设计

self 是什么？？？？？？？？？？？？？？？？？？？？？？？
Python 的 self 相当于 C++ 的 this 指针

"""


class Ball:
    def setName(self, name):
        self.name = name
    
    def kick(self):
        print('我叫%s,谁踢我...' % self.name)


print('--------------------------------------')
a = Ball()
a.setName('球A')
b = Ball()
b.setName('球B')
c = Ball()
c.setName('土豆')
a.kick()
c.kick()
print('--------------------------------------')

"""
如果你的对象实现了这些方法中的某一个，那么这个方法就会在特殊的情况下被Python所调用，而这一切都是自动发生的。
"""

"""
魔法方法： __init__(self)？？？？？？？？？？？？？？？？？
"""


class Ball:
    def __init__(self, name):
        self.name = name
    
    def kick(self):
        print('我叫%s,该死的,谁踢我...' % self.name)


b = Ball('土豆')
b.kick()
print('--------------------------------------')

"""
共有和私有？？？？？？？？？？？？？？？？？？？？？？？？？

在Python中定义私有变量只需要在变量名或函数名前加上"__"两个下划线，那么这个函数或变量就会为私有的了。
"""

"""
class Person:
    name = "小甲鱼"
p = Person()
print(p.name)
print('--------------------------------------')
"""


class Person:
    __name = '小甲鱼'  # 双下划线为 私有变量
    
    def getName(self):
        return self.__name


p = Person()
# print(p.__name)
# p.getName()
# print(p._Person__name)  # 这样可以访问私有变量


"""
继承？？？？？？？？？？？？？？？？？？？？？？？？？？

class DerivedClassName(BaseClassName): # 子类 继承  基类、父类或超类
    ...
"""


class Parent:
    def hello(self):
        print("正在调用父类的方法...")


class Child(Parent):
    pass


p = Parent()
p.hello()
print('--------------------------------------')

c = Child()
c.hello()
# 如果子类中定义与父类同名的方法或属性，则会自动覆盖父类对应的方法或属性
print('--------------------------------------')

import random as r


class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
    
    def move(self):
        self.x -= 1
        print("我的位置是：", self.x, self.y)


class Gold(Fish):
    pass


class Carp(Fish):
    pass


class Salmon(Fish):
    pass


class Shark(Fish):
    def __init__(self):
        self.hungry = True
    
    def eat(self):
        if self.hungry:
            print("吃货的梦想就是天天有的吃^_^")
            self.hungry = False
        else:
            print("太撑了，吃不下了！")


fish = Fish()
fish.move()
print('--------------------------------------')
goldfish = Gold()
goldfish.move()
print('--------------------------------------')
shark = Shark()
shark.eat()
print('--------------------------------------')
# shark.move() # 因为重写了父类的init方法，所以没有了x变量


"""
--调用未绑定的父类方法
--使用super函数
"""

"""
组合
"""


class Turtle:
    def __init__(self, x):
        self.num = x


class Fish:
    def __init__(self, x):
        self.num = x


class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
    
    def print_num(self):
        print('水池里总共有乌龟 %d 只，小鱼 %d 条！' % (self.turtle.num, self.fish.num))


print('-------------------------------------------------')
pool = Pool(1, 10)
pool.print_num()
print('-------------------------------------------------')

"""
类、类对象、实例对象
"""


class C:
    count = 0


a = C()
b = C()
c = C()
print(a.count)
print(b.count)
print(c.count)
c.count += 10
print(c.count)
print(a.count)
C.count += 100
print(a.count)
print(b.count)
print('-------------------------------------------------')


class C:
    def x(self):
        print("X-man!")


c = C()
c.x()
c.x = 1
print(c.x)
# c.x()  # 属性名和方法名冲突，会覆盖
# 不要试图在一个类里边定义出所有能想到的特性和方法，应该利用继承和组合机制来进行扩展
# 用不同的词性命名，如属性名用名词，方法名用动词
print('-------------------------------------------------')

"""
什么是绑定？？？？？？？？？？？？？？？？？？？？？？？？

Python严格要求方法需要有实例才能被调用，这种限制其实就是Python所谓的绑定概念
"""

"""
class BB:
    def printBB():
        print("no zuo no die")
               
BB.printBB()
bb = BB()
bb.printBB()  # 报错，因为在类里面的方法没有传self参数
"""


class CC:
    def setXY(self, x, y):
        self.x = x
        self.y = y
    
    def printXY(self):
        print(self.x, self.y)


dd = CC()
print(dd.__dict__)  # 查看实例对象的属性
print('-------------------------------------------------')

print(CC.__dict__)  # 查看类对象的属性
print('-------------------------------------------------')

dd.setXY(4, 5)
print(dd.__dict__)
print('-------------------------------------------------')

del CC
dd.printXY()
print('-------------------------------------------------')

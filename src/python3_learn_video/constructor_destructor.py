"""
构造  和  析构：

魔法方法总是被双下划线包围，例如 __init__(self[, ...])

魔法方法是面向对象的Python的一切，如果你不知道魔法方法，说明你还没能意识到面向对象的Python的强大

魔法方法的“魔力”体现在它们总能够在适当的时候被自动调用


有时候在类定义时有写__init__方法，有时候却没有，这是为什么？？？？？？？？？
"""


class Rectangel:
    def __init__(self, x, y):  # init 方法不能返回任何值
        self.x = x
        self.y = y
    
    def getPeri(self):
        return (self.x + self.y) * 2
    
    def getArea(self):
        return self.x * self.y


print('------------------------------------------------')
rect = Rectangel(3, 4)
print(rect.getArea())
print(rect.getPeri())
print('------------------------------------------------')

"""
第一个被调用的魔法方法： __new__(cls[, ...])
很少的时候去重写 new 方法
当继承一个不可变类型的时候，需要重写 new 方法
"""


class CapStr(str):  # str 不可修改
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)


a = CapStr('I love FishC.com!')
print(a)
print('------------------------------------------------')

"""
析构器：__del__(self)
"""


class C:
    def __init__(self):
        print("我是__init__方法，我被调用了...")
    
    def __del__(self):
        print("我是__del__方法，我被调用了...")


c1 = C()
print('------------------------------------------------')
c2 = c1
print('------------------------------------------------')
del c1
del c2
print('------------------------------------------------')

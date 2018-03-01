"""
与类和对象相关的一些BIF：

1.一个类被认为是其自身的子类

issubclass(class,classinfo)


2.classinfo可以是类对象组成的元组，只要class与其中任何一个候选类的子类，则返回True

issubclass(class,classinfo)

"""


class A:
    pass


class B(A):
    pass


print('--------------------------------------------')
print(issubclass(B, A))
print('--------------------------------------------')

print(issubclass(B, B))
print('--------------------------------------------')

print(issubclass(B, object))
print('--------------------------------------------')


class C:
    pass


print(issubclass(B, C))
print('--------------------------------------------')

""""
isinstance(object,classinfo)

1.如果第一个参数不是对象，则永远返回False

2.如果第二个参数不是类或者由类对象组成的元组，会抛出一个TypeError异常

"""

b1 = B()
print(isinstance(b1, B))
print(isinstance(b1, A))
print(isinstance(b1, C))
print(isinstance(b1, (A, B, C)))
print('--------------------------------------------')

"""
hasattr(object,name)

attr = attribute 属性
"""


class C:
    def __init__(self, x=0):
        self.x = x


c1 = C()
print(hasattr(c1, 'x'))
print('--------------------------------------------')

"""
getattr(object,name[,default])
"""
print(getattr(c1, 'x'))
print(getattr(c1, 'y', '您所访问的属性不存在....'))
print('--------------------------------------------')

"""
setattr(object,name,value)

设置指定属性
"""

setattr(c1, 'y', 'FishC')
print(getattr(c1, 'y', '您访问的属性不存在....'))
print('--------------------------------------------')

"""
delattr(object,name)

删除指定属性

delattr(c1,'y')
delattr(c1,'y')

"""

"""
property(fget=None,fset=None,fdel=None,doc=None)

通过属性设置属性，3个参数
"""


class C:
    def __init__(self, size=10):
        self.size = size
    
    def getSize(self):
        return self.size
    
    def setSize(self, value):
        self.size = value
    
    def delSize(self):
        del self.size
    
    x = property(getSize, setSize, delSize)


c1 = C()
print(c1.getSize())
print(c1.x)
c1.x = 18
print(c1.x)
print(c1.getSize())
print('--------------------------------------------')

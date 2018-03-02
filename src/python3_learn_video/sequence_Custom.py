"""
协议是什么？

协议（Protocols） 与其他编程语言中的接口很相似，它规定你哪些方法必须要定义。然而，在Python中的协议就显得不那么正式。事实上，在Python中，协议更像是一种指南。


容器类型的协议：

如果说你希望定制的容器是不可变的话，你只需要定义__len__()和__getitem__()方法

如果你希望定制的容器是可变的话，除了__len__()和__getitem__()方法，你还需要定义__setitem__()和__delitem__()两个方法

"""

"""
练习要求：

编写一个不可改变的自定义列表，要求记录列表中每个元素被访问的次数

"""


class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)
    
    def __len__(self):
        return len(self.values)
    
    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]


print('-------------------------------------------')
c1 = CountList(1, 3, 5, 7, 9)
c2 = CountList(2, 4, 6, 8, 10)
c1[1]
c2[1]
print(c1[1] + c2[1])
print(c1.count)
c1[1]
print('-------------------------------------------')

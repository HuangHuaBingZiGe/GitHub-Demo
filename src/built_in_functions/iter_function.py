#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

print("-----用法1：iter(object)-----")
print("-----实现了__iter__()方法或者__getitem__()方法-----")

obj = [1, 2, 3]
for i in iter(obj):
    print(i)
print("返回一个迭代器")
print(iter(obj))

print("-----用法2：iter(object, sentinel)-----")
print("如果传递了第二个参数，则object必须是一个可调用的对象（如，函数）")
print("此时，iter创建了一个迭代器对象，每次调用这个迭代器对象的__next__()方法时，都会调用object")
print("如果__next__的返回值等于sentinel，则抛出StopIteration异常，否则返回下一个值")


class counter:
    def __init__(self, _start, _end):
        self.start = _start
        self.end = _end
    
    def get_next(self):
        s = self.start
        if (self.start < self.end):
            self.start += 1
        else:
            raise StopIteration
        return s


c = counter(1, 5)
print("iter的第一个参数必须是一个调用对象，不能是带返回值的函数，应该是一个函数对象")
print("iter原理：相当于一个for循环，自带跳出功能，当iter的第一个可调用对象的返回值等于第二个给出的值时，跳出此函数，抛出StopIteration异常")
iterator = iter(c.get_next, 3)
print(type(iterator))
for i in iterator:
    print(i)

'''
https://docs.python.org/3/library/functions.html#iter
英文版原话：
Return an iterator object. The first argument is interpreted very differently depending on the presence of the second argument. Without a second argument, object must be a collection object which supports the iteration protocol (the __iter__() method), or it must support the sequence protocol (the __getitem__() method with integer arguments starting at 0). If it does not support either of those protocols, TypeError is raised. If the second argument, sentinel, is given, then object must be a callable object. The iterator created in this case will call object with no arguments for each call to its __next__() method; if the value returned is equal to sentinel, StopIteration will be raised, otherwise the value will be returned.
'''

print("-----iter一个有用的功能用法-----")
file = 'test.txt'
file_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + \
            '\\' + 'docs' + '\\' + 'txt' + '\\' + file
print("使用with open不用关心close")
with open(file_name) as fp:
    for line in iter(fp.readline, ''):
        print(line)

#!/usr/bin/python
# -*- coding: utf-8 -*-

print("------------------------------------------------")
# callable 方法，如果传入的参数是可以调用的函数，则返回 true ，否则返回 false
st = 'wyz'
print('字符串的doc属性是否可调用：')
print(callable(getattr(st, '__doc__')))
# False

print("------------------------------------------------")
print("字符串的split方法是否可调用：")
print(callable(getattr(st, 'split')))
# True

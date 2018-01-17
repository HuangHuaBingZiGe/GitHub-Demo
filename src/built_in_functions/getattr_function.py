#!/usr/bin/python
# -*- coding: utf-8 -*-

print("------------------------------------------------")
st = 'bingzi'
# getattr 方法，传入参数是对象和该对象的函数或者属性的名字，返回对象的函数或者属性实例
print("字符串的doc属性：")
print(getattr(st, '__doc__'))

print("------------------------------------------------")
print("字符串的encode方法：")
print(getattr(st, 'encode'))
# print(getattr(st,'__name__'))

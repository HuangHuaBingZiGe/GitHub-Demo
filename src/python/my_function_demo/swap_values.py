#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
1.将右边的a, b 生成一个tuple（元组），放到内存中
2.之后执行赋值操作，这时候会将tuple拆开
3.然后将tuple的第一个元素赋值给左边的第一个变量，第二个元素赋值给左边的第二个元素

a = 1
b = 2

b, a = a, b

"""

people = ['David', 'Pythonista', '1514551234']
name, title, phone = people
print
name
print
title
print
phone
print
"-----------------------------------------------------"

'''
使用这种语法时，需要确保左边的变量个数和右边tuple的个数一样
'''

people = [['David', 'Pythonista', '1514551234'], ['Wu', 'Student', '150231231']]
for name, title, phone in people:
    print
    name, phone
print
"-----------------------------------------------------"

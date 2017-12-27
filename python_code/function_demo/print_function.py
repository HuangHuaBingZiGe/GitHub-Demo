#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
---------------------------------------------------------------------------------------------

#   python2 不能使用help(print)，会报错
#   python3 可以使用help(print)

---------------------------------------------------------------------------------------------

#   python2 的print 的用法：print "abc"      print("abc")
#   python3 的print 的用法：print("abc")

---------------------------------------------------------------------------------------------

#   为什么python只有一个元素的元组要加逗号？
#   不加逗号，是str类型，加了，是tuple类型

---------------------------------------------------------------------------------------------

a = ('abc')
b = ('abc',)

---------------------------------------------------------------------------------------------

type(a)
#   str
type(b)
#   tuple

---------------------------------------------------------------------------------------------

a = 'my'

a
#带引号

---------------------------------------------------------------------------------------------

print a
#不带引号

#print格式化输出（字符串、整数）
#python的print语句和字符串操作符%一起结合使用，可以实现替换的可能
#这里的%s和%d是占位符，分别是为字符串类型和整型来服

---------------------------------------------------------------------------------------------

print "%s is %d old" % ("she",20)

#不换行
a = 1
b = 2
c = 3
print a, b, c

---------------------------------------------------------------------------------------------

"""

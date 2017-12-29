#!/usr/bin/python
# -*- coding: utf-8 -*-

print("\n")
print("-----迭代-----")
mylist = [1, 2, 3]
for i in mylist:
    print(i)
print("\n")

print("-----迭代器，用中括号的叫迭代器-----")
print("任何可以用 for in 来迭代读取的都是迭代容器，例如lists,strings,files.这些迭代器非常的便利")
print("你可以想取多少便取多少，但是你得存储所有的值，其中很多值都完全没有必要每次都保持在内存中")
mylist = [x * x for x in range(3)]
for i in mylist:
    print(i)
print("\n")

print("-----生成器，用圆括号的叫生成器-----")
print("Generators(生成器)也是可迭代的，但是你每次只能迭代它们一次，因为不是所有的迭代器都被一直存储在内存中的，他们临时产生这些值")
print("生成器几乎和迭代器是相同的，除了符号[]变为()。但是你无法用两次，因为他们只生成一次：他们生成0然后丢弃，继续统计1，接着是4，一个接着一个")
print("使用生成器表达式取代列表推导式可以同时节省 cpu 和 内存(RAM)")
mygenerator = (x * x for x in range(3))
for i in mygenerator:
    print(i)
print("\n")

print("-----Python的迭代器和生成器-----")
print(
    "对于string、list、dict、tuple等这类容器对象，使用for循环遍历是很方便的。在后台for语句对容器对象调用iter()函数，iter()是python的内置函数。iter()会返回一个定义了next()方法的迭代器对象，它在容器中逐个访问容器内元素，next()也是python的内置函数。在没有后续元素时，next()会抛出一个StopIteration异常，通知for语句循环结束")
s = 'abc'
it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))
print("\n")

print("")

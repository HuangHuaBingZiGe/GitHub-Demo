#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from functools import partial

print("-----遍历一个范围内的数字,直接遍历数组-----")
for i in [0, 1, 2, 3, 4, 5]:
    print(i ** 2)

print("-----遍历一个范围内的数字，使用range方法-----")
for i in range(6):
    print(i ** 2)

print("-----更好的方法，使用xrange，xrange在Python 3中已经改名为range-----")
print("xrange会返回一个迭代器，用来一次一个值地遍历一个范围，这种方式会比range更省内存")
'''
for i in xrange(6):
    print(i ** 2)
'''

print("-----遍历一个集合-----")
colors = ['red', 'green', 'blue', 'yellow']
for i in range(len(colors)):
    print(colors[i])

print("-----遍历一个集合，更好的方法-----")
for color in colors:
    print(color)

print("-----反向遍历-----")
for i in range(len(colors) - 1, -1, -1):
    print(colors[i])

print("-----反向遍历，更好的方法-----")
for color in reversed(colors):
    print(color)

print("-----遍历一个集合及其下标-----")
for i in range(len(colors)):
    print(i, '--->', colors[i])

print("-----遍历一个集合及其下标，更好的方法-----")
for i, color in enumerate(colors):
    print(i, '--->', color)

print("-----遍历2个集合-----")
names = ['raymond', 'rachel', 'matthew']
n = min(len(names), len(colors))
for i in range(n):
    print(names[i], '--->', colors[i])
for name, color in zip(names, colors):
    print(name, '--->', color)

print("-----遍历2个集合，更好的方法-----")
print("在python2中，zip在内存中生成一个新的列表，需要更多的内存。izip比zip效率更高")
print("在Python 3中，izip改名为zip，并替换了原来的zip成为内置函数")
for name, color in zip(names, colors):
    print(name, '--->', color)

print("-----有序地遍历，正序-----")
for color in sorted(colors):
    print(color)

print("-----有序地遍历，倒序-----")
for color in sorted(colors, reverse=True):
    print(color)

print("-----自定义排序顺序-----")


def compare_length(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0


'''
print(sorted(colors,cmp=compare_length))
'''
print("-----自定义排序顺序，更好的方法-----")
print("注释掉的上面的那个方法效率低，而且写起来很不爽")
print("Python3已经不支持比较函数了")
print(sorted(colors, key=len))

print("-----调用一个函数直到遇到标记值-----")
print(">>>>>当前文件的绝对路径为：>>>>>")
print(os.path.abspath(__file__))
print(">>>>>当前文件的文件夹绝对路径为：>>>>>")
print(os.path.dirname(os.path.abspath(__file__)))
print(">>>>>当前文件所在的文件夹的上一级文件夹所在的路径为：>>>>>")
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
blocks = []
file = 'test.txt'
file_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + \
            '\\' + 'docs' + '\\' + 'txt' + '\\' + file
while True:
    f = open(file_name, "r+")
    print(">>>>>文件名为：>>>>>" + f.name)
    block = f.read(9)
    f.close()
    print(">>>>>读取到的9个字节为：>>>>>" + block)
    print(">>>>>当读取到的变量中存的是123456789时跳出>>>>>")
    if block == '123456789':
        break
    blocks.append(block)

print("-----调用一个函数直到遇到标记值，更好的方法-----")
print("iter接受2个参数，第1个是反复调用的函数，第2个是标记值")
print("这个方法的优势在于iter的返回值是个迭代器，迭代器可以用在各种地方，set、sorted、min、max、heapq、sum.....")
blocks = []
f = open(file_name, "r+")
for block in iter(partial(f.read, 9), ''):
    blocks.append(block)
print(blocks)
f.close()

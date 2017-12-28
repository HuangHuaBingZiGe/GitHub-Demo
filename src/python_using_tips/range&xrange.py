#!/usr/bin/python
# -*- coding: utf-8 -*-

# xrange会返回一个迭代器，用来一次一个值地遍历一个范围
# 这种方式会比range更省内存
# xrange在Python 3中已经改名为range


print("-----遍历一个范围内的数字,直接遍历数组-----")
for i in [0, 1, 2, 3, 4, 5]:
    print(i ** 2)

print("-----遍历一个范围内的数字，使用range方法-----")
for i in range(6):
    print(i ** 2)

print("-----更好的方法，使用xrange-----")
'''
for i in xrange(6):
    print(i ** 2)
'''

#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
python2 中，u是unicode的编码，r是原始字符，例如：

u'你好'
#这里是把‘你好’用Unicode编码

r'\nabdcd\rds'
#这里加上r表示 把\nabdcd\rds看做原始字符，忽略一切转义字符

s1 = '百度知道'
s2 = u'百度知道'

type(s1)
type(s2)

print '520\n13213'
print u'520\n13213'
print r'520\n12321'
print R'520\n12321'

"""

"""
Python 2里的Unicode字符串在Python 3里就是普通字符串而已，因为在Python 3里字符串总是Unicode形式的，加不加u都一样

print('520\n13213')
print(u'520\n13213')
print(r'520\n12321')
print(R'520\n12321')

"""

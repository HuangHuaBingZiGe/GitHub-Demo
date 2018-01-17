#!/usr/bin/python
# -*- coding: utf-8 -*-

import string

# python3 无stof和stoi方法

# 将字符串转换成浮点型
# print(string.atof('1.11'))

# 将字符串转换为整型
# print(string.atoi('111'))

print("------------------------------------------------")
st = 'wyz'
print("字符串包括的属性和方法有：")
print(dir(st))
# 字符串的方法和属性
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

print("------------------------------------------------")
print("字符串模块包含的方法和属性有：")
print(dir(string))
# string模块的方法和属性
# ['ChainMap', 'Formatter', 'Template', '_TemplateMetaclass', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_re', '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']

print("------------------------------------------------")
print("列出字符串的所有可调用函数或属性：")
print([method for method in dir(st) if callable(getattr(st, method))])

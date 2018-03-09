"""
Python 标准库中包含一般任务所需要的模块:

PEP 是 Python Enhancement Proposals 的缩写
翻译过来就是Python增强建议书的意思

它是用来规范与定义Python的各种加强与延伸功能的技术规格，好让Python开发社区能有共同遵循的依据

每个PEP都有一个唯一的编号,这个编号一旦给定了就不会再改变

例如，PEP 3000 就是用来定义 Python 3.0 的相关技术规格
而PEP 333 则是Python的Web应用程序界面WSGI（Web Server Gateway Interface 1.0）的规范

关于PEP本身的相关规范是定义在PEP 1，而PEP 8 则定义了 Python 代码的风格指南

有关PEP的列表大家可以参考 PEP 0：
<https://www.python.org/dev/peps/>

"""

print('------------------------------------------------')
import timeit

print(timeit.__doc__)
print('------------------------------------------------')
print(dir(timeit))
print('------------------------------------------------')
print(timeit.__all__)  # 对外提供的接口、类、方法
print('------------------------------------------------')

from timeit import *

print(Timer)
print('------------------------------------------------')

import timeit

print(timeit.__file__)  # 查看源代码所在路径
print('------------------------------------------------')

print(help(timeit))  # 比doc详细，比官方文档简单
print('------------------------------------------------')

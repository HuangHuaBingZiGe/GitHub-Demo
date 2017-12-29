#!/usr/bin/python
# -*- coding: utf-8 -*-


from functools import partial


def add(a, b):
    print("a=")
    print(a)
    print("b=")
    print(b)
    return a + b


print("partial的第一个参数必须是一个可调用对象，可以是clase或者function")
print("提前绑定第一个参数，当动态调用函数传递的参数赋值给第2个位置")

plus3 = partial(add, 3)
print(plus3(4))

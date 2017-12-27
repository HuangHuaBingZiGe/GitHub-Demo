# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
装饰器是一个很著名的设计模式，经常被用于有切面需求的场景，较为经典的有插入日志、性能测试、事务处理等。
装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用。
概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能

Python装饰器（decorator）在实现的时候，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变），为了不影响，Python的functools包中提供了一个叫wraps的decorator来消除这样的副作用。写一个decorator的时候，最好在实现之前加上functools的wrap，它能保留原有函数的名称和docstring

执行顺序：装饰器调用从下到上，依次执行	@decorator_a、@decorator_b
相当于依次执行f = decorator_a(f)、f = decorator_b(f)
运行时是自上到下，先运行f(1)=decorator_b(f(1))、再运行f(1)=decorator_b(f(1))
"""


def decorator_a(func):
    print
    'Get in decorator_a'
    
    def inner_a(*args, **kwargs):
        print
        'Get in inner_a'
        return func(*args, **kwargs)
    
    return inner_a


def decorator_b(func):
    print
    'Get in decorator_b'
    
    def inner_b(*args, **kwargs):
        print
        'Get in inner_b'
        return func(*args, **kwargs)
    
    return inner_b


@decorator_b
@decorator_a
def f(x):
    print
    'Get in f'
    return x * 2


f(1)

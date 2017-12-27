#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
---------------------------------------------------------------------------------------------
1.python装饰器的出现

#   在没有装饰器之前，如果要在类中定义一个静态方法，需要使用以下2种方法：

class MyClass(object):
    def staticFoo():
        staticFoo = staticmethod(staticFoo)

#   等价于

class MyClass(object):
    @staticmethod
    def staticFoo():
        pass

---------------------------------------------------------------------------------------------

2.python装饰器类型与理解

(1) 无参数装饰器

    一个装饰器：
@g
def foo():
    pass

#   等价于

def foo():
    pass
foo = g(foo)

---------------------------------------------------------------------------------------------

    多个装饰器：
@g
@f
def foo():
    pass

#等价于

def foo():
    pass
foo = g(f(foo))

---------------------------------------------------------------------------------------------

(2) 含参数装饰器

    带有参数的一个装饰器：

    （decomaker()用deco_args做了些事并返回函数对象，而该函数对象正是以foo作为其参数的装饰器）

@decomaker(deco_args):
def foo():
    pass

#等价于

def foo():
    pass
foo = decomaker(deco_args)(foo)

---------------------------------------------------------------------------------------------

    带有参数的多个装饰器：

@deco1(deco_arg)
@deco2()
def foo():
    pass

#等价于

def foo():
    pass
foo = deco1(deco_arg)(deco2(foo))

---------------------------------------------------------------------------------------------

3.python装饰器执行过程的手动分解

from functools import wraps

def log(text):
    def decorator(func):
        @wraps(func)        # it works like : wraper.__name__ = func.__name__
        def wrapper(*args, **kwargs):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log('Hello')
def now(area):
    print area, '2016-01-23'

now('Beijing')
print 'The name of function now() is :', now.__name__

#   关于wraps，它是一个装饰器，作用：被用户自定义装饰器修改后的函数，它的函数名称，func.__name__跟原来一样，wraper.__name__ = func.__name__，使用wraps不可以改变原来函数的属性

"""

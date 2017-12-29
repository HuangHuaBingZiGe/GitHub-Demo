#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
functools.partial
functools.update_wrapper
functools.wraps
functools.total_ordering

"""
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

import logging
from functools import wraps


def logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        log = logging.getLogger(fn.__name__)
        log.debug('Start to run %s' % fn.__name__)
        out = fn(*args, **kwargs)
        log.debug('Finish running %s' % fn.__name__)
        return out
    
    return wrapper


@logger
def loadInitialJson(self, file=''):
    """loads the config json file. Path is where the config files are
    located"""
    print('Load json file completed!')


loadInitialJson('abc')

print
"----------------------------------------------------------------"

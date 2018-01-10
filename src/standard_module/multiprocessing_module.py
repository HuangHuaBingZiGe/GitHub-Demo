#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
multiprocessing.dummy
multiprocessing.dummy.Pool

"""

"""
from threading import Event,Thread

def f(e):
    print('f 0')
    e.wait()
    print('f 1')
    
e = Event()
t = Thread(target=f,args=(e,))
t.start()

e.set()
e.clear()
"""

"""
import threading
l = threading.local()
l.x = 1
def f():
    print(l.x)
f()
#threading.Thread(target=f).start()
def f():
    l.x = 5
threading.Thread(target=f).start()
"""

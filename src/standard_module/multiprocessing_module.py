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

"""
from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor(3)

def f(a,b):
    print('f',a,b)
    return a ** b

executor.submit(f,2,3)
future = executor.submit(f,2,4)
print(future.result())
# 同时调用多个线程
executor.map(f,[2,3,5],[4,5,6])

import time

def f(a,b):
    print('f',a,b)
    time.sleep(10)
    return a ** b

print(executor.map(f,[2,3,5,6,7],[4,5,6,7,8]))
"""

'''
from multiprocessing import Process
def f(s):
    print(s)
p = Process(target=f,args=('hello',))
p.start()
'''

'''
from multiprocessing import Process
x = 1
def f():
    global x
    x = 5
f()
print(x)
x = 1
p = Process(target=f)
p.start()
print(x)
'''

"""
from multiprocessing import Queue,Pipe,Process
q = Queue()
q.put(1)
print(q.get())
def f(q):
    print('start')
    print(q.get())
    print('end')
Process(target=f,args=(q,)).start()
print(q.put(100))
"""

"""
from multiprocessing import Queue,Pipe,Process
c1,c2 = Pipe()
c1.send('abc')
print(c2.recv())
c2.send('xyz')
print(c1.recv())

def f(c):
    c.send(c.recv() * 2)

c1,c2 = Pipe()
Process(target=f,args=(c2,)).start()
c1.send(55)
print(c1.recv())
"""

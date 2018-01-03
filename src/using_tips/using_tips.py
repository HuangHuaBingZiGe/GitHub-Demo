#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import doctest
import os
import sys
import threading
import urllib
from collections import ChainMap
from collections import deque
from contextlib import redirect_stdout
from decimal import getcontext, Decimal, setcontext, localcontext, Context
from functools import partial

from jedi.common import ignored

print("-----遍历一个范围内的数字,直接遍历数组-----")
for i in [0, 1, 2, 3, 4, 5]:
    print(i ** 2)

print("-----遍历一个范围内的数字，使用range方法-----")
for i in range(6):
    print(i ** 2)

print("-----更好的方法，使用xrange，xrange在Python 3中已经改名为range-----")
print("xrange会返回一个迭代器，用来一次一个值地遍历一个范围，这种方式会比range更省内存")
'''
for i in xrange(6):
    print(i ** 2)
'''

print("-----遍历一个集合-----")
colors = ['red', 'green', 'blue', 'yellow']
for i in range(len(colors)):
    print(colors[i])

print("-----遍历一个集合，更好的方法-----")
for color in colors:
    print(color)

print("-----反向遍历-----")
for i in range(len(colors) - 1, -1, -1):
    print(colors[i])

print("-----反向遍历，更好的方法-----")
for color in reversed(colors):
    print(color)

print("-----遍历一个集合及其下标-----")
for i in range(len(colors)):
    print(i, '--->', colors[i])

print("-----遍历一个集合及其下标，更好的方法-----")
for i, color in enumerate(colors):
    print(i, '--->', color)

print("-----遍历2个集合-----")
names = ['raymond', 'rachel', 'matthew']
n = min(len(names), len(colors))
for i in range(n):
    print(names[i], '--->', colors[i])
for name, color in zip(names, colors):
    print(name, '--->', color)

print("-----遍历2个集合，更好的方法-----")
print("在python2中，zip在内存中生成一个新的列表，需要更多的内存。izip比zip效率更高")
print("在Python 3中，izip改名为zip，并替换了原来的zip成为内置函数")
for name, color in zip(names, colors):
    print(name, '--->', color)

print("-----有序地遍历，正序-----")
for color in sorted(colors):
    print(color)

print("-----有序地遍历，倒序-----")
for color in sorted(colors, reverse=True):
    print(color)

print("-----自定义排序顺序-----")


def compare_length(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0


'''
print(sorted(colors,cmp=compare_length))
'''
print("-----自定义排序顺序，更好的方法-----")
print("注释掉的上面的那个方法效率低，而且写起来很不爽")
print("Python3已经不支持比较函数了")
print(sorted(colors, key=len))

print("-----调用一个函数直到遇到标记值-----")
print(">>>>>当前文件的绝对路径为：>>>>>")
print(os.path.abspath(__file__))
print(">>>>>当前文件的文件夹绝对路径为：>>>>>")
print(os.path.dirname(os.path.abspath(__file__)))
print(">>>>>当前文件所在的文件夹的上一级文件夹所在的路径为：>>>>>")
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
blocks = []
file = 'test.txt'
file_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + \
            '\\' + 'docs' + '\\' + 'txt' + '\\' + file
'''
while True:
    f = open(file_name, "r+")
    print(">>>>>文件名为：>>>>>" + f.name)
    block = f.read(9)
    f.close()
    print(">>>>>读取到的9个字节为：>>>>>" + block)
    print(">>>>>当读取到的变量中存的是123456789时跳出>>>>>")
    if block == '123456789':
        break
    blocks.append(block)
'''

print("-----调用一个函数直到遇到标记值，更好的方法-----")
print("iter接受2个参数，第1个是反复调用的函数，第2个是标记值")
print("这个方法的优势在于iter的返回值是个迭代器，迭代器可以用在各种地方，set、sorted、min、max、heapq、sum.....")
blocks = []
f = open(file_name, "r+")
print("iter的第一个参数必须是一个可调用对象，不能带括号的函数，应该一个去掉括号的带返回值的函数，当返回的值为空时，跳出循环")
print("partial的第一个参数也必须是一个可调用对象，对于读取的对象，5个字节读取一次，当读取的为空时，自动跳出")
print(type(f.read))
for block in iter(partial(f.read, 5), ''):
    blocks.append(block)
print(blocks)
f.close()

print("-----在循环内识别多个退出点-----")


def find(seq, target):
    found = False
    print("当前查找所在的序列为：")
    print(seq)
    print("要查找的为：")
    print(target)
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break
    if not found:
        return -1
    return i


pos = find(['a', 'b', 'c'], 'b')
print("查找到的节点的位置为：")
print(pos)

print("-----在循环内识别多个退出点，更好的方法-----")
print("for执行完所有的循环后就会执行else")
print("for-else用法：当for的判断当中没有break出去的时候，所有循环都走完，执行else中的情况；如果在for当中break出去了，不执行else")


def find(seq, target):
    print("当前查找所在的序列为：")
    print(seq)
    print("要查找的目标为：")
    print(target)
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        print("没有break")
        return -1
    return i


pos = find(['a', 'b', 'c'], 'b')
print("查找到的节点位置为：")
print(pos)

d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

print("-----遍历字典的key，第1种方法-----")
for k in d:
    print(k)

print("-----遍历字典的key，第2种方法-----")
print("当你需要修改字典的时候，使用这种方法")
print("如果你在迭代一个东西的时候修改它，那就是在冒天下之大不韪，接下来发生什么都活该!!!!!")
print("d.keys()把字典里所有的key都复制到一个列表里。然后你就可以修改字典了")
print("注意：如果在Python 3里迭代一个字典你得显示地写：list(d.keys())，因为d.keys()返回的是一个“字典视图”(一个提供字典key的动态视图的迭代器)")
for k in d.keys():
    if k.startswith('r'):
        print(d[k])

print("-----遍历一个字典的key和value-----")
print("这种方法并不快，每次必须要重新哈希并做一次查找")
for k in d:
    print(k, '--->', d[k])

print("产生一个很大的列表")
for k, v in d.items():
    print(k, '--->', v)

print("-----遍历一个字典的key和value，更好的方法-----")
print("iteritems()更好是因为它返回了一个迭代器")
print("注意：Python 3已经没有iteritems()了，items()的行为和iteritems()很接近")
'''
for k,v in d.iteritems():
    print k,'--->',v
'''

print("-----用key-value对构建字典-----")
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']
print("Python2 中，使用d = dict(izip(names, colors))")
d = dict(zip(names, colors))
print(d)

print("-----用字典计数-----")
colors = ['red', 'green', 'red', 'blue', 'green', 'red']
print("简单，基本的计数方法。适合初学者起步时学习")
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
print(d)

print("-----用字典计数，更好的方法-----")
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
print(d)

print("-----稍微潮点的方法，但有些坑需要注意，适合熟练的老手-----")
"""
d = defaultdict(int)
for color in colors:
    d[color] += 1
"""

print("-----用字典分组，第1部分和第2部分，方法1-----")
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']
print("在这个例子，我们按name的长度分组")
d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)
print(d)

print("-----用字典分组，第1部分和第2部分，方法2-----")
d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)
print(d)

print("-----用字典分组，第1部分和第2部分，方法3，更好的方法-----")
'''
d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)
print(d)
'''

print("-----字典的popitem()是原子的吗？-----")
print("popitem是原子的，所以多线程的时候没必要用锁包着它")
print("原则性：盒子只有一个兵乓球，一个人拿的话，其他人就拿不到了，这就是原子性，乒乓球就具有原子性，人就相当于原子")
print("原子性不论是多核还是单核，具有原子性的量，同一时刻只能有一个线程来对它进行操作")
print("如果把一个事务可看作是一个程序,它要么完整的被执行,要么完全不执行。这种特性就叫原子性")
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
while d:
    key, value = d.popitem()
    print(key, '--->', value)

print("-----连接字典-----")
defaults = {'color': 'red', 'user': 'guest'}
print("argparse，命令行解析包")
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args([])
command_line_args = {k: v for k, v in vars(namespace).items() if v}
print(command_line_args)

print("下面是通常的作法，默认使用第一个字典，接着用环境变量覆盖它，最后用命令行参数覆盖它")
print("然而不幸的是，这种方法拷贝数据太疯狂")
d = defaults.copy()
d.update(os.environ)
d.update(command_line_args)
print(d)

print("-----更好的方法-----")
print("ChainMap在Python 3中加入。高效而优雅")
d = ChainMap(command_line_args, os.environ, defaults)
print(d)

print("-----提高可读性-----")
print("位置参数和下标很漂亮")
print("但关键字和名称更好")
print("第一种方法对计算机来说很便利")
print("第二种方法和人类思考方式一致")

print("用关键字参数提高函数调用的可读性")
print("twitter_search('@obama', False, 20, True)")

print("-----更好的方法-----")
print("这种方法稍微(微秒级)慢一点，但为了代码的可读性和开发时间，值得")
print("twitter_search('@obama', retweets=False, numtweets=20, popular=True)")

print("-----用namedtuple提高多个返回值的可读性-----")
print("老的testmod返回值")
doctest.testmod()
# (0, 4)
# 测试结果是好是坏？你看不出来，因为返回值不清晰

print("-----用namedtuple提高多个返回值的可读性，更好的方法-----")
# 新的testmod返回值, 一个namedtuple
doctest.testmod()
# TestResults(failed=0, attempted=4)
print("namedtuple是tuple的子类，所以仍适用正常的元组操作，但它更友好")

print("-----创建一个nametuple----")
# TestResults = namedTuple('TestResults', ['failed', 'attempted'])

print("-----unpack序列-----")
p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'
print("其它语言的常用方法/习惯")
fname = p[0]
lname = p[1]
age = p[2]
email = p[3]
print(p)
print(fname, lname, age, email)

print("-----unpack序列，更好的方法-----")
print("此种方法用了unpack元组，更快，可读性更好")
fname, lname, age, email = p
print(p)
print(fname, lname, age, email)

print("-----更新多个变量的状态-----")
print("此种方法的问题：")
print("x和y是状态，状态应该在一次操作中更新，分几行的话状态会互相对不上，这经常是bug的源头")
print("操作有顺序要求")
print("太底层太细节")


def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        print(x)
        t = y
        y = x + y
        x = t


print("-----更新多个变量的状态，更好的方法-----")
print("此种方法：")
print("抽象层级更高，没有操作顺序出错的风险而且更效率更高")


def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print(x)
        x, y = y, x + y


print("-----同时状态更新-----")
'''
tmp_x = x + dx * t
tmp_y = y + dy * t
tmp_dx = influence(m, x, y, dx, dy, partial='x')
tmp_dy = influence(m, x, y, dx, dy, partial='y')
x = tmp_x
y = tmp_y
dx = tmp_dx
dy = tmp_dy
'''

print("-----同时状态更新，更好的方法-----")
'''
x, y, dx, dy = (x + dx * t,
                y + dy * t,
                influence(m, x, y, dx, dy, partial='x'),
                influence(m, x, y, dx, dy, partial='y'))
'''

print("-----优化的基本原则：-----")
print("除非必要，别无故移动数据")
print("稍微注意一下用线性的操作取代O(n**2)的操作")
print("-----总的来说，不要无故移动数据-----")

print("-----连接字符串-----")
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']
s = names[0]
for name in names[1:]:
    s += ',' + name
print(s)

print("-----连接字符串，更好的方法-----")
print(','.join(names))

print("-----更新序列-----")
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']
del names[0]

print("下面的代码标志着你用错了数据结构")
names.pop(0)
names.insert(0, 'mark')

print("-----更新序列，更好的方法-----")
names = deque(['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie'])
print("使用deque更有效率")
del names[0]
names.popleft()
names.appendleft('mark')

print("-----装饰器和上下文管理-----")
print("用于把业务和管理的逻辑分开")
print("分解代码和提高代码重用性的干净优雅的好工具")
print("起个好名字很关键")
print("记住蜘蛛侠的格言：能力越大，责任越大")

print("-----使用装饰器分离出管理逻辑-----")
print(" 混着业务和管理逻辑，无法重用")


def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page


print("-----使用装饰器分离出管理逻辑，更好的方法-----")
print("注意：Python 3.2开始加入了functools.lru_cache解决这个问题")
'''
@cache
def web_lookup(url):
    return urllib.urlopen(url).read()
'''

print("-----分离临时上下文-----")
print("保存旧的，创建新的")
old_context = getcontext().copy()
print(old_context)
getcontext().prec = 50
print(Decimal(355) / Decimal(113))
setcontext(old_context)

print("-----分离临时上下文，更好的方法-----")
print("译注：示例代码在使用标准库decimal，这个库已经实现好了localcontext")
with localcontext(Context(prec=50)):
    print(Decimal(355) / Decimal(113))

print("-----如何打开关闭文件-----")
file = 'test.txt'
file_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + \
            '\\' + 'docs' + '\\' + 'txt' + '\\' + file
f = open(file_name)
try:
    data = f.read()
    print(data)
finally:
    f.close()

print("-----如何打开关闭文件，更好的方法-----")
with open(file_name) as f:
    data = f.read()
    print(data)

print("-----如何使用锁-----")
print("创建锁")
lock = threading.Lock()
print(lock)
print("使用锁的老方法")
lock.acquire()
try:
    print('Critical section 1')
    print('Critical section 2')
finally:
    lock.release()

print("-----如何使用锁，更好的方法-----")
print("使用锁的新方法")
with lock:
    print('Critical section 1')
    print('Critical section 2')

print("-----分离出临时的上下文-----")
try:
    os.remove('somefile.tmp')
except OSError:
    pass

print("-----分离出临时的上下文，更好的方法-----")
print("ignored是Python 3.4加入的")
print("注意：ignored 实际上在标准库叫suppress(译注：contextlib.supress).")
with ignored(OSError):
    os.remove('somefile.tmp')

print("-----试试创建你自己的ignored上下文管理器-----")
print("把它放在你的工具目录，你也可以忽略异常")
print("译注：contextmanager在标准库contextlib中，通过装饰生成器函数，省去用__enter__和__exit__写上下文管理器")
'''
@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass
'''

print("-----分离临时上下文-----")
print("临时把标准输出重定向到一个文件，然后再恢复正常")
file = 'test.txt'
file_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + \
            '\\' + 'docs' + '\\' + 'txt' + '\\' + file
with open(file_name, 'w') as f:
    oldstdout = sys.stdout
    sys.stdout = f
    try:
        help(pow)
    finally:
        sys.stdout = oldstdout

print("-----分离临时上下文，更好的方法-----")
print("redirect_stdout在Python 3.4加入(译注：contextlib.redirect_stdout)， bug反馈")
with open('help.txt', 'w') as f:
    with redirect_stdout(f):
        help(pow)

print("-----实现你自己的redirect_stdout上下文管理器-----")
'''
@contextmanager
def redirect_stdout(fileobj):
    oldstdout = sys.stdout
    sys.stdout = fileobj
    try:
        yield fieldobj
    finally:
        sys.stdout = oldstdout
'''

print("-----简单的单句表达-----")
print("两个冲突的原则：")
print("一行不要有太多逻辑")
print("不要把单一的想法拆分成多个部分")
print("Raymond的原则：")
print("一行代码的逻辑等价于一句自然语言")

print("-----列表解析和生成器-----")
result = []
for i in range(10):
    s = i ** 2
    result.append(s)
print(sum(result))

print("-----列表解析和生成器，更好的方法-----")
print(sum(i ** 2 for i in range(10)))

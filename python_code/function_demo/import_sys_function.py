#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

模块：逻辑上组织代码的
包：组织模块的

------------------------------------------------------------------------------------------------------------------------------------------------

搜索路径：查找一组目录
路径搜索：查找某个文件的操作

------------------------------------------------------------------------------------------------------------------------------------------------

名称空间：名称（标识符）到对象的映射

#   默认搜索路径时在编译或安装时指定的，它可以在一个或两个地方修改（一个是启动python的shell或命令行的pythonpath环境变量），解释器启动后，也可以访问这个搜索路径，它会保存在sys.path变量里

#   如果你知道需要导入的模块，以及所在位置，直接使用  sys.path.append('/home/lib')

#   一个模块可能有很多拷贝，解释器会使用沿搜索路径顺序找到的第一个模块

#   Python中所有加载到内存的模块都放在sys.modules。
#   当import一个模块时首先会在这个列表中查找是否已经加载了此模块，如果加载了则只是将模块的名字加入到正在调用import的模块的Local名字空间中
#   如果没有加载则从sys.path目录中按照模块名称查找模块文件，模块文件可以是py、pyc、pyd，找到后将模块载入内存，并加入到sys.modules中，并将名称导入到当前的Local名字空间

#   Python在import其它模块时，是从sys.path中搜索的。
#   sys.path的初始值会受到PYTHONPATH、PYTHONHOME等环境变量的影响。
#   也可以在脚本运行过程中动态修改sys.path从而import自己需要的模块

------------------------------------------------------------------------------------------------------------------------------------------------

#   重新绑定：改变一个名字的绑定
#   解除绑定：删除一个名字

------------------------------------------------------------------------------------------------------------------------------------------------

#   在执行期间：有2个或3个活动的名称空间，局部名称空间、全局名称空间、内建名称空间（但局部名称空间在执行期间不断变化）

#   一个正常的python程序的执行过程中，至少存在2个名称空间：内建名称空间、全局名称空间，如果定义了函数，还有局部名称空间

#   python解释器：首先加载 内建名称空间：它由__builtins__模块中的名字构成，随后加载  全局名称空间，它会在模块开始执行后变为 活动名称空间，这样 我们 就有了 2个活动的 名称空间

------------------------------------------------------------------------------------------------------------------------------------------------

#   内建函数？
#   在启动python解释器后，即使没有创建任何的变量或函数，还是有很多函数可以使用,  abs(-1)   max(1,3)，这些函数称为内建函数，不需要我们做任何定义，在启动解释器的时候后，会自动加载到内存，可以直接使用
#   abs             <function abs>
#   type(abs)       builtin_function_or_method
#   max             <function max>
#   type(max)        builtin_function_or_method

------------------------------------------------------------------------------------------------------------------------------------------------

#   内建名称空间  与  __builtins__？
#   内建函数 也是 函数，虽然没有人为导入，但是在python解释器启动的时候，会自动导入
#   python解释器在启动的时候会首先加载  内建名称空间，内建名称空间有许多名字到对象之间映射，而这些名字就是内建函数的名称，对象就是内建函数本身（注意区分 函数名称 和 函数对象 的区别 ）
#   查看当前名称空间导入的模块   dir()
#   __builtins__这个模块，本身定义了一个名称空间——内建名称空间，dir(__builtins__)

------------------------------------------------------------------------------------------------------------------------------------------------

#   __builtins__ 与 __builtin__ 的简单区别？
#   内建名称空间  由 __builtins__模块中的名称空间定义
#   __builtins__    <module '__builtin__' (built-in)>
#   内建名称空间中的函数是在内建模块 __builtin__中定义的
#   __builtins__ 模块 引用了 __builtin__模块,__builtins__模块包含内建名称空间中内建名字的集合（因为它引用或者指向了__builtin__模块），真正的内建函数、异常、属性来自 __bulitin__模块
#   在python中，真正的只有__builtin_模块，并不存在__builtins__模块
#   import __builtin__
#   import __builtins__     No module named __builtins__
#   __builtins__模块，只是在python解释器启动的时候，解释器自动为我们创建的一个到__builtin__模块的引用

注意：
    如果在执行期间调用了一个函数，那么将创建出第三个名称空间，即局部名称空间。
    可以通过globals（）和locals（）内建函数判断出某一个名字属于哪个名称空间。

------------------------------------------------------------------------------------------------------------------------------------------------

#   __builtins__ 与 __builtin__ 的深入区别？

1.在主模块 __main__中

print __name__                  __main__
import __builtin__
__builtin__                     <module '__builtin__' (built-in)>
__builtins__                    <module '__builtin__' (built-in)>
__builtin__.__name__            '__builtin__'
__builtins__.__name__           '__builtin__'
__builtins__ == __builtin__     True
__builtins__ is __builtin__     True
id(__builtins__)                139948130257672
id(__builtin__)                 139948130257672

#   __builtins__ 和 __builtin__完全一样，都指向同一个模块对象，这也是python中引用传递的概念

#   创建一个变量，对它做一次引用传递

def func():
    print 'test'
func                            <function __main__.func>
funcs = func
funcs                           <function __main__.func>
func.__name__                   'func'
funcs.__name__                  'func'
funcs == func                   True
funcs is func                   True
id(funcs)                       51319824
id(func)                        51319824

------------------------------------------------------------------------------------------------------------------------------------------------

2.不是在主模块中

#   如果不是在主模块中使用 __builtins__，这时候，__builtins__这是对__builtin__.__dict__的一个简单引用

import __builtin__

print 'Module name:',__name__
#   Module name: __main__

print '*==test __builtin__ and __builtins__==*'
#   *==test __builtin__ and __builtins__==*

print '__builtin__ == __builtins__', __builtin__ == __builtins__
#   __builtin__ == __builtins__ True

print '__builtin__ is __builtins__', __builtin__ is __builtins__
#   __builtin__ is __builtins__ True

print 'id(__builtin__)', id(__builtin__)
#   id(__builtin__) 139866459421448

print 'id(__builtins__)', id(__builtins__)
#   id(__builtins__) 139866459421448

print '='*50
#   ==================================================

print '*==test __builtin__.__dict__ and __builtins__==*'
#   *==test __builtin__.__dict__ and __builtins__==*

print '__builtin__.__dict__ == __builtins__', __builtin__.__dict__ == __builtins__
#   __builtin__.__dict__ == __builtins__ False

print '__builtin__ is __builtins__', __builtin__.__dict__ is __builtins__
#   __builtin__ is __builtins__ False

print 'id(__builtin__)', id(__builtin__.__dict__)
#   id(__builtin__) 18188192

print 'id(__builtins__)', id(__builtins__)
#   id(__builtins__) 139866459421448

------------------------------------------------------------------------------------------------------------------------------------------------

#   总结：
    在启动python解释器或运行一个python程序时，内建名称空间都是从__builtins__模块中加载的，只是__builtins__本身是对python内建模块__builtin__的引用，而这种引用又分2种情况：
    不管是不是在主模块__main__中，__builtins__直接引用__builtin__模块，他们的属性、方法全部一致

------------------------------------------------------------------------------------------------------------------------------------------------

#   名称查询：
    访问一个属性的时候，解释器必须在3个名称空间中的一个找到它，首先从  局部名称空间开始，如果没有找到，查找全局名称空间，如果还没找到，在 内建名称空间 查找，如果还没找到，会报错

def foo():
    print "\ncalling foo()..."
    bar = 200
    print "in foo(), bar is", bar
bar = 100
print "in __main__, bar is", bar
foo()

#   输出：
in __main__, bar is 100

calling foo()...
in foo(), bar is 200


#   foo（）函数局部名称空间里的bar变量覆盖了全局的bar变量，虽然bar存在于全局名称空间里，但是程序首先找到的是 局部名称空间里的那个，所以“覆盖”了全局的那个

------------------------------------------------------------------------------------------------------------------------------------------------

#   无限制的名称空间

def foo():
    pass
foo.__doc__ = 'Oops, forgot to add doc str above!'
foo.version = 0.2

#   访问方法
mymodule.foo()

#   访问属性
mymodule.version()


#   定义实例属性
class MyUltimatePythonStorageDevice(object):
    pass
bag = MyUltimatePythonStorageDevice()
bag.x = 100
bag.y = 200
bag.version = 0.1
bag.completed = False

------------------------------------------------------------------------------------------------------------------------------------------------

"""

# 导入系统模块
import sys

# 查看模块的查找路径
print
sys.path

# 将指定文件夹下的模块添加到系统路径下
sys.path.append('/root/wyz_lianxi')

# 再次查看模块包含的查找路径
print
sys.path

#   导入新模块
#   import something

#   查看所有导入的模块名称
print
sys.modules.keys()

#   查看所有导入的模块的位置
print
sys.modules.values()

#   查看os模块的位置
print
sys.modules["os"]

#   查看所有的可用模块
print
help('modules')

#   查看当前导入的所有模块和他们来自的位置
print
sys.modules

#   查看当前的命名空间导入了哪些模块
print
dir()

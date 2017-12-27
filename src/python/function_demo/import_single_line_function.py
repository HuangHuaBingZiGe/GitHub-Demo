#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
---------------------------------------------------------------------------------------------
#something.py

#!/usr/bin/python
# -*- coding: utf-8 -*-

public_variable = 42
_private_variable = 141

def public_function():
    print("I'm a public function! yay!")

def _private_function():
    print("Ain't nobody accessing me from another module...usually")

class PublicClass(object):
    pass

class _WeirdClass(object):
    pass

---------------------------------------------------------------------------------------------

from something import *

#   注意： 在导入模块的时候，import * 是不会将单下划线开头的 方法、类、属性  加载到命名空间的

public_variable
#   42
_private_variable
#   name '_private_variable' is not defined
public_function()
#   I'm a public function! yay!
_private_function
#   name '_private_function' is not defined
c = PublicClass()
c
#   <somethin.PublicClass at 0x1c3eb50>
c = _WeirdClass()
#   name '_WeirdClass' is not defined

---------------------------------------------------------------------------------------------

# something_all.py

#   注意： 以“_”开头的私有变量、方法、类 可以放入到 __all__ 里面，在使用 from <module/package> import * 的时候，会加载 __all__参数，导入到命名空间；在只使用 import <module/package> 的时候不会加载 __all__

#   从包中导入*时，__all__与模块大致相同，除了处理包中的模块（与模块中指定名称相反）。 所以__all__指定当我们从<package> import *使用时，将加载并导入当前命名空间的所有模块

#   但是，不同的是，当你在一个包的__init__.py中省略__all__的声明时，来自<package> import *的声明根本就不会导入任何东西（不完全是真的）

#   从<module> import *不明确。 我们没有告诉我们我们正在进口什么，或者我们将什么名字带入我们的命名空间。 明确指定和导入我们所需要的东西会更好一些 那样的话，一个读者（很可能是你的未来的自我）不会混淆变量/函数/类/等的位置。 代码中使用的代码来自于...，这导致我们：

#!/usr/bin/python
# -*- coding: utf-8 -*-

__all__ = ['_private_variable', 'PublicClass']

# The rest is the same as before

public_variable = 42
_private_variable = 141

def public_function():
    print("I'm a public function! yay!")

def _private_function():
    print("Ain't nobody accessing me from another module...usually")

class PublicClass(object):
    pass

class _WeirdClass(object):
    pass

---------------------------------------------------------------------------------------------

from something import *
public_variable
#   42
_private_variable
#   141
public_function()
#   I'm a public function! yay!
_private_function
#   name '_private_function' is not defined
c = PublicClass()
c
#   <something.PublicClass at 0x1c3eb10>
c = _WeirdClass()
#   name '_WeirdClass' is not defined

---------------------------------------------------------------------------------------------

"""

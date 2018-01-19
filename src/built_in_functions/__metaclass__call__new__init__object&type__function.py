#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Python 中的 object：
    
    首先我們必須先牢牢記住一個重要觀念：Python 是一種物件導向語言；在 Python 裡面，所有你能想得到的東西都是 object
    
    我們可以用 type() 這個內建函數，來得知某樣東西的 type
    
    給 type() 一個 object 時，會回傳一個東西叫做 Type Object ，你可以用 print() 印出來看看是什麼樣子
"""
print("--------------------------------------------------")
print(type(1))  # <class 'int'>
print(type(1.1))  # <class 'float'>
print(type("hello"))  # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>
print(type({1, 2, 3}))  # <class 'set'>
print(type({1: 10, 2: 20}))  # <class 'dict'>

"""
上面的例子說明了，像 "hello" 這個字串，在 Python 中其實是 str 這個 class 的 instance

連函數（function）也是一個 object
"""


def func():
    return "hello"


print("--------------------------------------------------")
print(type(func))  # <class 'function'>
print(type(func()))  # <class 'str'>  因為 func() 回傳的是 "hello" 這個 string

"""
那我定義一個 class 的話，該 class 的 type 又是什麼？建立出來的 instance 的 type 又是什麼？我上面沒寫，因為這個問題的答案很違反直覺，下面就要來解釋
"""

"""
Python 中的 class：

    一般來說，物件導向語言中的「class」是用來「描述如何建立 object」的程式碼；我們寫 class 就是為了建立 object。然而在 Python 中：

連 class 本身也是 object
class 是 meta class 的 instance
meta class 是 class 的 class

當你一寫下 class 關鍵字 ，Python 會執行它，並建立一個 class object

這個 class object 並不是 class instance，而是 class 自己本身
這個 class object 的功能就是建立自己的 instance object

[注意]
為了避免混淆，接下來提到的所有 class object 指的皆為 「class 本身的 object」，而不是 class instance object
"""

"""
class object
既然 Python 的 class 自己也是 object，也就是說你可以把 class object :

assign 給 variable
copy 它
增加 attributes
當作 function parameter 來傳遞
前面提到的 type() 這內建函數極度詭異，當塞三個參數進去時，他的功能會變成建立 class object…怎麼做呢？官方文件是這樣寫：

type(name, bases, dict) 分別對應到 class attributes 中的：

name 會變成 __name__，也就是 class 的名稱
bases 會變成 __bases__，也就是該 class 要繼承自哪些 base class
dict 會變成 __dict__ ，也就是該 class 所有的 member

"""


class Hello:  # 預設繼承自 object
    pass


class Hello1(object):
    pass


print("--------------------------------------------------")
print(Hello)  # <class '__main__.Hello'>
print(Hello())  # <__main__.Hello object at 0x7f1cc5aedcc0>
print(type(Hello))  # <class 'type'>
print(type(Hello()))  # <class '__main__.Hello'>

DynamicHello = type("DynamicHello", (), {})
print("-------------------------------------------------")
print(DynamicHello)  # <class '__main__.DynamicHello'>
print(DynamicHello())  # <__main__.DynamicHello object at 0x7f1cc5aedcc0>
print(type(DynamicHello))  # <class 'type'>
print(type(DynamicHello()))  # <class '__main__.DynamicHello'>

"""
這兩種寫法的意義是完全相同的，真是他媽的莫名其妙對吧。分析一下上面這個鬼打牆的範例：

Hello (class object) 就是 class 自己本身的 object。 <class '__main__.Hello'>
Hello() (class instance object) 就是大家都知道的 instance 沒啥好說的。
透過 type() 可以得知一個 object 的 type：
Hello() 因為是 instance，很合理的 type 就是 class object <class '__main__.Hello'>
Hello 是 class object，那他的 type 呢？嗯，真是靠北，就是 type ，也就是 <class 'type'>
那還有個問題: type 自己本身的 type 是什麼？
"""

print("--------------------------------------------------")
print(type(Hello))  # <class 'type'>
print(type(type(Hello)))  # <class 'type'>

"""
类对象：类型为type，没有实例化，没有内存地址
类的实例对象：有内存地址
"""

"""
__class__：
    str 這個 class 建立所有的 string object
    int 這個 class 建立所有的 int object
    type 這個 class 建立了所有的 class object
    
透過 __class__ 這個特殊 attribute，可以得知一個 object 是什麼 class 的 instance
"""

print("-----------------------------------------------")
title = "The C++ Programming Language"
page = 42


def func():
    pass


class Hello:
    pass


hello = Hello()  # hello 是 Hello 的 instance
print(title.__class__)  # <class 'str'>
print(type(title))
print(page.__class__)  # <class 'int'>
print(func.__class__)  # <class 'function'>
print(hello.__class__)  # <class '__main__.Hello'>

"""
那…來看看這些 object 的 .__class__.__class__ 又是什麼
"""
print("-----------------------------------------------")
print(title.__class__.__class__)  # <class 'type'>
print(page.__class__.__class__)  # <class 'type'>
print(func.__class__.__class__)  # <class 'type'>
print(hello.__class__.__class__)  # <class 'type'>

"""
嗯嗯，Python 裡面所有的 class 都是 type 的 instance
"""

"""
Metaclass:
    metaclass 是 class 的 class，也就是說:
    object 是 class 的 instance
    class 是 metaclass 的 instance
"""

"""
type:

    type 是 Python 中的 metaclass:
    type 本身也是一個 class
    type 本身的 metaclass 就是他自己
    要寫一個 metaclass 的話，就繼承 type

__call__() 預設會呼叫 __new__() 跟 __init__()
"""


class Hello:
    pass


print("-----------------------------------------------")
print(Hello)  # 這是 class object 自己本身
print(Hello())  # 這是 class object 建立出來的 class instance
print(Hello.__call__())  # 這行實際的作用跟上一行完全相同

"""
Python 在實體化 Hello 時的過程：

 Hello()
                            ↓
                等同呼叫 Hello.__call__()
                            ↓
   呼叫 Hello.__new__() 建立出 object 並回傳該 object
                            ↓
再呼叫 Hello.__init__() 來讓該 object 初始化其他有的沒的

__call__() 在 class 中的預設行為，就是依序幫你呼叫 __new__() 跟 __init__()
"""

"""
最後整理：

假設我們定義了一個 class 叫 Hello

__call__ 定義了當 Hello 後面被加上小括號、當作 function 來呼叫時的行為。預設行為是依序呼叫 __new__() 跟 __init__()

__new__ 定義了 Hello 如何實體化，最後會回傳一個實體 object

__init__ 定義了 Hello 實體化後，其實體 object 如何初始化（例如 member variable 定義之類的，這是大家最熟悉的部份）

"""

"""
Singleton
嘗試一：透過 __new__
"""


class Single(object):
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance
    
    def __init__(self):
        print(id(self))  # 印出來的 instance id 都是相同的


print("-----------------------------------------------")
a = Single()  # 140341333464904
b = Single()  # 140341333464904
c = Single()  # 140341333464904

"""
嘗試二：透過 metaclass
還記得self只是約定成俗的東西、其實你要寫啥都可以吧？ cls 就是這樣的存在。Python 大家都習慣用 cls 當作指向 class 的變數名稱、並用 self 當作指向 instance 的變數名稱
"""


class Singleton(type):
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:  # 記得要透過 cls 來存取__instance 這個 class attribute 喔
            cls.__instance = super().__new__(cls, *args, **kwargs)  # 即使用了 super()還是得加 cls?!
        return cls.__instance


class Hello(metaclass=Singleton):
    pass


print("--------------------------------------------------")
print(id(Hello()))  # 兩次實體化 id 不同！失敗了！
print(id(Hello()))


class Singleton(type):
    __instance = None
    
    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:  # 記得要透過 cls 來存取__instance 這個 class attribute 喔
            cls.__instance = super().__call__(*args, **kwargs)  # 用了 super() 就別加 cls
        return cls.__instance


class Hello(metaclass=Singleton):
    pass


print("------------------------------------------------")
print(id(Hello()))
print(id(Hello()))  # id 相同，成功啦！

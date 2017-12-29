#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
---------------------------------------------------------------------------------------------

#   包是一个有层次的文件目录结构,它定义了一个由模块和子包组成的python应用程序执行环境

#   有Analog.py文件，导入子包
import Phone.Mobile.Analog
Phone.Mobile.Analog.dial()

---------------------------------------------------------------------------------------------

#   也可以使用from-import实现不同需求的导入
from Phone import Mobile
Mobile.Analog.dial('555-1212')

---------------------------------------------------------------------------------------------

#   还可以这么写
from Phone.Mobile import Analog
Analog.dial('555-1212')

---------------------------------------------------------------------------------------------

#   也可以这么写
from Phone.Mobile.Analog import dial
dial('555-1212')

---------------------------------------------------------------------------------------------

"""
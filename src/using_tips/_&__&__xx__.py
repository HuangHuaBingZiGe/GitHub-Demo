#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

单下划线（_）：
    1.在解释器中，"_"代表交互式解释器会话中上一条执行语句的结果，返回[Out]的那个值
        45
        _
    2.此时,"_"作为临时性的名称使用，不会在后面再次用到该名称
        n = 42
        for _ in range(n):
            print _
    3.国际化，django中"_"会被作为一个函数来使用

        注意：
            场景2和场景3的使用方法会相互冲突，需要避免同时使用

        from django.utils.translation import ugettext as _
        from django.http import HttpResponse
        def my_view(request):
            output = _("Welcome to my site")
            return HttpResponse(output)

--------------------------------------------------------------------------------------------------------------------

名称前的单下划线（_name）：

    1.在名称前的单下划线，用于指定该名称属性为“私有”，以“_”开头的名称只供内部使用
    2.以下划线"_"为前缀的名称应该被视为API中非公开的部分（不管是函数、方法还是数据成员），应该将它们看做是一种实现细节，在修改它们时无需对外通知
    3. 类似一种惯例，它对解释器来说有一定的意义
    from <模块/包名> import * ：表示以 “_”开头的名称都不会被导入，除非模块或包中的"__all__"列表显式地包含了它们

--------------------------------------------------------------------------------------------------------------------

名称前的双下划线（__function）：

    1.名称（方法名）前双下划线的用法并不是一种惯例，对解释器来说有特定的意义
    2.这种用法为了避免与子类定义的名称冲突
    3.__method_spam 这种形式（至少2个前导下划线，最多一个后续下划线），会被 _classname__method_spam 取代
    4.当创建A的类的子类的时候，不能轻易的覆写A中的方法__method_name
    5.python中的__method_spam 方法相当于 java当中的 final方法，不允许覆盖

class A(object):
    def _internal_use(self):
        pass
    def __method_name(self):
        pass

dir(A())


class B(A):
    def __method_name(self):
        pass

dir(B())

--------------------------------------------------------------------------------------------------------------------

名称前后的双下划线（__function__）：

    1.这种用法表示python中特殊的方法名
    2.其实，这只是一种惯例
    3.对python来说，这将确保不会与用户自定义的名称冲突
    4.通常，你将会覆写这些方法，并在里面实现你所需要的功能，以便python调用它们
    5.例如，当定义一个类时，你经常会覆写“__init__”方法
    6.虽然你也可以编写自己的特殊方法名，但是不要这么做！！！！

--------------------------------------------------------------------------------------------------------------------

"""

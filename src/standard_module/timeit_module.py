#!/usr/bin/python
# -*- coding: utf-8 -*-

import timeit

print(timeit.timeit("obj.method()", """
class SomeClass:
    def method(self):
        pass
obj = SomeClass()
"""))

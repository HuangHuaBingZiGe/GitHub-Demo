#!/usr/bin/python
# -*- coding: utf-8 -*-

print("--------------------------------------------------")
print("当前的list为：")
temp_list = [1, 2, 3, 4, 5]
print(temp_list)
print("当前的list的类型为：")
print(type(temp_list))

print("--------------------------------------------------")
print("当前的tuple为：")
temp_tuple = tuple(temp_list)
print(temp_tuple)
print("当前的tuple的类型为：")
print(type(temp_tuple))

print("--------------------------------------------------")
print("当前的list为：")
final_list = list(temp_tuple)
print(final_list)
print("当前的list的类型为：")
print(type(final_list))

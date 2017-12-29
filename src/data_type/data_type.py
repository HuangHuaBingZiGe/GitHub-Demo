#!/usr/bin/python
# -*- coding: utf-8 -*-

a = 1425
print(type(a))
b = (-45263)
print(type(b))
c = 0
print(type(c))
g = 1.03
print(type(g))
h = -11.23
print(type(h))
i = .34
print(type(i))
j = 2.12e-10
print(type(j))
k = 5E220
print(type(k))

x = complex(1, 2)
print(type(x))
print(x)
z = 1 + 2j
print(type(z))
z = 1 + 2J
print(type(z))

x = True
print(type(x))
y = False
print(type(y))

str1 = "String"
print(type(str1))
print(str1)
str2 = 'String'
print(type(str2))
print(str2)
str3 = 'Day"s'
print(type(str3))
print(str3)
str4 = "Day's"
print(type(str4))
print(str4)

print("This is a backslash (\\) mark.")
print("This is a tab \t key")
print("These are \' single quotes\'")
print("These are \" double quotes\"")
print("This is a new line \n New line")

string1 = "PYTHON TUTORIAL"
print(string1[0])
print(string1[-15])
print(string1[14])
print(string1[-1])
print(string1[4])
print(string1[-11])

string1 = "PYTHON TUTORIAL"
# string1[0] = 'A'
print(string1[0])

string1 = "PYTHON TUTORIAL"
print('Z' in string1)
print('P' in string1)
print('TUT' in string1)

tup1 = (0, -1, 12, 232.23, 100)
print(type(tup1))
print(tup1)
tup2 = ('Red', 'Black', 2000, "White")
print(tup2)
tup3 = "a1", "b1", "c1", "d1"
print(type(tup3))
print(tup3)

empty_tup1 = ()
print(empty_tup1)
single_tup1 = (100,)
print(type(single_tup1))
print(single_tup1)
single_tup2 = (100)
print(single_tup2)
print(type(single_tup2))

tup2 = ('Red', 'Black', 2000, "White")
print(tup2)
print(tup2[0])
print(tup2[3])

tup2 = ('Red', 'Black', 2000, "White")
print(tup2[0])
# tup2[0] = "White"
print(tup2[0])

tup2 = ('Red', 'Black', 2000, 12.12)
print(tup2[0:2])
print(tup2[1:2])
print(tup2[1:-2])
print(tup2[:3])

tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
tup3 = (7, 8, 9)
tup_123 = tup1 + tup2 + tup3
print(tup_123)
print(tup1 * 4)

my_list1 = [5, 12, 13, 14]
print(my_list1)
my_list2 = ['red', 'blue', 'black', 'white']
print(my_list2)
my_list3 = ['red', 12, 112.12]
print(my_list3)

my_list = []
print(my_list)

color_list = ['red', 'blue', 'black', 'white']
print(color_list[0])
print(color_list[0], color_list[3])
print(color_list[-1])
# print(color_list[4])

color_list = ['red', 'blue', 'black', 'white']
print(color_list[0:2])
print(color_list[1:2])
print(color_list[1:-2])
print(color_list[:3])
print(color_list[:])

color_list = ['red', 'blue', 'black', 'white']
print(color_list)
print(color_list[0])
color_list[0] = "White"
print(color_list)
print(color_list[0])

color_list1 = ["White", "Yellow"]
color_list2 = ["Red", "Blue", 'White']
color_list3 = ["Green", "Black"]
color_list = color_list1 + color_list2 + color_list3
print(color_list)
number = [1, 2, 3]
print(number[0] * 4)
print(number * 4)

a = [1, 2, 1, 3, 0, 4, 7, 8, 6]
b = [5, 5, 7, 8, 7, 9, 6, 1, 1, 2]
s1 = set(a)  # 去重
s2 = set(b)  # 去重
print(s1)
print(s2)
print(s1 - s2)  # 在s1中不在s2中，取差集
print(s1 | s2)  # 在s1中或在s2中，取并集
print(s1 & s2)  # 既在s1里又在s2里，取交集
print(s1 ^ s2)  # 只在s1或s2里，不同时出现在2个集合里面

pd = {"class": 'V', "section": 'A', "roll_no": 12}
print(pd["class"])
print(pd["section"])
print(pd["roll_no"])
print(pd)

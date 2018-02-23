# 列表：一个打了激素的数组——整数、浮点数、字符串、对象

"""
创建列表：
    ----创建一个普通列表
    ----创建一个混合列表
    ----创建一个空列表
"""

member = ['小甲鱼', '小布丁', '黑夜', '迷途', '怡静']
print(member)
print(id(member))

number = [1, 2, 3, 4, 5]
print(number)

mix = [1, '小甲鱼', 3.14, [1, 2, 3]]
print(mix)

empty = []
print(empty)
print('----------------------------------')

"""
向列表添加元素:
"""

# append 使用方法：只能添加一个参数
member.append('福禄娃娃')
print(member)
print(id(member))
print(len(member))
print('----------------------------------')

# extend 使用方法：1个列表扩展另一个列表，参数为列表类型
member.extend(['竹林小溪', 'Crazy迷恋'])
print(member)
print(len(member))
print('----------------------------------')

# insert使用方法：位置、参数
member.insert(1, '牡丹')
print(member)
print('----------------------------------')

# 从列表中获取元素
print(member[0])
print(member[1])

temp = member[0]
member[0] = member[1]
member[1] = temp
print(member)
print('----------------------------------')

# remove：从列表删除元素
member.remove('怡静')
print(member)
print(id(member))

# del：从列表删除元素
del member[1]
print(member)

# pop：从列表中删除元素
name = member.pop()
print(name)
print(member)
member.pop(1)
print(member)

# 列表分片（Slice）
print(member[1:3])
print(member[:3])
print(member[1:])
print(member[:])
print('----------------------------------')


"""
列表的一些常用操作符：
----比较操作符
----逻辑操作符
----连接操作符
----重复操作符
----成员关系操作符
"""

list1 = [123]
list2 = [234]
print(list1 > list2)

list1 = [123, 456]
list2 = [234, 123]
print(list1 > list2)

list3 = [123, 456]
print((list1 < list2) and (list1 == list3))

list4 = list1 + list2
print(list4)

print(list3 * 3)
list3 *= 3
print(list3)
list3 *= 5
print(list3)
print('----------------------------------')

print(123 in list3)
print(123 not in list3)
list5 = [123, ['小甲鱼', '牡丹'], 456]
print('小甲鱼' in list5)
print('小甲鱼' in list5[1])

print(list5[1][1])
print('----------------------------------')

# 列表的小伙伴们
print(dir(list))
print(list3.count(123))  # 统计次数
print(list3.index(123))  # 返回出现的位置
print(list3.index(123, 3, 7))  # 从索引为3的位置到索引为7的位置搜索123
print(id(list3))
print(list3)
print(list3.reverse())
print(list3)
print(id(list3))
print('----------------------------------')

list6 = [4, 2, 5, 1, 9, 23, 32, 0]
list6.sort()
print(list6)
print('----------------------------------')

list7 = list6[:]  # 真实的拷贝
print(list7)
print('----------------------------------')

list8 = list6  # 增加指向
print(list8)
list6.sort()
print(list6)
print(list7)
print(list8)

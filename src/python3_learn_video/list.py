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

"""
列表的一些常用操作符：
----比较操作符
----逻辑操作符
----连接操作符
----重复操作符
----成员关系操作符
"""

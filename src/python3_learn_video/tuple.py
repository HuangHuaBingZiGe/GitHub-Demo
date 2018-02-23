# 元组是不可改变的

# 创建 和 访问 一个元组

print('----------------------------------')
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple1)
print(tuple1[1])
print(tuple1[:5])
tuple2 = tuple1[:]
print(tuple2)
print('----------------------------------')
temp = (1)
print(type(temp))
temp2 = 2, 3, 4
print(type(temp2))
temp = []
print(type(temp))
temp = ()
print(type(temp))
print(8 * 8)
print(8 * (8,))
print('----------------------------------')

# 更新 和 删除一个元组

temp = ('小甲鱼', '黑夜', '迷途', '小布丁')
print(id(temp))
temp = temp[:2] + ('怡静',) + temp[2:]
print(id(temp))
print(temp)
print('----------------------------------')

# 删除元组，比较少使用

del temp


# 元组相关的操作符

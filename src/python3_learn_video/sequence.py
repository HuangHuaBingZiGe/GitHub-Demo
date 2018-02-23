"""
列表、元组、字符串的共同点：
    ——都可以通过索引得到每一个元素
    ——默认索引值总是从0开始
    ——可以通过分片的方法得到一个范围内的元素的集合
    ——有很多共同的操作符（重复操作符、拼接操作符、成员关系操作符）

"""

print(help(list))
print('----------------------------------')

a = list()
print(a)

b = 'I love FishC.com'
b = list(b)
print(b)

c = (1, 1, 2, 3, 5, 8, 13, 21, 34)
c = list(c)
print(c)

print('---------------------------------------------')
print(help(tuple))
print(len(a))
print(len(b))
print(b)
print(max(1, 2, 3, 4, 5))
print(max(b))
numbers = [1, 18, 13, 0, -98, 34, 54, 76, 32]
print(max(numbers))
print(min(numbers))
chars = '1234567890'
print(min(chars))

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print(max(tuple1))
numbers.append('a')
print(numbers)

"""
max = tuple1[0]

for each in tuple1:
    if each > max:
        max = each
        
return max
"""

print('--------------------------------------------')
print(max(tuple1))
tuple2 = (3.1, 2.3, 3.4)
print(sum(tuple2))

numbers.pop()
print(numbers)
print(sum(numbers))
print(sum(numbers, 8))
print(chars)

print(sorted(numbers))
print(list(reversed(numbers)))
print(list(enumerate(numbers)))

a = [1, 2, 3, 4, 5, 6, 7, 8, ]
b = [4, 5, 6, 7, 8]
print(list(zip(a, b)))

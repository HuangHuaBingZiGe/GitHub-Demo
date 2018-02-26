brand = ['李宁', '耐克', '阿迪达斯', '鱼c工作室']
slogan = ['一切皆有可能', 'Just do it', 'Impossible is nothing', '让编程改变世界']

print('---------------------------------------------')
print('鱼C工作室的口号是：', slogan[brand.index('鱼c工作室')])
print('---------------------------------------------')

dict1 = {'李宁': '一切皆有可能', '耐克': 'Just do it', '阿迪达斯': 'Impossible is nothing', '鱼C工作室': '让编程改变世界'}
print('鱼C工作室的口号是：', dict1['鱼C工作室'])
print('---------------------------------------------')

dict2 = {1: 'one', 2: 'two', 3: 'three'}
print(dict2[2])
print('---------------------------------------------')

dict3 = {}
print(dict3)
print('---------------------------------------------')
print(help(dict))
print('---------------------------------------------')

dict3 = dict((('F', 70), ('i', 105), ('s', 115), ('h', 104), ('C', 67)))
print(dict3)
print('---------------------------------------------')

dict4 = dict(小甲鱼='让编程改变世界', 苍井空='让AV征服所有宅男')
print(dict4)
print('---------------------------------------------')

dict4['苍井空'] = '所有AV从业者都要通过学习编程来提高职业技能'
print(dict4)
print('---------------------------------------------')

dict4['爱迪生'] = '天才就是99%的汗水加1%的灵感，但这1%的灵感远比99%的汗水更重要'
print(dict4)
print('---------------------------------------------')

dict1 = {}
print(dict1.fromkeys((1, 2, 3)))
print(dict1.fromkeys((1, 2, 3), 'number'))
print(dict1.fromkeys((1, 2, 3), ('one', 'two', 'three')))
print(dict1.fromkeys((1, 3), '数字'))
print('---------------------------------------------')

dict1 = dict1.fromkeys(range(32), '赞')
print(dict1)
print('---------------------------------------------')

for eachKey in dict1.keys():
    print(eachKey)
print('---------------------------------------------')

for eachKey in dict1.values():
    print(eachKey)
print('---------------------------------------------')

for eachItem in dict1.items():
    print(eachItem)
print('---------------------------------------------')

print(dict1.get(32))
print(dict1.get(32, '木有!'))
print(dict1.get(31, '木有！'))
print('---------------------------------------------')

print(32 in dict1)
print(31 in dict1)
print('---------------------------------------------')

print(dict1)
print(dict1.clear)
print(dict1)

a = {1: 'one', 2: 'two', 3: 'three'}
b = a.copy()
c = a
print(c)
print(a)
print(b)
print(id(a))
print(id(b))
print(id(c))
print('---------------------------------------------')

c[4] = 'four'
print(c)
print(a)
print(b)
print('---------------------------------------------')

a.pop(2)
print(a)
a.popitem()
print(a)
print('---------------------------------------------')

a.setdefault('小白')
a.setdefault(5, 'five')
print(a)
print('---------------------------------------------')

b = {'小白': '狗'}
a.update(b)
print(a)
print('---------------------------------------------')

num = {}
print(type(num))
num2 = {1, 2, 3, 4, 5}
print(type(num2))
print('---------------------------------------------')

num2 = {1, 2, 3, 4, 5, 5, 4, 3, 2}
print(num2)
print('---------------------------------------------')

"""
如何创建一个集合：
    ——直接把一堆元素用花括号括起来
    ——使用set（）工厂函数
"""
set1 = set([1, 2, 3, 4, 4, 5])
print(set1)
print('---------------------------------------------')

num1 = [1, 2, 3, 4, 5, 5, 3, 1, 0]
temp = []
for each in num1:
    if each not in temp:
        temp.append(each)
print(temp)
print('---------------------------------------------')

num1 = list(set(num1))
print(num1)
print('---------------------------------------------')

print(num2)
print(1 in num2)
print('1' in num2)
print('---------------------------------------------')

print(num2)
num2.add(6)
print(num2)
num2.remove(5)
print(num2)
print('---------------------------------------------')

"""
不可变集合：frozen
"""
num3 = frozenset({1, 2, 3, 4, 5, 6})
print('---------------------------------------------')

print(help(open))
print('---------------------------------------------')

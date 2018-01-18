#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

# random
# 是用于生成随机数的，我们可以利用它随机生成数字或者选择字符串


# random.seed(x)
# 改变随机数生成器的种子seed
# 一般不必特别去设定seed，Python会自动选择seed


# random.random()
# 用于生成一个随机浮点数n,0 <= n < 1


# random.uniform(a,b)
# 用于生成一个指定范围内的随机浮点数，生成的随机整数a<=n<=b


# random.randint(a,b)
# 用于生成一个指定范围内的整数，a为下限，b为上限，生成的随机整数a<=n<=b;若a=b，则n=a；若a>b，报错


# random.randrange([start], stop [,step])
# 从指定范围[start,stop)内，按指定基数递增的集合中获取一个随机数，基数缺省值为1


# random.choice(sequence)
# 从序列中获取一个随机元素，参数sequence表示一个有序类型，并不是一种特定类型，泛指list，tuple，字符串等


# random.shuffle(x[,random])
# 用于将一个列表中的元素打乱（洗牌），会改变原始列表


# random.sample(sequence,k) 从指定序列中随机获取k个元素作为一个片段返回，不会改变原有序列


"""
但是，有一点需要注意：python random是伪随机数。
  那么，可以借用python random实现真随机数吗？答案是No。所谓真随机数，是要求根据绝对随机事件产生的数，也就是说要求要有一个无因果关系的随机事件，那么，这玩意只存在与哲学领域……
  目前的随机数产生都是统计上的随机，因为随机源都是自然事件，顶天了算是混沌变量，绝对的无因果大概是不存在的。
  不过统计随机基本上都够用了吧……
  还是老老实实的用random模块吧….
"""

# 随机选取0到99的某个整数
print(random.randint(0, 99))

# 随机选取0到100间的偶数
print(random.randrange(0, 101, 2))

# 随机0-1之间的浮点数
print(random.random())

# 随机1-10之间的浮点数
print(random.uniform(1, 10))

# 随机1个字符
print(random.choice('abcdefg&#%^*f'))

# 多个字符中选取特定数量的字符
print(random.sample('abcdefghij', 3))

# 多个字符中选取特定数量的字符组成新字符串
new_st = random.sample(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], 3)
print(new_st)
print(list(','.join(new_st).replace(',', '')))

# 随机选取字符串
print(random.choice(['apple', 'pear', 'peach', 'orange', 'lemon']))

# 洗牌
items = [1, 2, 3, 4, 5, 6]
random.shuffle(items)
print("洗牌:", items)

# 从指定序列中随机获取k个元素作为一个片段返回，不会改变原有序列
item = [1, 2, 3, 4, 5]
lis = []
lis = random.sample(item, 2)
print(item)
print(lis)

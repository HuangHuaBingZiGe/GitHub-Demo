"""
yield :
    相当于 return 但是return一次就中断结束了

生成器  是 迭代器 的一种实现：

    所谓的协同程序就是可以运行的独立函数调用，函数可以暂停或者挂起，并在需要的时候从程序离开的地方继续或者重新开始

"""


def myGen():
    print("生成器被执行！")
    yield 1
    yield 2


print('------------------------------------')
myG = myGen()
print(next(myG))
print(next(myG))
print('------------------------------------')

for i in myGen():
    print(i)
print('------------------------------------')


def libs():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a


for each in libs():
    if each > 100:
        break
    print(each, end=' ')
print('------------------------------------')

a = [i for i in range(100) if not (i % 2) and i % 3]
print(a)
print('------------------------------------')

# 字典推导式
b = {i: i % 2 == 0 for i in range(10)}
print(b)
print('------------------------------------')

# 集合推导式，去重
c = {i for i in [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 3, 2, 1]}
print(c)
print('------------------------------------')

d = " I love fish"
print(d)
print('------------------------------------')

# 生成器推导式
e = (i for i in range(10))
print(e)
print(next(e))
for each in e:
    print(each)
print('------------------------------------')

# 生成器推导式
print(sum(i for i in range(100) if i % 2))

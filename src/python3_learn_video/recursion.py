def recursion():
    return recursion()


import sys

# 设置递归层数
sys.setrecursionlimit(10)

"""
递归求阶乘：
    ——写一个求阶乘的函数
        ——正整数阶乘指从1乘以2乘以3乘以4一直乘到所要求的数
        ——例如所给的数是5，则阶乘式是1*2*3*4*5，得到的积是120，所以120就是4的阶乘


print('---------------------------------------------')
def factorial(n):
    result = n
    for i in range(1,n):
        result *= i
    return result

number = int(input('请输入一个正整数：'))
result = factorial(number)
print("%d 的阶乘是：%d" % (number,result))
print('---------------------------------------------')


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
number = int(input('请输入一个正整数：'))
result = factorial(number)
print("%d 的阶乘是：%d" % (number,result))
print('---------------------------------------------')
"""

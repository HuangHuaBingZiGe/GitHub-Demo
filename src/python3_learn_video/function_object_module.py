"""
函数：Python的乐高积木
"""

print('------------------------------------')

"""
def MyFirstFunction():
    print('这是我创建的第一个函数！')
    print('我表示很激动。。。')
    print('在此，我要感谢TVB，感谢CCTV，感谢各位鱼友。')
    print('------------------------------------')

MyFirstFunction()
"""


def MySecondFunction(name):
    print(name + '我爱你！')
    print('------------------------------------')


MySecondFunction('小甲鱼')


def add(num1, num2):
    result = num1 + num2
    print(result)
    print('------------------------------------')


add(1, 2)


# 函数的返回值

def add(num1, num2):
    return (num1 + num2)


print(add(5, 6))
print('------------------------------------')


# 形参 和 实参
# 形式参数（parameter）、实际参数（argument）

def MyFirstFunction(name):
    '函数定义过程中的name是叫形参'
    # 因为Ta只是一个形式，表示占据一个参数位置
    print('传递进来的' + name + '叫做实参，因为Ta是具体的参数值！')
    print('------------------------------------')


MyFirstFunction('小鲫鱼')

# 函数文档
print(MyFirstFunction.__doc__)
print('------------------------------------')
print(help(MyFirstFunction))
print('------------------------------------')
print(help(print))
print('------------------------------------')


# 关键字参数

def SaySome(name, words):
    print(name + '->' + words)
    print('------------------------------------')


SaySome('小甲鱼', '让编程改变世界！')
SaySome(words='小甲鱼', name='让编程改变世界！')


# 默认参数

def SaySome(name='小甲鱼', words='让编程改变世界!'):
    print(name + '->' + words)
    print('------------------------------------')


SaySome()
SaySome('苍井空')
SaySome('苍井空', '你好')


# 收集参数（可变参数）
def test(*params):
    print('参数的长度是：', len(params))
    print('第二个参数是：', params[1])
    print('------------------------------------')


test(1, '小甲鱼', 3.14, 6, 7, 89)


def test(*params, exp=8):
    print('参数的长度是：', len(params), exp)
    print('第二个参数是：', params[1])


test(1, '小甲鱼', 3.14, 6, 7, 89, 10)

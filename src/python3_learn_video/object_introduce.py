"""
对象 = 属性 + 方法
"""


class Turtle:  # Python 中的类名约定以大写字母开头
    """关于类的一个简单例子"""
    # 属性
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'
    
    # 方法
    def climb(self):
        print('我正在很努力的向前爬....')
    
    def run(self):
        print('我正在快速的向前跑.....')
    
    def bite(self):
        print('咬你......')
    
    def eat(self):
        print('有的吃......')
    
    def sleep(self):
        print('困了，睡了......')


"""
tt = Turtle
print(tt)
tt1 = Turtle()
print(tt1)
tt.bite('')
"""

# 面向对象特性1：封装

print('------------------------------------------')
list1 = [2, 1, 7, 5, 3]
list1.sort()
print(list1)
list1.append(9)
print(list1)
print('------------------------------------------')


# 面向对象特性2：继承
# 子类自动共享父类之间数据和方法的机制

class MyList(list):
    pass


list2 = MyList()
list2.append(5)
list2.append(3)
list2.append(7)
print(list2)
list2.sort()
print(list2)
print('------------------------------------------')


# 面向对象特性3：多态

class A:
    def fun(self):
        print('我是小A...')


class B:
    def fun(self):
        print('我是小B...')


a = A()
b = B()
a.fun()
b.fun()
print('------------------------------------------')

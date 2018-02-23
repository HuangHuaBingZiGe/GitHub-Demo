# 函数（function）：有返回值

# 过程（procedure）：是简单的、特殊的、没有返回值的

print('-------------------------------------')


def hello():
    print('Hello FishC!')
    print('-------------------------------------')


temp = hello()
print(temp)
print(type(temp))
print('-------------------------------------')


# 再谈谈返回值
def back():
    return 1, '小甲鱼', 3.14


print(back())
print('-------------------------------------')


# 局部变量 （Local Variable）
# 全局变量 （Global Variable）

def discounts(price, rate):
    final_price = price * rate
    # print('这里试图打印全局变量old_price的值：',old_price)
    old_price = 50
    print('修改后old_price的值是1：', old_price)
    return final_price


old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = discounts(old_price, rate)
print('打折后的价格是：', new_price)
print('修改后old_price的值是2：', old_price)
print('-------------------------------------')

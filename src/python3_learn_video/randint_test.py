import random

secret = random.randint(1, 10)
print(secret)
print('--------------------------------')
temp = input("不妨猜一下小甲鱼心里想的是哪个数字？")
guess = int(temp)
while guess != secret:
    temp = input("不妨猜一下小甲鱼心里想的是哪个数字？")
    guess = int(temp)
    if guess == secret:
        print("猜对了")
    else:
        if guess > secret:
            print('大了')
        else:
            print('小了')
print('游戏结束')

print('--------------------------------')
temp = input("不妨猜一下小甲鱼心里想的是哪个数字？")
guess = int(temp)
if guess == 8:
    print("猜对了")
else:
    if guess > 8:
        print('大了')
    else:
        print('小了')
print('游戏结束')

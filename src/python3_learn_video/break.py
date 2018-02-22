bingo = '小甲鱼是帅哥'
answer = input('请输入小甲鱼最想听的一句话：')

while True:
    if answer == bingo:
        # 跳出本次循环
        break
    answer = input('抱歉，错了，请重新输入（答案正确才能退出游戏）：')

print('哎呦，帅')
print('您真是小甲鱼肚子里的蛔虫')

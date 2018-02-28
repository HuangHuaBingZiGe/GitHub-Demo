"""
def showMaxFactor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print('%d最大的约数是%d' %(num,count))
            break
        count -= 1
    else:
        print('%d是素数!' % num)
    
num = int(input('请输入一个数：'))
showMaxFactor(num)
"""

print('------------------------------------------')
try:
    print(int('abc'))
except ValueError as reason:
    print('出错啦：' + str(reason))
else:
    print('没有任何异常！')

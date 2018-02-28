"""
try:
    检测范围
except Exception[as reason]:
    出现异常 （Exception） 后的处理代码
finally:
    无论如何都会被执行的代码

"""

print('---------------------------------------------')
try:
    f = open('我为什么是一个文件.txt', 'w')
    print(f.write('我存在了!'))
    sum = 1 + '1'
except (OSError, TypeError):
    print('出错了！')
finally:
    f.close()
print('---------------------------------------------')

raise ZeroDivisionError('除数为零的异常')

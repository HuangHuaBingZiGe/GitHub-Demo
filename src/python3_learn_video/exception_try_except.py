"""
file_name = input('请输入需要打开的文件名：')
f = open(file_name)
print('文件的内容是：')
for each_line in f:
    print(each_line)
f.close()
"""

print('----------------------------------------------')
my_list = ['小甲鱼是帅哥']
# print(len(my_list))
assert len(my_list) > 0  # False 抛出异常

"""
try-except语句

try:
    检测范围
except Exception[as reason]:
    出现异常 （Exception） 后的处理代码

"""

try:
    f = open('我为什么是一个文件.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错了!\n错误的原因是：' + str(reason))
print('----------------------------------------------')

try:
    sum = 1 + '1'
    f = open('我为什么是一个文件.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错了!\n错误的原因是：' + str(reason))
except TypeError as reason:
    print('类型出错了!\n错误的原因是：' + str(reason))
print('----------------------------------------------')

try:
    int('abc')
    sum = 1 + '1'
    f = open('我为什么是一个文件.txt')
    print(f.read())
    f.close()
except:
    print('出错了！')
print('----------------------------------------------')

try:
    sum = 1 + '1'
    f = open('我为什么是一个文件.txt')
    print(f.read())
    f.close()
except (OSError, TypeError):
    print('出错了!')
print('----------------------------------------------')

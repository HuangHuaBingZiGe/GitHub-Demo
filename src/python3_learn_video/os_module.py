"""
模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py
模块可以被别的程序引入，以使用该模块中的函数等功能

OS：Operation  System  操作系统
"""

import os

print('-------------------------------')
print(os.getcwd())  # 获取当前的目录位置

print('-------------------------------')
os.chdir('E:\\')  # 改变当前目录位置
print(os.getcwd())
print('-------------------------------')

print(os.listdir('E:\\'))  # 打印当前目录下包含的文件和文件夹
print('-------------------------------')

# os.mkdir('E:\\A')  # 创建文件夹
# os.mkdir('E:\\A\\B') # 创建已存在的级联文件夹
# os.makedirs('E:\\B\\C') # 创建级联文件夹
# os.makedirs('E:\\B\\A') # 创建级联文件夹

# os.system('cmd') # 打开cmd
# os.system('calc') # 打开计算器

print(os.curdir)  # 当前路径
print(os.listdir(os.curdir))  # 查看当前路径下的文件和文件夹
print('-------------------------------')

print(os.path.basename('E:\\oracle\\hosts'))  # 去除路径返回文件名
print('-------------------------------')

print(os.path.dirname('E:\\oracle\\hosts'))  # 去除文件名返回路径
print('-------------------------------')

print(os.path.join('A', 'B', 'C'))
print(os.path.join(r'C:\\', 'A', 'B', 'C'))
print(os.path.split('E:\\A\\SEXY.AVI'))
print(os.path.split('E:\\A\\B\\C'))
print('-------------------------------')

print(os.path.splitext('E:\\A\\SEXY.AVI'))  # 获取后缀
print('-------------------------------')

print(os.path.getatime('E:\\test.txt'))
import time

print(time.gmtime(os.path.getatime('E:\\test.txt')))
print('-------------------------------')
print(time.localtime(os.path.getatime('E:\\test.txt')))
print('-------------------------------')
print(time.localtime(os.path.getmtime('E:\\test.txt')))
print('-------------------------------')

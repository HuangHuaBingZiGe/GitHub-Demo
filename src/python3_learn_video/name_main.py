"""
__name__ 和 __main__的关系：
    当作为整个模块导入时，__name__ 不等于 __main__

print('------------------------------------------------')
print(__name__)

import TemperatureConversion as tc
print(tc.__name__)
print('------------------------------------------------')

"""

"""
搜索路径：

print('------------------------------------------------')
import sys
print(sys.path)
print('------------------------------------------------')
sys.path.append("C:\\Program Files\\Python35\\test")
print(sys.path)
print('------------------------------------------------')
import TemperatureConversion
print('------------------------------------------------')
"""

"""
包（package）：
    1.创建一个文件夹，用于存放相关的模块，文件夹的名字即包的名字
    2.在文件夹中创建一个__init__.py的模块文件，内容可以为空

print('------------------------------------------------')
import sys
sys.path.append("C:\\Program Files\\Python35\\test")
import calc
print('------------------------------------------------')

"""

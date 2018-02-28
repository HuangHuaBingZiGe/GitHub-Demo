"""
pickle：泡菜

数据类型和二进制数据之间的转换工具

"""

import pickle

print('--------------------------------------------------')
my_list = [123, 3.14, '小甲鱼', ['another list']]
pickle_file = open('wyz.pkl', 'wb')  # 二进制的写入形式
pickle.dump(my_list, pickle_file)
pickle_file.close()

pickle_file = open('wyz.pkl', 'rb')
my_list2 = pickle.load(pickle_file)
print(my_list2)
print('--------------------------------------------------')

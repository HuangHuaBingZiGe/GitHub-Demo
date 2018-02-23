str1 = 'I love fishrc.com'
print('-------------------------------------------')
print(str1[:6])
print(str1[:6] + '插入的字符串' + str1[6:])

# 首字母改为大写
str2 = 'xiaoxie'
print(str2.capitalize())

# 将所有大写字符改为小写
str2 = 'DAXIExiaoxie'
print(str2.casefold())

# 左边和右边填充，内容居中
print(str2.center(40))

# 统计出现次数
print(str2)
print(str2.count('xi'))

# 是否以什么结束
print(str2.endswith('xi'))

# 将tab键变为8个空格
str3 = 'I\tlove\tfishC.com!'
print(str3.expandtabs())

# 以字符串作为分隔符
print(str2.join('12345'))
print(dir(str))

# 转换字符
print(str2.translate(str.maketrans('s', 'b')))
print(str.maketrans('s', 'b'))

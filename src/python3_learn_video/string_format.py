print('--------------------------------------------')
# 位置参数 {0} {1} {2}
print("{0} love {1}.{2}".format("I", "FishC", "com"))
print("{} love {}.{}".format("I", "FishC", "com"))

# 关键字参数
print("{a} love {b}.{c}".format(a="I", b="FishC", c="com"))
print("{0} love {b}.{c}".format("I", b="FishC", c="com"))

print('\ta')
print('\\')
print("{{0}}".format("不打印"))
print('{0:.1f}{1}'.format(27.657, 'GB'))

# 格式化字符及其ASCII码
print('%c' % 97)

print('%c %c %c' % (97, 98, 99))

# 格式化字符串
print('%s' % 'I love FishC.com')

# 格式化整数
print('%d + %d = %d' % (4, 5, 4 + 5))

# 格式化无符号八进制数
print('%o' % 10)

# 格式化无符号十六进制数
print('%x' % 10)

# 格式化无符号十六进制数（大写）
print('%X' % 10)
print('%X' % 160)

# 格式化定点数，可指定小数点后的精度
print('%f' % 27.658)

# 用科学计数法格式化定点数
print('%e' % 27.658)

# 作用同 %e，用科学计数法格式化浮点数
print('%E' % 27.658)

# 根据值的大小决定使用 %f 或 %e
print('%g' % 27.658)

# 格式化操作符辅助命令，5表示占多少位
print('%5.1f' % 27.658)

print('%.2e' % 27.658)

# 10表示占位10个
print('%10d' % 5)

# - 表示左对齐
print('%-10d' % 5)

# + 表示整数的前面显示 + 号
print('%+d' % 5)
print('%+d' % -5)

# o表示以八进制显示
print('%#o' % 10)

# X表示以十六进制显示
print('%#X' % 108)

# 以十进制显示
print('%#d' % 10)

# 以 0 填充，取代空格
print('%010d' % 5)

print('%-010d' % 5)

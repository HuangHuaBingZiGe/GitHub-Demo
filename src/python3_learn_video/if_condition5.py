# 三元操作符

x, y = 4, 3

if x < y:
    small = x
else:
    small = y

# 等价于

small = x if x < y else y
print(small)

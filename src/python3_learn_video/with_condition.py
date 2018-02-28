#  会报错   not readable
"""
try:
    f = open('data.txt','w')
    for each_line in f:
        print(each_line)
except OSError as reason:
    print('出错啦：' + str(reason))
finally:
    f.close()
"""

print('--------------------------------------------')
try:
    with open('data.txt', 'w') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print('出错啦：' + str(reason))

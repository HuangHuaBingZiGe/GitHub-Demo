f = open('E:\\a.txt')
print(f)
print(f.read(5))
print(f.tell())
print(f.seek(45, 0))
print(f.readline())
print(list(f))
f.seek(0, 0)

lines = list(f)
for each_line in lines:
    print(each_line)

f.seek(0, 0)
for each_line in f:
    print(each_line)

f = open('E:\\test.txt', 'w')
f.write('I love fish')
f.close()

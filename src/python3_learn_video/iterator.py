"""
迭代器：

iter()          __iter__()
next()          __next__()

"""

print('-----------------------------------------------')
for i in "FishC":
    print(i)
print('-----------------------------------------------')

links = {'鱼C工作室': 'http://www.fishc.com', \
         '鱼C论坛': 'http://bbs.fishc.com', \
         '鱼C博客': 'http://blog.fishc.com', \
         '支持小甲鱼': 'http://fishc.taobao.com'
         }
for each in links:
    print("%s -> %s" % (each, links[each]))
print('-----------------------------------------------')

string = "FishC"
it = iter(string)
print(next(it))
print(next(it))
print('-----------------------------------------------')

string = "FishC"
it = iter(string)
while True:
    try:
        each = next(it)
    except StopIteration:
        break
    print(each)
print('-----------------------------------------------')

for each in string:
    print(each)
print('-----------------------------------------------')


class Fibs:
    def __init__(self, n=10):
        self.a = 0
        self.b = 1
        self.n = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.n:
            raise StopIteration
        return self.a


fibs = Fibs(100)
for each in fibs:
    print(each)
print('-----------------------------------------------')

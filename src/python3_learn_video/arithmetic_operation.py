print('---------------------------------------------')
print(type(len))
print(type(dir))
print('---------------------------------------------')
print(type(int))
print(type(list))
"""
工厂函数 就是 类对象
"""
print('---------------------------------------------')


class C:
    pass


print(type(C))
print('---------------------------------------------')
a = int('123')
print(a)
b = int('456')
print(a + b)
print('---------------------------------------------')


class New_int(int):
    def __add__(self, other):
        return int.__sub__(self, other)
    
    def __sub__(self, other):
        return int.__add__(self, other)


a = New_int(3)
b = New_int(5)
print(a + b)
print('---------------------------------------------')


class Try_int(int):
    def __add__(self, other):
        return int(self) + int(other)
    
    def __sub__(self, other):
        return int(self) + int(other)


a = Try_int(3)
b = Try_int(5)
print(a + b)
print('---------------------------------------------')


class int(int):
    def __add__(self, other):
        return int.__sub__(self, other)


a = int('5')
print(a)
print('---------------------------------------------')
b = int(3)
print(a + b)
print('---------------------------------------------')


class Nint(int):
    def __radd__(self, other):
        return int.__sub__(self, other)


a = Nint(5)
b = Nint(3)
print(a + b)
print('---------------------------------------------')


class Nint(int):
    def __rsub__(self, other):
        return int.__sub__(other, self)


a = Nint(5)
print(3 - a)
print('---------------------------------------------')

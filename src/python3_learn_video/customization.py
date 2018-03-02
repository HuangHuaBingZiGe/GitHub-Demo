"""
简单定制：

基本要求：
--定制一个计时器的类
--start和stop方法代表启动计时和停止计时
--假设计时器对象t1，print（t1）和直接调用t1均显示结果
--当计时器未启动或已经停止计时，调用stop方法会给予温馨的提示
--两个计时器对象可以进行相加：t1 + t2
--只能使用提供的有限资源完成


需要的资源：
--使用time模块的localtime方法获取时间
    --扩展阅读：time模块详解（时间获取 或 转换）
--time.localtime返回struct_time的时间格式
--表现你的类：__str__ 和 __repr__

"""


class A():
    def __str__(self):
        return "小甲鱼是帅哥！"


print("--------------------------------")
a = A()
print(a)
print("--------------------------------")


class B():
    def __repr__(self):
        return "小甲鱼是帅哥！"


b = B()
print(b)
print("--------------------------------")

import time as t


class MyTimer():
    def __init__(self):
        self.unit = ['年', '月', '天', '小时', '分钟', '秒']
        self.prompt = "未开始计时！"
        self.lasted = []
        self.begin = 0
        self.end = 0
    
    def __str__(self):
        return self.prompt
    
    __repr__ = __str__
    
    def __add__(self, other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt
    
    # 开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示，请先调用 stop() 停止计时!"
        print("计时开始...")
        
        # 停止计时
    
    def stop(self):
        if not self.begin:
            print("提示，请先调用 start() 进行计时！")
        else:
            self.end = t.localtime()
            self._calc()
            print("计时结束！")
    
    # 内部方法，计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
        # 为下一轮计时初始化变量
        self.begin = 0
        self.end = 0


"""
t1 = MyTimer()
t1.start()
t1.stop()
print(t1)
print("--------------------------------")
"""

t1 = MyTimer()
t1.start()
print("--------------------------------")
print("--------------------------------")
print("--------------------------------")
t1.stop()
t1
print("--------------------------------")
t2 = MyTimer()
t2.start()
print("--------------------------------")
print("--------------------------------")
print("--------------------------------")
t2.stop()
t2
print(t1 + t2)
print("--------------------------------")

"""
进阶定制：

--如果开始计时的时间是 2022年2月22日16:30:30，停止时间是 2025年1月23日15:30:30，那按照我们用停止时间减开始时间的计算方式就会出现负数 3年-1月1天-1小时，你应该对此做一些转换

--现在的计算机速度都非常快，而我们这个程序最小的计算单位却只是秒，精度是远远不够的

"""

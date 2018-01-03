#!/usr/bin/python
# -*- coding: utf-8 -*-


"""

50个话题
9章
1.课程简介
2.数据结构相关话题
3.迭代器与生成器相关话题
4.字符串处理相关话题
5.文件I/O操作相关话题
6.数据编码与处理相关话题
7.类与对象相关话题
8.多线程与多进程相关话题
9.装饰器相关话题
"""

"""
第1章 课程简介
    1-1 课程简介
    1-2 在线编码工具WebIDE使用指南
    
第2章 数据结构与算法进阶训练
    2-1 如何在列表, 字典, 集合中根据条件筛选数据
    2-2 如何为元组中的每个元素命名, 提高程序可读性
    2-3 如何统计序列中元素的出现频度
    2-4 如何根据字典中值的大小, 对字典中的项排序
    2-5 如何快速找到多个字典中的公共键(key)
    2-6 如何让字典保持有序
    2-7 如何实现用户的历史记录功能(最多n条)
    
第3章 对象迭代与反迭代技巧训练
    3-1 如何实现可迭代对象和迭代器对象(1)
    3-2 如何实现可迭代对象和迭代器对象(2)
    3-3 如何使用生成器函数实现可迭代对象
    3-4 如何进行反向迭代以及如何实现反向迭代
    3-5 如何对迭代器做切片操作
    3-6 如何在一个for语句中迭代多个可迭代对象

第4章 字符串处理技巧训练
    4-1 如何拆分含有多种分隔符的字符串
    4-2 如何判断字符串a是否以字符串b开头或结尾
    4-3 如何调整字符串中文本的格式
    4-4 如何将多个小字符串拼接成一个大的字符串
    4-5 如何对字符串进行左, 右, 居中对齐
    4-6 如何去掉字符串中不需要的字符
    
第5章 文件I/O高效处理技巧训练
    5-1 如何读写文本文件
    5-2 如何处理二进制文件
    5-3 如何设置文件的缓冲
    5-4 如何将文件映射到内存
    5-5 如何访问文件的状态
    5-6 如何使用临时文件
    
第6章 csv，json，xml,excel高效解析与构建技巧训练
    6-1 如何读写csv数据
    6-2 如何读写json数据
    6-3 如何解析简单的xml文档
    6-4 如何构建xml文档
    6-5 如何读写excel文件

第7章 类与对象深度技术进阶训练
    7-1 如何派生内置不可变类型并修改实例化行为
    7-2 如何为创建大量实例节省内存
    7-3 如何让对象支持上下文管理
    7-4 如何创建可管理的对象属性
    7-5 如何让类支持比较操作
    7-6 如何使用描述符对实例属性做类型检查
    7-7 如何在环状数据结构中管理内存
    7-8 如何通过实例方法名字的字符串调用方法

第8章 多线程编程核心技术应用进阶训练
    8-1 如何使用多线程
    8-2 如何线程间通信
    8-3 如何在线程间进行事件通知
    8-4 如何使用线程本地数据
    8-5 如何使用线程池
    8-6 如何使用多进程
    
第9章 装饰器使用技巧进阶训练
    9-1 如何使用函数装饰器
    9-2 如何为被装饰的函数保存元数据
    9-3 如何定义带参数的装饰器
    9-4 如何实现属性可修改的函数装饰器
    9-5 如何在类中定义装饰器
    
"""

"""
6-1 如何读写csv数据

实际案例：
http://table.finance.yahoo.com/table.csv?s=000001.sz我们可以通过雅虎网站获取了中国股市（深市）数据集，它以csv数据格式存储:

Date,Open,High,Low,Close,Volume,Adj Close
2016-06-30,8.69,8.74,8.66,8.70,36220400,8.70
2016-06-29,8.63,8.69,8.62,8.69,36961100,8.69
2016-06-28,8.58,8.64,8.56,8.63,33651900,8.63

请将平安银行这支股票，在2016奶奶中成交量超过50000000的纪录存储到另一个csv文件中

解决方案：
使用标准库中的csv模块，可以使用其中reader和writer完成csv文件读写

"""
'''
urllib.request.urlretrieve("http://table.finance.yahoo.com/table.csv?s=000001.sz",'pingan.csv')

cat pingan.csv | less
'''

"""
# 使用二进制打开
# 有问题，其实csv文件不是二进制文件
rf = open(file_name,'rb')
reader = csv.reader(rf)
print(reader)
for row in reader:
    print(row)
"""

'''
file = 'test.csv'
file_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + \
            '\\' + 'docs' + '\\' + 'csv' +  '\\' + file

file_copy = 'pingan_copy.csv'
file_name_copy = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + \
            '\\' + 'docs' + '\\' + 'csv' +  '\\' + file_copy

with open(file_name,"rt",encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
    print(rows)

wf = open(file_name_copy,'w')
writer = csv.writer(wf)
writer.writerow(['Date','Open','High','Low','Close','Volume','Adj Close'])
writer.writerow(['Date','Open','High','Low','Close','Volume','Adj Close'])
wf.flush()

print("-----最好的方法-----")
print("python2和python3的csv.reader.next的方法有所区别")

file_copy_2 = 'pingan2.csv'
file_name_copy2 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + \
            '\\' + 'docs' + '\\' + 'csv' +  '\\' + file_copy_2

with open(file_name,'r') as rf:
    reader = csv.reader(rf)
    with open(file_name_copy2,'w') as wf:
        writer = csv.writer(wf)
        headers = next(reader)
        writer.writerow(headers)
        for row in reader:
            #if row[0] < '2016-01-01':
                #break
            if int(row[5]) > 36961100:
                writer.writerow(row)
print("end")
'''

'''
6-2 如何读写json数据

实际案例：
在web应用中常用JSON（JavaScript Object Notation）格式传输数据，例如我们利用Baidu语音识别服务做语音识别，将本地音频数据post到Baidu语音识别服务器，服务器响应结果为json字符串

{"corpus_no":"6303355448008565863","err_msg":"success.","err_no":0,"result":["你好 ,"],"sn":"418359718861467614305"}

在python中如何读写json数据？

解决方案：
使用标准库中的json模块，其中loads，dumps函数可以完成json数据的读写

'''

'''
#coding:utf-8
import requests
import json

# 录音
from record import Record
record = Record(channels=1)
audioData = record.record(2)

# 获取token
from secret import API_KEY,SECRET_KEY
authUrl = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + API_KEY + "&client_secret=" + SECRET_KEY
response = requests.get(authUrl)
res = json.loads(response.content)
token = res['access_token']

# 语音识别
cuid = 'xxxxxxxxxxx'
srvUrl = 'http://vop.baidu.com/server_api' + '?cuid=' + cuid + '&token=' + token
httpHeader = {
    'Content-Type':'audio/wav; rate = 8000',
}
response = requests.post(srvUrl,headers=httpHeader,data=audioData)
res = json.loads(response.content)
text = res['result'][0]

print(u'\n识别结果:')
print(text)

'''

'''
# dumps将python对象转换为json的字符串
l = [1,2,'abc',{'name': 'Bob','age':13}]
print(json.dumps(l))

d = {'b':None,'a':5,'c':'abc'}
print(json.dumps(d))

# 将逗号后的空格和冒号后的空格删除，将空格压缩掉
print(json.dumps(l,separators=[',', ':']))

# 对输出的字典中的键进行排序
print(json.dumps(d,sort_keys=True))

# 把json字符串转换为python对象
l2 = json.loads('[1,2,"abc",{"name": "Bob","age":13}]')
print(type(l2))

d2 = json.loads('{"b":null,"a":5,"c":"abc"}')
print(type(d2))
'''

'''
file = 'demo.json'
file_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + \
            '\\' + 'docs' + '\\' + 'json' +  '\\' + file

l = [1,2,'abc',{'name': 'Bob','age':13}]

# 将json写入文件当中，dump和load同理
with open(file_name,'w') as f:
    json.dump(l,f)
'''

'''
6-3 如何解析简单的xml文档

实际案例：
    xml是一种十分常用的标记性语言，可提供统一的方法来描述应用程序的结构化数据：
    
<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
</data>

python中如何解析xml文档？

解决方案：
    使用标准库中的xml.etree.ElementTree,其中的parse函数可以解析xml文档
    

from xml.etree.ElementTree import parse
import os

file = 'demo.xml'
file_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + \
            '\\' + 'docs' + '\\' + 'xml' +  '\\' + file

f = open(file_name)
et = parse(f)
print(et)
root = et.getroot()
print(root)
print(root.tag)
print(root.attrib)
print(root.text)
print(root.text.strip())
print(root.getchildren())
for child in root:
    print(child.get('name'))
print(root.find('country'))
print(root.findall('country'))
print(root.iterfind('country'))
for e in root.iterfind('country'):
    print(e.get('name'))
print(root.findall('rank')) # 找不到非子元素
print(root.iter())
print(list(root.iter()))
print(list(root.iter('rank')))
print(root.findall('country/*')) # *表示匹配孙子节点
print(root.findall('rank')) # 直接查找子元素
print(root.findall('.//rank')) # //表示查找所有层次
print(root.findall('.//rank/..')) # ..表示查找rank的所有父节点
print(root.findall('country[@name]')) # 查找包含name属性的country
print(root.findall('country[@name="Singapore"]'))#查找属性等于特定值的
print(root.findall('country[rank]'))# 查找包含rank的country
print(root.findall('country[rank="5"]'))
print(root.findall('country[1]')) #查找序号为1的country
print(root.findall('country[2]'))
print(root.findall('country[last()]')) #找最后一个country标签
print(root.findall('country[last()-1]')) #找倒数第二个

'''

'''
6-4 如何构建xml文档

实际案例：
    某些时候，我们需要将其他格式数据转换为xml
    例如，我们要把平安股票csv文件，转换成相应的xml,

test.csv
Date,Open,High,Low,Close,Volume,Adj Close
2016/6/1,8.69,8.74,8.66,8.7,36220400,8.7

pingan.xml
<Data>
    <Row>
        <Date>2016-07-05</Date>
        <Open>8.80</Open>
        <High>8.83</High>
        <Low>8.77</Low>
        <Close>8.81</Close>
        <Volume>42203700</Volume>
        <AdjClose>8.81</AdjClose>
    </Row>
</Data>

解决方案：
    使用标准库中的xml.etree.ElementTree，构建ElementTree，使用write方法写入文件


from xml.etree.ElementTree import Element,ElementTree

e = Element('Data') # tag名字 Data 创建元素
print(e.tag)
print(e.set('name','abc')) # 设置Data的属性

from xml.etree.ElementTree import tostring

print(tostring(e))

e.text='123'
print(tostring(e))

e2 = Element('Row') #创建子元素
e3 = Element('Open')
e3.text='8.80'
e2.append(e3)
print(tostring(e2))

e.text = None
e.append(e2)
print(tostring(e))

import os
file = 'demo1.xml'
file_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + \
            '\\' + 'docs' + '\\' + 'xml' +  '\\' + file

et = ElementTree(e)
et.write(file_name)

'''

'''
import csv
from xml.etree.cElementTree import Element,ElementTree
import os

file = 'pingan.csv'
file_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + \
            '\\' + 'docs' + '\\' + 'csv' +  '\\' + file

file1 = 'pingan.xml'
file_name1 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + \
            '\\' + 'docs' + '\\' + 'xml' +  '\\' + file1

def xml_pretty(e,level=0):
    if len(e) > 0:
        e.text = '\n' + '\t' * (level + 1)
        for child in e:
            xml_pretty(child,level + 1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level

def csvToXml(fname):
    with open(fname,'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        
        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag,text in zip(headers,row):
                e = Element(tag)
                e.text = text
                eRow.append(e)
    
    xml_pretty(root)
    return ElementTree(root)
        
et = csvToXml(file_name)
et.write(file_name1)

'''

'''
6-5 如何读写excel文件

实际案例：
    Microsoft Excel是日常办公中使用最频繁的软件，其数据格式为xls、xlsx，一种非常常用的电子表格，小学某班成绩，记录在excel文件中
    
姓名      语文      数学      外语
李雷      95         99       96
韩梅      98         100      93
张峰      94         95       95

利用python读写excel，添加“总分”列，计算每人的总分

解决方案：
    使用pip安装， $ pip install xlrd xlwt
    使用第三方库xlrd和xlwt，这两个库分别用于excel读和写
'''

'''
import xlrd
import os

file = 'sum_point.xlsx'
file_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + \
            '\\' + 'docs' + '\\' + 'excel' +  '\\' + file

book = xlrd.open_workbook(file_name)
print(book.sheets())
sheet = book.sheet_by_index(0)
print(sheet.nrows)
print(sheet.ncols)

cell = sheet.cell(0,0)
print(cell)

# cell.ctype 是枚举值  xlrd.XL...
print(type(cell.value))
print(cell.value)

cell2 = sheet.cell(1,1)
print(cell2)
print(type(cell2))
print(cell2.ctype)

print(sheet.row(1))
print(sheet.row_values(1))
print(sheet.row_values(1,1)) # 跳过第一个,第2个1表示从第一个开始

# sheet.put_cell  为表添加1个单元格


import xlwt

wbook  = xlwt.Workbook()
wsheet = wbook.add_sheet('sheet1')
# wsheet.write
# wbook.save('output.xlsx')

'''

'''
# 写入失败，有问题！！！！！！！！！
import os

import xlrd
import xlwt

file = 'sum_point.xlsx'
file_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + \
            '\\' + 'docs' + '\\' + 'excel' + '\\' + file

file1 = 'sum_point_copy.xlsx'
file_name1 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + \
             '\\' + 'docs' + '\\' + 'excel' + '\\' + file1

rbook = xlrd.open_workbook(file_name)
rsheet = rbook.sheet_by_index(0)

nc = rsheet.ncols
rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, u'总分', None)  # 添加总分的文字，第0行，第rsheet.ncols列，类型，文本

for row in range(1, rsheet.nrows):  # 第1行开始，跳过第0列
    t = sum(rsheet.row_values(row, 1))
    rsheet.put_cell(row, nc, xlrd.XL_CELL_NUMBER, t, None)

wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)
style = xlwt.easyxf('align:vertical center,horizontal center')

for r in range(rsheet.nrows):
    for c in range(rsheet.ncols):
        wsheet.write(r, c, rsheet.cell_value(r, c), style)

wbook.save(u'output.xlsx')
'''

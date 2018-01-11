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
8-1 如何使用多线程

python只适合处理IO密集型操作, 不能达到真正意义上的多线程操作

实际案例：
    http://table.finance.yahoo.com/table.csv?s=000001.sz我们通过雅虎网站获取了中国股市某支股票csv数据文件，现在要下载多只股票的csv数据，并将其转换为xml文件
    
如何使用线程来提高下载并处理的效率？

解决方案：
    使用标准库threading.Thread创建线程，在每一个线程中下载并转换一只股票数据

"""

'''
import csv
from xml.etree.ElementTree import Element,ElementTree
import requests
from io import StringIO

def download(url):
    response = requests.get(url,timeout=3)
    if response.ok:
        # 可支持文件操作的内存对象
        return StringIO(response.content)

def xml_pretty(e,level=0):
    if len(e) > 0:
        e.text = '\n' + '\t' * (level + 1)
        for child in e:
            xml_pretty(child,level + 1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level

def csvToXml(scsv,fxml):
    reader = csv.reader(scsv)
    headers = reader.next()
    headers = map(lambda h:h.replace(' ',''),headers)
    
    root = Element('Data')
    for row in reader:
        eRow = Element('Row')
        root.append(eRow)
        for tag,text in zip(headers,row):
            e = Element(tag)
            e.text = text
            eRow.append(e)
            
    xml_pretty(root)
    et = Element(root)
    et.write(fxml)
    
if __name__ == '__main__':
    url = 'http://table.finance.yahoo.com/table.csv?s=000001.sz'
    rf = download(url)
    if rf:
        with open('000001.xml','w') as wf:
            csvToXml(rf,wf)
'''

'''
import csv
from xml.etree.ElementTree import Element,ElementTree
import requests
from io import StringIO

def download(url):
    response = requests.get(url,timeout=3)
    if response.ok:
        # 可支持文件操作的内存对象
        return StringIO(response.content)

def xml_pretty(e,level=0):
    if len(e) > 0:
        e.text = '\n' + '\t' * (level + 1)
        for child in e:
            xml_pretty(child,level + 1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level

def csvToXml(scsv,fxml):
    reader = csv.reader(scsv)
    headers = reader.next()
    headers = map(lambda h:h.replace(' ',''),headers)

    root = Element('Data')
    for row in reader:
        eRow = Element('Row')
        root.append(eRow)
        for tag,text in zip(headers,row):
            e = Element(tag)
            e.text = text
            eRow.append(e)

    xml_pretty(root)
    et = Element(root)
    et.write(fxml)

if __name__ == '__main__':
    for sid in range(1,11):
        print('Download...(%d)' % sid)
        url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
        url %= str(sid).rjust(6,'0')
        rf = download(url)
        if rf is None:continue
        
        print('Convert to XML...(%d)' % sid)
        fname = str(sid).rjust(6,'0') + '.xml'
        with open(fname,'w')as wf:
            csvToXml(rf,wf)
'''

'''
import csv
from xml.etree.ElementTree import Element,ElementTree
import requests
from io import StringIO

def download(url):
    response = requests.get(url,timeout=3)
    if response.ok:
        # 可支持文件操作的内存对象
        return StringIO(response.content)

def xml_pretty(e,level=0):
    if len(e) > 0:
        e.text = '\n' + '\t' * (level + 1)
        for child in e:
            xml_pretty(child,level + 1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level

def csvToXml(scsv,fxml):
    reader = csv.reader(scsv)
    headers = reader.next()
    headers = map(lambda h:h.replace(' ',''),headers)

    root = Element('Data')
    for row in reader:
        eRow = Element('Row')
        root.append(eRow)
        for tag,text in zip(headers,row):
            e = Element(tag)
            e.text = text
            eRow.append(e)

    xml_pretty(root)
    et = Element(root)
    et.write(fxml)
    
def handle(sid):
    print('Download...(%d)' % sid)
    url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
    url %= str(sid).rjust(6, '0')
    rf = download(url)
    if rf is None: return
    
    print('Convert to XML...(%d)' % sid)
    fname = str(sid).rjust(6, '0') + '.xml'
    with open(fname, 'w')as wf:
        csvToXml(rf, wf)

from threading import Thread

# t = Thread(target=handle,args=(1,))
# t.start()
# print('main thread')

class MyThread(Thread):
    def __init__(self,sid):
        Thread.__init__(self)
        self.sid = sid
        
    def run(self):
        handle(self.sid)

threads = []
for i in range(1,11):
    t = MyThread(i)
    threads.append(t)
    # start会跳到run函数中
    t.start()

for t in threads:
    # 等待线程退出后再调用主函数
    t.join()

print('main Thread')
'''

"""
8-2 如何线程间通信

实际案例：
    http://table.finance.yahoo.com/table.csv?s=000001.sz我们通过雅虎网站获取了中国股市某支股票csv数据文件，现在要下载多只股票的csv数据，并将其转换为xml文件
    
    由于全局解释器锁的存在，多线程进行CPU密集型操作并不能提高执行效率，我们修改程序架构：
    
    1.使用多个DownloadThread线程进行下载（I/O操作）
    2.使用一个ConvertThread线程进行转换（CPU密集型操作）
    3.下载线程把下载数据安全地传递给转换线程
    
解决方案：
    使用标准库中Queue.Queue，它是一个线程安全的队列，Download线程把下载数据放入队列，Convert线程从队列里提取数据

"""

"""

import csv
from xml.etree.ElementTree import Element, ElementTree
import requests
from io import StringIO
from threading import Thread

# 生产者、消费者模型
from queuelib import queue
q = queue()

def xml_pretty(e, level=0):
    if len(e) > 0:
        e.text = '\n' + '\t' * (level + 1)
        for child in e:
            xml_pretty(child, level + 1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level

class DownloadThread(Thread):
    def __init__(self,sid,queue):
        Thread.__init__(self)
        self.sid = sid
        self.url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
        self.url %= str(sid).rjust(6, '0')
        self.queue = queue

    def download(self,url):
        response = requests.get(url, timeout=3)
        if response.ok:
            # 可支持文件操作的内存对象
            return StringIO(response.content)
    
    def run(self):
        print('Download',self.sid)
        # 1.下载
        data = self.download(self.url)
        # 2.把sid和data传递给convert线程
        # 加锁 lock
        self.queue.put((self.uid,data))
        
class ConvertThread(Thread):
    def __init__(self,queue):
        Thread.__init__(self)
        self.queue = queue

    def csvToXml(self,scsv, fxml):
        reader = csv.reader(scsv)
        headers = reader.next()
        headers = map(lambda h: h.replace(' ', ''), headers)
        
        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag, text in zip(headers, row):
                e = Element(tag)
                e.text = text
                eRow.append(e)
        
        xml_pretty(root)
        et = ElementTree(root)
        et.write(fxml)
        
    def run(self):
        while True:
            sid,data = self.queue.get()
            print('Convert',sid)
            if sid == -1:
                break
            if data:
                fname = str(sid).rjust(6,'0') + '.xml'
                with open(fname, 'w')as wf:
                    self.csvToXml(data, wf)
                    
q = queue()
dThreads = [DownloadThread(i,q) for i in range(1,11)]
cThread = ConvertThread(q)
for t in dThreads:
    t.start()
cThread.start()

for t in dThreads:
    t.join()
    
q.put((-1,None))
"""

"""
8-3 如何在线程间进行事件通知

实际案例：
    http://table.finance.yahoo.com/table.csv?s=000001.sz，我们通过雅虎网站获取了中国股市某支股票csv数据文件，现在要下载多只股票的csv数据，并将其转换为xml文件
    
额外需求：
    实现一个线程，将转换出的xml文件压缩打包，比如转换线程每生产出100个xml文件，就通知打包线程将它们打包成一个xxx.tgz文件，并删除xml文件，打包完成后，打包线程反过来通过转换线程，转换线程继续转换
    
解决方案：
    线程间的事件通知，可以使用标准库中Threading.Event
    1.等待事件一端调用wait，等待事件
    2.通知事件一端调用set，通知事件

"""

"""
import csv
from xml.etree.ElementTree import Element, ElementTree
import requests
from io import StringIO
from threading import Thread,Event
from queuelib import queue

def xml_pretty(e, level=0):
    if len(e) > 0:
        e.text = '\n' + '\t' * (level + 1)
        for child in e:
            xml_pretty(child, level + 1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level


class DownloadThread(Thread):
    def __init__(self, sid, queue):
        Thread.__init__(self)
        self.sid = sid
        self.url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
        self.url %= str(sid).rjust(6, '0')
        self.queue = queue
    
    def download(self, url):
        response = requests.get(url, timeout=3)
        if response.ok:
            # 可支持文件操作的内存对象
            return StringIO(response.content)
    
    def run(self):
        print('Download', self.sid)
        # 1.下载
        data = self.download(self.url)
        # 2.把sid和data传递给convert线程
        # 加锁 lock
        self.queue.put((self.uid, data))

class ConvertThread(Thread):
    def __init__(self, queue,cEvent,tEvent):
        Thread.__init__(self)
        self.queue = queue
        self.cEvent = cEvent
        self.tEvent = tEvent
    
    def csvToXml(self, scsv, fxml):
        reader = csv.reader(scsv)
        headers = reader.next()
        headers = map(lambda h: h.replace(' ', ''), headers)
        
        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag, text in zip(headers, row):
                e = Element(tag)
                e.text = text
                eRow.append(e)
        
        xml_pretty(root)
        et = ElementTree(root)
        et.write(fxml)
    
    def run(self):
        count = 0
        while True:
            sid, data = self.queue.get()
            print('Convert', sid)
            if sid == -1:
                self.cEvent.set()
                self.tEvent.wati()
                break
            if data:
                fname = str(sid).rjust(6, '0') + '.xml'
                with open(fname, 'w')as wf:
                    self.csvToXml(data, wf)
                count += 1
                if count == 5:
                    self.cEvent.set()
                    
                    self.tEvent.wait()
                    self.tEvent.clear()
                    count = 0

import tarfile
import os

class TarThread(Thread):
    def __init__(self,cEvent,tEvent):
        Thread.__init__(self)
        self.count = 0
        self.cEvent = cEvent
        self.tEvent = tEvent
        self.setDaemon(True)

    def tarXML(self):
        self.count += 1
        tfname = '%d.tgz' % self.count
        tf = tarfile.open(tfname, 'w:gz')
        for fname in os.listdir('.'):
            if tfname.endswith('.xml'):
                tf.add(fname)
                os.remove(fname)
        tf.close()
        
        if not tf.members:
            os.remove(tfname)
    
    def run(self):
        while True:
            self.cEvent.wait()
            self.tarXML()
            self.cEvent.clear()
            
            self.tEvent.set()

if __name__ == '__main__':
    q = queue()
    dThreads = [DownloadThread(i, q) for i in range(1, 11)]
    
    cEvent = Event()
    tEvent = Event()
    
    cThread = ConvertThread(q,cEvent,tEvent)
    tThread = TarThread(cEvent,tEvent)
    tThread.start()
    
    for t in dThreads:
        t.start()
    cThread.start()

    for t in dThreads:
        t.join()
    
    q.put((-1, None))
    print('main thread')
"""

"""
8-4 如何使用线程本地数据

实际案例：
    我们实现了一个web视频监控服务器，服务器端采集摄像头数据，客户端使用浏览器通过http请求接收数据，服务器使用推送的方式(multipart/x-mixed-replace)一直使用一个tcp连接向客户端传递数据，这种方式将持续占用一个线程，导致单线程服务器无法处理多客户端请求
    
改写程序，在每个线程中处理一个客户端请求，支持多客户端访问

解决方案：
    threading.local函数可以创建线程本地数据空间，其下属性对每个线程独立存在

"""

"""
import os,cv2,time,struct,threading
from socketserver import TCPServer,ThreadingTCPServer
from http.server import HTTPServer,BaseHTTPRequestHandler
from threading import Thread,RLock
from select import select

class JpegStreamer(Thread):
    def __init__(self,camera):
        Thread.__init__(self)
        self.cap = cv2.VideoCapture(camera)
        self.lock = RLock()
        self.pipes = {}
    
    def register(self):
        pr,pw = os.pipe()
        self.lock.acquire()
        self.pipes[pr] = pw
        self.lock.release()
        return pr
    
    def unregister(self,pr):
        self.lock.acquire()
        self.pipes.pop(pr)
        self.lock.release()
        pr.close()
        pw.close()
        
    def capture(self):
        cap = self.cap
        while cap.isOpened():
            ret,frame = cap.read()
            if ret:
                ret,data = cv2.imencode('.jpg',frame,(cv2.IMWRITE_JPEG_QUALITY,40))
                yield data.toString()
                
    def send(self,frame):
        n = struct.pack('l',len(frame))
        self.lock.acquire()
        if len(self.pipes):
            _,pipes,_ = select([],self.pipes.itervalues(),[],1)
            for pipe in pipes:
                os.write(pipe,n)
                os.write(pipe,frame)
        self.lock.release()
        
    def run(self):
        for frame in self.capture():
            self.send(frame)
            
class JpegRetriever(object):
    def __init__(self,streamer):
        self.streamer = streamer
        self.local = threading.local()
        
    def retriver(self):
        while True:
            ns = os.read(self.pipe,8)
            n = struct.unpack('l',ns)[0]
            data = os.read(self.local.pipe,n)
            yield data
            
    def __enter__(self):
        if hasattr(self.local,'pipe'):
            raise RuntimeError()
        
        self.pipe = streamer.register()
        return self.retriver()
            
    def __exit__(self, *args):
        self.streamer.unregister(self.local.pipe)
        del self.local.pipe
        return True
        
class Handler(BaseHTTPRequestHandler):
    retriever = None
    @staticmethod
    def setJpegRetriever(retriever):
        Handler.retriever = retriever
        
    def do_Get(self):
        if self.retriever is None:
            raise RuntimeError('no retriver')
        
        if self.path != '/':
            return
        
        self.send_response(200)
        self.send_header("Content-type",'multipart/x-mixed-replace;boundary=abcde')
        self.end_headers()
        
        with self.retriever as frames:
            for frame in frames:
                self.send_frame(frame)
            
    def send_frame(self):
        self.write.write('--abcde\r\n')
        self.write.write('Content-Type:image/jpeg\r\n')
        self.write.write('Content-Length:%d\r\n\r\n' % len(frame))
        self.write.write(frame)
        
if __name__ == '__main__':
    streamer = JpegStreamer(0)
    streamer.start()
    
    retriever = JpegRetriever(streamer)
    Handler.setJpegRetriever(retriever)
    
    print('Start server...')
    httpd = ThreadingTCPServer(('',9000),Handler)
    httpd.serve_forever()
"""

"""
8-5 如何使用线程池

实际案例：
    我们之前实现了一个多线程web视频监控服务器，我们需要对请求连接数做限制。以防止恶意用户发起大量连接而导致服务器创建大量线程，最终因资源耗尽而瘫痪。
    
    可以使用线程池，替代原来的每次请求创建线程。
    
解决方案：
    python3中有线程池实现
    使用标准库中concurrent.futures下的ThreadPoolExector，对象的submit和map方法可以用来启动线程池中线程，执行任务

"""

"""
import os, cv2, time, struct, threading
from socketserver import TCPServer, ThreadingTCPServer
from http.server import HTTPServer, BaseHTTPRequestHandler
from concurrent.futures import ThreadPoolExecutor
from threading import Thread, RLock
from select import select


class JpegStreamer(Thread):
    def __init__(self, camera):
        Thread.__init__(self)
        self.cap = cv2.VideoCapture(camera)
        self.lock = RLock()
        self.pipes = {}
    
    def register(self):
        pr, pw = os.pipe()
        self.lock.acquire()
        self.pipes[pr] = pw
        self.lock.release()
        return pr
    
    def unregister(self, pr):
        self.lock.acquire()
        self.pipes.pop(pr)
        self.lock.release()
        pr.close()
        pw.close()
    
    def capture(self):
        cap = self.cap
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                ret, data = cv2.imencode('.jpg', frame, (cv2.IMWRITE_JPEG_QUALITY, 40))
                yield data.toString()
    
    def send(self, frame):
        n = struct.pack('l', len(frame))
        self.lock.acquire()
        if len(self.pipes):
            _, pipes, _ = select([], self.pipes.itervalues(), [], 1)
            for pipe in pipes:
                os.write(pipe, n)
                os.write(pipe, frame)
        self.lock.release()
    
    def run(self):
        for frame in self.capture():
            self.send(frame)


class JpegRetriever(object):
    def __init__(self, streamer):
        self.streamer = streamer
        self.local = threading.local()
    
    def retriver(self):
        while True:
            ns = os.read(self.pipe, 8)
            n = struct.unpack('l', ns)[0]
            data = os.read(self.local.pipe, n)
            yield data
    
    def __enter__(self):
        if hasattr(self.local, 'pipe'):
            raise RuntimeError()
        
        self.pipe = streamer.register()
        return self.retriver()
    
    def __exit__(self, *args):
        self.streamer.unregister(self.local.pipe)
        del self.local.pipe
        return True


class Handler(BaseHTTPRequestHandler):
    retriever = None
    
    @staticmethod
    def setJpegRetriever(retriever):
        Handler.retriever = retriever
    
    def do_Get(self):
        if self.retriever is None:
            raise RuntimeError('no retriver')
        
        if self.path != '/':
            return
        
        self.send_response(200)
        self.send_header("Content-type", 'multipart/x-mixed-replace;boundary=abcde')
        self.end_headers()
        
        with self.retriever as frames:
            for frame in frames:
                self.send_frame(frame)
    
    def send_frame(self,frame):
        s = '--abcde\r\n'
        s += 'Content-Type:image/jpeg\r\n'
        self.write.write(s.encode('ascii'))
        self.write.write(frame)
        
class ThreadingPoolTCPServer(ThreadingTCPServer):
    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True,max_thread_num=100):
        super().__init__(server_address, RequestHandlerClass, bind_and_activate)
        self.executor = ThreadPoolExecutor(max_thread_num)
    
    def process_request(self, request, client_address):
        self.executor.submit(self.process_request_thread,request,client_address)
if __name__ == '__main__':
    streamer = JpegStreamer(0)
    streamer.start()
    
    retriever = JpegRetriever(streamer)
    Handler.setJpegRetriever(retriever)
    
    print('Start server...')
    httpd = ThreadingPoolTCPServer(('', 9000), Handler,max_thread_num=3)
    httpd.serve_forever()
"""

"""
8-6 如何使用多进程

实际案例：
    由于python中全局解释器锁（GIL）的存在，在任意时刻只允许一个线程在解释器中运行，因此python的多线程不适合处理cpu密集型的任务
    
    想要处理cpu密集型的任务，可以使用多进程模型
    
解决方案：
    使用标准库中的multiprocessing.Process，它可以启动子进程执行任务，操作接口，进程间通信，进程间同步等都与Threading.Thread类似

"""

"""
from multiprocessing import Process
from threading import Thread

def isArmstrong(n):
    a,t = [],n
    while t > 0:
        a.append(t % 10)
        t /= 10
    k = len(a)
    return sum(x ** k for x in a) == n

def findArmstrong(a,b):
    print(a,b)
    res = [k for k in range(a,b) if isArmstrong(k)]
    print('%s - %s:%s' % (a,b,res))
    
def findByThread(*argslist):
    workers = []
    for args in argslist:
        worker = Thread(target=findArmstrong,args=args)
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()
        
def findByProcess(*argslist):
    workers = []
    for args in argslist:
        worker = Process(target=findArmstrong,args=args)
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()
        
if __name__ == '__main__':
    import time
    start = time.time()
    # 多进程会更快
    findByProcess((20000000,25000000),(25000000,30000000))
    #findByThread((20000000,25000000),(25000000,30000000))
    print(time.time() - start)
"""

"""
9-1 如何使用函数装饰器

实际案例：
    某些时候我们想为多个函数，统一添加某种功能，比如计时统计，记录日志，缓存运算结果等等
    
    我们不想在每个函数内--添加完全相同的代码，有什么好的解决方案？
    
解决方案：
    定义装饰器函数，用它来生成一个在原函数基础添加了新功能的函数，替代原函数
    
    
题目1：斐波那契数列，又称黄金分割数列，指的是这样一个数列，1,1,2,3,5,8,13,21....，这个数列从第三项开始，每一项都等于前两项之和，求数列第n项

def fibonacci(n,cache=None):
    if cache is None:
        cache == {}
    if n in cache:
        return cache[n]
    if n <= 1:
        return 1
    cache[n] = fibonacci(n - 1,cache) + fibonacci(n - 2,cache)
    return cache[n]
    

def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# fibonacci = memo(fibonacci) 这条和 @memo 等价
print(fibonacci(50))


题目2：一个共有10个台阶的楼梯，从下面走到上面，一次只能迈1-3个台阶，并且不能后退，走完这个楼梯共有多少种方法

@memo
def climb(n,steps):
    count = 0
    if n == 0:
        count = 1
    elif n > 0:
        for step in steps:
            count += climb(n - step, steps)
    return count

print(climb(10,(1,2,3)))

"""

"""
9-2 如何为被装饰的函数保存元数据

实际案例：
    在函数对象中保存着一些函数的元数据，例如：
    f.__name__     : 函数的名字
    f.__doc__      : 函数文档字符串
    f.__module__   : 函数所属模块名
    f.__dict__     : 属性字典
    f.__defaults__ : 默认参数元组
    
我们在使用装饰器后，再使用上面这些属性访问时，看到的是内部包裹函数的元数据，原来函数的元数据便丢失掉了，应该如何解决？

解决方案：
    使用标准库functools中的装饰器wraps装饰内部包裹函数，可以制定将原函数的某些属性，更新到包裹函数上面

def f(a):
    '''f function'''
    return a * 2
print(f.__name__)
g = f
print(g.__name__)
print(f.__doc__)
print(f.__module__)
print(f.__defaults__)
def f(a,b=1,c=[]):
    print(a,b,c)
# defaults 保存默认参数
print(f.__defaults__)
f.__defaults__[1].append('abc')
# 默认参数尽量不要用可变对象 []
print(f(100))
print(f.__closure__)

def f():
    a = 2
    return lambda k: a ** k
g = f()
print(g.__closure__)
c = g.__closure__[0]
print(c.cell_contents)




from functools import update_wrapper,wraps,WRAPPER_ASSIGNMENTS,WRAPPER_UPDATES

def mydecorator(func):
    @wraps(func)
    def wrapper(*args,**kargs):
        '''wrapper function'''
        print('In wrapper')
        func(*args, **kargs)
    #update_wrapper(wrapper,func,('__name__','__doc__'),('__dict__',))
    #update_wrapper(wrapper, func)
    return wrapper()

@mydecorator
def example():
    '''example function'''
    print('In example')
    
print(example.__name__)
print(example.__doc__)
#print(WRAPPER_UPDATES)
#print(WRAPPER_ASSIGNMENTS)

"""

"""
9-3 如何定义带参数的装饰器

实际案例：
    实现一个装饰器，它用来检查被装饰函数的参数类型，装饰器可以通过参数指明函数参数的类型，调用时如果检测出类型不匹配则抛出异常
    
@typeassert(str,int,int)
def f(a,b,c):
    ...

@typeassert(y=list)
def g(x,y):
    ...
    
解决方案：
    提取函数签名：inspect.signature()
    带参数的装饰器，也就是根据参数定制化一个装饰器，可以看成生产装饰器的工厂，每次调用typeassert，返回一个特定的装饰器，然后用它去修饰其他函数
    
from inspect import signature

def typeassert(*ty_args,**ty_kargs):
    def decorator(func):
        # func -> a,b
        # d = {'a':int,'b':str}
        sig = signature(func)
        # 部分参数绑定
        btypes = sig.bind_partial(*ty_args,**ty_kargs).arguments
        def wrapper(*args,**kargs):
            # arg in d,instance(arg,d[arg])
            for name,obj in sig.bind(*args, **kargs).arguments.items():
                if name in btypes:
                    if not isinstance(obj,btypes[name]):
                        raise TypeError('"%s" must be "%s"' %(name,btypes[name]))
            return func(*args,**kargs)
        return wrapper
    return decorator

@typeassert(int,str,list)
def f(a,b,c):
    print(a,b,c)
f(1,'abc',[1,2,3])
f(1,2,[1,2,3])


from inspect import signature
def f(a,b,c=1):
    pass
sig = signature(f)
print(sig.parameters)
a = sig.parameters['a']
print(a.name)
print(a.kind)
print(a.default)
c = sig.parameters['c']
print(c.default)
print(sig.bind(str,int,int))
bargs = sig.bind(str,int,int)
print(bargs.arguments)
print(bargs.arguments['a'])
print(bargs.arguments['b'])
#print(sig.bind(str)) 做类型检查，参数必须填
print(sig.bind_partial(str))
# 只对部分参数校验

"""

"""
9-4 如何实现属性可修改的函数装饰器

实际案例：
    为分析程序内哪些函数执行时间开销较大，我们定义一个带timeout参数的函数装饰器，装饰功能如下：
    
    1.统计被装饰函数单次调用运行时间
    2.时间大于参数timeout的，将此次函数调用记录到log日志中
    3.运行时可修改timeout的值

解决方案：
    为包裹函数增添一个函数，用来修改闭包中使用的自由变量，在python3中：使用non访问嵌套作用域中的变量引用

"""

"""
#python2
from functools import wraps
import time
import logging

def warn(timeout):
    timeout = [timeout]
    def decorator(func):
        def wrapper(*args,**kargs):
            start = time.time()
            res = func(*args,**kargs)
            used = time.time() - start
            if used > timeout:
                msg = '"%s": %s > %s' %(func.__name__,used,timeout[0])
                logging.warn(msg)
            return res
        def setTimeout(k):
            # nonlocal timeout
            timeout[0] = k
        wrapper.setTimeout = setTimeout
        return wrapper
    return decorator

from random import randint
@warn(1.5)
def test():
    print('In test')
    while randint(0,1):
        time.sleep(0.5)

for _ in range(30):
    test()
    
test.setTimeout(1)
for _ in range(30):
    test()
"""

"""
#python3
from functools import wraps
import time
import logging

def warn(timeout):
    def decorator(func):
        def wrapper(*args, **kargs):
            start = time.time()
            res = func(*args, **kargs)
            used = time.time() - start
            if used > timeout:
                msg = '"%s": %s > %s' % (func.__name__, used, timeout)
                logging.warn(msg)
            return res
        def setTimeout(k):
            nonlocal timeout
            timeout = k
        wrapper.setTimeout = setTimeout
        return wrapper
    return decorator

from random import randint
@warn(1.5)
def test():
    print('In test')
    while randint(0, 1):
        time.sleep(0.5)

for _ in range(30):
    test()

test.setTimeout(1)
for _ in range(30):
    test()
"""

"""
9-5 如何在类中定义装饰器

实际案例：
    实现一个能将函数调用信息记录到日志的装饰器：
    1.把每次函数的调用时间，执行时间，调用次数写入日志
    2.可以对被装饰器函数分组，调用信息记录到不同日志
    3.动态修改参数，比如日志格式
    4.动态打开关闭日志输出功能
    
解决方案：
    为了让装饰器在使用上更为灵活，可以把类的实例方法作为装饰器，此时在包裹函数中就可以持有实例对象，便于修改属性和拓展功能

"""

"""
import logging
import time
from time import localtime,time,strftime,sleep

class CallingInfo(object):
    def __init__(self,name):
        log = logging.getLogger(name)
        log.setLevel(logging.INFO)
        fh = logging.FileHandler(name + '.log')
        log.addHandler(fh)
        log.info('Start'.center(50,'-'))
        self.log = log
        self.formatter = '%(func)s -> [%(time)s - %(used)s - %(ncalls)s]'
        
    def info(self,func):
        def wrapper(*args,**kargs):
            wrapper.ncalls += 1
            lt = localtime()
            start = time()
            res = func(*args,**kargs)
            used = time() - start
            info = {}
            info['func'] = func.__name__
            info['time'] = strftime('%x %X',lt)
            info['used'] = used
            info['ncalls'] = wrapper.ncalls
            msg = self.formatter % info
            self.log.info(msg)
            return res
        wrapper.ncalls = 0
        return wrapper
    
    def setFormatter(self,formatter):
        self.formatter = formatter
        
    def turnOn(self):
        self.log.setLevel(logging.INFO)
        
    def turnOff(self):
        self.log.setLevel(logging.WARN)

cinfo1 = CallingInfo('mylog1')
cinfo2 = CallingInfo('mylog2')

cinfo1.setFormatter('%(func)s -> [%(time)s - %(ncalls)s]')
cinfo2.turnOff()

@cinfo1.info
def f():
    print('in f')
    
@cinfo1.info
def g():
    print('in g')

@cinfo2.info
def h():
    print('in h')

from random import choice

for _ in range(50):
    choice([f,g,h])()
    sleep(choice([0.5,1,2]))
"""

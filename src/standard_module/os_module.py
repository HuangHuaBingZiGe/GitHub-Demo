#!/usr/bin/python
# -*- coding: utf-8 -*-



"""
os.path
os.makedirs
os.path.exists
os.path.abspath
os.path.dirname
"""

"""
直接从系统里面删除文件，不经过回收站
"""
# os.remove('E:\\test_123.txt')



"""
直接从系统里面删除空文件夹，不经过回收站
"""
# os.rmdir('E:\\test_123')



"""
直接从系统里面删除文件夹（文件夹里面可以有别的文件），不经过回收站。所以要小心不要误删
"""
# shutil.rmtree('E:\\test_123.txt')



"""
可使用第三方包，send2trash
可以删除任何东西，删除的东西送回回收站
"""
# send2trash.send2trash("E:\\test_123.txt")
# send2trash.send2trash("E:\\test_123")
# send2trash.send2trash("E:\\test_123\\")

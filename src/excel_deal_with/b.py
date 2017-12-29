# -*- coding:utf-8 -*-

import xlrd
from xlutils.copy import copy

# 定义目录名
DIR_NAME = u"E:\\"

#   定义文件名
FILE_NAME = u"数据集成每日作业运行情况登记表_20170327.xls"

if __name__ == '__main__':
    rb = xlrd.open_workbook(DIR_NAME + FILE_NAME)
    wb = copy(rb)
    ws = wb.get_sheet(0)
    
    for col_num in range(10, 12):
        for row_num in range(0, 74):
            ws.write(row_num, col_num, '')
    wb.save(DIR_NAME + FILE_NAME)
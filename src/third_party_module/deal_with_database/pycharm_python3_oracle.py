#!-*- encoding: utf-8 -*-
import cx_Oracle as oracle

'''
连接方法1：
conn = oracle.connect('bingzi','123456','localhost:1521/orcl')
连接方法2：
conn = oracle.connect('bingzi/123456@localhost/orcl')
conn = oracle.connect('user_name','password','ip:1521/service_name')

sql=cur.execute('SELECT * FROM wyz_test')
sql=cur.execute('SELECT * FROM all_all_tables where rownum <=10')
sql=cur.execute('select * from v$version')
'''

conn = oracle.connect('user_name', 'password', 'ip:1521/service_name')
cur = conn.cursor()
sql = cur.execute('select * from v$version')
print(sql.fetchall())
cur.close()

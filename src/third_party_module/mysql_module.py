#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
mysql.connector
mysql.connector.connect
mysql.connector.connect.cursor
mysql.connector.connect.cursor.execute
mysql.connector.connect.cursor.rowcount
mysql.connector.connect.cursor.fetchall
mysql.connector.connect.cursor.executemany
mysql.connector.connect.cursor.commit
mysql.connector.connect.cursor.close
mysql.connector.DatabaseError
"""

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="xxx", db="xxx")

cursor = mydb.cursor()

cursor.execute("select *  from TABLE_NAME")
print(cursor.fetchall())

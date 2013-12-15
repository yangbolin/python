#!/usr/bin/python 
#Filename:mysqldb.py

import MySQLdb

conn = MySQLdb.connect(host='10.20.149.14', user='atas',passwd='atas',db='atas')

cursor = conn.cursor()

count = cursor.execute('select * from atas_task_base')

print count,

conn.close()

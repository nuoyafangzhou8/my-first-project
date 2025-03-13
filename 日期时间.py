# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\日期时间.py


# 日期时间转换为字符串

import datetime

d=datetime.datetime.today()

print(d.strftime('%Y-%m-%d %H:%M:%S'))

print(d.strftime('%Y-%m-%d'))


# 字符串转换为日期时间

str_date='2020-02-09 10:40:26'
date=datetime.datetime.strptime(str_date,'%Y-%m-%d %H:%M:%S')

print(date)

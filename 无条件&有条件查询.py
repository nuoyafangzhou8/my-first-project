# # coding=utf-8
# # 代码文件：D:\LIXIAOKUN\python学习作业\无条件&有条件查询.py
# # 无条件查询
# # 引入sqllite3模块
# import sqlite3
#
# try:
#     # 1.建立数据库连接
#     con=sqlite3.connect(r'F:\SQLite_DB\my_school_db.db')
#     # 2.创建游标对象
#     cursor=con.cursor()
#     # 3.执行SQL查询操作
#     sql='SELECT s_id,s_name,s_sex,s_birthday FROM student'
#     cursor.execute(sql)
#     # 4.提取结果集
#     result_set=cursor.fetchall() # 从结果集中返回所有数据
#     for row in result_set: # 遍历结果集
#         print('学号：{0}-姓名：{1}-性别：{2}-出生日期：{3}'.format(row[0],row[1],row[2],row[3])) # 提取出字段的内容，row[0]是第一个字段的内容
# except sqlite3.Error as e: # sqlite3相关的异常
#     print('数据查询发生错误：{}'.format(e))
# finally:
#     # 5.关闭游标
#     if cursor:
#         cursor.close()
#     # 6.关闭数据连接
#     if con:
#         con.close()

# 有条件查询
import sqlite3

istr=input('请输入出生日期')
try:
    # 建立连接
    Con=sqlite3.connect(r'F:\SQLite_DB\my_school_db.db')
    # 建立游标
    Cursor=Con.cursor()
    # 执行SQL查询操作
    sql='SELECT s_id,s_name,s_sex,s_birthday FROM student WHERE s_birthday < ?'
    Cursor.execute(sql,[istr])
    # 提取结果集
    result_set=Cursor.fetchall()
    for row in result_set:
        print('学号：{0}-姓名：{1}-性别：{2}-出生日期：{3}'.format(row[0],row[1],row[2],row[3]))
except sqlite3.Error as e:
    print('数据查询发生错误：{}'.format(e))
# 关闭游标
if Cursor:
    Cursor.close()
# 关闭数据连接
if Con:
    Con.close()

# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\插入&更新数据&删除数据.py

# 插入数据
# import sqlite3
# try:
#     # 输入对象
#     i_name=input('请输入【姓名】：')
#     i_sex=input('请输入【性别】（1表示男，0表示女:')
#     i_birthday=input('请输入出生日期（yyyyMMdd):')
#     # 创建连接
#     con=sqlite3.connect(r'F:\SQLite_DB\my_school_db.db')
#     # 创建游标
#     cur=con.cursor()
#     # 执行SQL插入
#     sql='INSERT INTO student (s_name,s_sex,s_birthday) VALUES (?,?,?)'
#     cur.execute(sql,[i_name,i_sex,i_birthday])
#     # 提交数据库事务
#     con.commit()
#     print('插入数据成功。')
# except sqlite3.Error as e:
#     print('插入数据失败：{}'.format(e))
#     # 回滚数据
#     con.rollback()
# finally:
#     # 关闭游标
#     if cur:
#         cur.close()
#     # 关闭数据连接
#     if con:
#         con.close()

# # 更新数据
#
# import sqlite3
# try:
#     # 输入要更新的对象
#     i_id=input('请输入【学号】：')
#     i_name=input('请输入【姓名】：')
#     i_sex=input('请输入【性别】（1表示男，0表示女）：')
#     i_birthday=input('请输入【出生日期】：')
#     # 创建连接
#     con=sqlite3.connect(r'F:\SQLite_DB\my_school_db.db')
#     # 创建游标
#     cur=con.cursor()
#     # 执行SQL更新数据
#     sql='UPDATE student SET s_name=?,s_sex=?,s_birthday=? WHERE s_id=?'
#     cur.execute(sql,[i_name,i_sex,i_birthday,i_id])
#     # 提交数据库事务
#     con.commit()
#     print('更新数据成功。')
# except sqlite3.Error as e:
#     print('更新数据失败：{}'.format(e))
#     # 回滚数据
#     con.rollback()
# finally:
#     # 关闭游标
#     if cur:
#         cur.close()
#     # 关闭数据连接
#     if con:
#         con.close()

# 删除数据

import sqlite3

try:
    # 输入要删除的对象
    i_id=input('请输入要删除的学生的学号：')
    # 创建连接
    con=sqlite3.connect(r'F:\SQLite_DB\my_school_db.db')
    # 创建游标
    cur=con.cursor()
    # 执行SQL删除
    sql='DELETE FROM student WHERE s_id=?'
    cur.execute(sql,[i_id])
    # 提交数据库事务
    con.commit()
    print('删除数据成功。')
except sqlite3.Error as e:
    print('删除数据失败：{}'.format(e))
    # 回滚数据
    con.rollback()
finally:
    # 关闭游标
    if cur:
        cur.close()
    # 关闭数据连接
    if con:
        con.close()

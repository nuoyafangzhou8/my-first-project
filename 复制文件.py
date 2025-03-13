# coding=utf-8
# 代码路径：D:\LIXIAOKUN\python学习作业\复制文件.py

# f_name='复制文件_原文件.txt'
#
# with open(f_name,'r',encoding='gbk') as f:
#     lines=f.readlines()
#     copy_f_name='复制文件_目标文件.txt'
#     with open(copy_f_name,'w',encoding='utf-8') as copy_f: # 此处with嵌套了，不嵌套也可以
#         copy_f.writelines(lines)
#          print('文件复制成功')



# 练习一个复制文件的代码

# a_name='src_file.txt'
#
# with open(a_name,'r',encoding='gbk') as f: # 读取文件时必须采用encoding一致的方式读取，否则读取会失败
#     lines=f.readlines()
# b_name='copy_file.txt'
# with open(b_name,'w',encoding='utf-8') as copy_f:
#     copy_f.writelines(lines)
# print('复制成功')

# 封装一个复制文件的函数

def copy_file(f_name,copy_name):
    with open(f_name,'r') as f:
        lines=f.readlines()
    with open(copy_name,'w',encoding='utf-8') as copy_f:
        copy_f.writelines(lines)
    print('文件复制成功')

copy_file('复制文件_原文件.txt','复制文件_目标文件.txt')






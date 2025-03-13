
# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\复制二进制文件.py

f_name='电压与电流-LTE.jpg'
with open(f_name,'rb') as f:
    lines=f.readlines()
    copy_f_name='电压与电流-NR.jpg'
    with open(copy_f_name,'wb') as copy_f:
        copy_f.writelines(lines)
        print('文件复制成功')

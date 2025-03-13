# coding=utf-8
# 代码路径 D:\LIXIAOKUN\python学习作业\关闭文件.py

# fname='test.txt'
# f=None
# try:
#     f=open(fname)
#     print('打开文件成功')
#     content=f.read()
#     print(content)
# except FileNotFoundError as e:
#     print('文件不存在，请先使用文件打开.py创建文件')
# except OSError as e:
#     print('处理OSError异常')
# finally:
#     if f is not None:
#         f.close()
#         print('关闭文件成功')


#使用with as 模块自动资源管理
f_name='test.txt'
with open(f_name) as f:
    content=f.read()
    print(content)

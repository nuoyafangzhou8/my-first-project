# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\实例变量.py

class Dog:
    def __init__(self,name,age):
        self.name=name # 创建和初始化实例变量name
        self.age=age   # 创建和初始化实例变量age

d=Dog('球球',2)
print('我们家狗狗名叫{0}，{1}岁了。'.format(d.name,d.age))

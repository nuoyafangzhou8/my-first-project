# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\构造方法.py

class Dog:
    def __init__(self,name,age,sex='雌性'):
        self.name=name # 创建和初始化实例变量name
        self.age=age   # 创建和初始化实例变量age
        self.sex=sex   # 创建和初始化实例变量sex

d1=Dog('球球',2)
d2=Dog('哈哈',1,'雄性')
d3=Dog(name='拖布',sex='雄性',age=3)
print('我们家狗狗名叫{0}，{1}岁了,{2}。'.format(d1.name,d1.age,d1.sex))
print('我们家狗狗名叫{0}，{1}岁了,{2}。'.format(d2.name,d2.age,d2.sex))
print('我们家狗狗名叫{0}，{1}岁了,{2}。'.format(d3.name,d3.age,d3.sex))

# coding=utf-8
# 代码文件=D:\LIXIAOKUN\python学习作业\私有方法.py

class Account:
    __interest_rate=0.0568 # 类变量利率interest_rate(私有）

    def __init__(self,owner,amount):
        self.owner=owner # 创建并初始化公有实例变量owner
        self.__amount=amount # 创建并初始化私有实例变量__amount

    def __get_info(self):
        return '{0}:金额：{1} 利率：{2}。'.format(self.owner,self.__amount,Account.__interest_rate)


    def desc(self):
        print(self.__get_info())

account=Account('Tony',800000.0)
account.desc()
# account.__get_info()# 发生错误




# 练习一个使用私有变量和私有方法的计算水果价格的程序

class Payload:
    __weight=10 # 私有变量weight为10

    def __init__(self,fruit,price):
        self.fruit=fruit
        self.__price=price #创建并初始化私有变量__price

    def __count(self):
        return '{0}需要花费{1}元'.format(self.fruit,self.__price*Payload.__weight)

    def aaa(self):
        print(self.__count())

payload=Payload('apple',2)
payload.aaa()


# 再练习一个使用私有变量和私有方法计算学生总数的程序

class Total:
    __banji_person=30

    def __init__(self,nianji,num_ban):
       self.nianji=nianji
       self.__num_ban=num_ban

    def __total_person(self):
        return '{0}共有{1}*{2}={3}人'.format(self.nianji,self.__num_ban,Total.__banji_person,self.__num_ban*Total.__banji_person)

    def bbb(self):
        print(self.__total_person())

renshu=Total('二年级',14)
renshu.bbb()
    
    

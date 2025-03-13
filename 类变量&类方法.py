# coding=utf-8
# 代码文件=D:\LIXIAOKUN\python学习作业\类变量&类方法.py

class Account:
    interest_rate=0.0568 # 类变量利率interest_rate

    def __init__(self,owner,amount):
        self.owner=owner # 创建并初始化实例变量owner
        self.amount=amount # 创建并初始化实例变量amount
    # 类方法
    @classmethod
    def interest_by(cls,amt):
        return cls.interest_rate*amt

account=Account('Tony',800000.0) # 创建一个对象account
interest=Account.interest_by(12000.0) # 调用类方法时用类名
print('计算利息：{0:.4f}'.format(interest)) 

print('账户名： {0}'.format(account.owner)) # 对实例变量通过“对象.实例变量”形式访问
print('账户金额： {0}'.format(account.amount))
print('利率： {0}'.format(Account.interest_rate)) # 对类变量通过“类名.类变量”形式访问

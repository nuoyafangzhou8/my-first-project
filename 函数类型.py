# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\函数类型.py

# 定义加法函数
def add(a,b):
    return a+b
# 定义减法函数
def sub(a,b):
    return a-b
# 定义平方函数
def square(a):
    return a*a
# 定义计算函数
def calc(opr):
    if opr=='+':
       return add
    else:
        return sub
f1=calc('+') # f1实际上是add函数
f2=calc('-') # f2实际上是sub函数
    
print(type(f1))

print('10+5={}'.format(f1(10,5)))
print('10-5={}'.format(f2(10,5)))

# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\lambda函数.py


# 定义计算函数
def calc(opr):
    if opr=='+':
       return lambda a,b:a+b # 代替add函数
    else:
        return lambda a,b:a-b # 代替sub函数
f1=calc('+') 
f2=calc('-') 
    
print(type(f1))

print('10+5={}'.format(f1(10,5)))
print('10-5={}'.format(f2(10,5)))




# 练习一个合并参数的lambda函数的程序

def merge():
    
    return lambda a,b:a+b

f1=merge()
print(f1('rt','cd'))

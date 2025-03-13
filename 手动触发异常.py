# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\手动触发异常.py

class ZhejieketangException(Exception):
    def __init__(self,message):
        super().__init__()

i=input('请输入数字：')
n=8888
try:
    result=n/int(i)
    print(result)
    print('{0}除以{1}等于{2}'.format(n,i,result))
except ZeroDivisionError as e:
    #print('不能除以0，异常：{}'.format(e))
    raise ZhejieketangException('不能除以0')
except ValueError as e:
    #print('输入的是无效数字，异常：{}'.format(e))
    raise ZhejieketangException('输入的是无效数字')

# coding=utf-8
# 文件路径：D:\LIXIAOKUN\python学习作业/除0异常

i=input('请输入数字：')

n=8888
try:
    result=n/int(i)
    print(result)
    print('{0}除以{1}等于{2}'.format(n,i,result))
except ZeroDivisionError as e: #except
    print('不能除以0，异常：{}'.format(e))
except ValueError as e:
    print('输入的是无效数字，异常：{}'.format(e))




# 多重异常捕获

i=input('请输入数字：')

n=8888
try:
    result=n/int(i)
    print(result)
    print('{0}除以{1}等于{2}'.format(n,i,result))
except(ZeroDivisionError,ValueError) as e: #except
    print('异常发生：{}'.format(e))

#try-except嵌套
    
i=input('请输入数字：')

n=8888
try:
    i2=int(i)
    try:
        result=n/int(i)
        print(result)
        print('{0}除以{1}等于{2}'.format(n,i,result))
    except ZeroDivisionError as e: #except
        print('不能除以0，异常：{}'.format(e))
except ValueError as e:
    print('输入的是无效数字，异常：{}'.format(e))

#fanally 释放资源

i=input('请输入数字：')

n=8888
try:
    result=n/int(i)
    print(result)
    print('{0}除以{1}等于{2}'.format(n,i,result))
except ZeroDivisionError as e: #except
    print('不能除以0，异常：{}'.format(e))
except ValueError as e:
    print('输入的是无效数字，异常：{}'.format(e))
finally:
    #释放资源代码
    print('资源释放...')
    
    

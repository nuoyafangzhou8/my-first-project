# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\过滤函数filter.py

# 提供过滤条件函数
def f1(x):
    return x>50 # 找出大于50的元素

data1=[66,15,91,28,98,50,7,80,99]
filtered=filter(f1,data1)
data2=list(filtered) # 转换为列表
print(data2)




# 练习写一个查找字符串中含有空格的参数的函数

# 定义一个过滤条件函数
def f1(x):
    if x.find(' ')!=-1:
        return True # 查找含有空格的字符串

data1=['1','2','star','are you ok','yes,you are right','main']
filtered=filter(f1,data1)
data2=list(filtered)
print(data2)

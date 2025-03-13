# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\映射函数map.py

# 提供编号规则的函数
def f1(x):
    return x*2 # 变换规则为乘以2

data1=[66,15,91,28,98,50,7,80,99]
filtered=map(f1,data1)
data2=list(filtered) # 转换为列表
print(data2)




# 练习写一个给每个名字加一个’name-‘前缀的函数

# 定义一个给每个名字加一个’name-‘前缀的规则的函数
def f1(x):

    return 'name-'+x

name=['Lucy','Tom','Janny','Amy','Lissa','Ken']
name1=list(map(f1,name)) # 列表列出增加规则后的参数
print(name1)

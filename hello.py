# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\hello.py

import world
from world import z
from world import x as x2

x=100
y=20

print(y) # 访问当前模块变量y
print(world.y) # 访问world模块变量y
print(z) # 访问world模块变量z
print(x2) # x2是world模块x别名

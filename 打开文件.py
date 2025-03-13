# coding=utf-8
# 代码路径：D:\LIXIAOKUN\python学习作业\打开文件.py


f=open('test.txt','w+')
f.write('World')
print('创建test.txt文件,World写入文件')

f=open('test.txt','r+')
f.write('Hello')
print('打开test.txt文件，Hello覆盖文件内容')


f=open('test.txt','a')
f.write(' ')
print(r'打开test.txt文件，在文件尾部追加" "')

fname='D:/LIXIAOKUN/python学习作业/test.txt'
#fname=r'D:\LIXIAOKUN\python学习作业\test.txt' #文件路径使用反斜杠需要在前面加上r
#fname='D:\\LIXIAOKUN\\python学习作业\\test.txt' #文件路径使用反斜杠，在反斜杠前需要加转译符“|”
f=open(fname,'a+')
f.write('World')
print('打开test.txt文件，在文件尾部追加World')
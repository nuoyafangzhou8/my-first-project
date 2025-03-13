# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\使用属性.py


# 使用get,set方法获取和修改成员变量
class Dog:
    def __init__(self,name,age,sex='雌性'):
        self.name=name # 创建和初始化实例变量name
        self.__age=age   # 创建和初始化私有实例变量age
        self.sex=sex   # 创建和初始化实例变量sex

    def get(self):
        return self.__age

    def set(self,i):
        self.__age=i
        return self.__age
       
       

d1=Dog('球球',2)

print('我们家狗狗名叫{0}，{1}岁了,{2}。'.format(d1.name,d1.set(3),d1.sex))


# 使用属性方法获取和修改成员变量
class Dog:
    def __init__(self,name,age,sex='雌性'):
        self.name=name # 创建和初始化实例变量name
        self.__age=age   # 创建和初始化私有实例变量age
        self.sex=sex   # 创建和初始化实例变量sex

    @property     # 修饰器
    def age(self):
        return self.__age
    @age.setter   # 修饰器
    def age(self,age):
        self.__age=age
        
       
       

d1=Dog('球球',2)

print('我们家狗狗名叫{0}，{1}岁了,{2}。'.format(d1.name,d1.age,d1.sex))

d1.age=3  #给属性赋值

print('我们家狗狗名叫{0}，{1}岁了,{2}。'.format(d1.name,d1.age,d1.sex))

# 练习一个使用属性方法获取和修改学生姓名的程序

class Student:
    def __init__(self,name,banji,score):
        self.__name=name
        self.banji=banji
        self.score=score

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name=name

student=Student('小明','三（9）班',95)
print('{0}的班级是{1}，成绩是{2}'.format(student.name,student.banji,student.score))
student.name='小华'
student.score=89
print('{0}的班级是{1}，成绩是{2}'.format(student.name,student.banji,student.score))

# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\实例方法.py

class Dog:
    # 构造方法
    def __init__(self,name,age,sex='雌性'):
        self.name=name # 创建和初始化实例变量name
        self.age=age   # 创建和初始化实例变量age
        self.sex=sex   # 创建和初始化实例变量sex
    
     # 实例方法
    def run(self):
        print('{}在跑。。。'.format(self.name))
    def speak(self,sound):
         print('{0}在叫：{1}！'.format(self.name,sound))

# 创建一个Dog实例     
dog=Dog('球球',2)
# 调用实例方法
dog.run()
dog.speak('汪')

#创建Dog实例d1，d2，d3
d1=Dog('球球',2)
d2=Dog('哈哈',1,'雄性')
d3=Dog(name='拖布',sex='雄性',age=3)
#调用构造方法
print('我们家狗狗名叫{0}，{1}岁,{2}。'.format(d1.name,d1.age,d1.sex))
print('我们家狗狗名叫{0}，{1}岁了,{2}。'.format(d2.name,d2.age,d2.sex))
print('我们家狗狗名叫{0}，{1}岁了,{2}。'.format(d3.name,d3.age,d3.sex))



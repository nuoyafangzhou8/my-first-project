# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\继承&多继承.py

#继承
class Animal:

    def __init__(self,name):
        self.name=name # 实例变量name

    def show_info(self):
        return '动物的名字：{0}'.format(self.name)

    def move(self):
        print('动一动...')

class Cat(Animal):

    def __init__(self,name,age):
        super().__init__(name)
        self.age=age # 实例变量age

cat=Cat('Tom',2)
cat.move()
print(cat.show_info())


# 多继承
class Horse:
    def __init__(self,name):
        self.name=name # 实例变量name

    def show_info(self):
        return  '马的名字：{0}'.format(self.name)

    def run(self):
        print('马跑...')

class Donkey:
    def __init__(self,name):
        self.name=name # 实例变量name

    def show_info(self):
        return  '驴的名字：{0}'.format(self.name)

    def run(self):
        print('驴跑...')

    def roll(self):
        print('驴打滚...')


class Mule(Horse,Donkey):

    def __init__(self,name,age):
        super().__init__(self)
        self.age=age # 实例变量age

    # 方法重写
    #def show_info(self):
    #    return  '骡：{0},{1}岁'.format(self.name,self.age)



m=Mule('骡宝莉',1)
m.run()  #继承父类Horse方法
m.roll()  #继承父类Donkey方法

print(m.show_info()) #继承父类Horse方法
        

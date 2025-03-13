def start(obj): # 接收obj对象具有speak()方法
    obj.speak()

class Animal:
    def speak(self):
        print('动物叫，但不知道是哪种动物叫！')

class Dog(Animal):
    def speak(self):
        print('小狗：汪汪叫...')

class Cat(Animal):
    def speak(self):
        print('小猫，喵喵叫...')

class Car:
    def speak(self):
        print('小汽车：嘀嘀叫...')

start(Dog())
start(Cat())
start(Car())

class Animal:
    def speak(self):
        print('动物叫，但不知道是哪种动物叫！')

class Dog(Animal):
    def speak(self):
        print('小狗：汪汪叫...')

class Cat(Animal):
    def speak(self):
        print('小猫，喵喵叫...')

an1=Dog()
an2=Cat()
an1.speak()
an2.speak()

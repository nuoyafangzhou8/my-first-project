num1=int(input('输入班级1的学生数量：'))
class1=set()
for i in range(0,num1):
    name=input('输入学生%d姓名：'%(i+1))
    class1.add(name)
num2=int(input('输入班级2的学生数量：'))
class2=set()
for i in range(0,num2):
    name=input('输入学生%d姓名：'%(i+1))
    class2.add(name)
same=class1&class2
diff=class2-class1
print('重名的学生：')
for name in same:
    print(name)
print('在班级2出现但没有在班级1出现的学生名字')
for name in diff:
    print(name)

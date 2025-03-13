# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\函数举例.py


def rect_area(width,height):
    area=width*height
    return area


def rect_area1(width,height):
    area=width*height
    print('{0}*{1}长方形的面积：{2}'.format(width,height,area))


def make_coffee(name='卡布奇诺'):
    return "制作一杯{0}咖啡。".format(name)


def sum(*numbers):
    total=0.0
    for number in numbers:
        total+=number
    return total
print(sum(100.0,20.0,30.0))
      
print(sum(30.0,80.0))




def show_info(**info):
    print('---show_info---')
    for key,value in info.items():
        print('{0}-{1}'.format(key,value))

show_info(name='Tony',age=18,sex=True)
show_info(student_name='tony',student_no='1000')





x=20
def print_value():
    # global x # 将x变量提升为全局变量
    x=10
    print('函数中x={0}'.format(x))



print_value()
print('全局变量x={0}'.format(x))
      
    

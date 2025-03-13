# # 导入turtle
# import turtle
#
# # 定义画笔
# pen = turtle.Turtle()
# # 改变画笔形状
# pen.shape('circle')
# # 设置画笔规格
# pen.pensize(5)
# # 设置画笔颜色
# pen.pencolor('red')
# # 向右旋转90度
# pen.right(90)
# # 向前走100
# pen.forward(300)
# # 向右旋转90度
# pen.right(90)
# # 向前走100
# pen.forward(300)
# # 向右旋转90度
# pen.right(90)
# # 向前走100
# pen.forward(300)
# # 向右旋转90度
# pen.right(90)
# # 向前走100
# pen.forward(300)
#
# turtle.done()


# # 填充颜色
# import turtle
#
# # 定义画笔
# pen=turtle.Turtle()
# pen.pensize(3)
# pen.pencolor('green')
# # 填充色
# b=(.5,.7,1.0)
# pen.fillcolor(b)
# # 开始填充
# pen.begin_fill()
# # 绘制图形
# # pen.hideturtle()
# pen.fd(200)
# pen.goto(60,70)
# pen.home()
# # 结束填充
# pen.end_fill()
# # 画图完成
# turtle.done()

# # 绘制五角星
# import turtle
#
# # 定义画笔
# pen = turtle.Turtle()
# pen.pencolor('red')  # 画笔颜色为红色
# pen.speed(9)  # 绘画速度为9
# # 填充色
# pen.fillcolor('red')  # 填充色为红色
# # 开始绘制
# pen.hideturtle()  # 隐藏画笔
# pen.penup()  # 抬起画笔
# pen.goto(-100, 150)  # 将起始位置更新到（-100，150）
# pen.begin_fill()  # 开始填充
# for i in range(5):  # 开始画图，执行5次以下划线操作
#     pen.pendown()  # 放下画笔
#     pen.fd(200)  # 前进200个像素
#     pen.right(144)  # 向右转144度
# pen.end_fill()  # 结束填充
# # 绘制完成
# turtle.done()

# # 绘制奥运五环
#
# import turtle
#
# # 定义画笔
# pen=turtle.Turtle()
# pen.width(5)
# # 绘制第一个环
# pen.circle(60)
# # 绘制第二个环
# pen.penup()
# pen.fd(140)
# pen.down()
# pen.color('red')
# pen.circle(60)
# # 绘制第三个环
# pen.penup()
# pen.fd(140)
# pen.pendown()
# pen.color('yellow')
# pen.circle(60)
# # 绘制第四个环
# pen.up()
# pen.goto(210,-50)
# pen.pendown()
# pen.color('blue')
# pen.circle(60)
# # 绘制第五个环
# pen.up()
# pen.fd(-140) # 或者 pen.goto(60,-50)
# pen.pendown()
# pen.color('green')
# pen.circle(60)
# # 绘制完成
# turtle.done()

# 绘制一棵美丽的大树

import turtle


def branch(sz, level):
    if level > 0:
        # 设置画笔颜色，角度，移动距离后绘制向右的树枝
        pen.pencolor(0, 255 // level, 0)  # 255//level 保证颜色随着层数增加变浅
        pen.fd(sz)  # 移动sz的距离
        pen.right(angle)  # 向右旋转angle的角度
        # 递归调用branch函数，绘制下一级树枝
        branch(0.8 * sz, level - 1)
        # 在绘制完向右的树枝后绘制向左的树枝
        pen.pencolor(0, 255 // level, 0)
        pen.left(2 * angle)
        # 递归调用branch函数
        branch(0.8 * sz, level - 1)
        # 在绘制完向左的树枝后返回初始位置
        pen.pencolor(0, 255 // level, 0)
        pen.right(angle)
        pen.fd(-sz)


if __name__ == '__main__':
    # 定义画笔
    pen = turtle.Turtle()
    pen.hideturtle()  # 隐藏画笔
    turtle.colormode(255)  # 修改颜色模式为0-255
    pen.speed('fastest')  # 修改绘画速度为最快
    angle = 30  # 常量angle赋值30
    pen.right(-90)  # 画笔转为-90度
    branch(80, 7)  # 初始调用branch函数
    turtle.done()  # 绘制完成

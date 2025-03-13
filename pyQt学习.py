# coding = utf - 8
# 代码文件：D:\LIXIAOKUN\python学习作业\pyQt学习.py
# 编写你的第一个PyQt
# GUI程序
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
#
# app = QApplication(sys.argv)
# # 创建窗口对象
# window = QWidget()
# # 设置窗口标题
# window.setWindowTitle('你好Qt!')
# # 设置窗口大小
# window.resize(400, 300)
# # 设置窗口位置
# window.move(600, 300)
# # 显示窗口
# window.show()
# # 让应用程序进入主事件循环
# app.exec_()


# # 以面向对象的方式实现PyQt GUI
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
#
#
# # 创建我的窗口类
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         # 设置窗口大小
#         self.resize(400, 300)
#         # 设置窗口位置
#         self.move(600, 300)
#         # 设置窗口标题
#         self.setWindowTitle('你好Qt!')
#
#
# # 创建main函数
# def main():
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     app.exec_()
#
#
# if __name__ == '__main__':
#     # 调用main函数
#     main()

# # 放上控件
# import sys
# from PyQt5.QtWidgets import *
#
# # 创建窗口类
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#     def initUI(self):
#         # 设置窗口大小
#         self.resize(400,300)
#         # 设置窗口位置
#         self.move(600,300)
#         # 设置窗口标题
#         self.setWindowTitle('添加控件')
#         # 创建标签控件
#         label=QLabel(self)
#         # 设置在标签上显示的文字
#         label.setText('Hello Word!')
#         # 设置标签位置
#         label.move(180,120)
#         # 创建按钮控件
#         button=QPushButton(self)
#         # 设置按钮上显示的文字
#         button.setText('OK')
#         # 设置按钮大小
#         button.move(170,160)
#
#
# # 创建main函数
# def main():
#     app=QApplication(sys.argv)
#     window=MyWindow()
#     window.show()
#     app.exec_()
#
# if __name__=='__main__':
#     # 调用main函数
#     main()

# # 信号与槽
# import sys
# from PyQt5.QtWidgets import *
#
# # 创建窗口类
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#     def initUI(self):
#         # 设置窗口大小
#         self.resize(400,300)
#         # 设置窗口位置
#         self.move(600,300)
#         # 设置窗口标题
#         self.setWindowTitle('信号与槽')
#         # 设置标签文本
#         self.label=QLabel(self)
#         self.label.setText('Hello World!')
#         # 设置标签位置
#         self.label.move(180,120)
#         # 设置按钮文本
#         button=QPushButton(self)
#         button.setText('OK')
#         # 设置按钮位置
#         button.move(170,160)
#         # 添加事件处理，连接信号与槽
#         button.clicked.connect(self.click_success)
#     # 定义槽函数,槽函数与initUI并列
#     def click_success(self):
#         self.label.setText('你好世界！') # 需要将label定义为成员变量self.label,才能在槽函数中引用。
#
#
# # 创建main函数
# def main():
#     app=QApplication(sys.argv)
#     window=MyWindow()
#     window.show()
#     app.exec_()
# if __name__=='__main__':
#     # 调用main
#     main()

# 鼠标事件
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtCore import Qt



# 创建窗口类
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口大小
        self.resize(400, 300)
        # 设置窗口位置
        self.move(600, 300)
        # 设置窗口名称
        self.setWindowTitle('鼠标事件')
        # 设置标签文本
        self.label = QLabel(self)
        self.label.setText('Hello,World')
        # 设置文本位置
        self.label.move(180, 120)
        # # 设置按钮
        # button=QPushButton(self)
        # button.setText('OK')
        # button.move(170,160)

    # 重写鼠标按下事件
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label.setText('鼠标左键按下')
        elif event.button() == Qt.RightButton:
            self.label.setText('鼠标右键按下')
        else:
            self.label.setText('鼠标未知按下')
    # 重写鼠标释放事件
    def mouseReleaseEvent(self, event):
        self.label.setText('鼠标释放')
    # 重写鼠标移动事件
    def mouseMoveEvent(self, event):
        self.label.setText('鼠标移动')

# 创建main函数
def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

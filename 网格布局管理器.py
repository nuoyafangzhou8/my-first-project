# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\网格布局管理器.py

# 引用相关库
import sys
from PyQt5.QtWidgets import *


# 创建窗口类
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()  # 调用初始化界面设计

    def initUI(self):
        # 设置窗口大小
        self.resize(400, 300)
        # 设置窗口标题
        self.setWindowTitle('网格布局管理器')
        # 创建网格布局管理器对象
        gridlayout = QGridLayout(self)
        # button1 = QPushButton('1', self)
        # button2 = QPushButton('2', self)
        # button3 = QPushButton('3', self)
        button1 = QPushButton('1', self)
        button2 = QPushButton('2', self)
        button3 = QPushButton('3', self)
        button4=QPushButton('4',self)
        button5=QPushButton('5',self)
        button6=QPushButton('6',self)
        # # 将按钮放到网格布局管理器
        # gridlayout.addWidget(button1, 0, 0)
        # gridlayout.addWidget(button2, 0, 1)
        # gridlayout.addWidget(button3, 1, 0)
        # # 将按钮与on_click关联
        # button1.clicked.connect(self.on_click)
        # button2.clicked.connect(self.on_click)
        # button3.clicked.connect(self.on_click)
        # 包含跨越的网格布局管理器
        gridlayout.addWidget(button1,0,0)
        gridlayout.addWidget(button2,0,1)
        gridlayout.addWidget(button3,2,2)
        gridlayout.addWidget(button4,3,0,2,3)
        gridlayout.addWidget(button5, 2, 3)
        gridlayout.addWidget(button6, 4, 3)
        # 将按钮与on_click关联
        button1.clicked.connect(self.on_click)
        button2.clicked.connect(self.on_click)
        button3.clicked.connect(self.on_click)
        button4.clicked.connect(self.on_click)
        button5.clicked.connect(self.on_click)
        button6.clicked.connect(self.on_click)
    # 定义on_click函数
    def on_click(self):
        sender = self.sender()
        msg = '您单击了{}按钮'.format(sender.text())
        print(msg)


# 定义main函数
def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

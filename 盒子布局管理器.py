# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\盒子布局管理器.p

import sys
from PyQt5.QtWidgets import *

# 定义窗口类
class MyWindow(QWidget):
    # 构造方法
    def __init__(self):
        super().__init__()
        self.initUI() # 初始化界面设计
    # 定义initUI
    def initUI(self):
        # 设置窗口大小
        self.resize(400,150)
        # 设置窗口标题
        self.setWindowTitle('盒子布局管理器')
        # 创建水平盒子布局管理器对象
        hboxlayout=QHBoxLayout(self)   # 创建水平盒子布局管理器
        # vboxlayout=QVBoxLayout(self)
        buttonBlue=QPushButton('Blue',self) #创建按钮Blue
        buttonRed=QPushButton('Red',self)
        buttonGreen=QPushButton('Green',self)

        buttonBlue.clicked.connect(self.on_click) # 将按钮Blue与on_click连接起来（Blue是信号，on_click是槽）
        buttonRed.clicked.connect(self.on_click)
        buttonGreen.clicked.connect(self.on_click)
        # 将按钮放到水平盒子布局管理器中
        hboxlayout.addStretch(1)
        hboxlayout.addWidget(buttonBlue)
        hboxlayout.addStretch(1)
        hboxlayout.addWidget(buttonRed)
        hboxlayout.addStretch(1)
        hboxlayout.addWidget(buttonGreen)
        hboxlayout.addStretch(1)
        # 设置窗口的布局管理器
        # self.setLayout(hboxlayout)
    # 定义槽on_click。如果要作为槽函数与信号连接就需要定义为类的方法而不能作为局部函数
    def on_click(self):
        sender=self.sender() # sender函数用于返回事件源对象
        msg='您单击了{}按钮'.format(sender.text()) # text函数用于返回按钮标签上的文本
        print(msg)
# 定义main函数
def main():
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    app.exec_()
if __name__=='__main__':
    main()

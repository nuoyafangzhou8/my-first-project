# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\表单布局管理器.py

import sys
from PyQt5.QtWidgets import *

# 创建窗口类
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    # 定义初始化界面设计函数
    def initUI(self):
        # 设置窗口大小
        self.resize(400,300)
        # 设置窗口名称
        self.setWindowTitle('表单布局管理器')
        # 创建表单布局管理器对象
        form=QFormLayout(self)
        # 添加表单
        form.addRow(QLabel('用户名：'),QLineEdit())
        form.addRow(QLabel('密码：'), QLineEdit())
        # 创建水平盒子管理器对象
        hbox=QHBoxLayout(self)
        # 创建两个按钮
        button1=QPushButton('确定',self)
        button2 = QPushButton('撤销', self)
        # 按钮与on_click关联
        button1.clicked.connect(self.on_click)
        button2.clicked.connect(self.on_click)
        # 将按钮放到水平盒子管理器
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        # 将盒子放到表单管理器
        form.addRow(hbox)
    # 定义on_click函数
    def on_click(self):
        sender=self.sender()
        msg='您点击了{}'.format(sender.text())
        print(msg)
# 定义main函数
def main():
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    app.exec_()
if __name__=='__main__':
    main()



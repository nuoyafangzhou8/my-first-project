# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\键盘事件学习.py

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel

# 创建我的窗口类
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    # 定义initUI
    def initUI(self):
        # 设置窗口大小
        self.resize(400,300)
        # 设置窗口位置
        self.move(600,300)
        # 设置窗口标题
        self.setWindowTitle('键盘事件')
        # 设置文本标签
        self.label=QLabel(self)
        self.label.setText('Hello,World')
        # 设置标签位置
        self.label.move(180,120)

    # 重写键盘按下事件
    def keyPressEvent(self,event):
        self.label.setText('键盘按下')
    # 重写键盘释放事件
    def keyReleaseEvent(self,event):
        self.label.setText('键盘释放')

# 创建main函数
def main():
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()
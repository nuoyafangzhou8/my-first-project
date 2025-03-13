# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\常用控件.py

# # 文本输入控件
# import sys
# from PyQt5.QtWidgets import *
#
# # 创建窗口类
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#     # 定义初始化界面设计函数
#     def initUI(self):
#         # 设置窗口大小
#         self.resize(400,300)
#         # 设置窗口名称
#         self.setWindowTitle('表单布局管理器')
#         # 创建表单布局管理器对象
#         form=QFormLayout(self)
#         # 添加表单
#         txtUserid=QLineEdit()
#         txtUserid.setText('Tony')
#         form.addRow(QLabel('用户名：'),txtUserid)
#         txtPwd=QLineEdit()
#         txtPwd.setEchoMode(QLineEdit.Password) # setEchoMode设置文本框显示模式，QLineEdit.Password设置密码模式
#         QLineEdit()
#         form.addRow(QLabel('密码：'), txtPwd)
#         txtCom=QTextEdit()
#         form.addRow(txtCom)
#
# 定义main函数
# def main():
#     app=QApplication(sys.argv)
#     window=MyWindow()
#     window.show()
#     app.exec_()
# if __name__=='__main__':
#     main()

# 单选按钮

# import sys
#
#
# from PyQt5.QtWidgets import *
#
#
# # 创建窗口类
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     # 定义初始化界面设计
#     def initUI(self):
#         # 设置窗口大小
#         self.resize(400, 300)
#         # 设置窗口名称
#         self.setWindowTitle('单选按钮')
#
#         # 创建水平盒子布局管理器对象
#         hbox = QHBoxLayout(self)
#         # 创建单选按钮
#         rbred = QRadioButton('red')
#         rbgreen = QRadioButton('green')
#         rbblue = QRadioButton('blue')
#         rbblue.setChecked(True) # 设置该按钮默认为选中状态
#         # 创建标签
#         label = QLabel('选择你喜欢的颜色：')
#         # 添加到水平盒子布局管理器
#         hbox.addWidget(label)
#         hbox.addWidget(rbred)
#         hbox.addWidget(rbgreen)
#         hbox.addWidget(rbblue)
#         # 关联信号与槽
#         rbred.toggled.connect(self.on_click)
#         rbgreen.toggled.connect(self.on_click)
#         rbblue.toggled.connect(self.on_click)
#         # 设置采用水平盒子布局管理器
#         self.setLayout(hbox)
#     # 定义on_click
#     def on_click(self):
#         rb=self.sender()
#         if rb.isChecked(): # 判断单击的按钮是否处于选中状态
#             message='选择你喜欢的颜色是{}色'.format(rb.text())
#             print(message)
# 定义main函数
# def main():
#     app=QApplication(sys.argv)
#     window=MyWindow()
#     window.show()
#     app.exec_()
# if __name__=='__main__':
#     main()

# # 单选按钮组
# import sys
# from PyQt5.QtWidgets import *
# # 创建窗口类
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     # 定义初始化界面设计
#     def initUI(self):
#         # 设置窗口大小
#         self.resize(600, 300)
#         # 设置窗口名称
#         self.setWindowTitle('单选按钮组')
#
#         # 创建水平盒子布局管理器对象
#         hbox = QHBoxLayout()
#         # 创建垂直盒子布局管理器对象
#         vbox=QVBoxLayout()
#         # 创建单选按钮
#         btn_1=QRadioButton('男')
#         btn_2=QRadioButton('女')
#         btn_1.setChecked(True)
#         btn_3=QRadioButton('大')
#         btn_4=QRadioButton('中')
#         btn_5=QRadioButton('小')
#         btn_4.setChecked(True)
#
#         # 放入盒子布局管理器
#         hbox.addWidget(btn_1)
#         hbox.addWidget(btn_2)
#         vbox.addWidget(btn_3)
#         vbox.addWidget(btn_4)
#         vbox.addWidget(btn_5)
#         # 创建表单布局管理器
#         layout=QFormLayout(self)
#         # 添加到表单布局管理器
#         layout.addRow(QLabel('请选择性别：'),hbox)
#         layout.addRow(QLabel('请选择字号：'),vbox)
#         # 创建按钮组1
#         bg1=QButtonGroup(self)
#         bg1.addButton(btn_1)
#         bg1.addButton(btn_2)
#         bg2=QButtonGroup(self)
#         bg2.addButton(btn_3)
#         bg2.addButton(btn_4)
#         bg2.addButton(btn_5)
#         # 信号与槽进行关联
#         btn_1.toggled.connect(self.on_click1)
#         btn_2.toggled.connect(self.on_click1)
#         btn_3.toggled.connect(self.on_click2)
#         btn_4.toggled.connect(self.on_click2)
#         btn_5.toggled.connect(self.on_click2)
#     # 定义on_click1
#     def on_click1(self):
#         rb=self.sender()
#         if rb.isChecked():
#             message='您选择的性别为{}'.format(rb.text())
#             print(message)
#     # 定义on_click2
#
#     def on_click2(self):
#         rb2 = self.sender()
#         if rb2.isChecked():
#             message = '您选择的字号为{}'.format(rb2.text())
#             print(message)
# # 定义main函数
# def main():
#     app=QApplication(sys.argv)
#     window=MyWindow()
#     window.show()
#     app.exec_()
# if __name__=='__main__':
#     main()

# # 复选框
# import sys
# from PyQt5.QtWidgets import *
#
# # 定义窗口类
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#     # 定义初始化界面设计
#     def initUI(self):
#         # 设置窗口大小
#         self.resize(400,200)
#         # 设置窗口标题
#         self.setWindowTitle('复选框')
#         # 创建垂直盒子管理器
#         layout=QVBoxLayout(self)
#         # 创建标签
#         label=QLabel('选择你喜欢的编程语言：')
#         # 创建复选框
#         bt1=QCheckBox('Python')
#         bt1.setChecked(True)
#         bt2=QCheckBox('C语音')
#         bt3=QCheckBox('Java')
#         bt4=QCheckBox('C++')
#         # 将复选框放到盒子中
#         layout.addWidget(label)
#         layout.addWidget(bt1)
#         layout.addWidget(bt2)
#         layout.addWidget(bt3)
#         layout.addWidget(bt4)
#         # 关联信号与槽
#         bt1.stateChanged.connect(self.btn_clicked) # stateChanged 获取复选框标签
#         bt2.stateChanged.connect(self.btn_clicked)
#         bt3.stateChanged.connect(self.btn_clicked)
#         bt4.stateChanged.connect(self.btn_clicked)
#         # 使用垂直盒子管理器布局
#         self.setLayout(layout)
#     # 定义btn_clicked
#     def btn_clicked(self):
#         bt=self.sender()
#         if bt.isChecked():
#             message='您选择的语言有{}'.format(bt.text())
#             print(message)
# # 定义main函数
# def main():
#     app=QApplication(sys.argv)
#     window=MyWindow()
#     window.show()
#     app.exec_()
# if __name__=='__main__':
#     main()

# 列表控件
# import sys
# from PyQt5.QtWidgets import *
#
#
# # 创建窗口类
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     # 创建初始化界面设计函数
#     def initUI(self):
#         # 设置窗口大小
#         self.resize(600, 300)
#         # 设置窗口名称
#         self.setWindowTitle('列表控件')
#         # 创建列表控件
#         list = QListWidget()
#         # 添加列表项
#         list.addItem('Python')
#         list.addItem('Java')
#         list.addItems(['C语言', 'C++'])
#         # 创建表单布局管理器
#         layout = QFormLayout(self)
#         layout.addRow(QLabel('选择你喜欢的编程语言：'), list)
#         # 关联信号与槽
#         list.currentItemChanged.connect(self.selectionchange)
#
#     # 定义槽函数
#     def selectionchange(self, item):
#         print(item.text())
#
#
# # 定义main函数
# def main():
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     app.exec_()
#
#
# if __name__ == '__main__':
#     main()

# #下拉列表控件
# import sys
# from PyQt5.QtWidgets import *
#
#
# # 创建窗口类
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     # 创建初始化界面设计函数
#     def initUI(self):
#         # 设置窗口大小
#         self.resize(400, 300)
#         # 设置窗口名称
#         self.setWindowTitle('下拉列表控件')
#         # 创建列表控件
#         cb = QComboBox()
#         # 添加列表项
#         cb.addItem('苹果')
#         cb.addItem('香蕉')
#         cb.addItems(['橘子', '葡萄'])
#         # 创建表单布局管理器
#         layout = QFormLayout(self)
#         layout.addRow(QLabel('选择你喜欢的水果：'), cb)
#         # 关联信号与槽
#         cb.currentIndexChanged.connect(self.selectionchange)
#
#     # 定义槽函数
#     def selectionchange(self, idx):
#         ckb=self.sender()
#         message='您喜欢的水果是{}，索引是{}'.format(ckb.currentText(),idx)
#         print(message)
#
#
# # 定义main函数
# def main():
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     app.exec_()
#
#
# if __name__ == '__main__':
#     main()

# # 表格控件&表格事件处理
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QFont
#
#
# data=[['0036','高等数学','李放','人民邮电出版社','20000812','1'],['0004','FLASH精选','刘扬','中国纺织出版社','19990312','2']]
#
# column_names=['书籍编号','书籍名称','作者','出版社','出版日期','库存数量']
#
# # 创建窗口类
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#     def initUI(self):
#         # 设置窗口大小
#         self.resize(450, 300)
#         # 设置窗口名称
#         self.setWindowTitle('表格控件-图书信息')
#         # 创建垂直盒子管理器
#         layout=QVBoxLayout()
#         # 创建表格控件
#         table=QTableWidget()
#         # 将表格放到布局管理器中
#         layout.addWidget(table)
#         # 设置表格的行数
#         table.setRowCount(len(data))
#         # 设置表格的列数
#         table.setColumnCount(len(column_names))
#         # 设置表格的字体
#         table.setFont(QFont('微软雅黑',10))
#         # 设置表格的列标签
#         table.setHorizontalHeaderLabels(column_names)
#         # 设置表格禁止被编辑
#         table.setEditTriggers(QAbstractItemView.NoEditTriggers)
#         # 获取列视图
#         horizontalHeader=table.horizontalHeader()
#         # 设置表格的列宽根据内容自适应
#         horizontalHeader.setSectionResizeMode(QHeaderView.ResizeToContents)
#         # 设置表格列标签字体
#         horizontalHeader.setFont(QFont('微软雅黑',10))
#         # 设置表格的选择行为
#         table.setSelectionBehavior(QAbstractItemView.SelectRows)
#
#         # 设置表格的数据
#         for row in range(len(data)): # 循环每行
#             for col in range(len(data[row])): # 循环每列
#                 # 设置表格单元格（row,col）的数据，每个单元都是个QTableWidgetItem对象
#                 table.setItem(row,col,QTableWidgetItem(data[row][col]))
#         # 设置布局为垂直盒子管理
#         self.setLayout(layout)
#         # 将表格项目改变信号连接到on_click函数
#         table.itemSelectionChanged.connect(self.on_click)
#     # 定义on_click函数
#     def on_click(self):
#         table1=self.sender()
#         selectedRowNo=table1.currentRow() # 获取选中的行号
#         print(data[selectedRowNo]) # 获取选中的行数据
# # 定义main函数
# def main():
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     app.exec_()
#
#
# if __name__ == '__main__':
#     main()

# 练习一个打印出单击的表格项目
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

data = [['0036', '高等数学', '李放', '人民邮电出版社', '20000812', '1'],
        ['0004', 'FLASH精选', '刘扬', '中国纺织出版社', '19990312', '2']]

column_names = ['书籍编号', '书籍名称', '作者', '出版社', '出版日期', '库存数量']


# 创建窗口类
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口大小
        self.resize(450, 300)
        # 设置窗口名称
        self.setWindowTitle('表格控件-图书信息')
        # 创建垂直盒子管理器
        layout = QVBoxLayout()
        # 创建表格控件
        table = QTableWidget()
        # 将表格放到布局管理器中
        layout.addWidget(table)
        # 设置表格的行数
        table.setRowCount(len(data))
        # 设置表格的列数
        table.setColumnCount(len(column_names))
        # 设置表格的字体
        table.setFont(QFont('微软雅黑', 10))
        # 设置表格的列标签
        table.setHorizontalHeaderLabels(column_names)
        # 设置表格禁止被编辑
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 获取列视图
        horizontalHeader = table.horizontalHeader()
        # 设置表格的列宽根据内容自适应
        horizontalHeader.setSectionResizeMode(QHeaderView.ResizeToContents)
        # 设置表格列标签字体
        horizontalHeader.setFont(QFont('微软雅黑', 10))
        # 设置表格的选择行为
        table.setSelectionBehavior(QAbstractItemView.SelectItems)

        # 设置表格的数据
        for row in range(len(data)):  # 循环每行
            for col in range(len(data[row])):  # 循环每列
                # 设置表格单元格（row,col）的数据，每个单元都是个QTableWidgetItem对象
                table.setItem(row, col, QTableWidgetItem(data[row][col]))
        # 设置布局为垂直盒子管理
        self.setLayout(layout)
        # 将表格项目改变信号连接到on_click函数
        table.itemClicked.connect(self.on_click)

    # 定义on_click函数
    def on_click(self):
        table1 = self.sender()
        selectedRowNo = table1.currentRow()  # 获取选中的行号
        selectedColumbNo = table1.currentColumn()  # 获取选中的列号

        print(data[selectedRowNo][selectedColumbNo])  # 获取选中的数据


# 定义main函数
def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

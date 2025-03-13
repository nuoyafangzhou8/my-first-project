# # coding=utf-8
# # 代码文件：D:\LIXIAOKUN\python学习作业\事件处理.py
#
# # 引入wx
# import wx
#
# # 定义窗口类
# class MyFrame(wx.Frame):
#     def __init__(self):
#         super().__init__(None,title='事件处理',size=(300,400),pos=(100,100))
#         #我的代码
#         panel=wx.Panel(parent=self)
#         # 将 statictext 定义为实例变量.statictext如果不是MyFrame的示例变量，在on_click方法中就是无法识别的未定义变量
#         self.statictext=wx.StaticText(parent=panel,label='请单击OK按钮',pos=(110,20))
#         # 创建一个按钮
#         b=wx.Button(parent=panel,label='OK',pos=(100,50))
#         # 将按钮与处理事件绑定 事件绑定需要在构造函数内进行，以便在点击按钮时可用调用到
#         self.Bind(wx.EVT_BUTTON, self.on_click, b)
#     # 定义on_click方法，定义需要在构造函数外，MyFrame类内进行，否则会报'MyFrame' object has no attribute 'on_click'错误
#     def on_click(self,event):
#         self.statictext.SetLabelText('Hello World.')
#
# # 创建应用程序对象
# app=wx.App()
# # 创建窗口对象
# frm=MyFrame()
# # 显示窗口
# frm.Show()
# # 进入主事件循环
# app.MainLoop()


# 练习一个事件处理程序

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='开启幸运一天')
        #我的代码
        panel=wx.Panel(self)
        self.statictext=wx.StaticText(parent=panel,label='请点击OK按钮',pos=(110,20))
        b=wx.Button(parent=panel,label='OK',pos=(100,50))
        self.Bind(wx.EVT_BUTTON,self.on_click,b)
    def on_click(self,event):
        self.statictext.SetLabelText('LUCY Day!')

app=wx.App()
frm=MyFrame()
frm.Show()
app.MainLoop()

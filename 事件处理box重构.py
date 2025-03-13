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
#         # 创建垂直方向的盒子布局管理器对象vbox
#         vbox=wx.BoxSizer(wx.VERTICAL)
#         # 添加静态文本到vbox布局管理器,两个控件proportion都为1，占比为二分之一，控件水平居中，刚好包裹控件，设置顶部有边框，边框宽度为30
#         vbox.Add(self.statictext,proportion=1,flag=wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE|wx.TOP,border=30)
#         # 添加按钮b到vbox布局管理器,两个控件proportion都为1，占比为二分之一，完全填满有效空间，设置底部边框，边框宽度为10
#         vbox.Add(b,proportion=1,flag=wx.EXPAND|wx.BOTTOM,border=10)
#         #设置面板（panel)采用vbox布局管理器。两个控件都在面板上所以需要设置面板布局为盒子布局。
#         panel.SetSizer(vbox)
#
#     # 定义on_click方法，定义需要在构造函数外，MyFrame类内进行，否则会报'MyFrame' object has no attribute 'on_click'错误
#     def on_click(self,event):
#         self.statictext.SetLabelText('Hello World.')


# app=wx.App()
# frm=MyFrame()
# frm.Show()
# app.MainLoop()


# 练习一个事件处理程序

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='开启幸运一天')
        #我的代码
        panel=wx.Panel(self)
        self.statictext=wx.StaticText(parent=panel,label='请点击OK按钮',pos=(500,100))
        b=wx.Button(parent=panel,label='OK',pos=(500,500))
        self.Bind(wx.EVT_BUTTON,self.on_click,b)
        vbox=wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.statictext,proportion=2,flag=wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE|wx.TOP,border=30)
        vbox.Add(b,proportion=1,flag=wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE|wx.ALL,border=10)
        panel.SetSizer(vbox)


    def on_click(self,event):
        self.statictext.SetLabelText('LUCY Day!')

app=wx.App()
frm=MyFrame()
frm.Show()
app.MainLoop()

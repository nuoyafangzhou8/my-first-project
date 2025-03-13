# # coding=utf-8
# # 代码文件：D:\LIXIAOKUN\python学习作业\事件处理.py
#
# # 引入wx
# import wx
#
# # 定义窗口类
# class MyFrame(wx.Frame):
#     def __init__(self):
#         super().__init__(None,title='布局管理器嵌套',size=(300,120))
#         panel=wx.Panel(self)
#         self.statictext=wx.StaticText(parent=panel,label='请单击按钮')
#         b1=wx.Button(parent=panel,id=10,label='Button1')
#         b2=wx.Button(parent=panel,id=11,label='Button2')
#
#         # 创建水平方向盒子布局管理器
#         hbox=wx.BoxSizer(wx.HORIZONTAL)
#         # 添加b1到hbox布局管理
#         hbox.Add(b1,proportion=1,flag=wx.EXPAND|wx.ALL,border=10)
#         # 添加b2到hbox布局管理
#         hbox.Add(b2,proportion=1,flag=wx.EXPAND|wx.ALL,border=10)
#         # 创建垂直方向盒子布局管理器
#         vbox=wx.BoxSizer(wx.VERTICAL)
#         # 添加静态文本到vbox布局管理
#         vbox.Add(self.statictext,proportion=1,flag=wx.ALIGN_CENTER|wx.FIXED_MINSIZE|wx.TOP,border=10)
#         # 将水平布局管理器hbox嵌套到垂直布局管理器vbox中
#         vbox.Add(hbox,proportion=1,flag=wx.CENTER)
#
#         # 设置面板（panel)采用垂直布局管理器vbox
#         panel.SetSizer(vbox)
#
#         # 将两个按钮（b1和b2）单击事件绑定到self.on_click方法
#         self.Bind(wx.EVT_BUTTON,self.on_click,id=10,id2=20) #绑定id为参数id~id2的的按钮
#
#     # 定义on_click 事件方法
#     def on_click(self,event):
#         event_id=event.GetId() # 获得绑定按钮的ID
#         print(event_id)
#         if event_id==10: # 根据ID判读单击了哪个按钮
#             self.statictext.SetLabelText('Button1单击')
#         else:
#             self.statictext.SetLabelText('Button2单击')
#
#
# app=wx.App()
# frm=MyFrame()
# frm.Show()
# app.MainLoop()





# 练习一个盒子嵌套的事件处理程序

import wx

# 定义窗口类
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='开启幸运一天')
        # 定义窗口中的面板，静态文本，按钮
        panel=wx.Panel(parent=self)
        self.statictext=wx.StaticText(parent=panel,label='请单击按钮')
        b1=wx.Button(panel,id=10,label='Button1')
        b2=wx.Button(panel,id=12,label='Button2')

        # 创建水平布局盒子布局管理器hbox
        hbox=wx.BoxSizer(wx.HORIZONTAL)
        # 将b1,b2放到hbox中
        hbox.Add(b1,proportion=1,flag=wx.EXPAND|wx.ALL,border=10)
        hbox.Add(b2,proportion=1,flag=wx.EXPAND|wx.ALL,border=10)
        # 创建垂直布局盒子布局管理器vbox
        vbox=wx.BoxSizer(wx.VERTICAL)
        # 将静态文本和hbox放到vbox中布局
        vbox.Add(self.statictext,proportion=1,flag=wx.ALIGN_CENTER|wx.FIXED_MINSIZE|wx.TOP,border=10)
        vbox.Add(hbox,proportion=1,flag=wx.CENTER)

        #设置面板采用垂直布局管理模式
        panel.SetSizer(vbox)

        # 绑定事件b1,b2与self.on_click方法
        self.Bind(wx.EVT_BUTTON,self.on_click,id=10,id2=20)

    # 定义on_click事件
    def on_click(self,event):
        event_id=event.GetId()
        print(event_id)
        if event_id==10:
            self.statictext.SetLabel('Happy Day')
        else:
            self.statictext.SetLabel('Lucy Day')

# 创建app，窗口实例，并显示和加入主事件循环
app=wx.App()
frm=MyFrame()
frm.Show()
app.MainLoop()

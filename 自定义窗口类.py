# # 使用wxPython时需要导入模块wx
# import wx
# # 自定义窗口类
# class MyFrame(wx.Frame):
#     def __init__(self):
#         super().__init__(None,title='第一个xwPython程序！',size=(400,300),pos=(100,100)) # None 表示没有父窗口，size窗口大小，pos窗口位置
#         # 我的代码
# # 创建应用程序对象
# app=wx.App()
# # 创建窗口对象
# frm=MyFrame()
# # 显示窗口 窗口默认隐藏，需要调用Show（）方法才能显示
# frm.Show()
# #进入主事件循环   主要进入主事件循环，不断维持窗口运行
# app.MainLoop()

# # 使用wxPython时需要导入模块wx
# import wx
# # 自定义窗口类
# class MyFrame(wx.Frame):
#     def __init__(self):
#         super().__init__(None,title='第一个xwPython程序！',size=(400,300),pos=(100,100)) # None 表示没有父窗口，size窗口大小，pos窗口位置
#         # 我的代码
#         panel=wx.Panel(parent=self) # 创建面板对象，参数parent传递的是self，即设备面板所在的父容器为当前窗口对象
#         # 创建静态文本对象，并放到设备面板，因此parent传递的为panel，label为文本中显示的文字，pas为文本的位置
#         statictext=wx.StaticText(parent=panel,label='Hello World!',pos=(10,10))
# # 创建应用程序对象
# app=wx.App()
# # 创建窗口对象
# frm=MyFrame()
# # 显示窗口 窗口默认隐藏，需要调用Show（）方法才能显示
# frm.Show()
# #进入主事件循环   主要进入主事件循环，不断维持窗口运行
# app.MainLoop()


# 练习一个窗口

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='Python学习对话框',size=(500,500),pos=(100,200))
        # 我的代码加控件
        panel=wx.Panel(parent=self)
        statictext=wx.StaticText(parent=panel,label='好好学习，天天向上',pos=(20,20))

app=wx.App()
frm=MyFrame()
frm.Show()
app.MainLoop()

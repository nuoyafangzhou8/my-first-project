# # coding=utf-8
# # 代码文件：D:\LIXIAOKUN\python学习作业\复选框和单选按钮.py
#
# import wx
#
# # 定义窗口
# class MyFrame(wx.Frame):
#     def __init__(self):
#         super().__init__(None,title='复选框和单选按钮')
#         # 创建面板，复选框（3个），单选按钮（2个），静态文本（2个）
#         panel=wx.Panel(self)
#         cb1=wx.CheckBox(panel,id=1,label='Python') # 调用复选框方法wx.CheckBox
#         cb2=wx.CheckBox(panel,id=2,label='Java')
#         cb3=wx.CheckBox(panel,id=3,label='C++')
#         radio1=wx.RadioButton(panel,id=4,label='男',style=wx.RB_GROUP) # 设置wx.RB_GROUP为一组的开始，到下一个设置wx.RB_GROUP的wx.RadioButton前的都为一组。即radio1与radio2一组且互斥。
#         radio2=wx.RadioButton(panel,id=5,label='女') # 调用单选按钮方法wx.RadioButton
#         st1=wx.StaticText(panel,label='选择你喜欢的编程语言：')
#         st2=wx.StaticText(panel,label='选择性别：')
#         # 将3个复选框和st1放到水平布局盒子管理器hbox1
#         hbox1=wx.BoxSizer()
#         hbox1.Add(st1,flag=wx.LEFT|wx.RIGHT,border=10)
#         hbox1.Add(cb1)
#         hbox1.Add(cb2)
#         hbox1.Add(cb3)
#         # 将2个单选按钮和st2放到水平布局盒子管理器hbox2
#         hbox2=wx.BoxSizer()
#         hbox2.Add(st2,flag=wx.LEFT|wx.RIGHT,border=10)
#         hbox2.Add(radio1)
#         hbox2.Add(radio2)
#         # 将hbox1和hbox2放到垂直盒子管理器vbox
#         vbox=wx.BoxSizer(wx.VERTICAL)
#         vbox.Add(hbox1,flag=wx.ALL,border=10)
#         vbox.Add(hbox2,flag=wx.ALL,border=10)
#         # 设置面板采用采用垂直盒子管理器vbox
#         panel.SetSizer(vbox)
#         # 绑定复选框和多选事件到on_checkbox_click,wx.EVT_CHECKBOX
#         self.Bind(wx.EVT_CHECKBOX,self.on_checkbox_click,id=1,id2=3)
#         # 绑定单选框和单选事件到on_radio_click，wx.EVT_RADIOBUTTON
#         self.Bind(wx.EVT_RADIOBUTTON,self.on_radio_click,id=4,id2=5)
#     # 定义on_checkbox_click方法
#     def on_checkbox_click(self,event):
#         cb=event.GetEventObject() # 从事件对象中取出事件源对象（复选框）
#         print('选择{0}，状态{1}'.format(cb.GetLabel(),cb.IsChecked())) # cb.GetLabel()获取到复选框的标签，cb.IsChecked()获取到事件状态
#     # 定义on_radio_click方法
#     def on_radio_click(self,event):
#         rb=event.GetEventObject()
#         print('{}被选中'.format(rb.GetLabel()))
#
# # 创建app程序和frm对象实例并显示出来和加入主循环
# app=wx.App()
# frm=MyFrame()
# frm.Show()
# app.MainLoop()

# 练习一个考试内容，通过不通过的盒子布局
import wx

# 定义窗口类
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='考试结果')
        # 创建面板，复选框内容（4个），单选按钮（2个），静态文本（2个）
        panel=wx.Panel(self)
        cb1=wx.CheckBox(panel,id=1,label='语文')
        cb2=wx.CheckBox(panel,id=2,label='数学')
        cb3=wx.CheckBox(panel,id=3,label='英语')
        cb4=wx.CheckBox(panel,id=4,label='理综')
        radio1=wx.RadioButton(panel,id=5,label='通过')
        radio2=wx.RadioButton(panel,id=6,label='不通过')
        st1=wx.StaticText(panel,label='考试科目：')
        st2=wx.StaticText(panel,label='本次考试是否通过：')
        # 创建水平盒子hbox1，并把st1,复选框放进去
        hbox1=wx.BoxSizer()
        hbox1.Add(st1,flag=wx.LEFT|wx.RIGHT,border=10)
        hbox1.Add(cb1,flag=wx.ALL,border=10)
        hbox1.Add(cb2,flag=wx.ALL,border=10)
        hbox1.Add(cb3,flag=wx.ALL,border=10)
        hbox1.Add(cb4,flag=wx.ALL,border=10)
        # 创建水平盒子hbox2，并把st2,单选按钮放进去
        hbox2=wx.BoxSizer()
        hbox2.Add(st2,flag=wx.LEFT|wx.RIGHT,border=10)
        hbox2.Add(radio1,flag=wx.ALL,border=10)
        hbox2.Add(radio2,flag=wx.ALL,border=10)
        # 创建垂直盒子，并把hbox1和hbox2放进去
        vbox=wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox1,flag=wx.ALL,border=10)
        vbox.Add(hbox2,flag=wx.ALL,border=10)
        # 设置面板使用垂直盒子布局
        panel.SetSizer(vbox)
        # 绑定复选框事件到on_checkbox_click
        self.Bind(wx.EVT_CHECKBOX,self.on_checkbox_click,id=1,id2=4)
        # 绑定单选按钮事件到on_radio_click
        self.Bind(wx.EVT_RADIOBUTTON,self.on_radio_click,id=5,id2=6)
    # 定义on_checkbox_click方法
    def on_checkbox_click(self,event):
        cb=event.GetEventObject()
        print('考试科目有：{0}，状态{1}'.format(cb.GetLabel(),cb.IsChecked()))
    # 定义on_radio_click方法
    def on_radio_click(self,event):
        rb=event.GetEventObject()
        print('考试是否通过：{}'.format(rb.GetLabel()))
# 创建app，窗口并显示和加入主循环
app=wx.App()
frm=MyFrame()
frm.Show()
app.MainLoop()
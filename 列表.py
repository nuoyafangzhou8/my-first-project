# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\列表.py

import wx
#定义窗口
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='列表',size=(350,175))
        # 定义面板，静态文本，单选列表，多选列表
        panel=wx.Panel(self)
        st1=wx.StaticText(panel,label='选择你喜欢的编程语言：')
        st2=wx.StaticText(panel,label='选择你喜欢吃的水果：')
        list1=['Python','C++','Java']
        lb1=wx.ListBox(panel,choices=list1,style=wx.LB_SINGLE) # 列表第二个参数是choices，第三个是style=wx.LB_SINGLE，代表单选
        list2=['苹果','橘子','香蕉']
        lb2=wx.ListBox(panel,choices=list2,style=wx.LB_EXTENDED) # 列表第二个参数是choices，第三个是style=wx.LB_EXTENDED，代表多选
        # 创建水平盒子hbox1和hbox2，并放入
        hbox1=wx.BoxSizer()
        hbox1.Add(st1,flag=wx.LEFT|wx.RIGHT,border=5)
        hbox1.Add(lb1)
        hbox2=wx.BoxSizer()
        hbox2.Add(st2,flag=wx.LEFT|wx.RIGHT,border=5)
        hbox2.Add(lb2)
        # 创建垂直盒子vbox并放入
        vbox=wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox1,flag=wx.ALL|wx.EXPAND,border=5)
        vbox.Add(hbox2,flag=wx.ALL|wx.EXPAND,border=5)
        # 设置panel使用垂直布局盒子
        panel.SetSizer(vbox)
        # 绑定单选列表事件与on_listbox1
        self.Bind(wx.EVT_LISTBOX,self.on_listbox1,lb1) # 绑定列表用常量EVT_LISTBOX
        # 绑定多选列表事件与on_listbox2
        self.Bind(wx.EVT_LISTBOX,self.on_listbox2,lb2)
    # 定义on_listbox1
    def on_listbox1(self,event):
        listbox1=event.GetEventObject()
        print('选择{}'.format(listbox1.GetSelection())) # 获取单选选项用GetSelection方法
    # 定义on_listbox2
    def on_listbox2(self,event):
        listbox2=event.GetEventObject()
        print('选择{}'.format(listbox2.GetSelections())) # 获取多选选项用GetSelections方法
# 定义app，窗口并显示和进入主循环
app=wx.App()
frm=MyFrame()
frm.Show()
app.MainLoop()
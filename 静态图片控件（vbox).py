# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\静态图片控件.py

import wx

# 定义窗口
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='静态图片控件')
        # 创建面板，静态图片控件，按钮控件
        self.panel=wx.Panel(self)
         # 创建wx.Bitmap图像对象的列表
        self.bmps=[wx.Bitmap(r'C:\Users\Administrator\Desktop\工作频段带宽new\电压与电流-LTE.jpg',wx.BITMAP_TYPE_JPEG),
                   wx.Bitmap(r'C:\Users\Administrator\Desktop\工作频段带宽new\工作频段带宽-LTE峰速.png',wx.BITMAP_TYPE_PNG),
                   wx.Bitmap(r'C:\Users\Administrator\Desktop\工作频段带宽new\功率-LTE.png',wx.BITMAP_TYPE_PNG)]
        b1=wx.Button(self.panel,id=1,label='Button1')
        b2=wx.Button(self.panel,id=2,label='Button2')
        # 设置静态图片控件对象，self.bmps[0]是静态图片控件对象要显示的图片对象
        self.image = wx.StaticBitmap(self.panel, bitmap=self.bmps[0])
        # 创建垂直布局盒子,并放入
        vbox=wx.BoxSizer(wx.VERTICAL)
        vbox.Add(b1,proportion=1,flag=wx.EXPAND)
        vbox.Add(b2,proportion=1,flag=wx.EXPAND)
        vbox.Add(self.image,proportion=4,flag=wx.EXPAND)
        # 设置面板为垂直布局
        self.panel.SetSizer(vbox)

        # 绑定单击事件与on_click
        self.Bind(wx.EVT_BUTTON,self.on_click,id=1,id2=2)
    # 定义on_click方法
    def on_click(self,event):
        event_id=event.GetId()
        if event_id==1:
            self.image.SetBitmap(self.bmps[1]) # 重新设置图片，实现图片切换
        else:
            self.image.SetBitmap(self.bmps[2])
        self.panel.Layout()  # 重新设置panel面板布局
# 创建app和窗口并显示出来和加入主循环
app=wx.App()
frm=MyFrame()
frm.Show()
app.MainLoop()
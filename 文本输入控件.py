import wx

# 定位窗口类
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='文本输入控件')
        # 创建面板，文本输入控件和静态文本
        panel=wx.Panel(self)
        tc1=wx.TextCtrl(panel)
        tc2=wx.TextCtrl(panel,style=wx.TE_PASSWORD)
        tc3=wx.TextCtrl(panel,style=wx.TE_MULTILINE)
        userid=wx.StaticText(panel,label='用户ID:')
        pwd=wx.StaticText(panel,label='密码：')
        content=wx.StaticText(panel,label='多行文本：')
        #创建垂直布局盒子管理器
        vbox=wx.BoxSizer(wx.VERTICAL)
        #将文本输入控件和静态文本按顺序放进vbox
        vbox.Add(userid,flag=wx.EXPAND|wx.LEFT,border=10)
        vbox.Add(tc1,flag=wx.EXPAND|wx.ALL,border=10)
        vbox.Add(pwd,flag=wx.EXPAND|wx.LEFT,border=10)
        vbox.Add(tc2,flag=wx.EXPAND|wx.ALL,border=10)
        vbox.Add(content,flag=wx.EXPAND|wx.LEFT,border=10)
        vbox.Add(tc3,flag=wx.EXPAND|wx.ALL,border=10)
        #设置面板使用垂直布局
        panel.SetSizer(vbox)

        #设置tc1初始值
        tc1.SetValue('Tony')
        #获取tc1的值
        print('读取用户ID:{0}'.format(tc1.GetValue()))
# 创建app，窗口对象
app=wx.App()
frm=MyFrame()
frm.Show()
app.MainLoop()
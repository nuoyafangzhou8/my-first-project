# 使用wxPython时需要导入模块wx
import wx
# 创建应用程序对象
app=wx.App()
# 创建窗口对象
frm=wx.Frame(None,title='第一个xwPython程序！',size=(400,300),pos=(100,100)) # None 表示没有父窗口，size窗口大小，pos窗口位置
# 显示窗口 窗口默认隐藏，需要调用Show（）方法才能显示
frm.Show()
#进入主事件循环   主要进入主事件循环，不断维持窗口运行
app.MainLoop()
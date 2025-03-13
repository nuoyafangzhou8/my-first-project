# conding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\线程停止.py

# import threading
# import time
# # 线程停止变量
# isruning=True # 创建一个线程停止变量控制线程结束
#
# # 工作线程体函数
# def workthread_body(): # 工作线程体执行一些任务
#     while isruning: # 工作线程体“死循环”
#         # 线程开始工作
#         print('工作线程执行中...')
#         # 线程休眠
#         time.sleep(5)
#     print('工作线程结束。')
#
# # 控制线程体函数
# def controlthread_body(): # 控制线程体从控制台读取指令，根据指令线程停止变量
#     global isruning # 由于需要在线程体重修改变量isruning,因此需要将isruning声明为global
#     while isruning: # 控制线程体“死循环”
#         # 从键盘输入停止指令exite
#         command=input('请输入停止指令：')
#         if command=='exit':
#             isruning=False
#             print('控制线程结束。')
#
# # 主线程
# # 创建工作线程对象workthread
# workthread=threading.Thread(target=workthread_body) # 工作线程用来执行一些任务
# # 启动线程workthread
# workthread.start()
#
# # 创建控制线程对象controlthread
# controlthread=threading.Thread(target=controlthread_body) # 控制线程控制修改线程停止变量
# # 启动控制线程controlthread
# controlthread.start()

# 练习一个累加函数，直到输入exit停止

import threading
import time

# 定义线程停止变量
isruning=True

# 工作线程从0开始累加
def workthread_body():
    i=0
    value = 0
    while isruning:
        # 执行工作线程操作
        i=i+1
        value=value+i
        # 线程休眠
        time.sleep(1)
        print('第{0}次执行后value值为{1}'.format(i,value))
    print('工作线程结束')
# 控制线程
def controlthread_body():
    global isruning
    while isruning:
        command = input('请输入停止标志exit:')
        if command=='exit':
            isruning=False
    print('控制线程结束')

# 主线程
# 创建工作线程对象
workbody=threading.Thread(target=workthread_body)
# 启动工作线程
workbody.start()
# 创建控制线程对象
controlbody=threading.Thread(target=controlthread_body)
# 启动控制线程
controlbody.start()

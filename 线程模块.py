# # coding=utf-8
# # 代码文件：D:\LIXIAOKUN\python学习作业\线程模块.py
#
# # 线程模块
# import threading
#
# # 当前线程对象
# t=threading.current_thread()
# # 当前线程名称
# print(t.name)
# # 返回当前处于活跃状态的线程个数
# print(threading.active_count())
# # 当前主线程对象
# t=threading.main_thread()
# # 主线程名
# print(t.name)

# # 自定义函数实现线程体
#
# import threading
# import time
#
# # 线程体函数
# def thread_body():
#     # 当前线程对象
#     t=threading.current_thread()
#     for n in range(5):
#         # 当前线程名
#         print('第{0}次执行线程{1}'.format(n,t.name))
#         # 线程休眠
#         time.sleep(2) # 该函数可以使当前线程休眠2秒，只有当前线程休眠，其它线程才有机会执行
#     print('线程{0}执行完成!'.format(t.name))
#
# # 主线程
# # 创建线程对象t1
# t1=threading.Thread(target=thread_body) # 指定函数体的函数名，注意在函数名后面不要跟小括号
# # 创建线程对象t2
# t2=threading.Thread(target=thread_body,name='Mythread')
# # 启动线程t1
# t1.start()
# # 启动线程t2
# t2.start()

# 自定义线程类实现线程体

import threading
import time

# 定义子线程类
class smallThread(threading.Thread): # 自定义线程类，继承thread类
    def __init__(self,name=None): # 定义线程类的构造方法，name参数是线程名
        super().__init__(name=name)
    # 线程体函数
    def run(self): # 重写父类Thread的run方法
        # 当前线程对象
        t=threading.current_thread()
        for n in range(5):
            # 当前线程名
            print('第{0}次执行线程{1}'.format(n,t.name))
            # 线程休眠
            time.sleep(2)
        print('线程{0}执行完成！'.format(t.name))
# 主线程
# 创建线程对象t1
t1=smallThread()
# 创建线程对象t2
t2=smallThread(name='MyThread') # 通过自定义线程类创建线程对象
# 启动线程t1
t1.start()
# 启动线程t2
t2.start()


smal
# coding=utf-8
# 代码文件：D:\LIXIAOKUN\python学习作业\等待线程结束.py

# import threading
# import time
#
# # 共享变量
# value=[] # 定义一个共享变量value,该变量是多个线程都可以访问的变量
# # 线程体函数
# def thread_body():
#     # 当前线程对象
#     print('t1子线程开始...')
#     for n in range(5):
#         print('t1子线程执行...')
#         value.append(n) # 在子线程体重修改变量value的内容
#         # 线程休眠
#         time.sleep(2)
#     print('t1子线程结束。')
# # 主线程
# print('主线程开始执行...')
# # 创建线程对象t1
# t1=threading.Thread(target=thread_body)
# # 启动线程进程t1
# t1.start()
# # 主线程被阻塞，等待t1线程结束
# t1.join() # 在当前线程（主线程）中调用t1的join（）方法，因此会导致当前线程阻塞，等待t1线程结束
# print('value={0}'.format(value)) # t1线程结束，继续执行，访问并输出变量value
# print('主线程继续执行...')

# 练习一个等待线程结束,主进程是1到4累加，子进程是值乘以2。当主进程进行到3的时候进入子进程。
import threading
import time
value=0
# 子线程
def thread_body():
    global value
    value=value*2
    time.sleep(2)
# 主线程
for i in range(5):
    value=value+i # 注意当i=3时先执行此步骤再进到子进程
    print('i={0}时，value={1}'.format(i,value))
    if i==3:
        # 创建t1子线程对象
        t1 = threading.Thread(target=thread_body)
        # 启动子线程t1
        t1.start()
        t1.join()
        print('子线程结束后value值为：{}'.format(value))
print('主线程继续')



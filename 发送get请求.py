# # coding=utf-8
# # 代码文件：D:\LIXIAOKUN\python学习作业\发送get请求py
# # 发送get请求
# import urllib.request
#
# url='http://localhost:8080/docs/?action=query&ID=10' # 请求URL地址
# # 创建Request对象，默认是GET请求
# req=urllib.request.Request(url)
# # 发送网络请求，response是需要释放的对象，可以使用withas代码块管理和释放
# with urllib.request.urlopen(req) as response:
#     data=response.read() # 读取数据，为字节序列数据
#     json_data=data.decode() # 将字节序列数据转换为字符串
#     print(json_data)

# # 发送post请求
# import urllib.request
#
# url='http://localhost:8080/docs/'
# # 准备HTTP参数
# params_dict={'action':'query','ID':'10'} # 准备将参数放到字典中
# params_str=urllib.parse.urlencode(params_dict) # 将字典参数转换为字符串，形式为action=query&ID=10
# print(params_str)
#
# #字符串转换为字节序列对象
# params_bytes=params_str.encode() # 发送post请求时的参数必须是以字节序列形式发送
# # 发送post请求
# req=urllib.request.Request(url,data=params_bytes) # 创建Request对象,其中提供了data参数，这种请求是post请求
# with urllib.request.urlopen(req) as response:
#     data=response.read()
#     json_data=data.decode()
#     print(json_data)


# Json解码
import urllib.request
import json

url='http://localhost:8080/docs/?action=query&ID=10' # 请求URL地址
# 创建Request对象，默认是GET请求
req=urllib.request.Request(url)
# 发送网络请求，response是需要释放的对象，可以使用withas代码块管理和释放
with urllib.request.urlopen(req) as response:
    data=response.read() # 读取数据，为字节序列数据
    json_data=data.decode() # 将字节序列数据转换为字符串
    print('JSON字符串:',json_data)

    py_dict = json.loads(json_data)
    print('备忘录ID:',py_dict['ID'])
    print('备忘录日期：',py_dict['CDate'])
    print('备忘录内容：',py_dict['Context'])
    print('用户ID:',py_dict['UserID'])

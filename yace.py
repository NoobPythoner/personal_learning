#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#设置路径:Defualt Settings---Editor--File and Code Templates

import time
import json
import random
from urllib.error import URLError
from urllib import request
import http.client
import requests
import gevent
from gevent import monkey
#from multiprocessing import Pool
# 补丁
monkey.patch_all()

#** 请求URL **
url = 'http://10.176.139.189:8080/nlp/segmentation'
headers = {'Content-Type': 'application/json'}

error=[]
error1 = []
count = 0
query_list = ['你好','今天天气真好','好开心啊','明天是周五了','好想买房子啊','十一的机票你买好了吗？']

def run():
    """三种模拟请求"""
    #num = random.randint(1, 9)
    #data = make_data(query_list)
    global error
    global count
    while True:
        for i in query_list:
            data1 = {'AppId':'triotest',
           'longitude':113.937862,
           'latitude':22.521726,
           'gpsType':'GCT02',
           'sig':'b893e',
           'query':i
           }
            print(data1)
            try:
                resp = requests.post(url=url, data = json.dumps(data1), headers=headers)
                count = count + 1
                if count % 1000 == 0:
                    print(count)
                print("状态:\n", resp)
                print("请求头:\n", resp.headers)
                print("服务器返回值为:\n", resp.content.decode())
                if resp.status_code != 200:
                    error.append("0")
                elif resp.status_code == 200:
                    pass  # 正常返回的情况下
            except Exception as e:
                error1.append("re0")
                print(count)
                print('请求错误：', e)

def call_gevent(count):
    """调用gevent 模拟高并发"""
    begin_time = time.time()
    run_gevent_list = []
    for i in range(count):
        print('--------------%d--Test-------------' % i)
        run_gevent_list.append(gevent.spawn(run()))
    gevent.joinall(run_gevent_list)
    end = time.time()
    print('单次测试时间（平均）s:', (end - begin_time) / count)
    print('累计测试时间 s:', end - begin_time)
    print("运行失败用例数:",error.count("0"))
    print("运行报错数:",error.count("re0") )


if __name__ == '__main__':
    # 10万并发请求
    test_count = 200
    call_gevent(count = test_count)
    


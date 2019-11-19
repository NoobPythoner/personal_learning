#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import uuid
import pandas as pd

url = 'http://172.17.18.18?/sessionid=?dfdf&query=?'
data1 = pd.read_excel(r'C:\Users\Administrator\Desktop\query_test.xlsx')
session_id = data1['id']
query_text = data1['query']
print('f')
count = 0
filename = "result"+str(count)
while True:

    m = len(session_id)
    data = []
    temp_id = []
    #temp_id = [uuid.uuid1() for i in range(m)]
    #mm = session_id[0]
    #for i in range(1,m):
        #if session_id[i] == session_id[i-1]:
           #temp_id[i] = temp_id[i-1]
    temp_id.append(uuid.uuid1()) # temp_id[0]先赋值
    for i in range(1, m):
        if session_id[i] == session_id[i - 1]:
            temp_id.append(temp_id[i - 1])   # 给temp_id[i]赋值,i从1开始
        else:
            temp_id.append(uuid_uuid1())

    for x,y in zip(temp_id,query_text):
        url_all =''
        r = requests.post(url_all,data=json.dumps(data3))
        if r.status_code == 200:
            data.append(r)
        else if r.status_code in (500,501,502....)
             print("服务器故障，睡眠半小时后重新发送")
             sleep(30)
             r= requests.post(...)  #此处或者做成循环，每次睡醒就发送请求，如果还是500系列，继续循环，如果是其他号码，就跳出循环
        else:
            print("报错,错误码: %s" % r.status_code)
            data.append('请求错误')

    path = r'C:\Users\Administrator\Desktop\'
    filename = "result"+str(count)
    data_result = pd.to_excel(path+filename)
    count=count+1







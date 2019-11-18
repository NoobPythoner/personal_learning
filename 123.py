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
    temp_id = [uuid.uuid1() for i in range(m)]
    #mm = session_id[0]
    for i in range(1,m):
        if session_id[i] == session_id[i-1]:
           temp_id[i] = temp_id[i-1]
    for x,y in zip(temp_id,query_text):
        url_all =''
        r = requests.post(url_all,data=json.dumps(data3))
        if r.status_code == 200:
            data.append(r)
        else:
            data.append('请求错误')

    path = r'C:\Users\Administrator\Desktop'
    filename = "result"+count
    data_result = pd.to_excel(r'C:\Use')
    count=count+1







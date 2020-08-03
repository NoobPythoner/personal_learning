#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import numpy as np
from sklearn.externals import joblib
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
############Log设置###################################
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("./logs.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

logger.addHandler(handler)
logger.addHandler(console)
#######################################################
model = joblib.load('./model.pkl')
@app.route('/predict', methods=['POST'])
def hotEventPredict():
    """
     :readMe:回归模型预测热榜标题阅读量
     :param:输入长度为10的一组数
     [
        {"Title":"xxxx","readAmount":[]},
        {"Title":"xxxx","readAmount":[]},
        .........
]
     :return:返回由这一组数据预测得到的结果

    """
    records = request.get_json()
    if len(records[0]["readAmount"]) != 10:
        return jsonify({"result": "err", "message": "输入参数不足10个！"})
    try:
        dataX = [record['readAmount'] for record in records]
    except Exception as e:
        logger.info(e)
        return jsonify({"result": "err", "message": e})
    res = model.predict(dataX)
    result = [int(np.exp(y) - 1) for y in res]

    return jsonify({"result":"ok","data":result})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

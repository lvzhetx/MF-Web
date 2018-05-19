# -*- coding: utf-8 -*-
# File  : mf_server.py
# Author: Tomcat
# Date  : 2018/4/8 
# USAGE
# Submit a request via cURL:
# 	 'http://localhost:5000/predict' post内容为words的字符串，用空格隔开
# Submit a request via Python:
#	python request.py

from keras.applications import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
import flask
from flask import request
import io
import sys
import MoodFeeler as mf
app = flask.Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
	data = {"success": False}

	# 确保语句正确post
	if flask.request.method == "POST":
		if flask.request.form['words']:

			preds = mf.predict(request.form['words'].split(" "))
			# 表明请求正确
			data["success"] = True
	print(preds[0][1])
	return ('此语句是积极的概率%.8lf   消极的概率%.8lf'%(preds[0][0],preds[0][1]))

if __name__ == "__main__":
	print(("*正在在此服务器加载模型和Flask..."
		"请等待操作完成！"))
	app.run(host='0.0.0.0') #设置为0.0.0.0即可支持外部IP访问

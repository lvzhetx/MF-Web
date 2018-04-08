
import requests
MFURL = "http://127.0.0.1:5000/predict"

# submit the request

r = requests.post(MFURL, data = {'words':'今天好开心啊草拟吗'}).json()

# ensure the request was sucessful
if r["success"]:
		print("请求成功")
# otherwise, the request failed
else:
	print("请求失败")

#  基于Flask的RESTfulAPI of MoodFeeler

---

### 模型数据下载
http://qn.lvzhetx.com/o_1cdsmbsr0105d1o6115g91r9218kha.h5

---

### 环境要求：
graphviz=0.8.2
h5py=2.7.1
jieba=0.39
Keras=2.1.5
lxml=3.8.0
matplotlib=2.0.2
numpy=1.14.2
opencv-python=3.4.0.12
pandas=0.22.0
pydot-ng=1.0.0
scikit-image=0.13.1
scikit-learn=0.19.0
tensorboard=1.6.0
tensorflow=1.6.0
tensorflow-tensorboard=1.5.1
zhon=1.1.5

---

### 如何使用

1.模型下载后放在MoodFeeler文件夹下，命名为test_model.h5
test_model.h5

2.运行mf_server.py

3.看见端口号出来之后就可以post了

---


### 示例代码


```
<form name="form" action="http://45.40.242.154:5000/predict" onsubmit="return validateForm()" method="post" >
    <div class="form-group">
	    <label class="sr-only" for="form-email">句子</label>
    	<input type="text" name="words" placeholder="今天好开心啊" id="words">
    </div>
<button type="submit" >提交</button>
</form>
```

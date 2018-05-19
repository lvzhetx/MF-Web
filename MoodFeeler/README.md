# MoodFeeler

## 运行环境

Python 3.6.3

依赖在 requirements.txt 文件里

```bash
pip install -r requirements.txt # 安装依赖
```

* 将test_model.h5放置在model目录下


## 运行示例 
```
>>> import MoodFeeler as mf
>>> mf.predict(['你这么努力，忍受那么多寂寞和纠结，我们也没觉得你有多优秀。', '微笑拥抱每一天，做像向日葵般温暖的女子'])

array([[0.30009958, 0.6999004 ],
       [0.8481712 , 0.15182886]], dtype=float32)
```

---
* 要求向predict中传入一个list，list由str组成，返回一个ndarray，每行中的第一个实数为对应句子positive的概率，第二个实数为negative的概率。
---

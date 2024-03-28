# [GUET-CTF2019]zips

## 知识点

`压缩包及时间戳密码爆破`

## 解题

先爆破`222.zip`

密码为`723456`

`111.zip`文件里`伪加密`

解密后`setup.sh`

```
#!/bin/bash
#
zip -e --password=`python -c "print(__import__('time').time())"` flag.zip flag
```

是`python2`运行的

根据时间往前推获取密码

```
1701014072.27
```

这样的格式,纯出自,只需要`1xxxxxxxxx.xx`这样的数字格式爆破即可

最终密码为`1558080832.15`
# hashcat

## 知识点

`office2john`

## 解题

What kind of document is this_

`010editor`查看后发现是个`office`文件

有文档加密

使用`office2john`

```
python3 .\office2john.py '.\What kind of document is this_.doc' > hash.txt
john --wordlist=top6000.txt res.txt
john --show res.txt
```

![image-20231130235408815](./img/85-1.png?lastModify=1711207788)

后缀改为`pptx`

在里面发现一个隐藏的文本框,设置字体为红色即可

![image-20231130235719667](./img/85-2.png?lastModify=1711207788)
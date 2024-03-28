# [GUET-CTF2019]soul sipse

## 知识点

`steghide无密码分解`

`Unicode`

## 解题

![image-20231204202803375](./img/90-1.png)

没有什么有效信息,`binwalk`试试

![image-20231204203042638](./img/90-2.png)

![image-20231204203117398](./img/90-3.png)

`steghide`无密码分解出`download.txt`

```
https://share.weiyun.com/5wVTIN3
```

下载得到`GUET.png`，修改为正确的`PNG`文件头

![在这里插入图片描述](./img/90-4.png)

保存得到正常的图片。如下

![在这里插入图片描述](./img/90-5.png)

`Unicode`解码

![在这里插入图片描述](./img/90-6.png)

```
 4070
+1234
------
 5304
```

```
flag{5304}
```


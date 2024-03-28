# [SUCTF 2019]Game

## 知识点

`lsb低位隐写`

`3DES密文特征Salted`

## 解题

首先在`src.zip`下面找到了一个`index.html`,`base32`解码成功

![image-20231128205224012](./img/59-1.png)

然后来看照片,`010editor`和`zsteg`都没找到什么东西

用`stegsolve`看看有没有`lsb低位隐写`

![image-20231128205112619](./img/59-2.png)

发现一串`base64`字符串

![image-20231128205653175](./img/59-3.png)

以`Salted`开头,可能是`AES`或`3DES`

https://www.sojson.com/encrypt_triple_des.html

![image-20231128210342031](./img/59-4.png)
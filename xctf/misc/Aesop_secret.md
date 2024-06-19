# Aesop_secret

## 知识点

`AES加解密`

## 解题

首先得到一个`GIF`动图，使用`GIMP`打开显示`ISCC`

![](./img/Aesop_secret-1.png)

然后用`strings`发现一串加密字符串，看起来是`rabbit`或者`AES 3DES`之类的 一个个解，发现是`AES` 密钥为`ISCC`两次解密即可

![](./img/Aesop_secret-2.png)

![](./img/Aesop_secret-3.png)

![](./img/Aesop_secret-4.png)
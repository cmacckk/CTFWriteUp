# [MRCTF2020]Unravel!!

## 知识点

`AES解密`

`SilentEye`

## 解题

三个文件

```
c@pc /m/c/U/c/D/a/Unravel> ll
total 11M
-rwxrwxrwx 1 c c 399K Mar 12  2020 JM.png*
-rwxrwxrwx 1 c c 5.8M Mar 15  2020 Look_at_the_file_ending.wav*
-rwxrwxrwx 1 c c 4.8M Mar 12  2020 win-win.zip*
```

先看看第一个文件

![image-20231130105832762](./img/73-1.png)

似乎是`base64`,解码看看

![image-20231130111631531](./img/73-2.png)

发现`salted`,应该是`AES`或`3DES`

找密钥,`binwalk`看看照片

![image-20231130111834449](./img/73-3.png)

发现`AES`密钥

![image-20231130112245185](./img/73-4.png)

使用`SilentEye`[Decode](https://so.csdn.net/so/search?q=Decode&spm=1001.2101.3001.7020)`Ending.wav`

![image-20231130112427165](./img/73-5.png)
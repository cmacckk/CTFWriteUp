# [NPUCTF2020]碰上彩虹，吃定彩虹！

## 知识点

`autokey`

`零宽度字符隐写`

`encrypto软件`

## 解题

解压出三个文件

```
total 32K
-rwxrwxrwx 1 c c 123 Apr 14  2020 lookatme.txt*
-rwxrwxrwx 1 c c 565 Apr 19  2020 maybehint.txt*
-rwxrwxrwx 1 c c 30K Apr 19  2020 secret*
```

首先`010editor`打开`lookatme.txt`

发现有换行和后面有数据

![image-20231217180123952](./img/134-1.png)

应该是`morse`码,`20`看作`.`,`09`看作`-`

```
.- ..- - --- -.- . -.--
```

`Morse`解密后为`AUTOKEY`

脚本爆破

![image-20231217181536343](./img/134-2.png)

得到结果` CONGRATULATIONSONFINDINGMYSECRETNOWIWILLGIVEYOUTHEPASSWORDITISIAMTHEPASSWD`

查看`maybehint.txt`

![image-20231217181734453](./img/134-3.png)

`零宽度字符隐写`

```python
import zwsp_steg

c = '​​​​​​‌​‍​‌​​​​​​‌‌​‌​​​​​​​​‌​‌‍​​​​​​‌‌‌​​​​​​​​​‌​‌‍​​​​​​‌​‍‍‍​​​​​​‌‌​​‍​​​​​​‌‌​‌​​​​​​​‌‌‌​‍​​​​​​​‌​‌‍​​​​​​​‍‍‍​​​​​​​‌​​‌​​​​​​​​‍‌‍‌​​​​​​‌​​​‍​​​​​​​‍‌​​'
    
print(zwsp_steg.decode(c, mode=zwsp_steg.MODE_ZWSP))
```

从`sublime`里复制到代码

```
do u know NTFS?
```

用`NtfsStreamEditor2`打开,注意要用`7zip`解压,不然找不到隐藏文件

![image-20231217202828459](./img/134-4.png)

一堆乱码且多次出现高频词,应该是词频分析

```python
from collections import Counter

with open('./demo.txt', 'r') as f:
    c = Counter(f.read())
    sorted_char_count = sorted(c.items(), key=lambda x: x[1], reverse=True)
    for res in sorted_char_count:
        print(res[0], end='')
```

运行结果

```
ZW5jcnlwdG8=
```

`base64`解码

`encrypto`

`010editor`分析`secret`文件，找了下文件头发现没有匹配的文件类型

到这边又有新东西了，`encrypto`加密

下载`encrypto`软件

对`1.txt`进行加密，会让你输入`hint`和`password`，加密后生成`1.crypto`文件

将`secret`后缀加上`crypto`即可打开

密钥为`iamthepasswd`

![image-20231217212227805](./img/134-5.png)

删除后重新输入即可

- 仔细观察图片可以发现，由五种不同颜色的横条分隔开的六块⻩色有略微深浅的差异， 用 `gimp` 或 `ps` 打开提取一下颜色
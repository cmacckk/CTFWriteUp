# [RCTF2019]disk

## 知识点

`不同密码挂载内容不同`

## 解题

`vmdk`文件

`010editor`搜索关键字

![image-20231206104007681](./img/108-4.png)

接着使用`7zip`打开，得到`FAT`文件

![image-20231206104214149](./img/109-2.png)

`FAT`文件就可以使用`VeraCrypt`进行[挂载](https://so.csdn.net/so/search?q=挂载&spm=1001.2101.3001.7020)

![image-20231206104804345](./img/109-3.png)

进入挂载的`A`盘

![image-20231206104844233](./img/109-4.png)

![image-20231206104904636](./img/109-5.png)

图片名提示：`useless file for ctf just ignore it`，图片无用，在`password.txt`有个`Password 2`，这里就有个盲区知识点，在挂载输入密码的时候，不同的密码可以进入不同的文件系统

重新挂宅，输入密码为：`RCTF2019`

![image-20231206105017740](./img/109-6.png)

无法直接打开

![image-20231206105106414](./img/109-7.png)

`010editor`->`file`->`Open Drive`,我环境好像有点问题

使用`winhex`,`tools`->`Open Drive`,有报错,点`ok`,即可打开

![image-20231206105701574](./img/109-8.png)

![image-20231206105825471](./img/109-9.png)

找到第二段`flag`
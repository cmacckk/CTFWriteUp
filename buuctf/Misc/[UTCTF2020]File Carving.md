# [UTCTF2020]File Carving

## 知识点

`图片隐写文件`

`ELF文件`

## 解题

![image-20231130122525896](./img/78-1.png)

发现好像有其他文件,`binwalk`一下,`010editor`看一下`hidden_binary`,发现是`elf`文件,即`linux`可执行文件,运行看看

![image-20231130122658880](./img/78-12.png)

![image-20231130122714621](./img/78-3.png)
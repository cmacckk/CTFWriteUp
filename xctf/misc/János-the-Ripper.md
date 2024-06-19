# János-the-Ripper

## 知识点

`john`

## 解题

看题目猜测是`爆破`，通过`file`命令发现是`zip`文件，然后使用`zip2john`导出

![](./img/János-the-Ripper-2.png)

然后使用`john`破解

![](./img/János-the-Ripper-1.png)

发现密码为`fish`，解压即可获得`flag`

![](./img/János-the-Ripper-3.png)
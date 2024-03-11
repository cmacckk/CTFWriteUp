# [FireshellCTF2020]Caas

## 知识点

`c语言预处理`

## 解题

刚开始叫我们输入代码编译，不知道是什么语言，尝试一下`js`

![](./img/[FireshellCTF2020]Caas-1.png)

发现是`c`语言的编译器

包含一个文件作为头文件时。会由于文件内容不能解析而报错

![](./img/[FireshellCTF2020]Caas-2.png)

那么直接包含`/flag`就可以通过报错获得`flag`

![](./img/[FireshellCTF2020]Caas-3.png)
# simple_transfer

## 知识点

`流量分析`

`文件隐藏`

## 解题

首先使用`wireshark`打开流量包，没有发现什么东西

然后使用`binwalk`查看有没有隐藏文件时，发现了一个`pdf`文件

![](./img/simple_transfer-1.png)

然后用`binwalk`导出失败，使用`foremost`导出后发现`flag`

![](./img/simple_transfer-2.png)
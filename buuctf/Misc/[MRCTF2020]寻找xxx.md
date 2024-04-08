# [MRCTF2020]寻找xxx

## 知识点

`频谱图`

`dtmf2num`

`sonic visualier`

## 解题

`拨号声音`

得到一个`wav`文件

听起来是拨号，用 `dtmf2num` 获取拨号内容 ：

![image-20231206162412105](./img/125-6.png)

提交到公众号不行，应该是有错误，分析[频谱图](https://so.csdn.net/so/search?q=频谱图&spm=1001.2101.3001.7020)：

 一个拨号音是由一个高频和一个低频组成，拨号频谱表如下：

![ ](/Users/gongtaiyun/security/CTFWriteUp/buuctf/Misc/img/126-2.png)

用`sonic visualier`打开：

![image-20231206162649168](./img/126-3.png)

![ ](./img/126-4.png)


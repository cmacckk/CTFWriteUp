# [CISCN2019 华东南赛区]Web11

## 知识点

`SSTI`

`smarty`

## 解题

看到题目首页大概就猜测到是模板注入

![](./img/[CISCN2019 华东南赛区]Web11-1.png)

注入点应该是`XFF`

![](./img/[CISCN2019 华东南赛区]Web11-2.png)

直接用`smarty`的`payload`打就行

![](./img/[CISCN2019 华东南赛区]Web11-3.png)

![](./img/[CISCN2019 华东南赛区]Web11-4.png)
# [GKCTF 2021]签到

## 知识点

`HTTP流量分析`

## 解题

追踪`http`流

![image-20231130002915313](./img/71-1.png)

发现会返回`hex`编码

解码后发现是需要`reverse`一下

最后导出`http`流中发现数据

解码后发现

![image-20231130003046893](./img/71-2.png)

**整理一下得到flag{Welc0me_GkC4F_m1siCCCCCC!}**
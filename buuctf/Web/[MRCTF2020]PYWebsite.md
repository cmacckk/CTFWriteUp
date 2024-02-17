# [MRCTF2020]PYWebsite

## 知识点

`X-Forwarded-For`

`脑洞`

## 解题

要求有授权码才可以获得`flag`,随便输入发现弹窗，估计是前端验证，查看源码发现判断条件

![](./img/[MRCTF2020]PYWebsite-1.png)

用这串`hash`值去`cmd5`查，发现是付费记录，继续看发现有`flag.php`，访问

![](./img/[MRCTF2020]PYWebsite-2.png)

用`XFF`头试试，发现回显`flag`

![](./img/[MRCTF2020]PYWebsite-3.png)


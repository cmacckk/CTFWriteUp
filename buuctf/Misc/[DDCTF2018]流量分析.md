# [DDCTF2018]流量分析

## 知识点

`HTTP流量分析`

`SSL`

## 解题


 > 流量分析
> 200pt
>
> 提示一：若感觉在中间某个容易出错的步骤，若有需要检验是否正确时，可以比较MD5: 90c490781f9c320cd1ba671fcb112d1c
> 提示二：注意补齐私钥格式
> -----BEGIN RSA PRIVATE KEY-----
> XXXXXXX
> -----END RSA PRIVATE KEY-----

根据提示要找到RSA KEY。

```
tcp contains "KEY"
```

![image-20231130113354246](G:/CTFWriteUp/buuctf/Misc/img/74-3.png)

![image-20231130113637784](G:/CTFWriteUp/buuctf/Misc/img/75-1.png)

![image-20231130113730756](G:/CTFWriteUp/buuctf/Misc/img/75-2.png)

![image-20231130113924858](G:/CTFWriteUp/buuctf/Misc/img/75-3.png)

保存为`jpg`

![image-20231130114004252](G:/CTFWriteUp/buuctf/Misc/img/75-4.png)

`OCR`识别后修改错处

```
-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQDCm6vZmclJrVH1AAyGuCuSSZ8O+mIQiOUQCvN0HYbj8153JfSQ
LsJIhbRYS7+zZ1oXvPemWQDv/u/tzegt58q4ciNmcVnq1uKiygc6QOtvT7oiSTyO
vMX/q5iE2iClYUIHZEKX3BjjNDxrYvLQzPyGD1EY2DZIO6T45FNKYC2VDwIDAQAB
AoGAbtWUKUkx37lLfRq7B5sqjZVKdpBZe4tL0jg6cX5Djd3Uhk1inR9UXVNw4/y4
QGfzYqOn8+Cq7QSoBysHOeXSiPztW2cL09ktPgSlfTQyN6ELNGuiUOYnaTWYZpp/
QbRcZ/eHBulVQLlk5M6RVs9BLI9X08RAl7EcwumiRfWas6kCQQDvqC0dxl2wIjwN
czILcoWLig2c2u71Nev9DrWjWHU8eHDuzCJWvOUAHIrkexddWEK2VHd+F13GBCOQ
ZCM4prBjAkEAz+ENahsEjBE4+7H1HdIaw0+goe/45d6A2ewO/lYH6dDZTAzTW9z9
kzV8uz+Mmo5163/JtvwYQcKF39DJGGtqZQJBAKa18XR16fQ9TFL64EQwTQ+tYBzN
+04eTWQCmH3haeQ/0Cd9XyHBUveJ42Be8/jeDcIx7dGLxZKajHbEAfBFnAsCQGq1
AnbJ4Z6opJCGu+UP2c8SC8m0bhZJDelPRC8IKE28eB6SotgP61ZqaVmQ+HLJ1/wH
/5pfc3AmEyRdfyx6zwUCQCAH4SLJv/kprRz1a1gx8FR5tj4NeHEFFNEgq1gmiwmH
2STT5qZWzQFz8NRe+/otNOHBR2Xk4e8IS+ehIJ3TvyE=
-----END RSA PRIVATE KEY-----
```

![在这里插入图片描述](G:/CTFWriteUp/buuctf/Misc/img/75-5.png)

提供`SSL`私钥之后就可以查看`http`传输内容了

![image-20231130114449521](G:/CTFWriteUp/buuctf/Misc/img/75-6.png)

追踪`http`流
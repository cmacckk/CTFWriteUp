# [BJDCTF2020]认真你就输了

## 知识点

`foremost`

## 解题

`xls`文件打开后说是`flag`在下面

`linux`用`strings`命令查一下

```
$ strings 10.xls| grep flag   
xl/charts/flag.txtK
xl/charts/flag.txt
```

直接`foremost`分离后即可获取到`flag`

![image-20231125173503920](file:///G:/CTFWriteUp/buuctf/Misc/img/19-1.png?lastModify=1711202731)
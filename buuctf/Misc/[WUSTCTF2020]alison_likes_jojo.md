# [WUSTCTF2020]alison_likes_jojo

## 知识点

`binwalk`

`zip压缩包密码爆破`

`outguess`

## 解题

两个文件

发现`boki.jpg`有合并文件

`binwalk`分离

分离出一个`zip`压缩包,`6`位数字爆破

得到`base.txt`

```
WVRKc2MySkhWbmxqV0Zac1dsYzBQUT09
```

`base64`三次解密后为

`killerqueen`

应该是密钥之类的,试试使用`outguess`

```bash
outguess -r -k killerqueen jljy.jpg data.txt
```

获得`flag`
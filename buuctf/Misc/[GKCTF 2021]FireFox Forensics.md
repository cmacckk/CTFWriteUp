# [GKCTF 2021]FireFox Forensics

## 知识点

`firefox登录凭证`

## 解题

> 取证大佬说这是一份登录凭证文件

题目提示是`火狐(firefox)`的登陆凭证，使用[Firepwd工具](https://github.com/lclevy/firepwd)破解。将`key4.db`、`logins.json`复制到`firepwd`目录下，用`firepwd.py`破解。

```bash
python3 .\firepwd.py .\logins.json
```

![image-20231206103401615](./img/108-3.png)
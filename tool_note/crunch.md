# crunch - 字典生成工具

## 介绍

crunch - generate wordlists from a character set

```bash
crunch <min-len> <max-len> [<charset string>] [options]
```

## 参数

```
 oprions
     -b     指定文件输出的大小，避免字典文件过大  
     -c     指定文件输出的行数，即包含密码的个数
     -d     限制相同元素出现的次数
     -e     定义停止字符，即到该字符串就停止生成
     -f     调用库文件（/etc/share/crunch/charset.lst）
     -i     改变输出格式，即aaa,aab -> aaa,baa
     -I     通常与-t联合使用，表明该字符为实义字符
     -m     通常与-p搭配
     -o     将密码保存到指定文件
     -p     指定元素以组合的方式进行
     -q     读取密码文件，即读取pass.txt
     -r     定义重某一字符串重新开始
     -s     指定一个开始的字符，即从自己定义的密码xxxx开始
     -t     指定密码输出的格式
     -u     禁止打印百分比（必须为最后一个选项）
     -z     压缩生成的字典文件，支持gzip,bzip2,lzma,7z  
```

[参考文章](https://www.freebuf.com/sectool/170817.html)

特殊字符

```
%      代表数字
^      代表特殊符号
@      代表小写字母
,      代表大写字符
```

### 常用方式

- 生成一个`4`位数的`纯数字`字典

```bash
crunch 4 4 -t %%%% -o dict.txt
```


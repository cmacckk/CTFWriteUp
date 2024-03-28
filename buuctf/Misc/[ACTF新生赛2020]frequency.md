# [ACTF新生赛2020]frequency

## 知识点

`字频分析`

## 解题

根据题目名称frequency与文件内容猜测应该是字频方向

如果打开文档是空白的，就搜索

![image-20231205211319733](./img/103-1.png)

![image-20231205211409712](./img/103-2.png)

再结合文档内容，合并在一起去解码（如果直接统计字频没有什么思路，刚刚试过了）

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

![image-20231205211931927](./img/[ACTF新生赛2020]frequency-1.png)


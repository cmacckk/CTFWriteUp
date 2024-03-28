# [DDCTF2018]第四扩展FS

## 知识点

`foremost分离`

`频次统计`

## 解题

得到一张`jpg`

![FS](./img/116-1.png)

详细信息里面有内容

![image-20231206140524620](./img/116-2.png)

`foremost`分离一下

![image-20231206140606147](./img/116-3.png)

根据详细信息中的备注作为密码,解压出一个文件

![image-20231206140737503](./img/116-4.png)

频次统计

```python
from collections import Counter

with open('./file.txt', 'r') as f:
    cont = f.read()
    res = Counter(cont)
    print(''.join(res.keys()))
```

![image-20231206141406795](./img/116-5.png)

组合一下即可
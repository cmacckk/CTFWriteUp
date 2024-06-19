# Wire1

## 知识点

`python对sql注入流量分析`

## 解题

使用代码处理数据

```python
import pyshark


pcap = pyshark.FileCapture('./timu.pcapng', display_filter='http.request==true')

d = {}

def update_max_value(dictionary, key, value):
    if key not in dictionary or value > dictionary[key]:
        dictionary[key] = value

for i, v in enumerate(pcap):
    # print(v)
    data = v.http.request_uri_query
    res = data.strip('id=').strip('--+').split('=')
    data = int(res[1])
    pos = int(res[0].split(',')[-2])
    update_max_value(d, pos, data)

for v in d.values():
    print(chr(v), end='')
```

![](./img/wire1-1.png)
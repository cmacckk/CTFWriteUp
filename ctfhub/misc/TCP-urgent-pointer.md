# TCP-urgent-pointer

## 知识点

`流量分析 python`

## 解题

筛选`tcp`流量中`urgent-pointer>0`的数据，转为`hex`再`base64`解码

```python
import pyshark
import binascii
import base64


pcap = pyshark.FileCapture('./havefun.pcapng', display_filter='tcp.urgent_pointer>0')

res = ''

for i, cap in enumerate(pcap):
    res += str(hex(int(cap.tcp.urgent_pointer))).replace('0x', '')

print(res)
flag = binascii.unhexlify(res)
print(flag)
print(base64.b64decode(flag.decode()))
```


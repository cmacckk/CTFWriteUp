# 奇怪的TTL字段

## 知识点

`TTL拼接图片`

## 解题

```python
import binascii

with open('xctf/pic/ttl.txt', 'r') as file:
    lines = file.readlines()

    ttl_data = ''
    for line in lines:
        prefix = "{0:b}".format(int(line[4:])).zfill(8)
        ttl_data += prefix[0:2]

flag = ''
for i in range(0, len(ttl_data), 8):
    flag += chr(int(ttl_data[i:i + 8], 2))

# 打印出来的flag前一段为ffd8ffe1001845786966000049492a00080000000000000000000000
# ffd8ff明显是图片的文件头，因此需要存储成图片
print(flag)

flag = binascii.unhexlify(flag)
with open('./res.jpg', 'wb') as file:
    file.write(flag)
```


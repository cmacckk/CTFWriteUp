# misc1

## 知识点

`16进制凯撒加密`

## 解题

> d4e8e1f4a0f7e1f3a0e6e1f3f4a1a0d4e8e5a0e6ece1e7a0e9f3baa0c4c4c3d4c6fbb9e1e6b3e3b9e4b3b7b7e2b6b1e4b2b6b9e2b1b1b3b3b7e6b3b3b0e3b9b3b5e6fd

直接`hex`解密失败，使用两个为一组，转为`十进制`减数字爆破

```python
a = "d4e8e1f4a0f7e1f3a0e6e1f3f4a1a0d4e8e5a0e6ece1e7a0e9f3baa0c4c4c3d4c6fbb9e1e6b3e3b9e4b3b7b7e2b6b1e4b2b6b9e2b1b1b3b3b7e6b3b3b0e3b9b3b5e6fd"
step = 2
b = [a[i:i+step] for i in range(0,len(a),step)]
# print(b)
str = []
for i in b:
    str.append(i)
for j in range(50,150):
    for i in str:
        print(chr(int(i,16)-j),end="")
    print()
```


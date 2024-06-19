# Time_losing

## 知识点

`时间差ASCII`

## 解题

```python
import os,time
 
flag = ""
oldtime = 2000000000

for i in range(0,47):  #题目中47个文件
    file = r'./{0}.txt'.format(i) # 文件路径
    newtime = int(os.path.getmtime(file)) #获取最近修改时间
    key = newtime - oldtime  #新修改时间戳减去题目描述时间戳
    flag += chr(key) #转换为ASCII值
    
print(flag)
```


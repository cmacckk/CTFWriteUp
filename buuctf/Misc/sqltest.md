# sqltest

## 知识点

`sql盲注数据包分析`

## 解题

看数据包发现是盲注

以最后查找`flag`的特征值为判断条件来查有哪些成功的

首先我们观察流量包，可以看到很多条这样的`http`请求，`url`中有`select`， `SCHEMA_name`等，可以确定是对`mysql`数据库的盲注

我们来把url的部分提取出来
一种方法是`导出http对象`，但是这样的话接下来就要手动读注入信息了，这很不方便

所以我们用`tshark`提取

```bash
tshark -r sqltest.pcapng -Y "http.request" -T fields -e http.request.full_uri > data.txt
# 下面这个参考
tshark -r sqlmap.pcapng -Y "ip.src == xxx.xxx.xxx.xxx && http.response" -T fields -E separator="~" -e http.response_for.uri -e http.file_data > data.txt
```

```bash
c@pc /m/c/U/c/Downloads> head -n 5 data.txt
http://172.16.80.11/index.php?act=news&id=1%20and%20length((select%20count(*)%20from%20information_schema.SCHEMATA))>100
http://172.16.80.11/index.php?act=news&id=1%20and%20length((select%20count(*)%20from%20information_schema.SCHEMATA))>50
http://172.16.80.11/index.php?act=news&id=1%20and%20length((select%20count(*)%20from%20information_schema.SCHEMATA))>25
http://172.16.80.11/index.php?act=news&id=1%20and%20length((select%20count(*)%20from%20information_schema.SCHEMATA))>12
http://172.16.80.11/index.php?act=news&id=1%20and%20length((select%20count(*)%20from%20information_schema.SCHEMATA))>6
```

获取值（628-972）
这一步就是我们要找的flag了，写一个脚本提取一下。我们知道注入语句为

```
id=1 and ascii(substr(((select concat_ws(char(94), flag)  from db_flag.tb_flag  limit 0,1)), {第i个字符}, 1))>{字符的ascii值}
```

我们把`第i个字符`和`ascii值`提取出来，取i变化时的值，脚本为：

```python
import urllib.parse
f = open("data.txt","r").readlines()

s = []
for i in range(627,972):
    data = urllib.parse.unquote(f[i]).strip()
    payload = data.split("and")[1]
    positions = payload.find("from db_flag.tb_flag  limit 0,1)), ")
    data1 = payload[positions+35:].split(",")[0]
    data2 = payload[positions+35:].split(">")[1]
    s.append([data1,data2])

for i in range(1,len(s)):
    if s[i][0]!=s[i-1][0]:
        print(chr(int(s[i-1][1])),end="")
print(chr(int(s[-1][1])))

```

下方仅为参考

```python
import urllib.parse
# 读入数据，数据中存在不可见字符，因此用rb模式
f = open("data.txt", "rb").readlines()

# 注入语句。
pattern = "AND ORD(MID((SELECT IFNULL(CAST(username AS NCHAR),0x20) FROM `security`.users ORDER BY username LIMIT 10,1),"
# 注入成功
trueInjection = "You are in..........."
temp = {}

for i in range(0, len(f)):
    line = str(f[i])[2:]
    # 上一步插入的分隔符，把数据分为url和data两部分
    if line.find("~") == -1:
        continue

    url, data = line.split("~")[0],line.split("~")[1]
    
    url = urllib.parse.unquote(url).strip()

    positions = url.find(pattern)
    if positions != -1:
        # 截取参数，data1 表示第几位数据，data2表示这一位数据的ascii值
        data1 = url[positions+len(pattern):].split(",")[0]
        data2 = url[positions+len(pattern):].split(">")[1].split(" ")[0]
        
        # data3: 注入结果的判断
        if data.find(trueInjection) != -1:
            data3 = True
        else:
            data3 = False
        if data1 not in temp:
            temp[data1]=[(data2,data3)]
        else:
            temp[data1].append((data2,data3))

    else:
        continue

# 盲注使用了二分法，所以也要根据这一点写代码解析数据
text=""
for i in temp:
    small = -1
    large = -1
    for j in temp[i]:
        if j[1] :
            small = j[0]
        else:
            large = j[0]
    if large != -1:
        text+=chr(int(large))
print(text)
```


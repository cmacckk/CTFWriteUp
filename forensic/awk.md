# AWK

## 输出单词个数

AWK中变量无需声明即可直接使用，NF记录着当前行的列数，即单词数量，所以将其相加即可:

```bash
awk '{ x+=NF } END { print x}' ColorBlind.txt
```

## 去除重复行

```bash
awk '{ if ( !line[$0] ) print $0; line[$0]++ }' ColorBlind.txt
```

## 输出大于20个字符的行

```bash
awk 'length > 20 ' ColorBlind.txt
```

## 输出black & white歌词出现次数

```bash
awk '/black & white/ {x++} END{print x}' ColorBlind.txt
```

## 正则替换

```bash
awk '{gsub(/[0-9]+/,"");print}' /tmp/passwd
```

## 找到谁在破解密码

```bash
awk '/Failed/{print $(NF-3)}' secure-20161219 |sort |uniq -c  |sort -nk1
```

## 过滤出包含Failed password的行 并统计每个ip地址出现的次数

```bash
awk '/Failed/{fa[$(NF-3)]++}END{for(pol in fa)print pol,fa[pol]}' secure-20161219 |sort -rnk2
```

## 统计secure文件中每个用户，被同一ip破解多少次

### 进破解使用的用户及地址定向到文件中

```bash
awk '/Failed/{print $(NF-5),$(NF-3)}' secure-20161219 >user-ip.log
```

### 对文件进行去重排序测

```bash
awk '{h[$1" "$2]++}END{for(p in h) print p,h[p]}' user-ip.log |head 
```

### 操作日志文件，取出数据

```
awk '/Failed/{h[$(NF-5)" "$(NF-3)]++}END{for(p in h) print p,h[p]}'  secure-20161219 |head
```

### 统计nginx access.log文件中对ip地址去重并统计重复数

```bash
awk '{h[$1]++}END{for(i in h) print i,h[i]}' access.log |sort -nrk2 |head
```

### 统计access.log文件中每个ip地址使用了多少流量

```bash
[root@clsn6 awk]# awk '{sum=sum+$10}END{print sum}' access.log 
2478496663
[root@clsn6 awk]# awk '{sum=sum+$10}END{print sum/1024^3}' access.log 
2.30828
```

### 每个ip使用的流量

```bash
[root@clsn6 awk]# awk '{h[$1]=h[$1]+$10}END{for(p in h) print p,h[p]/1024^2 }' access.log |sort -rnk2|column -t |head 
114.83.184.139   29.91
117.136.66.10    21.3922
116.216.30.47    20.4716
223.104.5.197    20.4705
116.216.0.60     18.2584
```

### 统计access.log文件中每个ip地址使用了多少流量和每个ip地址的出现次数

```bash
[root@clsn6 awk]# awk '{count[$1]++;sum[$1]=sum[$1]+$10}END{for(pol in sum)print pol,count[pol],sum[pol]}' access.log |sort -nrk2 |column -t |head 
58.220.223.62    12049  12603075
112.64.171.98    10856  15255013
114.83.184.139   1982   31362956
117.136.66.10    1662   22431302
115.29.245.13    1318   1161468
223.104.5.197    961    21464856
116.216.0.60     957    19145329
```


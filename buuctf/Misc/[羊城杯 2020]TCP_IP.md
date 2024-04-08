# [羊城杯 2020]TCP_IP

## 知识点

`HTTP流量分析`

`base91`

## 解题

```bash
tshark -r .\attachment.pcap -T fields -e ip.id > data.txt
```

![ ](./img/135-1.png)

`16`进制解密

```
b'@iH<,{*;oUp/im"QPl`yR*ie}NK;.D!Xu)b:J[Rj+6KKM7P@iH<,{*;oUp/im"QPl`yR'
```

`base91`解码

```
flag{wMt84iS06mCbbfuOfuVXCZ8MSsAFN1GA}
```

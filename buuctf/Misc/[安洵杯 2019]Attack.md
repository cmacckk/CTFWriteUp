# [安洵杯 2019]Attack

## 知识点

`dmp文件`

`mimikatz读取密码`

## 解题

搜索`flag`

发现一个压缩包

![image-20231128173305505](./img/58-1.png)

重新分析流量包，搜索查看常用协议，发现在http协议中存在lsass.dmp

![image-20231128203342676](./img/58-2.png)

（`*.dmp`文件是`windows`系统中的错误转储文件，当`Windows`发生错误蓝屏的时候，系统将当前内存【含虚拟内存】中的数据直接写到文件中去，方便定位故障原因。）

（`*`里面包含主机用户密码信息）

**关于lsass**
`lsass`是`windows`系统的一个进程，用于本地安全和登陆策略。`mimikatz`可以从` lsass.exe `里获取`windows`处于`active`状态账号明文密码。本题的`lsass.dmp`就是内存运行的镜像，也可以提取到账户密码

把`lsass.dmp`复制到`mimikatz`的目录，然后运行`mimikatz`

```
//提升权限
privilege::debug
//载入dmp文件
sekurlsa::minidump lsass.dmp
//读取登陆密码
sekurlsa::logonpasswords full
```

![image-20231128204009002](./img/58-3.png)
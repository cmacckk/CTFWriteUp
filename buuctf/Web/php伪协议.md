# 伪协议

```protocal
file:// — 访问本地文件系统
http:// — 访问 HTTP(s) 网址
ftp:// — 访问 FTP(s) URLs
php:// — 访问各个输入/输出流（I/O streams）
zlib:// — 压缩流
data:// — 数据（RFC 2397）
glob:// — 查找匹配的文件路径模式
phar:// — PHP 归档
ssh2:// — Secure Shell 2
rar:// — RAR
ogg:// — 音频流
expect:// — 处理交互式的流
```

## 1.php://filter

`php://filter`用于读取源码

```url
?page=php://filter/read=convert.base64-encode/resource=../flag.php
```

## 2.file://

用于访问本地文件系统，不受`allow_url_fopen`与`allow_url_include`的影响

即`file:// [文件的绝对路径和文件名]`

```url
?path=file:///var/www/html/flag.txt
```

## 3.php://input

`php://input` 可以访问请求的原始数据的只读流, 将`post`请求中的数据作为`PHP`代码执行

`php://input` 可以用来生成一句话

利用该方法，我们可以直接写入`php`文件，输入`file=php://input`，然后使用`burp`抓包，写入`php`代码

![php伪协议 Image 1](./img/26-1.png)

## 4.data://

利用`data://`伪协议可以直接达到执行`php`代码的效果，例如执行`phpinfo()`函数：

![php伪协议 Image 2](./img/26-2.png)
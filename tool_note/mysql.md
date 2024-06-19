## 修改密码

### 方法一

```mysql
mysql> set password for root@localhost = password('123456'); 
```

### 方法二

```bash
mysqladmin -uroot -p123456 password 123 
```

### 方法三

```bash
mysql> use mysql; 
mysql> update user set password=password('123') where user='root' and host='localhost'; 
mysql> flush privileges; 
```

### 方法四

```
update user set password=password("123") where user="root";
```


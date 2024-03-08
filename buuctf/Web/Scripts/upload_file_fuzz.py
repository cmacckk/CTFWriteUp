import requests
import time

printer_chars = [chr(i) for i in range(33, 127)]    # 可打印字符组

url = 'http://1d0510b4-e285-46ad-92ae-87a8dc851d38.node5.buuoj.cn:81/index.php?act=upload'

def upload_file_fuzz(fuzz_dict):
    for char in printer_chars:
        resp = requests.post(url, files={'file': ('demo.txt', ('12345' + char).encode())}, timeout=8)
        time.sleep(0.19)        # 尽量设置时间不要太过
        # print(resp.text)
        if 'illegal char' not in resp.text:
            print(f"字符可用 ===> {char}")

if __name__ == '__main__':
    upload_file_fuzz(printer_chars)
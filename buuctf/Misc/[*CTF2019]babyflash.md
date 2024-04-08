# [*CTF2019]babyflash

## 知识点

`JPEXS Free Flash Decompiler`

`黑白图片组合二维码`

## 解题

使用`JPEXS Free Flash Decompiler`分解文件

首先用`Audacity`打开，就可以得到一部分`flag`

![image-20231222103939241](./img/140-1.png)

黑色作为黑色小块，白色作为白色小块

绘制二维码

```python
from PIL import Image
import os



path = 'C:/Users/cc/Downloads/images/'

images_fn_list = os.listdir(path)

images_fn_list.sort(key=lambda x: int(x.split('.')[0]))
# print(dir_list)

qr_data = ''

for image_name in images_fn_list:
    img = Image.open(os.path.join(path, image_name))
    im = img.load()
    if im[0, 0] == (0, 0, 0):   # 黑色
        qr_data += '1'
    elif im[0, 0] == (255, 255, 255):   # 白色
        qr_data += '0'
        
width = height = 21

new_image = Image.new('RGB', (width, height))
i = 0

for w in range(width):
    for h in range(height):
        if qr_data == '1':
            new_image.putpixel([w, h], (0, 0, 0))
        elif qr_data[i] == '0':
            new_image.putpixel([w, h], (255, 255, 255))
        i += 1
        
new_image.save('flag.png')
```

扫描二维码即可获得领一部分`flag`


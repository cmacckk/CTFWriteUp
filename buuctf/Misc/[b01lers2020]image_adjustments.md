# [b01lers2020]image_adjustments

## 知识点

`python图像处理`

## 解题

`adjust.py`

```python
#!/usr/bin/env python3

from PIL import Image
from random import randint
import sys

f = './flag.png'

img = Image.open(f)

print('Width: {}\n'.format(img.size[0]))
print('Height: {}\n'.format(img.size[1]))

pixels = img.load()
for r in range(img.size[0]):
    for c in range(img.size[1]):
        print('{}: {}'.format(c, pixels[r, c]))

    backup_row = []
    for c in range(img.size[1]):
        backup_row += [pixels[r,c]]

    start = randint(0, img.size[1])
    for c in range(img.size[1]):
        pixels[r, (c + start) % img.size[1]] = backup_row[c]

img.save('./attachment.png')
img.show()
```

`solve.py`

```python
from PIL import Image
from random import randint

img = Image.open('attachment.png')

print('Width: {}\n'.format(img.size[0]))
print('Height: {}\n'.format(img.size[1]))

pixels = img.load()
for r in range(img.size[0]):
    backup_row = []
    
    for c in range(img.size[1]):
        backup_row += [pixels[r, c]]
        
    start = randint(0, img.size[1])
    done = False
    for i in range(0, img.size[1]):
        if done:
            break
        for c in range(img.size[1]):
            pixels[r, (c + i) % img.size[1]] = backup_row[c]
            if(pixels[r, 163] == (255, 0, 0, 255) and pixels[r, 171] == (255, 0, 0, 255) and pixels[r, 175] == (255, 255, 255, 255) and pixels[r, 150] == (255, 255, 255, 255)):
                done = True
                print("Done: {}".format(r))
                
img.save('flag.png')
```


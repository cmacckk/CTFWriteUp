# [MRCTF2020]千层套路

## 知识点

`嵌套多层压缩包`

## 解题

`压缩包解密`

```python
import zipfile
import os


first_zip_filename = '0573.zip'
path = 'C:/Users/cc/Downloads/attachment/'

def unzip(path, filename):
    current_file = os.path.join(path, filename)
    # print(current_file)
    os.chdir(path) # 改变当前工作路径，方便添加文件夹
    
    zip_file = zipfile.ZipFile(current_file)
    
    unzip_filename = zip_file.namelist()[0]
    
    zip_file.extractall(path=path,
                        members=zip_file.namelist(),
                        pwd=filename[:-4].encode())      # 密码去除.zip后的文件名
    
    # 解压后会解压到path变量目录下
    
    zip_file.close()
    
    return unzip_filename

filename = first_zip_filename

if __name__ == '__main__':
    while True:
        if filename == '':
            exit(0)
        else:
            filename = unzip(path, filename)
            print('unzip %s'%filename)
```

解压后的文件为`qr.txt`,内容如下

![image-20231128164532453](./img/55-1.png)

因为是`40000`行`RGB`,所以尺寸为`200*200`,绘图

```python
from PIL import Image
from itertools import product

f = open('./qr.txt', 'r')

max = 200

picture = Image.new('RGB', (max, max))
for x, y in product(range(max), range(max)):
    string = f.readline()
    picture.putpixel([x, y], eval(string))      # eval后可直接转为元组
    
picture.show()
```

![image-20231128165507455](./img/55-2.png)
# [INSHack2018]42.tar.xz

## 知识点

解压递归的`.tar.xz`压缩包

## 解题

```bash
while [ "find . -type f -name '*.tar.xz' | wc -l" -gt 0 ]; do find -type f -name "*.tar.xz" -exec tar xf '{}' \; -exec rm -- '{}' \;; done;
```

等一会取消运行就可以得到`flag`了

`python脚本` 会爆磁盘

```python
import lzma
import shutil
import tarfile
import os

def unzx(filename):
    print(filename)
    inputs = lzma.open(filename)
    out = open(filename.split(".")[0]+".tar","wb")
    shutil.copyfileobj(inputs,out)
    out.close()
    inputs.close()
    os.remove(filename)
    

def untar(filename):
    print(filename)
    tar = tarfile.open(filename)
    names = tar.getnames()
    if os.path.isdir(filename):
        pass
    else:
        os.mkdir(filename.split(".")[0]+"/")
    for name in names:
        tar.extract(name,filename.split(".")[0]+"/")
    tar.close()
    os.remove(filename)

def unpack(dirs):
    #print(dirs)
   
    files = os.listdir(dirs)
    #print(files)
    for file in files:
        unzx(dirs+"/"+file)
        untar(dirs+"/"+file.split(".")[0]+".tar")
        unpack(dirs+"/"+file.split(".")[0])


unpack("42")
```

## [BSidesSF2019]dis
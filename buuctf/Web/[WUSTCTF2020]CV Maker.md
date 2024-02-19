# [WUSTCTF2020]CV Maker

## 知识点

`文件上传`

## 解题

注册账号时发现抱报错，但是没找到有用的信息

![CV Maker1](file:///G:/CTFWriteUp/buuctf/Web/img/17-1.png?lastModify=1708305010)

登录试试，发现头像处有上传点，尝试上传`webshell`

![CV Maker2](file:///G:/CTFWriteUp/buuctf/Web/img/17-2.png?lastModify=1708305010)

![CV Maker2](file:///G:/CTFWriteUp/buuctf/Web/img/17-3.png?lastModify=1708305010)

简单上传一个马 头像处发生改变 查看一下头像信息 `ctrl+shift+c`选中头像

![CV Maker3](file:///G:/CTFWriteUp/buuctf/Web/img/17-4.png?lastModify=1708305010)

![CV Maker4](file:///G:/CTFWriteUp/buuctf/Web/img/17-5.png?lastModify=1708305010)

发现可直接利用`webshell`，执行命令获取`flag`即可

![CV Maker3](file:///G:/CTFWriteUp/buuctf/Web/img/17-6.png?lastModify=1708305010)
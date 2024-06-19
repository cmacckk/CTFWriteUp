# MISCall

## 知识点

`git stash`

## 解题

没给后缀名，使用`file`命令然后解压得到`flag.txt`,结果提示nothing

使用`git log`查看没发现其他提交记录，使用`git stash show`发现`s.py`，然后`git stash apply`即可恢复

![](./img/MISCall-2.png)
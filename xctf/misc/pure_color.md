# pure_color

## 知识点

`图片隐藏`

## 解题

`exiftool`和`strings`没找到什么东西，`zsteg`也没什么特别的信息，使用`StegSolve`查看图层，发现在`blue plane 0`发现`flag`

![](./img/pure_color -1.png)

`flag{true_steganographers_doesnt_need_any_tools}`
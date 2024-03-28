# [MRCTF2020]不眠之夜

## 知识点

`碎片图片拼接`

## 解题

用到两个工具：`montage`和`gaps`,

`montage`的作用是把乱序图片先按拼图的总大小拼成一张图

`gaps`的作用是将一张图按指定的`size`切割并尝试将其拼好

`gaps`安装

注:要删掉一张没用的损坏图片

120张，每张都是`200 x 100`，应该`长：10张图片`，`宽：12张图片`，那么拼起来的总图就应该是`长：2000 x 宽：1200`

方法一:

```bash
# 拼接为一张图片
montage *.jpg -tile 10x12 -geometry 200x100+0+0 flag.jpg
# 还原原图片
gaps run flag.jpg res.jpg --generations=40 --population=120 --size=200
```

方法二:

```
montage *.jpg -tile 10x12 -resize 4000x2400 -geometry +0+0 out.jpg #把图片碎片合成一个图片
gaps --image=out.jpg --generations=90 --population=120 --size=200 #还原原图片
```

![image-20231130225627726](./img/82-1.png)

`*.jpg`指目标为目录下所有的`jpg`格式图片

`-geometry +0+0`的用处是让图片之间没有间隙

`resize`后是最终合成图片的长x宽

`tile`后是从左往右张数x从上往下张数

`size`如何确定？

这道题的图片有一个特点，那就是长是宽的两倍，所以我们可以将一张子图片视为两张拼图（每张拼图是正方形的）

于是有，拼图的宽度，也就是`size`为`600/12=50`

![res](./img/82-2.png)
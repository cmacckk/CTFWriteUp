## 常见文件头

```
JPEG (jpg)，文件头 ffd8ffe0 文件尾 ffd9
PNG (png)，文件头：89504E47
GIF (gif)，文件头：47494638
TIFF (tif)，文件头：49492A00
Windows Bitmap (bmp)，文件头：424D
CAD (dwg)，文件头：41433130
Adobe Photoshop (psd)，文件头：38425053
Rich Text Format (rtf)，文件头：7B5C727466
XML (xml)，文件头：3C3F786D6C
HTML (html)，文件头：68746D6C3E
Email [thorough only] (eml)，文件头：44656C69766572792D646174653A
Outlook Express (dbx)，文件头：CFAD12FEC5FD746F
Outlook (pst)，文件头：2142444E
MS Word/Excel (xls.or.doc)，文件头：D0CF11E0
MS Access (mdb)，文件头：5374616E64617264204A
WordPerfect (wpd)，文件头：FF575043
Postscript (eps.or.ps)，文件头：252150532D41646F6265
Adobe Acrobat (pdf)，文件头：255044462D312E
Quicken (qdf)，文件头：AC9EBD8F
Windows Password (pwl)，文件头：E3828596
ZIP Archive (zip)，文件头：504B0304
RAR Archive (rar)，文件头：52 61 72 21 1A 07 00
Wave (wav)，文件头：57415645
AVI (avi)，文件头：41564920
Real Audio (ram)，文件头：2E7261FD
Real Media (rm)，文件头：2E524D46
MPEG (mpg)，文件头：000001BA
MPEG (mpg)，文件头：000001B3
Quicktime (mov)，文件头：6D6F6F76
Windows Media (asf)，文件头：3026B2758E66CF11
MIDI (mid)，文件头：4D546864
```

## 图片解题流程

1.看图片详细信息

2.`010editor`查看并搜索对应字符串,比如`flag` `key` `pass`

3.改宽高

4.查看是不是合并文件,是否需要`foremost`分离

5.`lsb`隐写和各通道查看,`zsteg`爆破

6.`steginfo`查看是否有隐藏信息

## 金三胖

解压有个`gif动图`

直接上`StegSolve`

## 你竟然赶我走

找半天没找到

`010editor`也没发现什么东西

最后放到`linux`下

```bash
strings biubiu.png | grep flag
```

找到`flag`

## 二维码

解压后发现一个二维码

然后`010editor`发现了两个文件

`binwalk`分离一下

```bash
binwalk -e qr_code.png
```

然后得到一个压缩包，里面的文件文件名为`4number.txt`

然后爆破`4`位数字

发现压缩包密码为`7639`

解压得到`flag`

## 大白

解压发现一张大白的照片

看着好像显示不全

详细信息和`010edit`也没什么信息

更改宽高

![image-20231123222342795](./img/1-1.png)

重新打开文件即可查看到`flag`

![image-20231123222438166](./img/1-2.png)

## N种方法解决

`010editor`

```
data:image/jpg;base64,iVBORw0KGgoAAAANSUhEUgAAAIUAAACFCAYAAAB12js8AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAArZSURBVHhe7ZKBitxIFgTv/396Tx564G1UouicKg19hwPCDcrMJ9m7/7n45zfdxe5Z3sJ7prHbf9rXO3P4lLvYPctbeM80dvtP+3pnDp9yF7tneQvvmcZu/2lf78zhU+5i9yxv4T3T2O0/7eud68OT2H3LCft0l/ae9ZlTo+23pPvX7/rwJHbfcsI+3aW9Z33m1Gj7Len+9bs+PIndt5ywT3dp71mfOTXafku6f/2uD09i9y0n7NNd2nvWZ06Ntt+S7l+/68MJc5O0OSWpcyexnFjfcsI+JW1ukpRfv+vDCXOTtDklqXMnsZxY33LCPiVtbpKUX7/rwwlzk7Q5JalzJ7GcWN9ywj4lbW6SlF+/68MJc5O0OSWpcyexnFjfcsI+JW1ukpRfv+vDCXOTWE7a/i72PstJ2zfsHnOTpPz6XR9OmJvEctL2d7H3WU7avmH3mJsk5dfv+nDC3CSWk7a/i73PctL2DbvH3CQpv37XhxPmJrGctP1d7H2Wk7Zv2D3mJkn59bs+nDA3ieWEfdNImylJnelp7H6bmyTl1+/6cMLcJJYT9k0jbaYkdaansfttbpKUX7/rwwlzk1hO2DeNtJmS1Jmexu63uUlSfv2uDyfMTWI5Yd800mZKUmd6Grvf5iZJ+fW7PjzJ7v12b33LSdtvsfuW75LuX7/rw5Ps3m/31rectP0Wu2/5Lun+9bs+PMnu/XZvfctJ22+x+5bvku5fv+vDk+zeb/fWt5y0/Ra7b/ku6f71+++HT0v+5l3+tK935vApyd+8y5/29c4cPiX5m3f5077emcOnJH/zLn/ar3d+/flBpI+cMDeNtJkSywn79BP5uK+yfzTmppE2U2I5YZ9+Ih/3VfaPxtw00mZKLCfs00/k477K/tGYm0baTInlhH36iSxflT78TpI605bdPbF7lhvct54mvWOaWJ6m4Z0kdaYtu3ti9yw3uG89TXrHNLE8TcM7SepMW3b3xO5ZbnDfepr0jmlieZqGd5LUmbbs7onds9zgvvU06R3TxPXcSxPrW07YpyR1pqTNKUmdKUmdk5LUaXzdWB/eYX3LCfuUpM6UtDklqTMlqXNSkjqNrxvrwzusbzlhn5LUmZI2pyR1piR1TkpSp/F1Y314h/UtJ+xTkjpT0uaUpM6UpM5JSeo0ft34+vOGNLqDfUosN7inhvUtJ+ybRtpMd0n39Goa3cE+JZYb3FPD+pYT9k0jbaa7pHt6NY3uYJ8Syw3uqWF9ywn7ppE2013SPb2aRnewT4nlBvfUsL7lhH3TSJvpLunecjWV7mCftqQbjSR1puR03tqSbkx/wrJqj7JPW9KNRpI6U3I6b21JN6Y/YVm1R9mnLelGI0mdKTmdt7akG9OfsKzao+zTlnSjkaTOlJzOW1vSjelPWFbp8NRImylJnWnL7r6F7zN3STcb32FppUNTI22mJHWmLbv7Fr7P3CXdbHyHpZUOTY20mZLUmbbs7lv4PnOXdLPxHZZWOjQ10mZKUmfasrtv4fvMXdLNxndYWunQlFhutHv2W42n+4bds7wl3VuuskSJ5Ua7Z7/VeLpv2D3LW9K95SpLlFhutHv2W42n+4bds7wl3VuuskSJ5Ua7Z7/VeLpv2D3LW9K97avp6GQ334X3KWlz+tukb5j+hO2/hX3Ebr4L71PS5vS3Sd8w/Qnbfwv7iN18F96npM3pb5O+YfoTtv8W9hG7+S68T0mb098mfcP0Jxz/W+x+FPethvUtN2y/m7fwnvm1+frzIOklDdy3Gta33LD9bt7Ce+bX5uvPg6SXNHDfaljfcsP2u3kL75lfm68/D5Je0sB9q2F9yw3b7+YtvGd+bb7+vCEN7ySpMzXSZrqL3bOcsN9Kns4T2uJRk6TO1Eib6S52z3LCfit5Ok9oi0dNkjpTI22mu9g9ywn7reTpPKEtHjVJ6kyNtJnuYvcsJ+y3kqfzxNLiEUosJ+xTYvkudt9yg3tqpM2d5Cf50mKJEssJ+5RYvovdt9zgnhppcyf5Sb60WKLEcsI+JZbvYvctN7inRtrcSX6SLy2WKLGcsE+J5bvYfcsN7qmRNneSn+RLK5UmbW4Sywn7lOzmhH3a0u7ZN99hadmRNjeJ5YR9SnZzwj5taffsm++wtOxIm5vEcsI+Jbs5YZ+2tHv2zXdYWnakzU1iOWGfkt2csE9b2j375jtcvTz+tuX0vrXF9sxNkjrTT+T6rvyx37ac3re22J65SVJn+olc35U/9tuW0/vWFtszN0nqTD+R67vyx37bcnrf2mJ75iZJneknUn+V/aWYUyNtpqTNqZE2UyNtGlvSjTsT9VvtKHNqpM2UtDk10mZqpE1jS7pxZ6J+qx1lTo20mZI2p0baTI20aWxJN+5M1G+1o8ypkTZT0ubUSJupkTaNLenGnYnl6TujO2zP3DTSZkp2c8L+0xppM32HpfWTIxPbMzeNtJmS3Zyw/7RG2kzfYWn95MjE9sxNI22mZDcn7D+tkTbTd1haPzkysT1z00ibKdnNCftPa6TN9B2uXh5/S9rcbEk37jR2+5SkzpSkzo4kdaavTg6/JW1utqQbdxq7fUpSZ0pSZ0eSOtNXJ4ffkjY3W9KNO43dPiWpMyWpsyNJnemrk8NvSZubLenGncZun5LUmZLU2ZGkzvTVWR/e0faJ7Xdzw/bMKbGc7PbNE1x3uqNtn9h+Nzdsz5wSy8lu3zzBdac72vaJ7Xdzw/bMKbGc7PbNE1x3uqNtn9h+Nzdsz5wSy8lu3zzBcsVewpyS1LmTWG7Y3nLCPm1JN05KLP/D8tRGzClJnTuJ5YbtLSfs05Z046TE8j8sT23EnJLUuZNYbtjecsI+bUk3Tkos/8Py1EbMKUmdO4nlhu0tJ+zTlnTjpMTyP/R/i8PwI//fJZYb3Jvv8Pd/il+WWG5wb77D3/8pflliucG9+Q5//6f4ZYnlBvfmO1y9PH7KFttbfhq+zySpMyVtbr7D1cvjp2yxveWn4ftMkjpT0ubmO1y9PH7KFttbfhq+zySpMyVtbr7D1cvjp2yxveWn4ftMkjpT0ubmO1y9ftRg9y0n7FPD+paTtk9O71sT13Mv7WD3LSfsU8P6lpO2T07vWxPXcy/tYPctJ+xTw/qWk7ZPTu9bE9dzL+1g9y0n7FPD+paTtk9O71sT1/P7EnOTWG5wb5LUmRptn3D/6b6+eX04YW4Syw3uTZI6U6PtE+4/3dc3rw8nzE1iucG9SVJnarR9wv2n+/rm9eGEuUksN7g3SepMjbZPuP90X9+8PpwwN0mb72pYfzcn1rf8NHwffXXWhxPmJmnzXQ3r7+bE+pafhu+jr876cMLcJG2+q2H93ZxY3/LT8H301VkfTpibpM13Nay/mxPrW34avo++OuvDCXOT7OZGu7e+5YT9XYnlhH36DlfvfsTcJLu50e6tbzlhf1diOWGfvsPVux8xN8lubrR761tO2N+VWE7Yp+9w9e5HzE2ymxvt3vqWE/Z3JZYT9uk7XL1+1GD3LX8avt8klhu2t5yc6F+/68OT2H3Ln4bvN4nlhu0tJyf61+/68CR23/Kn4ftNYrlhe8vJif71uz48id23/Gn4fpNYbtjecnKif/3+++HTnub0fd4zieUtvLfrO1y9PH7K05y+z3smsbyF93Z9h6uXx095mtP3ec8klrfw3q7vcPXy+ClPc/o+75nE8hbe2/Udzv9X+sv/OP/881/SqtvcdpBh+wAAAABJRU5ErkJggg==
```

`base64`解码后发现是个`png`文件，保存为`png`文件,打开是个二维码

扫码获得`flag`

## 乌镇峰会种图

`010editor`搜索末尾直接发现`flag`

## wireshark

`wireshark`打开

题目：管理员的密码即是答案

直接搜索`pass`关键字

找到密码

![](./img/2-1.png)

## 基础破解

`4`位数字加密

解压发现`rar`文件，`ARCHAR`破解

口令为`2563`,`base64`解密

## 文件中的秘密

`alt+enter`查看属性，详细信息里有`flag`

## LSB

`LSB`隐写

在`Red plane0` `Green plane0` `Blue plane0`图片上方有东西

`stegsolve`将`Red Green Blue `的`0`位打勾

`BitOrder`为`LSBFirst`

因为文件头为`png`，最后`SaveBin`为`png`

扫码即可

### lsb zsteg爆破

```bash
zsteg 文件名 --all
```

## zip伪加密

将该位置从`09`改为`00`

![image-20231123230105301](./img/3-1.png)

![image-20231123230212021](./img/3-2.png)

## 被嗅探的流量

![image-20231123230335463](./img/4-1.png)

搜索`flag`后直接找到`flag`

## rar

`ARCHAR`破解

密码为`8795`

## qr

扫码即可获取`flag`

## 镜子里面的世界

`zsteg`直接命令扫出来

```bash
zsteg 文件名 --all
```

## ningen

`010editor`看有压缩包的文件头，里面有个`txt`文件

`binwalk`分离有点问题

`foremost`分离后解密

将分离出的`zip`文件根据题目提示`4位数字`解密

密码为`8368`

解压后读取到`flag`

## 爱因斯坦

详细信息中有`this_is_not_password`信息

发现有图片拼接了两个压缩包

`foremost`分离后

使用之前的`this_is_not_password`解密

## 小明的保险箱

`foremost`分离文件

`rar` `4`位纯数字密码破解

密码为`7869 `

解密即可获取`flag`

## easycap

追踪第一个`tcp`流即可获得`flag`

![image-20231125151556206](./img/5-1.png)

## 隐藏的钥匙

详细信息没有可用信息

`010editor`搜索`flag`

找到一串被`base64`编码的字符串，`base64`解码即可获取`flags`

![image-20231125151736480](./img/6-1.png)

## 另外一个世界

在文件末尾找到了一串二进制信息

![image-20231125152054581](./img/7-1.png)

转为字符串为

![image-20231125152125927](./img/7-2.png)

## FLAG

`LSB`最低位隐写的时候发现`PK`即压缩包

`save bin`为`1.zip`

解压后发现一个文件

放到`kali`里用命令查看文件信息

```
file 1
```

![image-20231125153158999](./img/8-2.png)

是个`elf`文件,直接运行即可获取`flag`

![image-20231125153336515](./img/8-3.png)

## 神秘龙卷风

根据题目提示`4`位数字，使用`ARCHAR`暴破密码

密码为`5463`

![image-20231125153836011](./img/9-1.png)

`brainfuck`解密即可获取`flag`

## 数据包中的线索

`wireshark`打开数据包没有啥东西

导出`HTTP`发现文件`fenxi.php`比较可疑

先看看

![image-20231125154212739](./img/10-1.png)

发现`fenxi.php`内容应该为`base64编码`，解码后发现文件头为`jpg`头

![image-20231125154312639](./img/10-2.png)

保存为`jpg`文件后发现`flag`

![image-20231125154338970](./img/10-3.png)

`Capture2Text`

## 假如给我三天光明

盲文对照表

![在这里插入图片描述](./img/11-2.png)

密码为`kmdonowg`

解压后发现一个音频文件`.wav`，使用`audacity`打开，看波形猜测为摩斯电码

![image-20231125155754266](./img/12-1.png)

较长的蓝色即为“-”，较短的即为“.”，每一段由-和.组成的即为一个字符。可以按顺序将其莫斯解密，得到

```
-.-.  -  ..-.  .--  .--.  .  ..  -----  ---..  --...  ...--  ..---  ..--..  ..---  ...--  -..  --..
```

最后去除`ctf`并`小写字符串`提交

## 后门查杀

`D盾`扫描目录,发现木马

![image-20231125160803286](./img/13-1.png)

查看木马

![image-20231125160843649](./img/13-2.png)

## webshell后门

一样`D盾`扫

![image-20231125161052165](./img/14-1.png)

## 来首歌吧

`wav`文件，使用`audacity`打开

![image-20231125162947139](./img/15-1.png)

发现是`摩斯密码`

```
..... -... -.-. ----. ..--- ..... -.... ....- ----. -.-. -... ----- .---- ---.. ---.. ..-. ..... ..--- . -.... .---- --... -.. --... ----- ----. ..--- ----. .---- ----. .---- -.-.
```

解密即可`5BC925649CB0188F52E617D70929191C`

## 荷兰宽带数据泄露

解压后有一个`conf.bin`的文件

刚开始有点懵逼,后面看博客才知道原来要用`RoutePassView来查`

![image-20231125163734048](./img/16-1.png)

`Username`这个就是我们要找的值

## 面具下的flag

打开照片,查看详细信息,没有什么东西

`010editor`查看一下

![image-20231125164007319](./img/16-2.png)

发现有文件拼接

`binwalk`分离一下,有一个`flag.vmdk`了

但是还是看看压缩包先

压缩包有加密,先看看是不是`伪加密`

![image-20231125164629347](./img/16-3.png)

确实是`伪加密`

![image-20231125165050463](./img/16-4.png)

`7-zip`解压`vmdk`文件

```bash
7z x flag.vmdk -o./
```

发现文件列表为

```
┌──(c㉿ex)-[~/Desktop/fla]
└─$ tree                                  
.
|-- $RECYCLE.BIN
|   `-- S-1-5-21-2200156829-3544857562-508093875-1001
|       `-- desktop.ini
|-- [SYSTEM]
|   |-- $AttrDef
|   |-- $BadClus
|   |-- $Bitmap
|   |-- $Boot
|   |-- $Extend
|   |   |-- $ObjId
|   |   |-- $Quota
|   |   |-- $Reparse
|   |   `-- $RmMetadata
|   |       |-- $Repair
|   |       |-- $Repair:$Config
|   |       |-- $Txf
|   |       `-- $TxfLog
|   |           |-- $Tops
|   |           |-- $Tops:$T
|   |           `-- $TxfLog.blf
|   |-- $LogFile
|   |-- $MFT
|   |-- $MFTMirr
|   |-- $Secure
|   |-- $Secure:$SDS
|   |-- $UpCase
|   `-- $Volume
|-- key_part_one
|   `-- NUL
`-- key_part_two
    |-- where_is_flag_part_two.txt
    `-- where_is_flag_part_two.txt:flag_part_two_is_here.txt

10 directories, 23 files
```

`key_part_one/NUL`内容`brainfuck`解密后为

```
flag{N7F5_AD5
```

`key_part_two/where_is_flag_part_two.txt:flag_part_two_is_here.txt`

`ook`解密后为

```
_i5_funny!}
```

## 九连环

伪加密

直接找`Hex` `50 4B 01 02`然后后`4个hex`后的`2个hex`置为`00`

![image-20231125170940941](./img/17-1.png)

![image-20231125171548540](./img/17-2.png)

解压出来两个文件

![image-20231125171608307](./img/17-32.png)

两个文件,不太可能又是`伪加密`了

`steghide`看看图片有没有什么信息

```bash
steghide info good-已合并.jpg
```

![image-20231125171800313](./img/17-4.png)

把文件导出来

```
steghide extract -sf good-已合并.jpg
```

```
steghide extract -sf good-已合并.jpg
Enter passphrase: 
wrote extracted data to "ko.txt".
```

把`ko.txt`放到`windows`上读

内容为

```
看到这个图片就是压缩包的密码：
bV1g6t5wZDJif^J7
```

获得`flag`

## 被劫持的神秘礼物

![image-20231125172844497](./img/18-1.png)

过滤`http`包

![image-20231125172924391](./img/18-2.png)

## [BJDCTF2020]认真你就输了

`xls`文件打开后说是`flag`在下面

`linux`用`strings`命令查一下

```bash
$ strings 10.xls| grep flag   
xl/charts/flag.txtK
xl/charts/flag.txt
```

直接`foremost`分离后即可获取到`flag`

![image-20231125173503920](./img/19-1.png)

## [BJDCTF2020]藏藏藏

`010editor`打开后没找到什么

`steginfo`打开看了也没什么东西

`foremost`试试

发现分离出了一个`doc`文件

打开`doc`扫描里面的二维码即可获取`flag`

## 被偷走的文件

搜索`flag`发现有`flag.rar`,直接看看能不能导出

导出`ftp-data`对象

然后`4`位数密码暴破

密码为`5790`

## 刷新过的图片

`F5隐写`

题目提示

> 浏览图片的时候刷新键有没有用呢 注意：得到的 flag 请包上 flag{} 提交

半天都没有发现怎么做,看博客才知道用`F5-steganography`

切换到`java8`环境

```bash
java Extract ./file/Misc.jpg
```

文件输出到`F5-steganography`目录下面

发现`output.txt`

发现`output.txt`是`zip`文件

后缀名改为`zip`

发现用了`伪加密`

![image-20231125211156859](./img/20-1.png)

修改加密位后解密,即可获取`flag`

## [GXYCTF2019]佛系青年

`zip伪加密`

![image-20231125213458436](./img/21-1.png)

`与佛论禅`解密即可

## [BJDCTF2020]你猜我是个啥

`zip`解压失败

`010editor`查看是个`png`图片

在最后发现`flag`

![image-20231125213636841](./img/22-1.png)

## snake

发现有图片拼接,并且有`key`后面有`base64`的字符串

![image-20231125213811318](./img/23-1.png)

`base64`解密后为

```
What is Nicki Minaj's favorite song that refers to snakes?
```

![image-20231125224011261](./img/23-2.png)

## 秘密文件

打开流量包

发现有`ftp`流量

追踪`ftp`流

![image-20231125225820185](./img/24-1.png)

发现压缩包,`foremost`分离

得到一个`rar`压缩包

用`ARCHAR`破解密码,密码为`1903`

## [BJDCTF2020]just_a_rar

得到一个`rar`,文件名位`4位数.rar`

爆破结果为`2016`

得到一个`jpg`文件

`flag`在详细信息的备注里

## [BJDCTF2020]鸡你太美

有两张图片

副本那张显示有问题

`010editor`查看发现副本缺少`gif`文件头

插入`4`个字节文件头

打开`gif`即可获取`flag`

![image-20231125231440016](./img/25.1.png)

## 菜刀666

打开流量包

搜索`flag`发现`flag.txt`所在的压缩包,转储后发现有密码

没有伪加密,找找密码在哪

一个个看`tcp`流,在第`7`个流里发现文件

![image-20231125233844654](./img/26-1.png)

`Z1`进行`url`和`base64`解码后为一张图片的路径

![image-20231125233952098](./img/26-2.png)

`Z2`看起来是`jpg`文件的文件头

在`010editor`中`ctrl+shift+v`粘贴为`hex`存储

即可看到图片

![1](./img/26-3.png)

`foremost`分离出压缩包

用该密码解压即可

## [BJDCTF2020]一叶障目

`图片高度隐藏`

![image-20231126010631381](./img/27-1.png)

即可查看到图片高度隐藏信息

![image-20231126011009102](./img/27-2.png)

## [SWPU2019]神奇的二维码

扫码发现没有信息

![image-20231126011202874](./img/28-1.png)

`010editor`发现有合并文件,有个`rar`里包含`flag`文件

`foremost`分离居然失败了

使用`binwalk`

```
├─17012.rar
├─18394.rar
├─7104.rar
├─716A.rar
└─看看flag在不在里面^_^.rar
```

然后找到一个`doc`多次`base64`解码后得到`comEON_YOuAreSOSoS0great`

`encode.txt`里的内容`base64`解密后为`asdfghjkl1234567890`

两个有压缩包的密码,最后在`18394`里面找到`wav`文件

`morse`解密后获得`flag`

这题考点难道就是耐心?

## [BJDCTF2020]纳尼

头部本来应该为`GIF89a`,只剩下了`9a`,插入文件头即可

然后`stegsolve`逐祯读取

最后`base64`解码

## 梅花香之苦寒来

![image-20231126095108087](./img/29-1.png)

图内有大量`hex`数据

`hex`解密后为`坐标`

![image-20231126095150090](./img/29-2.png)

看来需要画图了

`matplotlib`绘图

去除文本左右的`(`和`)`

![image-20231126100526994](./img/30-1.png)

```python
import matplotlib.pyplot as plt
import numpy as np


# 用不了
# x = []
# y = []

# with open('./res.txt', 'r') as f:
#     txt = f.read().strip().replace('(', '').replace(')', '').split('\n')
#     for t in txt:
#         x.append(t.split(',')[0])
#         y.append(t.split(',')[1])
#     print(x[:5])
#     print(y[:5])
    
#     plt.plot(x, y, '.')
#     plt.show()

x, y = np.loadtxt('./res.txt', delimiter=',', unpack=True)

plt.plot(x, y, '.')
plt.show()
```

`QR Research`解码即可

## [HBNIS2018]excel破解

![image-20231126101434080](./img/31-1.png)

`010editor`打开即可看到内容

## [HBNIS2018]来题中等的吧

![附件5](./img/31-2.png)

`摩斯密码`解密即可

## 穿越时空的思念

`摩斯电码`

`audacity`

## [ACTF新生赛2020]outguess

`outguess`

在图片详细信息的备注里发现

`公正民主公正文明公正和谐`

`社会主义核心价值观解码`后为`abc`

```bash
outguess -r mmm.jpg -k abc res.txt
```

`res.txt`的内容即为`flag`

## 谁赢了比赛？

`010editor`打开时发现好像有压缩包

`foremost`分离看看

![image-20231126104327786](./img/32-1.png)

分离出了一个`rar`文件,有密码,尝试4位数字爆破

![image-20231126104222673](./img/32-2.png)

在`gif`里每帧进行查看

![image-20231126104911830](./img/32-3.png)

`310祯`有东西

保存看看每个通道

![image-20231126104953989](./img/32-4.png)

## [WUSTCTF2020]find_me

详细信息看到

```
⡇⡓⡄⡖⠂⠀⠂⠀⡋⡉⠔⠀⠔⡅⡯⡖⠔⠁⠔⡞⠔⡔⠔⡯⡽⠔⡕⠔⡕⠔⡕⠔⡕⠔⡕⡍=
```

第一眼看是盲文

结果看了一下对不上

需要用在线工具来解的盲文

https://www.qqxiuzi.cn/bianma/wenbenjiami.php?s=mangwen

```
wctf2020{y$0$u_f$1$n$d$_M$e$e$e$e$e}
```

## [SWPU2019]我有一只马里奥

`010editor`查看,发现似乎有其他文件,`foremost`试试

![image-20231126105555165](./img/33-1.png)

`foremost`解压有问题

使用`binwalk -e attachment.exe`

```
1.txt
39DC3
39DC3.zlib
3A8F8
3A8F8.zlib
50000.rar
```

`1.txt`内容为

```
ntfs      
flag.txt
```

`NTFS`流隐藏文件,扫描`1.txt`所在目录即可，使用工具`NtfsStreamsEditor`

![image-20231126115831583](./img/33-2.png)

## [GUET-CTF2019]KO

`brainfuck` `ook`解密

## [GXYCTF2019]gakki

发现`rar`文件

![image-20231126120211372](./img/34-1.png)

`foremost`分离

## [GXYCTF2019]gakki

`字频统计`

`010editor`发现有个压缩包拼接

`binwalk -e`分离

分离后发现压缩包有密码

`ARCHAR`4位数破解密码

破解密码解压后,发现一大堆无意义的字符串

看别人博客说是统计每个字符出现的次数,将出现次数最多的几个字符串拼接即可获得`flag`

```python
import string


with open('./flag.txt', 'r') as f:
    printables = string.printable
    file_contents = f.read().strip()
    res = {}
    for _, v in enumerate(printables):
        res[v] = file_contents.count(v)

    sort_res = sorted(res.items(), key=lambda x: x[1], reverse=True)
    # print(sort_res)
    
    for _, v in enumerate(sort_res):
        print(v[0], end='')
```

## [ACTF新生赛2020]base64隐写

加密程序

```python
# -*- coding: cp936 -*-
import base64
flag = 'Tr0y{Base64isF4n}' #flag
bin_str = ''.join([bin(ord(c)).replace('0b', '').zfill(8) for c in flag])
base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
with open('0.txt', 'rb') as f0, open('1.txt', 'wb') as f1: #'0.txt'是明文, '1.txt'用于存放隐写后的 base64
    for line in f0.readlines():
        rowstr = base64.b64encode(line.replace('\n', ''))
        equalnum = rowstr.count('=')
        if equalnum and len(bin_str):
            offset = int('0b'+bin_str[:equalnum * 2], 2)
            char = rowstr[len(rowstr) - equalnum - 1]
            rowstr = rowstr.replace(char, base64chars[base64chars.index(char) + offset])
            bin_str = bin_str[equalnum*2:]
        f1.write(rowstr + '\n')
```

`python3`

```python
import base64
b64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
with open('ComeOn!.txt', 'rb') as f:
    flag = ''
    bin_str = ''
    for line in f.readlines():
        stegb64 = str(line, "utf-8").strip("\n")
        rowb64 = str(base64.b64encode(base64.b64decode(stegb64)), "utf-8").strip("\n")
        offset = abs(b64chars.index(stegb64.replace('=', '')[-1]) - b64chars.index(rowb64.replace('=', '')[-1]))
        equalnum = stegb64.count('=')  # no equalnum no offset
        if equalnum:
            bin_str += bin(offset)[2:].zfill(equalnum * 2)
            # flag += chr(int(bin(offset)[2:].zfill(equalnum * 2), 2))
            # print(flag) 这样写得不出正确结果
        print([chr(int(bin_str[i:i + 8], 2)) for i in range(0, len(bin_str), 8)])
```

## [MRCTF2020]ezmisc

改一下图片高度即可

再重新打开图片文件即可查看到`flag`

## [HBNIS2018]caesar

简单`carsar`解密

## [SWPU2019]伟大的侦探

使用软件`010editor` `ebcdlc`编码

![image-20231126165938157](./img/35-1.png)

![image-20231126170048776](./img/35-2.png)

![img](./img/35-3.png)

`flag{iloveholmesandwllm}`

## [HBNIS2018]低个头

看键盘

根据题目提示，低下头能看见键盘，把键盘上的这几个键连接起来

![image-20220731142749966](./img/36-1.png)

## 黑客帝国

![image-20231126170715129](./img/37-2.png)

发现`rar`头,保存为文件,有密码,`4`位数破解

![image-20231126170644881](./img/37-1.png)

![image-20231126171128706](./img/37-3.png)

`jpg`的文件头改为了`png`的文件头

![image-20231126171229528](./img/37-4.png)

## [MRCTF2020]你能看懂音符吗

![image-20231126171412752](./img/38-1.png)

修复`rar`文件头

![image-20231126171506322](./img/38-2.png)

![image-20231126171745735](./img/38-3.png)

## [SUCTF2018]single dog

`010editor`发现有个压缩包文件

`binwalk`分离一下

发现`1.txt`

![image-20231126172206614](./img/39-1.png)

`AAEncode`解密

## 我吃三明治

发现有信息,看了下好像是`base32`或者`hex`,解码是`base32`

![image-20231126172412285](./img/40-1.png)

## [SWPU2019]你有没有好好看网课?

`010editor`没有发现什么信息

![image-20231126172756555](./img/41-1.png)

爆破密码解压后有个`docx`和一个`mp4`

`docx`的数字对应着`mp4`的帧

`kinovea`打开视频

![image-20231126174038292](./img/41-2.png)

![image-20231126174317361](./img/41-3.png)

![img](./img/41-4.png)

 最后组合起来,就是`wllmup_up_up`

这个就是压缩包`flag2.zip`的密码

解压后`hex`得到`flag`

![image-20231126174535618](./img/41-5.png)

## [ACTF新生赛2020]NTFS数据流

用`7z`或者`winrar`解压,`bandzip`解压会出问题

`NtfsStreamsEditor`扫描即可

![image-20231126175115508](./img/42-1.png)

## sqltest

看数据包发现是盲注

以最后查找`flag`的特征值为判断条件来查有哪些成功的

首先我们观察流量包，可以看到很多条这样的`http`请求，`url`中有`select`， `SCHEMA_name`等，可以确定是对`mysql`数据库的盲注

我们来把url的部分提取出来
一种方法是`导出http对象`，但是这样的话接下来就要手动读注入信息了，这很不方便

所以我们用`tshark`提取

```bash
tshark -r sqltest.pcapng -Y "http.request" -T fields -e http.request.full_uri > data.txt
# 下面这个参考
tshark -r sqlmap.pcapng -Y "ip.src == xxx.xxx.xxx.xxx && http.response" -T fields -E separator="~" -e http.response_for.uri -e http.file_data > data.txt
```

```bash
c@pc /m/c/U/c/Downloads> head -n 5 data.txt
http://172.16.80.11/index.php?act=news&id=1%20and%20length((select%20count(*)%20from%20information_schema.SCHEMATA))>100
http://172.16.80.11/index.php?act=news&id=1%20and%20length((select%20count(*)%20from%20information_schema.SCHEMATA))>50
http://172.16.80.11/index.php?act=news&id=1%20and%20length((select%20count(*)%20from%20information_schema.SCHEMATA))>25
http://172.16.80.11/index.php?act=news&id=1%20and%20length((select%20count(*)%20from%20information_schema.SCHEMATA))>12
http://172.16.80.11/index.php?act=news&id=1%20and%20length((select%20count(*)%20from%20information_schema.SCHEMATA))>6
```

获取值（628-972）
这一步就是我们要找的flag了，写一个脚本提取一下。我们知道注入语句为

```
id=1 and ascii(substr(((select concat_ws(char(94), flag)  from db_flag.tb_flag  limit 0,1)), {第i个字符}, 1))>{字符的ascii值}
```

我们把`第i个字符`和`ascii值`提取出来，取i变化时的值，脚本为：

```python
import urllib.parse
f = open("data.txt","r").readlines()

s = []
for i in range(627,972):
    data = urllib.parse.unquote(f[i]).strip()
    payload = data.split("and")[1]
    positions = payload.find("from db_flag.tb_flag  limit 0,1)), ")
    data1 = payload[positions+35:].split(",")[0]
    data2 = payload[positions+35:].split(">")[1]
    s.append([data1,data2])

for i in range(1,len(s)):
    if s[i][0]!=s[i-1][0]:
        print(chr(int(s[i-1][1])),end="")
print(chr(int(s[-1][1])))

```

下方仅为参考

```python
import urllib.parse
# 读入数据，数据中存在不可见字符，因此用rb模式
f = open("data.txt", "rb").readlines()

# 注入语句。
pattern = "AND ORD(MID((SELECT IFNULL(CAST(username AS NCHAR),0x20) FROM `security`.users ORDER BY username LIMIT 10,1),"
# 注入成功
trueInjection = "You are in..........."
temp = {}

for i in range(0, len(f)):
    line = str(f[i])[2:]
    # 上一步插入的分隔符，把数据分为url和data两部分
    if line.find("~") == -1:
        continue

    url, data = line.split("~")[0],line.split("~")[1]
    
    url = urllib.parse.unquote(url).strip()

    positions = url.find(pattern)
    if positions != -1:
        # 截取参数，data1 表示第几位数据，data2表示这一位数据的ascii值
        data1 = url[positions+len(pattern):].split(",")[0]
        data2 = url[positions+len(pattern):].split(">")[1].split(" ")[0]
        
        # data3: 注入结果的判断
        if data.find(trueInjection) != -1:
            data3 = True
        else:
            data3 = False
        if data1 not in temp:
            temp[data1]=[(data2,data3)]
        else:
            temp[data1].append((data2,data3))

    else:
        continue

# 盲注使用了二分法，所以也要根据这一点写代码解析数据
text=""
for i in temp:
    small = -1
    large = -1
    for j in temp[i]:
        if j[1] :
            small = j[0]
        else:
            large = j[0]
    if large != -1:
        text+=chr(int(large))
print(text)
```

## john-in-the-middle

可以看到都是`HTTP`的数据包，导出`HTTP`得到如下：

![image-20231126190354701](./img/44-1.png)

使用`stegslove`打开`scanlines.png`，在很[多通道](https://so.csdn.net/so/search?q=多通道&spm=1001.2101.3001.7020)都发现了一条线

![image-20231126190432630](./img/44-2.png)

`logo.png`图片中有条缺口

![image-20231126190512220](./img/44-3.png)

![image-20231126191122448](./img/44-4.png)

其实这个也勉强能看出来

将两张图片使用`stegslove`进行`Image Combiner`进行对比

`scanlines.png` `SUB` `logo.png`找到

![image-20231126191217277](./img/44-5.png)

## [ACTF新生赛2020]swp

导出`HTTP`对象后发现有`secret.zip`

猜测是`zip伪加密`

使用`ZipCenOp.jar`

![image-20231126191935235](./img/45-1.png)

![image-20231126192034948](./img/45-2.png)

## [UTCTF2020]docx

`doc`里没有什么信息

解压后在`word/medie`里发现`flag`

## [GXYCTF2019]SXMgdGhpcyBiYXNlPw==

`base64隐写`

```python
def get_base64_diff_value(s1, s2):
    base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    res = 0
    for i in xrange(len(s2)):
        if s1[i] != s2[i]:
            return abs(base64chars.index(s1[i]) - base64chars.index(s2[i]))
    return res


def solve_stego():
    with open('flag.txt', 'rb') as f:
        file_lines = f.readlines()
        bin_str = ''
        for line in file_lines:
            steg_line = line.replace('\n', '')
            norm_line = line.replace('\n', '').decode('base64').encode('base64').replace('\n', '')
            diff = get_base64_diff_value(steg_line, norm_line)
            print diff
            pads_num = steg_line.count('=')
            if diff:
                bin_str += bin(diff)[2:].zfill(pads_num * 2)
            else:
                bin_str += '0' * pads_num * 2
            print goflag(bin_str)


def goflag(bin_str):
    res_str = ''
    for i in xrange(0, len(bin_str), 8):
        res_str += chr(int(bin_str[i:i + 8], 2))
    return res_str


if __name__ == '__main__':
    solve_stego()

```

`python2`运行

## 喵喵喵

详细信息 `010editor`和`binwalk大法`都没发现什么

上`stegsolve`

![image-20231126194047226](./img/46-1.png)

应该是`lsb`低位隐写,上`zsteg`看看

![image-20231126194507791](./img/46-2.png)

修复文件头,发现只显示了一般,修改高度

![image-20231126194713700](./img/46-3.png)

![image-20231126195122970](./img/46-4.png)

下载后只有个`flag.txt`,没有`flag`,猜测`NTFS流隐写`

![image-20231126195441747](./img/46-5.png)

`uncompyle6`转为`python`后为

```python
# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.8 (tags/v3.9.8:bb3fdcf, Nov  5 2021, 20:48:33) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: flag.py
# Compiled at: 2017-12-05 23:42:15
import base64

def encode():
    flag = '*************'
    ciphertext = []
    for i in range(len(flag)):
        s = chr(i ^ ord(flag[i]))
        if i % 2 == 0:
            s = ord(s) + 10
        else:
            s = ord(s) - 10
        ciphertext.append(str(s))

    return ciphertext[::-1]


ciphertext = [
 '96', '65', '93', '123', '91', '97', '22', '93', '70', '102', '94', 
 '132', '46', '112', '64', '97', '88', '80', '82', '137', '90', '109', 
 '99', '112']
# okay decompiling flag.pyc
```

解密脚本为

```python
ciphertext = ['96', '65', '93', '123', '91', '97', '22', '93', '70', '102', '94', 
'132', '46', '112', '64', '97', '88', '80', '82', '137', '90', '109', 
'99', '112']


def decode(ciphertext):
    flag = ''
    for i, v in enumerate(ciphertext):
        if i % 2 == 0:
            s = int(v) - 10
        else:
            s = int(v) + 10
        flag += chr(s ^ i)
    print(flag)

if __name__ == '__main__':
    decode(ciphertext[::-1])
```

## 间谍启示录

拿到`iso`文件先解压了一下,其他没发现什么内容

看`systemzx.exe`的时候发现有文件拼接

`binwalk -e systemzx.exe`分离出了一个压缩包

解压后有`flag.exe` `文件已被销毁.exe`

运行`flag.exe`即可获取`机密文件.txt` 里面有`flag`

## [RoarCTF2019]黄金6年

`kinovea`打开视频逐帧看

![image-20231126201352287](./img/47-1.png)

![image-20231126201436818](./img/47-2.png)

![image-20231126201602072](./img/47-3.png)

![image-20231126201541182](./img/47-4.png)

![image-20231126201646293](./img/47-5.png)

![image-20231126201719318](./img/47-6.png)

![image-20231126201807149](./img/47-7.png)

![image-20231126201828134](./img/47-8.png)

提交之后不对

然后`010editor`在文件最后发现一串`base64`编码的字符串

解码后发现为`rar`文件

解压密码为`iwantplayctf`

## 小易的U盘

解压后发现`autorun.inf`

![image-20231126202607870](./img/48-1.png)



`autoflag - 副本 (32).exe`用`ida`打开

`Shift+F12`发现`flag`

![image-20231126202755875](./img/48-2.png)

## [WUSTCTF2020]爬

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

## Mysterious

`010editor`没发现啥东西

用`ida`打开 `Shift+F12`查看字符串

![image-20231126212809857](./img/50-1.png)

进入`sub_401090`函数看看

`F5`查看源码

![image-20231126212925750](./img/50-2.png)

`flag{123_Buff3r_0v3rf|0w}`

## [WUSTCTF2020]alison_likes_jojo

两个文件

发现`boki.jpg`有合并文件

`binwalk`分离

分离出一个压缩包,`6`位数字爆破

得到`base.txt`

```
WVRKc2MySkhWbmxqV0Zac1dsYzBQUT09
```

`base64`三次解密后为

`killerqueen`

应该是密钥之类的,试试使用`outguess`

```bash
outguess -r -k killerqueen jljy.jpg data.txt
```

获得`flag`

## 弱口令

`lsb弱口令`

没发现伪加密

爆破也没破出来

`bandzip`看了也没注意到注释

![image-20231126222650718](./img/51-1.png)

复制到`sublime`可以看见

![image-20231126223052289](./img/51-2.png)

摩斯解密为`HELL0FORUM`

槽点`lsb.py`和`crypt.py`要在一起

卡半天

```bash
python2 lsb.py extract 女神.png res.txt 123456
```

## [安洵杯 2019]吹着贝斯扫二维码

### 批处理加后缀的两种方法

```
@echo off
ren * *.jpg
```

```python
import os

path = 'C:\\Users\\Administrator\\Downloads\\test'
for i in os.listdir('./test'):
	if i == 'flag.zip':
		continue
	else:
		oldname = os.path.join(path,i)
		newname = os.path.join(path,i+'.jpg')
		os.rename(oldname,newname)
```

`ps`拼接二维码

懒,就用别人拼好的了

![在这里插入图片描述](./img/52-1.png)

```
BASE Family Bucket ??? 
85->64->85->13->16->32

那我们就反着来解
```

![image-20231126230047155](./img/52-2.png)

![image-20231126230317851](./img/52-3.png)

## zip

很多压缩包，但是里面的内容非常小，小于5字节，可以尝试使用`CRC32爆破`得到其内容

```python
import zipfile
import os
import itertools
import string
import binascii

f = open('out.txt', 'w')

dic = string.ascii_letters + string.digits + '+/='

def crack_crc(crc):
    for i, j, k, h in itertools.product(dic, dic, dic, dic):
        s = i + j + k + h
        if crc == (binascii.crc32(s.encode())):
            return s



# crc = zipfile.ZipFile('./out0.zip', 'r').getinfo('data.txt').CRC

for i in range(0, 68):
    filename = 'out%s.zip'%i
    res = crack_crc(zipfile.ZipFile(filename, 'r').getinfo('data.txt').CRC)
    f.write(res)
    print(f'loading {filename}')

print('Finish...')
f.close()
```

![image-20231126233850518](./img/52-4.png)

文件尾是`rar`的文件尾,加一个`rar`的文件头

压缩包注释中有`flag`

![image-20231126234106223](./img/52-5.png)

## 从娃娃抓起

`中文电码` http://code.mcdvisa.com/

`五笔 `http://life.chacuo.net/convertwubi 

http://www.zd9999.com/wb/search.asp

> 0086 1562 2535 5174
> bnhn s wwy vffg vffg rrhy fhnv
>
> 请将你得到的这句话转为md5提交，md5统一为32位小写。
> 提交格式：flag{md5}

`人工智能也要从娃娃抓起`

## [GUET-CTF2019]zips

先爆破`222.zip`

密码为`723456`

`111.zip`文件里`伪加密`

解密后`setup.sh`

```
#!/bin/bash
#
zip -e --password=`python -c "print(__import__('time').time())"` flag.zip flag
```

是`python2`运行的

根据时间往前推获取密码

```
1701014072.27
```

这样的格式

最终密码为`1558080832.15`

## [WUSTCTF2020]girlfriend

听起来像是在打电话输入号码的声音，猜测`DTMF拨号音识别`

`dtmf2num.exe`

![image-20231127125544797](./img/53-1.png)

```
999*666*88*2*777*33*6*999*4*444*777*555*333*777*444*33*66*3*7777
```

手机键盘密码

![在这里插入图片描述](./img/53-2.png)

```
999     --->   y
666     --->   o
88      --->   u
2       --->   a
777     --->   r
33      --->   e
6       --->   m
999     --->   y
4       --->   g
4444    --->   i
777     --->   r
555     --->   l
333     --->   f
777     --->   r
444     --->   i
33      --->   e
66      --->   n
3       --->   d
7777    --->   s
```

[参考](https://blog.csdn.net/mochu7777777/article/details/105412940)

## [UTCTF2020]file header

将`png`文件头加上即可

## [DDCTF2018](╯°□°）╯︵ ┻━┻

题目

```
(╯°□°）╯︵ ┻━┻
50pt

(╯°□°）╯︵ ┻━┻

d4e8e1f4a0f7e1f3a0e6e1f3f4a1a0d4e8e5a0e6ece1e7a0e9f3baa0c4c4c3d4c6fbb9b2b2e1e2b9b9b7b4e1b4b7e3e4b3b2b2e3e6b4b3e2b5b0b6b1b0e6e1e5e1b5fd
```

一开始被这个`(╯°□°）╯︵ ┻━┻`误导以为是`jjencode`跟`AAencode`,密文试了`hex`，尝试了好久没啥结果，后面又有人说是翻转，试了很久还是没结果。然后跑了下移位密码获取`flag`

```python
s='d4e8e1f4a0f7e1f3a0e6e1f3f4a1a0d4e8e5a0e6ece1e7a0e9f3baa0c4c4c3d4c6fbb9e1e6b3e3b9e4b3b7b7e2b6b1e4b2b6b9e2b1b1b3b3b7e6b3b3b0e3b9b3b5e6fd'
for j in range(20):
    s1=''
    for x in range(len(s)//2):
        s1+=chr((int(s[x*2:x*2+2],16)-j)%128)
    print(s1)
```

![image-20231127130449188](./img/54-1.png)

`python2`运行

提交才发现不对

```python
string = 'd4e8e1f4a0f7e1f3a0e6e1f3f4a1a0d4e8e5a0e6ece1e7a0e9f3baa0c4c4c3d4c6fbb9b2b2e1e2b9b9b7b4e1b4b7e3e4b3b2b2e3e6b4b3e2b5b0b6b1b0e6e1e5e1b5fd'
flag = ''
for i in range(len(string)/2):
    tmp = int(string[2*i:2*i+2], 16)
    tmp = tmp & 0b01111111
    flag += chr(tmp)
print flag
```

## [XMAN2018排位赛]通行证

题目：`a2FuYmJyZ2doamx7emJfX19ffXZ0bGFsbg==`

`base64解密`

```
kanbbrgghjl{zb____}vtlaln
```

利用[栅栏密码网站](http://ctf.ssleye.com/railfence.html)进行`**加密**`，Key等于`7`.开始以为是解密

```
kzna{blnl_abj_lbh_trg_vg}
```

`rot13`解密

```
xman{oyay_now_you_get_it}
```

## [MRCTF2020]千层套路

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

## 百里挑一

> 好多漂亮的壁纸，赶快挑一张吧！ 注意：得到的 flag 请包上 flag{} 提交

打开流量包,把所有的照片保存到导出到文件夹

使用`exiftool`

![image-20231128170133698](./img/56-1.png)

另外一半在`tcp114`流里

![image-20231128170402066](./img/56-2.png)

## [MRCTF2020]CyberPunk

是到了2020.9.17这个日子，会给我们flag，修改下当前系统时间

![image-20231128171201622](./img/57-1.png)

## [SUCTF2018]followme

下载附件，拖进[wireshark](https://so.csdn.net/so/search?q=wireshark&spm=1001.2101.3001.7020)中查看协议分级

![image-20231128171732371](./img/57-2.png)

`http`协议占的比较多

`http`占了大部分，导出`http`对象，很多个文件，查看

![image-20231128172021656](./img/57-3.png)

看了几个文件,`password`参数不同,应该是在爆破密码

`grep`看看关键词`flag`和`CTF`

![image-20231128172152507](./img/57-4.png)

## [安洵杯 2019]Attack

搜索`flag`

发现一个压缩包

![image-20231128173305505](./img/58-1.png)

重新分析流量包，搜索查看常用协议，发现在http协议中存在lsass.dmp

![image-20231128203342676](./img/58-2.png)

（`*.dmp`文件是`windows`系统中的错误转储文件，当`Windows`发生错误蓝屏的时候，系统将当前内存【含虚拟内存】中的数据直接写到文件中去，方便定位故障原因。）

（`*`里面包含主机用户密码信息）

**关于lsass**
`lsass`是`windows`系统的一个进程，用于本地安全和登陆策略。`mimikatz`可以从` lsass.exe `里获取`windows`处于`active`状态账号明文密码。本题的`lsass.dmp`就是内存运行的镜像，也可以提取到账户密码

把`lsass.dmp`复制到`mimikatz`的目录，然后运行`mimikatz`

```
//提升权限
privilege::debug
//载入dmp文件
sekurlsa::minidump lsass.dmp
//读取登陆密码
sekurlsa::logonpasswords full
```

![image-20231128204009002](./img/58-3.png)

## [SUCTF 2019]Game

首先在`src.zip`下面找到了一个`index.html`,`base32`解码成功

![image-20231128205224012](./img/59-1.png)

然后来看照片,`010editor`和`zsteg`都没找到什么东西

用`stegsolve`看看有没有`lsb低位隐写`

![image-20231128205112619](./img/59-2.png)

发现一串`base64`字符串

![image-20231128205653175](./img/59-3.png)

以`Salted`开头,可能是`AES`或`3DES`

https://www.sojson.com/encrypt_triple_des.html

![image-20231128210342031](./img/59-4.png)

## USB

虽然能正常解压,但文件头不对,`7A`改为`74`

```
52 61 72 21 1A 07 00 CF 90 73 00 00 0D 00 00 00 00 00 00 00 D7 62 74 A0 90 2C 00 38 B0
```

![image-20231128210633086](./img/60-1.png)

然后解压出`233.png`

用`stegsolve`打开

![image-20231128211105030](./img/60-2.png)

蓝色`0`通道发现一张二维码

扫描得到`ci{v3erf_0tygidv2_fc0}`

看起来是栅栏密码,但是没有`a`,无法构成`flag`

再看看`key.ftm`.`binwalk`看一下

发现`key.pcap`

全是`USB`协议

```bash
tshark -r key.pcap -T fields -e usb.capdata > usbdata.txt
```

导出`usbdata.txt`后跑脚本

```python
import sys
import os

DataFileName = "usb.dat"

presses = []

normalKeys = {"04":"a", "05":"b", "06":"c", "07":"d", "08":"e", "09":"f", "0a":"g", "0b":"h", "0c":"i", "0d":"j", "0e":"k", "0f":"l", "10":"m", "11":"n", "12":"o", "13":"p", "14":"q", "15":"r", "16":"s", "17":"t", "18":"u", "19":"v", "1a":"w", "1b":"x", "1c":"y", "1d":"z","1e":"1", "1f":"2", "20":"3", "21":"4", "22":"5", "23":"6","24":"7","25":"8","26":"9","27":"0","28":"<RET>","29":"<ESC>","2a":"<DEL>", "2b":"\t","2c":"<SPACE>","2d":"-","2e":"=","2f":"[","30":"]","31":"\\","32":"<NON>","33":";","34":"'","35":"<GA>","36":",","37":".","38":"/","39":"<CAP>","3a":"<F1>","3b":"<F2>", "3c":"<F3>","3d":"<F4>","3e":"<F5>","3f":"<F6>","40":"<F7>","41":"<F8>","42":"<F9>","43":"<F10>","44":"<F11>","45":"<F12>"}

shiftKeys = {"04":"A", "05":"B", "06":"C", "07":"D", "08":"E", "09":"F", "0a":"G", "0b":"H", "0c":"I", "0d":"J", "0e":"K", "0f":"L", "10":"M", "11":"N", "12":"O", "13":"P", "14":"Q", "15":"R", "16":"S", "17":"T", "18":"U", "19":"V", "1a":"W", "1b":"X", "1c":"Y", "1d":"Z","1e":"!", "1f":"@", "20":"#", "21":"$", "22":"%", "23":"^","24":"&","25":"*","26":"(","27":")","28":"<RET>","29":"<ESC>","2a":"<DEL>", "2b":"\t","2c":"<SPACE>","2d":"_","2e":"+","2f":"{","30":"}","31":"|","32":"<NON>","33":":","34":"\"","35":"<GA>","36":"<","37":">","38":"?","39":"<CAP>","3a":"<F1>","3b":"<F2>", "3c":"<F3>","3d":"<F4>","3e":"<F5>","3f":"<F6>","40":"<F7>","41":"<F8>","42":"<F9>","43":"<F10>","44":"<F11>","45":"<F12>"}

def main():
    # check argv
    if len(sys.argv) != 2:
        print("Usage : ")
        print("        python UsbKeyboardHacker.py data.pcap")
        print("Tips : ")
        print("        To use this python script , you must install the tshark first.")
        print("        You can use `sudo apt-get install tshark` to install it")
        print("Author : ")
        print("        WangYihang <wangyihanger@gmail.com>")
        print("        If you have any questions , please contact me by email.")
        print("        Thank you for using.")
        exit(1)

    # get argv
    pcapFilePath = sys.argv[1]
    
    # get data of pcap
    os.system("tshark -r %s -T fields -e usb.capdata 'usb.data_len == 8' > %s" % (pcapFilePath, DataFileName))

    # read data
    with open(DataFileName, "r") as f:
        for line in f:
            presses.append(line[0:-1])
    # handle
    result = ""
    for press in presses:
        if press == '':
            continue
        if ':' in press:
            Bytes = press.split(":")
        else:
            Bytes = [press[i:i+2] for i in range(0, len(press), 2)]
        if Bytes[0] == "00":
            if Bytes[2] != "00" and normalKeys.get(Bytes[2]):
                result += normalKeys[Bytes[2]]
        elif int(Bytes[0],16) & 0b10 or int(Bytes[0],16) & 0b100000: # shift key is pressed.
            if Bytes[2] != "00" and normalKeys.get(Bytes[2]):
                result += shiftKeys[Bytes[2]]
        else:
            print("[-] Unknow Key : %s" % (Bytes[0]))
    print("[+] Found : %s" % (result))

    # clean the temp data
    os.system("rm ./%s" % (DataFileName))


if __name__ == "__main__":
    main()
```

得到`KEYXINAN`

![image-20231128211950118](./img/60-3.png)

[参考1](https://guokeya.github.io/post/buuctf-usbwei-ji-ni-ya-mi-ma-rar-xiu-fu-usb-liu-liang/)

[参考2](https://www.cnblogs.com/vuclw/p/16422232.html)

维吉尼亚解密后栅栏解密(有密钥的凯撒密码)

![image-20231128212148942](./img/60-4.png)

## [UTCTF2020]basic-forensics

`010editor`搜索后可以直接获取`flag`

## [BSidesSF2019]zippy

搜索`flag`发现压缩密码

![image-20231128220732656](./img/61-1.png)

`binwalk`分离流量包分离出`zip`文件

解压获取`flag`

## 虚假的压缩包

解压后先解压虚假的压缩包

`010editor`修复伪加密,解压后有`key.txt`

```
数学题
n = 33
e = 3
解26

-------------------------
答案是
```

`exp`

```python
from factordb.factordb import FactorDB
import gmpy2

n = 33
e = 3

conn = FactorDB(n)
conn.connect()
p, q = conn.get_factor_list()

d = gmpy2.invert(e, (p-1) * (q-1))

print(pow(int(26), d, n))
```

结果是`5`,所以解压密码是`答案是5`

发现有个`png`,但是后缀为`jpg`的文件,改为`png`让`010editor`识别

修改高度时发现

![image-20231128222113951](./img/62-1.png)

叫我们`异或5`,那我们对每个数据`hex`都`异或5`

编写代码

```python
import binascii
flag_data = ''

with open('./亦真亦假', 'r') as f:
    xor_data = f.read()
    
    for data in xor_data:
        tmp = int(data, 16) ^ 5
        flag_data += hex(tmp)[2:]
        
    print(flag_data)
    
    write_file = open('res.txt', 'wb')
    write_file.write(binascii.unhexlify(flag_data))
    write_file.close()
```

写入`txt`后发现似乎是`doc`数据,改后缀为`doc`查看

搜索`flag`,发现`flag`被隐藏,更改一下文字颜色即可

## [RCTF2019]draw

`logo`语言编程

> cs pu lt 90 fd 500 rt 90 pd fd 100 rt 90 repeat 18[fd 5 rt 10] lt 135 fd 50 lt 135 pu bk 100 pd setcolor pick [ red orange yellow green blue violet ] repeat 18[fd 5 rt 10] rt 90 fd 60 rt 90 bk 30 rt 90 fd 60 pu lt 90 fd 100 pd rt 90 fd 50 bk 50 setcolor pick [ red orange yellow green blue violet ] lt 90 fd 50 rt 90 fd 50 pu fd 50 pd fd 25 bk 50 fd 25 rt 90 fd 50 pu setcolor pick [ red orange yellow green blue violet ] fd 100 rt 90 fd 30 rt 45 pd fd 50 bk 50 rt 90 fd 50 bk 100 fd 50 rt 45 pu fd 50 lt 90 pd fd 50 bk 50 rt 90 setcolor pick [ red orange yellow green blue violet ] fd 50 pu lt 90 fd 100 pd fd 50 rt 90 fd 25 bk 25 lt 90 bk 25 rt 90 fd 25 setcolor pick [ red orange yellow green blue violet ] pu fd 25 lt 90 bk 30 pd rt 90 fd 25 pu fd 25 lt 90 pd fd 50 bk 25 rt 90 fd 25 lt 90 fd 25 bk 50 pu bk 100 lt 90 setcolor pick [ red orange yellow green blue violet ] fd 100 pd rt 90 arc 360 20 pu rt 90 fd 50 pd arc 360 15 pu fd 15 setcolor pick [ red orange yellow green blue violet ] lt 90 pd bk 50 lt 90 fd 25 pu home bk 100 lt 90 fd 100 pd arc 360 20 pu home

https://www.calormen.com/jslogo/

在线运行即可

![image-20231128223516698](./img/63-1.png)

## [ACTF新生赛2020]明文攻击

`zip`文件格式

![0](./img/64-2.png)

更改文件头为`50 4B`

![image-20231128223904004](./img/64-1.png)

解压出`flag.txt`

```
this is the flag.
```



然后进行明文攻击，因为压缩包的大小不同，可以用`winrar`自动进行修复
(因为flag.txt的crc32相同，但是压缩后的大小都不同！而且res.zip包压缩后大小比较大)
最后明文攻击跑出flag
明文攻击用ARCHPR这个软件即可。

要解压的文件为`res.zip`

![0](./img/65-1.png)

![image-20231129103535262](./img/65-2.png)

## [SWPU2019]Network

`TTL`隐写

```
    IP报文在路由间穿梭的时候每经过一个路由，TTL就会减1，当TTL为0的时候，该报文就会被丢弃。
    TTL所占的位数是8位，也就是0-255的范围，但是在大多数情况下通常只需要经过很小的跳数就能完成报文的转发，
    远远比上限255小得多，所以我们可以用TTL值的前两位来进行传输隐藏数据。
    如：须传送H字符，只需把H字符换成二进制，每两位为一组，每次填充到TTL字段的开头两位并把剩下的6位设置为1（xx111111），这样发4个IP报文即可传送1个字节。
```

根据上述规则，可以知道TTL隐写中用到四个值：`00 111111`（63）,`01 111111`（127）,`10 111111`（191）,`11 111111`（255）,解密的时候只取前两位，然后转换成ascii
简化一下，可以这么认为：
用

```
00 替换 63
01 替换 127
10 替换 191
11 替换 255
```

简化一下，可以这么认为：
用



```
00 替换 63
01 替换 127
10 替换 191
11 替换 255
```

于是可以写脚本：



```python
import binascii
f=open("attachment.txt","r")
f2=open("result.txt","wb")
num=''
res=''
for i in f:
    if int(i)==63:
        num+="00"
    if int(i)==127:
        num+="01"
    if int(i)==191:
        num+="10"
    if int(i)==255:
        num+="11"
for j in range(0,len(num),8):
    res += chr(int(num[j:j+8],2))#转换为字符
res = binascii.unhexlify(res)#unhexlify:从十六进制字符串返回二进制数据
f2.write(res)
```

发现结束后`010editor`查看后发现为`zip`文件,并且有`伪加密`

更改伪加密位后,更改后缀名为`zip`解压

得到一串字符串

![image-20231129221331675](./img/66-1.png)

有很多层`base64`,编写代码

```python
import base64

with open('./flag.txt', 'r') as f:
    b64 = f.read().strip()
    txt = b64
    while True:
        txt = base64.urlsafe_b64decode(txt)
        if "flag" in txt.decode():
            print(txt.decode())
            exit(0)
```

[参考](https://www.cnblogs.com/yunqian2017/p/14671031.html)

## [MRCTF2020]Hello_ misc

首先`010editor`发现有个合并文件`zip`文件

然后解压`zip`文件发现有密码,更改`伪加密`处依旧有代码

`stegsolve`看看,在`red`通道发现有隐藏信息

![image-20231129225447285](./img/67-1.png)

在`Red7`通道发现`png`文件

![image-20231129225534304](./img/67-2.png)

发现`png`文件中给出了压缩包密码

![image-20231129225622429](./img/67-3.png)

![image-20231129225728113](./img/67-4.png)

发现就是上一题的`TTL`隐写

```python
with open('out.txt','r') as Dec:
    res = ''
    for i in Dec.readlines():
        Bin = '{:08b}'.format(int(i))
        print(Bin)
        Sub_Bin = Bin[:-6]
        res += Sub_Bin
    print(res)

    for j in range(0,len(res),8):
        full_bin = res[j:j+8]
        print(chr(int(full_bin,2)),end="")

```

`rar-passwd:0ac1fe6b77be5dbe`

[参考](https://blog.csdn.net/mochu7777777/article/details/109680577)

![image-20231129230138512](./img/67-5.png)

```
MTEwMTEwMTExMTExMTEwMDExMTEwMTExMTExMTExMTExMTExMTExMTExMTExMTExMTAxMTEwMDAwMDAxMTExMTExMTExMDAxMTAx
MTEwMTEwMTEwMDAxMTAxMDExMTEwMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTAxMTExMTExMTExMTExMTEwMTEwMDEx
MTEwMDAwMTAxMTEwMTExMDExMTEwMTExMTExMTAwMDExMTExMTExMTExMDAxMDAxMTAxMTEwMDAwMDExMTExMDAwMDExMTExMTEx
MTEwMTEwMTAwMDAxMTExMDExMTEwMTExMTExMDExMTAxMTExMTExMTEwMTEwMTEwMTAxMTExMTExMTAwMTEwMTExMTExMTExMTEx
MTEwMTEwMTAxMTExMTExMDExMTEwMTExMTAxMDExMTAxMTExMTExMTEwMTEwMTEwMTAxMTAxMTExMTAwMTEwMTExMTExMTExMTEx
MTEwMTEwMTAwMDAxMTAwMDAwMTEwMDAwMDAxMTAwMDExMTAwMDAwMTEwMTEwMTEwMTAxMTEwMDAwMDAxMTExMDAwMDExMTExMTEx
```

![image-20231129230859115](./img/67-6.png)

还以为是二进制转啥,其实是大文字

把`1`全部替换为`空格`

![image-20231129231017971](./img/67-7.png)

```python
import base64

txt = '''MTEwMTEwMTExMTExMTEwMDExMTEwMTExMTExMTExMTExMTExMTExMTExMTExMTExMTAxMTEwMDAwMDAxMTExMTExMTExMDAxMTAx
MTEwMTEwMTEwMDAxMTAxMDExMTEwMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTAxMTExMTExMTExMTExMTEwMTEwMDEx
MTEwMDAwMTAxMTEwMTExMDExMTEwMTExMTExMTAwMDExMTExMTExMTExMDAxMDAxMTAxMTEwMDAwMDExMTExMDAwMDExMTExMTEx
MTEwMTEwMTAwMDAxMTExMDExMTEwMTExMTExMDExMTAxMTExMTExMTEwMTEwMTEwMTAxMTExMTExMTAwMTEwMTExMTExMTExMTEx
MTEwMTEwMTAxMTExMTExMDExMTEwMTExMTAxMDExMTAxMTExMTExMTEwMTEwMTEwMTAxMTAxMTExMTAwMTEwMTExMTExMTExMTEx
MTEwMTEwMTAwMDAxMTAwMDAwMTEwMDAwMDAxMTAwMDExMTAwMDAwMTEwMTEwMTEwMTAxMTEwMDAwMDAxMTExMDAwMDExMTExMTEx'''

b64_seg = txt.split('\n')
# print(b64_seg)c
for i, v in enumerate(b64_seg):
    print(base64.b64decode(b64_seg[i]).decode().replace('1', ' '))
```

## [UTCTF2020]zero

> Lorem ipsum dolor ‌‌‌‌‍﻿‍‍sit amet‌‌‌‌‍﻿‍‌, consectetur adipiscing‌‌‌‌‍‬‍‬ elit.‌‌‌‌‍‬﻿‌‌‌‌‌‍‬‌‍ Phasellus quis tempus ante, nec vehicula mi. ‌‌‌‌‍‬‍﻿Aliquam nec‌‌‌‌‍﻿‬﻿ nisi ut neque interdum auctor.‌‌‌‌‍﻿‍﻿ Aliquam felis ‌‌‌‌‍‬‬‌orci, vestibulum ‌‌‌‌‍﻿‬‍sit amet ante‌‌‌‌‍‌﻿‬ at, consectetur‌‌‌‌‍‌﻿﻿ lobortis eros.‌‌‌‌‍‍‍‌ ‌‌‌‌‍‌‌‌Orci varius natoque ‌‌‌‌‍﻿‌﻿penatibus et ‌‌‌‌‍‬‌﻿magnis‌‌‌‌‌﻿‌‍‌‌‌‌‌﻿‌‍ dis ‌‌‌‌‍‍﻿﻿parturient montes, nascetur ridiculus ‌‌‌‌‌﻿‍‌‌‌‌‌‌﻿‬‍mus. In finibus‌‌‌‌‌﻿‌‬ magna‌‌‌‌‌﻿‍﻿ mauris, quis‌‌‌‌‍‬‌‍ auctor ‌‌‌‌‍‬‌‍libero congue quis. ‌‌‌‌‍‬‬‬Duis‌‌‌‌‍‬‌‬ sagittis consequat urna non tristique. Pellentesque eu lorem ‌‌‌‌‍﻿‌‍id‌‌‌‌‍‬‬﻿ quam vestibulum ultricies vel ac purus‌‌‌‌‌﻿‌‍.‌‌‌‌‌﻿‍‌‌‌‌‌‍﻿﻿‍

刚开始以为是字频分析,放到`qiupqiup`没发现什么

用`cat`打开,发现很多不可见字符

![image-20231129231602064](./img/68-1.png)

用`vim`打开

![image-20231129231628969](./img/68-2.png)

零宽度字符隐写：https://330k.github.io/misc_tools/unicode_steganography.html

![image-20231129231724473](./img/68-3.png)

[参考](https://blog.csdn.net/mochu7777777/article/details/109817723)

## [WUSTCTF2020]spaceclub

![image-20231129234323396](./img/69-1.png)

刚开始以为是`摩斯密码`,其实是二进制,短的空格为`0`,长的空格为`1`,替换,`先替换长空格,再替换短空格`,最后

![image-20231129234641009](./img/70-1.png)

去除`换行符`

![image-20231129234721832](./img/70-2.png)

## [GKCTF 2021]签到

追踪`http`流

![image-20231130002915313](./img/71-1.png)

发现会返回`hex`编码

解码后发现是需要`reverse`以下

最后导出`http`流中发现数据

解码后发现

![image-20231130003046893](./img/71-2.png)

**整理一下得到flag{Welc0me_GkC4F_m1siCCCCCC!}**

## [ACTF新生赛2020]music

文件异常，并且出现多次字符`A1`

猜测对整个原文件进行了异或，使用`010 Editor`在`工具->十六进制运算->二进制异或`对整个文件内容进行异或

![image-20231130004312094](./img/72-1.png)

异或后听声音即可获得`flag`

## [MRCTF2020]Unravel!!

有三个文件

```
c@pc /m/c/U/c/D/a/Unravel> ll
total 11M
-rwxrwxrwx 1 c c 399K Mar 12  2020 JM.png*
-rwxrwxrwx 1 c c 5.8M Mar 15  2020 Look_at_the_file_ending.wav*
-rwxrwxrwx 1 c c 4.8M Mar 12  2020 win-win.zip*
```

先看看第一个文件

![image-20231130105832762](./img/73-1.png)

似乎是`base64`,解码看看

![image-20231130111631531](./img/73-2.png)

发现`salted`,应该是`AES`或`3DES`

找密钥,`binwalk`看看照片

![image-20231130111834449](./img/73-3.png)

发现`AES`密钥

![image-20231130112245185](./img/73-4.png)

使用`SilentEye`[Decode](https://so.csdn.net/so/search?q=Decode&spm=1001.2101.3001.7020)`Ending.wav`

![image-20231130112427165](./img/73-5.png)

## [CFI-CTF 2018]webLogon capture

![image-20231130112613849](./img/73-6.png)

第一个流中的`url`解码即可

![image-20231130112642835](./img/74-2.png)

## [DDCTF2018]流量分析

> 流量分析
> 200pt
>
> 提示一：若感觉在中间某个容易出错的步骤，若有需要检验是否正确时，可以比较MD5: 90c490781f9c320cd1ba671fcb112d1c
> 提示二：注意补齐私钥格式
> -----BEGIN RSA PRIVATE KEY-----
> XXXXXXX
> -----END RSA PRIVATE KEY-----

根据提示要找到RSA KEY。

```
tcp contains "KEY"
```

![image-20231130113354246](./img/74-3.png)

![image-20231130113637784](./img/75-1.png)

![image-20231130113730756](./img/75-2.png)

![image-20231130113924858](./img/75-3.png)

保存为`jpg`

![image-20231130114004252](./img/75-4.png)

`OCR`识别后修改错处

```
-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQDCm6vZmclJrVH1AAyGuCuSSZ8O+mIQiOUQCvN0HYbj8153JfSQ
LsJIhbRYS7+zZ1oXvPemWQDv/u/tzegt58q4ciNmcVnq1uKiygc6QOtvT7oiSTyO
vMX/q5iE2iClYUIHZEKX3BjjNDxrYvLQzPyGD1EY2DZIO6T45FNKYC2VDwIDAQAB
AoGAbtWUKUkx37lLfRq7B5sqjZVKdpBZe4tL0jg6cX5Djd3Uhk1inR9UXVNw4/y4
QGfzYqOn8+Cq7QSoBysHOeXSiPztW2cL09ktPgSlfTQyN6ELNGuiUOYnaTWYZpp/
QbRcZ/eHBulVQLlk5M6RVs9BLI9X08RAl7EcwumiRfWas6kCQQDvqC0dxl2wIjwN
czILcoWLig2c2u71Nev9DrWjWHU8eHDuzCJWvOUAHIrkexddWEK2VHd+F13GBCOQ
ZCM4prBjAkEAz+ENahsEjBE4+7H1HdIaw0+goe/45d6A2ewO/lYH6dDZTAzTW9z9
kzV8uz+Mmo5163/JtvwYQcKF39DJGGtqZQJBAKa18XR16fQ9TFL64EQwTQ+tYBzN
+04eTWQCmH3haeQ/0Cd9XyHBUveJ42Be8/jeDcIx7dGLxZKajHbEAfBFnAsCQGq1
AnbJ4Z6opJCGu+UP2c8SC8m0bhZJDelPRC8IKE28eB6SotgP61ZqaVmQ+HLJ1/wH
/5pfc3AmEyRdfyx6zwUCQCAH4SLJv/kprRz1a1gx8FR5tj4NeHEFFNEgq1gmiwmH
2STT5qZWzQFz8NRe+/otNOHBR2Xk4e8IS+ehIJ3TvyE=
-----END RSA PRIVATE KEY-----
```

![在这里插入图片描述](./img/75-5.png)

提供`SSL`私钥之后就可以查看`http`传输内容了

![image-20231130114449521](./img/75-6.png)

追踪`http`流即可

## [MRCTF2020]pyFlag

每张图结尾都附加了一部分的`zip`数据

![image-20231130115856095](./img/76-1.png)

按顺序拼接

没发现伪加密,试试`ARCHAR`爆破

![image-20231130120125765](./img/76-2.png)

`.hint.txt`

```
我用各种baseXX编码把flag套娃加密了，你应该也有看出来。
但我只用了一些常用的base编码哦，毕竟我的智力水平你也知道...像什么base36base58听都没听过
提示：0x10,0x20,0x30,0x55
```

`flag.txt`

```
G&eOhGcq(ZG(t2*H8M3dG&wXiGcq(ZG&wXyG(j~tG&eOdGcq+aG(t5oG(j~qG&eIeGcq+aG)6Q<G(j~rG&eOdH9<5qG&eLvG(j~sG&nRdH9<8rG%++qG%__eG&eIeGc+|cG(t5oG(j~sG&eOlH9<8rH8C_qH9<8oG&eOhGc+_bG&eLvH9<8sG&eLgGcz?cG&3|sH8M3cG&eOtG%_?aG(t5oG(j~tG&wXxGcq+aH8V6sH9<8rG&eOhH9<5qG(<E-H8M3eG&wXiGcq(ZG)6Q<G(j~tG&eOtG%+<aG&wagG%__cG&eIeGcq+aG&M9uH8V6cG&eOlH9<8rG(<HrG(j~qG&eLcH9<8sG&wUwGek2)
```

官方脚本

```python
#!/usr/bin/env python

import base64
import re

def baseDec(text,type):
    if type == 1:
        return base64.b16decode(text)
    elif type == 2:
        return base64.b32decode(text)
    elif type == 3:
        return base64.b64decode(text)
    elif type == 4:
        return base64.b85decode(text)
    else:
        pass

def detect(text):
    try:
        if re.match("^[0-9A-F=]+$",text.decode()) is not None:
            return 1
    except:
        pass
    
    try:
        if re.match("^[A-Z2-7=]+$",text.decode()) is not None:
            return 2
    except:
        pass

    try:
        if re.match("^[A-Za-z0-9+/=]+$",text.decode()) is not None:
            return 3
    except:
        pass
    
    return 4

def autoDec(text):
    while True:
        if b"MRCTF{" in text:
            print("\n"+text.decode())
            break

        code = detect(text)
        text = baseDec(text,code)

with open("flag.txt",'rb') as f:
    flag = f.read()

autoDec(flag)
```

[参考](https://blog.csdn.net/mochu7777777/article/details/109829704)

## [GKCTF 2021]excel 骚操作

打开之后，基本是一个空白的`excel`，一开始以为是用压缩软件解压缩，然后`flag`藏在那里面，后来发现没有

![image-20231130121024247](./img/77-1.png)

然后设置单元格格式为常规，可以显示出很多数字

![image-20231130121122813](./img/77-2.png)

将`1`替换为`黑色`

![image-20231130121356565](./img/77-3.png)

![image-20231130121421615](./img/77-4.png)

修改合适的行高，列宽，

![image-20231130121736581](./img/77-5.png)

## [UTCTF2020]File Carving

![image-20231130122525896](./img/78-1.png)

发现好像有其他文件,`binwalk`一下,`010editor`看一下`hidden_binary`,发现是`elf`文件,即`linux`可执行文件,运行看看

![image-20231130122658880](./img/78-12.png)

![image-20231130122714621](./img/78-3.png)

## [watevrCTF 2019]Evil Cuteness

`010editor`打开发现有隐藏文件

![image-20231130122922399](./img/79-1.png)

`binwalk`一下

在`abc`文件里得到`watevr{7h475_4c7u4lly_r34lly_cu73_7h0u6h}`

## 派大星的烦恼

> 派大星最近很苦恼，因为它的屁股上出现了一道疤痕！我们拍下了它屁股一张16位位图，0x22，0x44代表伤疤两种细胞，0xf0则是派大星的赘肉。还原伤疤，知道是谁打的派大星！(答案为32位的一串字符串) 注意：得到的 flag 请包上 flag{} 提交

![image-20231130211620145](./img/80-1.png)

![image-20231130211752525](./img/80-2.png)

![image-20231130212516174](./img/80-3.png)

![image-20231130212647313](./img/80-4.png)

思路歪了

其实是

```
"DD"DD""""D"DD""""""DD"""DD"DD""D""DDD""D"D"DD""""""DD""D""""DD"D"D"DD""""D"DD""D"""DD"""""DDD""""D"DD"""D"""DD"""D""DD"D"D"DD"""DD""DD"D"D""DD""DD"DD"""D"""DD""DD"DD""D"D""DD"D"D"DD"""D"""DD"""D"DD""DD"""DD"D"D""DD"""D"DD""DD""DD"""""DDD""DD""DD"""D""DD""
```

`D`表示`1`

`""`表示`0`

然后逆序转二进制即可

![image-20231130213008971](./img/80-5.png)

再将得到的字符串`逆序`提交

```
flag{6406950a54184bd5fe6b6e5b4ce43832}
```

## [QCTF2018]X-man-A face

![Xman-Aface-61df10385eaccbb3627ca3926c6ae174](./img/81-1.png)

得到一张这样的图

`GIMP`把右上角复制挪到左上角和左下角即可

![image-20231130223759679](./img/81-2.png)

`base32`解密即可

![image-20231130223833666](./img/81-3.png)

## [MRCTF2020]不眠之夜

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

## [INSHack2017]sanity

`markdown`格式打开直接给了`flag`

## 粽子的来历

题给了四个损坏的压缩包

![img](./img/83-1.png)

![image-20231130231604838](./img/83-2.png)

将`IComeFromAlibaba`都改为`ÿ`

修改后可正常打开

![image-20231130231812475](./img/83-3.png)

![image-20231130232013213](./img/83-4.png)

间距大的为1 较小的为0

![image-20231130232108448](./img/83-5.png)

## key不在这里

![image-20231130232525349](./img/84-1.png)

扫码后`url`解码发现`m`似乎是`ascii`数据

脚本跑一下

```python
from urllib.parse import quote, unquote
s = '10210897103375566531005253102975053545155505050521025256555254995410298561015151985150375568'
temp = ''
 
while len(s):
    if int(s[:3]) < 127:
        temp += chr(int(s[:3]))
        s = s[3:]
    else:
        temp += chr(int(s[:2]))
        s = s[2:]
print(temp)
print(unquote(temp))
```

## hashcat

What kind of document is this_

`010editor`查看后发现是个`office`文件

有文档加密

使用`office2john`

```bash
python3 .\office2john.py '.\What kind of document is this_.doc' > hash.txt
john --wordlist=top6000.txt res.txt
john --show res.txt
```

![image-20231130235408815](./img/85-1.png)

后缀改为`pptx`

在里面发现一个隐藏的文本框,设置字体为红色即可

![image-20231130235719667](./img/85-2.png)

## 蜘蛛侠呀

所有的`icmp`包后面都跟了一串数据，使用`tshark`把这些全部提取出来

```bash
tshark -r out.pcap -T fields -e data > data.txt
```

发现有重复,去重

```python
with open('data.txt', 'r') as file:
    res_list = []
    lines = file.readlines()
    print('[+]去重之前一共{0}行'.format(len(lines)))
    print('[+]开始去重，请稍等.....')
    for i in lines:
        if i not in res_list:
            res_list.append(i)
    print('[+]去重后一共{0}行'.format(len(res_list)))
    print(res_list)

with open('data1.txt', 'w') as new_file:
    for j in res_list:
        new_file.write(j)
```

![image-20231201001304080](./img/86-1.png)

`16进制`转字符串

```python
from Crypto.Util.number import long_to_bytes
import binascii


write_file = open('./data2.txt', 'w')

with open('./data1.txt', 'r') as f:
    lines = f.read().strip().split('\n')
    for _, v in enumerate(lines):
        # long_to_bytes(v)
        data = binascii.unhexlify(v).decode()
        write_file.write(data)
    write_file.close()
```

![image-20231201002009068](./img/86-2.png)

去掉首尾两行,再去掉`$$START$$`和`换行符`,`base64`解码

```python
import base64

with open('./data2.txt', 'rb') as f:
    with open('res.zip','wb') as new_file:
        new_file.write(base64.b64decode(f.read()))
```

![flag](./img/86-3.png)

`时间隐写`,使用`identify`

```bash
identify -format "%T" flag.gif
2050502050502050205020202050202020205050205020502050205050505050202050502020205020505050205020206666
```

`20`替换为`0`
`50`替换为`1`

```
011011010100010000110101010111110011000101110100
```

```
In [3]: int('011011010100010000110101010111110011000101110100', 2)
Out[3]: 120139720634740

In [4]: hex(120139720634740)
Out[4]: '0x6d44355f3174'

In [5]: import binascii

In [6]: binascii.unhexlify("6d44355f3174")
Out[6]: b'mD5_1t'
```

[参考](https://blog.csdn.net/mochu7777777/article/details/109645038)

## voip

`主菜单->电话->VoIP通话`

![image-20231201003336316](./img/87-1.png)

听力播报`flag`

`主菜单->电话->RTP->RTP流`

![image-20231201003647025](./img/87-2.png)

## [SCTF2019]电单车

发现一个音频文件

![image-20231204201144593](./img/88-1.png)

然后以短的为 0，长的为 1进行替换
`0 0111010010101010011000100`

`PT2242`信号：前面4bit表示同步码，中间的20bit表示地址码，后面的4bit表示功能码，最后一位是停止码。
也就是 `0。。。01110100101010100110。0010。0`

## [UTCTF2020]sstv

![在这里插入图片描述](./img/89-2.png)

```bash
sudo apt install qsstv
```

`Options->Configuration->Sound**`勾选`From file`

然后点击开始按钮

![image-20231204202531960](./img/89-4.png)

![image-20231204202439401](./img/89-3.png)

## [GUET-CTF2019]soul sipse

![image-20231204202803375](./img/90-1.png)

没有什么有效信息,`binwalk`试试

![image-20231204203042638](./img/90-2.png)

![image-20231204203117398](./img/90-3.png)

`steghide`无密码分解出`download.txt`

```
https://share.weiyun.com/5wVTIN3
```

下载得到`GUET.png`，修改为正确的`PNG`文件头

![在这里插入图片描述](./img/90-4.png)

保存得到正常的图片。如下

![在这里插入图片描述](./img/90-5.png)

`Unicode`解码

![在这里插入图片描述](./img/90-6.png)

```
 4070
+1234
------
 5304
```

```
flag{5304}
```

## [UTCTF2020]spectogram

![image-20231204203448994](./img/91-1.png)

下载个`Sonic Visualiser`分析一下：[Sonic Visualiser下载地址：https://www.sonicvisualiser.org/download.html](https://www.sonicvisualiser.org/download.html)

打开文件后，在`Layer`选项中点击`Add Peak Frequency Spectrogram`或者`Shift+K`，然后将右边选项调整成如下图所示：

![image-20231204204231804](./img/91-2.png)

## [安洵杯 2019]easy misc

`foremost分离+掩码+盲水印+词频统计`

题目给了三个文件

![image-20231204214246450](./img/92-1.png)

`read`文件夹

![image-20231204214315735](./img/92-2.png)

`hint.txt`

```
hint:取前16个字符
```

应该是词频统计，取出现频率最高的前十六个字符

可不知道看哪一个`txt`文件

再看压缩包，加密，但注释有提示

![image-20231204214747313](./img/92-3.png)

```
(math.sqrt(2524921)*85/5+2)/15-1794
```

![image-20231204215033791](./img/92-4.png)

前面的算式解出来是`7`

`七个数字+字符串掩码`

![image-20231204215222934](./img/92-5.png)

替换表

```
a = dIW
b = sSD
c = adE 
d = jVf
e = QW8
f = SA=
g = jBt
h = 5RE
i = tRQ
j = SPA
k = 8DS
l = XiE
m = S8S
n = MkF
o = T9p
p = PS5
q = E/S
r = -sd
s = SQW
t = obW
u = /WS
v = SD9
w = cw=
x = ASD
y = FTa
z = AE7
```

最后是那张`png`

`foremost`分离出两张一样的`png`，盲水印

![image-20231204215407801](./img/92-6.png)

![image-20231204215455032](./img/92-7.png)



![00000000.png_Bwm](./img/92-8.png)

`词频统计脚本`

```python
import re

file = open('D:/edge/read/11.txt')    
line = file.readlines()
file.seek(0,0)
file.close()

result = {}
for i in range(97,123):
    count = 0
    for j in line:
        find_line = re.findall(chr(i),j)
        count += len(find_line)
    result[chr(i)] = count
res = sorted(result.items(),key=lambda item:item[1],reverse=True)

num = 1
for x in res:
        print('频数第{0}: '.format(num),x)
        num += 1
```

```python
import re

file = open('./11.txt')    
line = file.readlines()
file.seek(0,0)
file.close()

result = {}
for i in range(97,123):
    count = 0
    for j in line:
        find_line = re.findall(chr(i),j)
        count += len(find_line)
    result[chr(i)] = count
res = sorted(result.items(),key=lambda item:item[1],reverse=True)

num = 1

result = ''

for i, x in enumerate(res):
        # print('频数第{0}: '.format(num),x)
        if i < 15:
            result += x[0]
        num += 1
        
# print(result)

tables = '''a = dIW
b = sSD
c = adE 
d = jVf
e = QW8
f = SA=
g = jBt
h = 5RE
i = tRQ
j = SPA
k = 8DS
l = XiE
m = S8S
n = MkF
o = T9p
p = PS5
q = E/S
r = -sd
s = SQW
t = obW
u = /WS
v = SD9
w = cw=
x = ASD
y = FTa
z = AE7'''

tb = {}

for data in tables.split('\n'):
    tb[data.strip().replace(' ', '').split('=')[0]] = data.strip().replace(' ', '').split('=')[1]

# print(tb)
for s in result:
    for k, v in tb.items():
        if k == s:
            print(v, end='')
        
```

```
QW8obWdIWT9pMkF-sd5REtRQSQWjVfXiE/WSFTajBtcw
```

`base64`解密后`base85`解密

```
flag{have_a_good_day1}
```

我解密就异常了,挺奇怪

## Business Planning Group

`010 Editor`打开图片，搜索`IEND`，发现结尾之后附加了东西

![image-20231204221603559](./img/93-1.png)

`BPG`开头的，网上找一下相关文件格式

![在这里插入图片描述](./img/93-2.png)

竟然图像文件，将这些数据另存出来为`bpg`文件，发现`Windows`的图像软件不能直接打开，网上能打开的工具

![image-20231204222208517](./img/93-3.png)

拖动过去让`bpgview.exe`打开即可,或者使用`honeyview`

![image-20231204222427371](./img/93-4.png)

![image-20231204222650925](./img/93-5.png)

## 大流量分析（一）

> 某黑客对A公司发动了攻击，以下是一段时间内我们获取到的流量包，那黑客的攻击ip是多少？（答案加上flag{}）附件链接: https://pan.baidu.com/s/1EgLI37y6m9btzwIWZYDL9g 提取码: 9jva 注意：得到的 flag 请包上 flag{} 提交

![img](./img/94-1.png)

## [湖南省赛2019]Findme



![image-20231204223248052](./img/95-1.png)

### 1.png

### 第一张图片打开显示为`CRC`错误

![image-20231204223319352](./img/95-2.png)

跑脚本改一下

```python
import struct
import binascii
import os

m = open("1.png", "rb").read()
k = 0
for i in range(5000):
    if k == 1:
        break
    for j in range(5000):
        c = m[12:16] + struct.pack('>i', i) + struct.pack('>i', j) + m[24:29]
        crc = binascii.crc32(c) & 0xffffffff
        if crc == 0x000C4ED3:
            k = 1
            print(hex(i), hex(j))
            break
```

![image-20231204223747262](./img/95-3.png)

![image-20231204223759265](./img/95-4.png)

 继续往下看 发现了端倪

发现了`chunk2`和`chunk3`都缺少了`IDAT`块

返回直接修改

```
IDAT块的数值是：49 44 41 54
```

![image-20231204224004353](./img/95-5.png)

保存图片后再次打开图片就已经正常了

![1](./img/95-6.png)

然后再用`Stegsolve`打开 在`Blue plane 2`发现了一张二维码

![image-20231204224116074](C:\Users\cc\Desktop\95-7.png)

在`blue plane2`发现一个二维码

![image-20231204224304647](./img/95-8.png)

### 2.png

![image-20231204224426668](./img/95-9.png)

在`chunk7`后面发现一个`7z`文件头

`binwalk`一下,发现文件不对,`foremost`同样,应该是文件被修改了,复制保存到新文件里看看

再仔细查看发现这是压缩包的头被更改了

那就把`30 7A`->`50 4B`

![image-20231204225043750](./img/95-10.png)

然后保存 压缩包就能正常打开了

![image-20231204225126554](./img/95-11.png)

`1000`个文件

含有明文的一定是最大或者最小的

那就按照大小排个序

![image-20231204225223162](./img/95-12.png)

### 3.png

接下来分析第三张图片

发现了图片的`CRC`有些不同

看了别人的wp得知：chunk[0]-chunk[6]的每一个数据块的crc值都是可打印的Ascii字符

然后用[在线网址](https://coding.tools/cn/hex-to-ascii)转换一下

得到第三段明文：`3RlZ30=`

### 4.png

在chunk[4]发现明文

![img](./img/95-13.png)

第四段明文：`cExlX1BsY`

### 5.png

在结尾发现提示

![img](./img/95-14.png)

1：`ZmxhZ3s0X3`

2：`1RVcmVfc`

3：`3RlZ30=`

4：`cExlX1BsY`

5：`Yzcllfc0lN`

```python3
import base64
import itertools

l = ['ZmxhZ3s0X3', '1RVcmVfc', '3RlZ30=', 'cExlX1BsY', 'Yzcllfc0lN']
l2 = list(itertools.permutations(l, 5))
for data in l2:
    tmp = ''.join(data)
    try:
        print(base64.b64decode(tmp))
    except:
        continue
```

![image-20231204230329379](./img/95-15.png)

## [GKCTF 2021]你知道apng吗

![](./img/96-1.png)

https://products.aspose.app/imaging/zh-hans/image-view/apng

## [ACTF新生赛2020]剑龙

![image-20231204232859304](./img/97-2.png)

密码为`welcom3!;`

![image-20231204232915447](./img/97-3.png)



![image-20231204232736996](./img/97-1.png)

想要flag吗？解出我的密文吧~
`U2FsdGVkX1/7KeHVl5984OsGUVSanPfPednHpK9lKvp0kdrxO4Tj/Q==`

![image-20231204233038489](./img/97-4.png)

`Salted`开头,试试`AES`和`DES`

![image-20231204233231687](./img/97-5.png)

`python3 stegosaurus.py -x O_O.pyc`

记得改一下后缀名

![image-20231204233813689](./img/97-6.png)

## [HDCTF2019]你能发现什么蛛丝马迹吗

`Volatility`分析

查看文件的`Profile`

![image-20231205182619027](./img/98-1.png)

`profile`选`Win2003SP0x86`好像不对

![image-20231205182946606](./img/98-2.png)

应该是`Win2003SP1x86`

![image-20231205183028537](./img/98-3.png)

看一下`cmd`进程

![image-20231205183135612](./img/98-4.png)

`DumpIt.exe`

发现`Flag`字样，将`DumpIt.exe`这个程序dump下来

```bash
volatility_2.6_lin64_standalone -f memory.img --profile=Win2003SP1x86 memdump -p 1992
--dump-dir=./
```

![image-20231205183521498](./img/98-5.png)

`foremost`分离`1992.dmp`

![image-20231205183608796](./img/98-6.png)

![image-20231205183715546](./img/98-7.png)

![image-20231205183656758](./img/98-8.png)

## greatescape

找到`FTP`传的`ssc.key`

![image-20231205205624216](./img/99-1.png)

通过分析流量猜测，这应该在向`ftp`服务器传送私钥，我们得到了私钥，就可以解密`TLS`报文

`Edit->Preference->Protocols->TLS`，点击`Edit`，然后点击`+`添加`Key File`

![image-20231205205838804](./img/99-2.png)

## [INSHack2019]INSAnity

`typora`打开即可

![image-20231205205948771](./img/100-1.png)

## [INSHack2019]Sanity

同上,`typora`打开即可

## 很好的色彩呃？

![pass](./img/101-1.png)

![image-20231205210520149](./img/101-2.png)

`6`个颜色`HTML标记值为`

```
8b8b61
8b8b61
8b8b70
8b8b6a
8b8b65
8b8b73
```

`6161706a6573`,`十六进制转字符串`

![image-20231205210700135](./img/101-3.png)

## [INSHack2018]Self Congratulation

![image-20231205210836998](./img/102-1.png)

图片左上角存在类似二维码的图片

黑白相间块的话就按照二维的方式来转化为二进制，`白为0`，`黑为1`

```
00110001001
10010001100
11001101000
01101010011
01100011011
10011100000
```

https://www.qqxiuzi.cn/bianma/erjinzhi.php

![image-20231205210956886](./img/102-2.png)

## [ACTF新生赛2020]frequency

根据题目名称frequency与文件内容猜测应该是字频方向

如果打开文档是空白的，就搜索

![image-20231205211319733](./img/103-1.png)

![image-20231205211409712](./img/103-2.png)

再结合文档内容，合并在一起去解码（如果直接统计字频没有什么思路，刚刚试过了）

```python
import string


with open('./flag.txt', 'r') as f:
    printables = string.printable
    file_contents = f.read().strip()
    res = {}
    for _, v in enumerate(printables):
        res[v] = file_contents.count(v)

    sort_res = sorted(res.items(), key=lambda x: x[1], reverse=True)
    # print(sort_res)
    
    for _, v in enumerate(sort_res):
        print(v[0], end='')
```

![image-20231205211931927](C:\Users\cc\AppData\Roaming\Typora\typora-user-images\image-20231205211931927.png)

## [BSidesSF2019]table-tennis

### 方法一

`python解析数据包`

```python
from scapy.all import *
from scapy.layers.inet import ICMP

packets = rdpcap('./attachment.pcapng')
for pack in packets:    # 遍历每一个数据包
    if pack.haslayer(ICMP):
        if pack[ICMP].type == 0:  # 每一个ICMP的type值为0的包(响应包)
            print(pack[ICMP].load[-8:].decode(), end='')
            # 每个数据包的最后8位是有效数据
```

![image-20231206092346246](./img/104-1.png)

把其中的`base64`字符串取出来，然后解码一下就得到了flag。

### 方法二

提取的都是`16`进制，然后写个脚本处理一下

```bash
tshark -r attachment.pcapng -T fields -e data |sed '/^ *$/d' > data.txt
```

```python
file = open("data.txt","r")
str = ""
k = 1
for i in file.readlines():
    if (k%2==1):
        str += i[16:32]#有效数据段
    k += 1
str = str.replace("\n","")
# print(str)
for i in range(0,len(str),2):
    print(chr(int(str[i:i+2],16)),end="")
```

## [2022红包题]虎年大吉

在文件尾有

```
6<.#Q<(?#$XllOOjeSg9Y.!JYYiWF&jhIkW\W@qGCggt'1-%'K2E<cTI/
```

放到`cipherchey`里发现

![image-20231206094809212](./img/105-1.png)

## [MRCTF2020]小O的考研复试

![在这里插入图片描述](./img/106-1.png)

```python
a=2
for i in range(19260816):
    a = a * 10 + 2
    a%=(1e9+7)

print(a)
```

`577302567`

## 真的很杂

`binwalk`分离出来一个项目目录

![image-20231206100618699](./img/107-1.png)

```
./d2j-dex2jar.bat classes.dex
```

![image-20231206100744513](./img/107-2.png)

![image-20231206100814919](./img/107-3.png)

![image-20231206100927997](./img/107-4.png)

爆破`字母`和`数字`

`flag{25f991b27fcdc2f7a82a2b34386e81c4}`

## [INSHack2019]gflag

![在这里插入图片描述](./img/108-1.png)

https://ncviewer.com/

![image-20231206102529545](./img/108-2.png)

## [GKCTF 2021]FireFox Forensics

> 取证大佬说这是一份登录凭证文件

题目提示是`火狐(firefox)`的登陆凭证，使用[Firepwd工具](https://github.com/lclevy/firepwd)破解。将`key4.db`、`logins.json`复制到`firepwd`目录下，用`firepwd.py`破解。

```bash
python3 .\firepwd.py .\logins.json
```

![image-20231206103401615](./img/108-3.png)

## [RCTF2019]disk

`vmdk`文件

`010editor`搜索关键字

![image-20231206104007681](./img/108-4.png)

接着使用`7zip`打开，得到`FAT`文件

![image-20231206104214149](./img/109-2.png)

`FAT`文件就可以使用`VeraCrypt`进行[挂载](https://so.csdn.net/so/search?q=挂载&spm=1001.2101.3001.7020)

![image-20231206104804345](./img/109-3.png)

进入挂载的`A`盘

![image-20231206104844233](./img/109-4.png)

![image-20231206104904636](./img/109-5.png)

图片名提示：`useless file for ctf just ignore it`，图片无用，在`password.txt`有个`Password 2`，这里就有个盲区知识点，在挂载输入密码的时候，不同的密码可以进入不同的文件系统

重新挂宅，输入密码为：`RCTF2019`

![image-20231206105017740](./img/109-6.png)

无法直接打开

![image-20231206105106414](./img/109-7.png)

`010editor`->`file`->`Open Drive`,我环境好像有点问题

使用`winhex`,`tools`->`Open Drive`,有报错,点`ok`,即可打开

![image-20231206105701574](./img/109-8.png)

![image-20231206105825471](./img/109-9.png)

找到第二段`flag`

## [INSHack2018]INSanity

正常`typora`打开即可获取`flag`

## [GWCTF2019]huyao

猜测`盲水印`

一直试即可出`flag`

![image-20231206110202771](./img/110-1.png)

![huyao.png_FBwm](./img/110-2.png)

## 寂静之城

> 出题人非常喜欢开小说，据说最近出题人对这篇小说非常入迷：https://www.douban.com/group/topic/5221588/。你能通过这点线索发现什么？hacking to the gate! 注意：得到的 flag 请包上 flag{} 提交

脑洞大开的社工

![image-20231206111747722](./img/111-1.png)

`出题人`账号异常了,看看以前的`wp`,跳过这题

https://www.onctf.com/posts/83401e0a.html#%E5%85%AB%E5%8D%81%E4%BA%94%E3%80%81%E5%AF%82%E9%9D%99%E4%B9%8B%E5%9F%8E

## [MRCTF2020]摇滚DJ（建议大声播放

`wav`文件,`qsstv`解析即可

![image-20231206112254946](./img/112-1.png)

`flag{r3ce1ved_4n_img}`

## [GUET-CTF2019]520的暗示

`xor异或`

打开是一个`photo.dat`文件,发现文件头没啥东西,但是`33`特别多,试试异或一下`0x33`

![image-20231206113057953](./img/113-1.png)

文件与`0x33`异或，得到一张图片

![image-20231206113530342](./img/113-2.png)

发现是个`jpg`格式的文件

```python
data = open('photo.dat', 'rb')
strs = data.read()
flag = open("1.jpg",'ab+')
for i in strs:
    flag.write(bytes([i ^ 0x33]))
```

![1](./img/113-3.png)

后面其实是根据LTE定位基站地址，最后定位到`桂林电子科技大学花江校区`，也就是flag为`flag{桂林电子科技大学花江校区}`。

## [XMAN2018排位赛]file

`lost+found`恢复

给了一个文件`attachment.img`,使用`7z`解压

![image-20231206114512413](./img/114-1.png)

最后一个文件显示`lost+found`,用`extundelete`恢复

```
extundelete attachment.img --restore-all
```

![image-20231206114601603](./img/114-2.png)

![image-20231206114620375](./img/115-2.png)

## 我爱Linux

在文件尾发现冗余的数据

![image-20231206115151752](./img/115-3.png)

使用`trid`工具分析下

![image-20231206120111724](./img/115-4.png)

是Python `Pickle`序列号数据

脚本转换

```python
import pickle

fp = open("data.txt", "rb+")
fw = open('result.txt', 'w')
a = pickle.load(fp)
pickle = str(a)
fw.write(pickle)
fw.close()
fp.close()
```

脚本

```python
flag = [
    [(3, 'm'), (4, '"'), (5, '"'), (8, '"'), (9, '"'), (10, '#'), (31, 'm'), (32, '"'), (33, '"'), (44, 'm'), (45, 'm'),
     (46, 'm'), (47, 'm'), (50, 'm'), (51, 'm'), (52, 'm'), (53, 'm'), (54, 'm'), (55, 'm'), (58, 'm'), (59, 'm'),
     (60, 'm'), (61, 'm'), (66, 'm'), (67, '"'), (68, '"'), (75, '#')],
    [(1, 'm'), (2, 'm'), (3, '#'), (4, 'm'), (5, 'm'), (10, '#'), (16, 'm'), (17, 'm'), (18, 'm'), (23, 'm'), (24, 'm'),
     (25, 'm'), (26, 'm'), (31, '#'), (37, 'm'), (38, 'm'), (39, 'm'), (43, '"'), (47, '"'), (48, '#'), (54, '#'),
     (55, '"'), (57, '"'), (61, '"'), (62, '#'), (64, 'm'), (65, 'm'), (66, '#'), (67, 'm'), (68, 'm'), (72, 'm'),
     (73, 'm'), (74, 'm'), (75, '#')],
    [(3, '#'), (10, '#'), (15, '"'), (19, '#'), (22, '#'), (23, '"'), (25, '"'), (26, '#'), (29, 'm'), (30, 'm'),
     (31, '"'), (36, '"'), (40, '#'), (47, 'm'), (48, '"'), (53, 'm'), (54, '"'), (59, 'm'), (60, 'm'), (61, 'm'),
     (62, '"'), (66, '#'), (71, '#'), (72, '"'), (74, '"'), (75, '#')],
    [(3, '#'), (10, '#'), (15, 'm'), (16, '"'), (17, '"'), (18, '"'), (19, '#'), (22, '#'), (26, '#'), (31, '#'),
     (36, 'm'), (37, '"'), (38, '"'), (39, '"'), (40, '#'), (45, 'm'), (46, '"'), (52, 'm'), (53, '"'), (61, '"'),
     (62, '#'), (66, '#'), (71, '#'), (75, '#')],
    [(3, '#'), (10, '"'), (11, 'm'), (12, 'm'), (15, '"'), (16, 'm'), (17, 'm'), (18, '"'), (19, '#'), (22, '"'),
     (23, '#'), (24, 'm'), (25, '"'), (26, '#'), (31, '#'), (36, '"'), (37, 'm'), (38, 'm'), (39, '"'), (40, '#'),
     (43, 'm'), (44, '#'), (45, 'm'), (46, 'm'), (47, 'm'), (48, 'm'), (51, 'm'), (52, '"'), (57, '"'), (58, 'm'),
     (59, 'm'), (60, 'm'), (61, '#'), (62, '"'), (66, '#'), (71, '"'), (72, '#'), (73, 'm'), (74, '#'), (75, '#')],
    [(23, 'm'), (26, '#'), (32, '"'), (33, '"')], [(24, '"'), (25, '"')], [],
    [(12, '#'), (17, 'm'), (18, '"'), (19, '"'), (23, 'm'), (24, 'm'), (25, 'm'), (26, 'm'), (33, '#'), (36, 'm'),
     (37, 'm'), (38, 'm'), (39, 'm'), (40, 'm'), (41, 'm'), (46, 'm'), (47, 'm'), (52, 'm'), (53, 'm'), (54, 'm'),
     (65, 'm'), (66, 'm'), (67, 'm'), (68, 'm'), (71, 'm'), (72, 'm'), (73, 'm'), (74, 'm'), (75, 'm'), (76, 'm')],
    [(2, 'm'), (3, 'm'), (4, 'm'), (9, 'm'), (10, 'm'), (11, 'm'), (12, '#'), (15, 'm'), (16, 'm'), (17, '#'),
     (18, 'm'), (19, 'm'), (22, '"'), (26, '"'), (27, '#'), (30, 'm'), (31, 'm'), (32, 'm'), (33, '#'), (40, '#'),
     (41, '"'), (45, 'm'), (46, '"'), (47, '#'), (50, 'm'), (51, '"'), (55, '"'), (58, 'm'), (59, 'm'), (60, 'm'),
     (64, '#'), (65, '"'), (68, '"'), (69, 'm'), (75, '#'), (76, '"')],
    [(1, '#'), (2, '"'), (5, '#'), (8, '#'), (9, '"'), (11, '"'), (12, '#'), (17, '#'), (24, 'm'), (25, 'm'), (26, 'm'),
     (27, '"'), (29, '#'), (30, '"'), (32, '"'), (33, '#'), (39, 'm'), (40, '"'), (44, '#'), (45, '"'), (47, '#'),
     (50, '#'), (51, 'm'), (52, '"'), (53, '"'), (54, '#'), (55, 'm'), (57, '#'), (58, '"'), (61, '#'), (64, '#'),
     (65, 'm'), (68, 'm'), (69, '#'), (74, 'm'), (75, '"')],
    [(1, '#'), (2, '"'), (3, '"'), (4, '"'), (5, '"'), (8, '#'), (12, '#'), (17, '#'), (26, '"'), (27, '#'), (29, '#'),
     (33, '#'), (38, 'm'), (39, '"'), (43, '#'), (44, 'm'), (45, 'm'), (46, 'm'), (47, '#'), (48, 'm'), (50, '#'),
     (55, '#'), (57, '#'), (58, '"'), (59, '"'), (60, '"'), (61, '"'), (65, '"'), (66, '"'), (67, '"'), (69, '#'),
     (73, 'm'), (74, '"')],
    [(1, '"'), (2, '#'), (3, 'm'), (4, 'm'), (5, '"'), (8, '"'), (9, '#'), (10, 'm'), (11, '#'), (12, '#'), (17, '#'),
     (22, '"'), (23, 'm'), (24, 'm'), (25, 'm'), (26, '#'), (27, '"'), (29, '"'), (30, '#'), (31, 'm'), (32, '#'),
     (33, '#'), (37, 'm'), (38, '"'), (47, '#'), (51, '#'), (52, 'm'), (53, 'm'), (54, '#'), (55, '"'), (57, '"'),
     (58, '#'), (59, 'm'), (60, 'm'), (61, '"'), (64, '"'), (65, 'm'), (66, 'm'), (67, 'm'), (68, '"'), (72, 'm'),
     (73, '"')], [], [], [],
    [(5, '#'), (8, '#'), (16, 'm'), (17, 'm'), (18, 'm'), (19, 'm'), (23, 'm'), (24, 'm'), (25, 'm'), (26, 'm'),
     (30, 'm'), (31, 'm'), (32, 'm'), (33, 'm'), (38, 'm'), (39, 'm'), (40, 'm'), (50, '#'), (57, '#'), (64, '#'),
     (71, 'm'), (72, 'm'), (73, 'm')],
    [(2, 'm'), (3, 'm'), (4, 'm'), (5, '#'), (8, '#'), (9, 'm'), (10, 'm'), (11, 'm'), (15, '#'), (16, '"'), (19, '"'),
     (20, 'm'), (22, 'm'), (23, '"'), (26, '"'), (27, 'm'), (29, '#'), (34, '#'), (36, 'm'), (37, '"'), (41, '"'),
     (44, 'm'), (45, 'm'), (46, 'm'), (50, '#'), (51, 'm'), (52, 'm'), (53, 'm'), (57, '#'), (58, 'm'), (59, 'm'),
     (60, 'm'), (64, '#'), (65, 'm'), (66, 'm'), (67, 'm'), (73, '#')],
    [(1, '#'), (2, '"'), (4, '"'), (5, '#'), (8, '#'), (9, '"'), (11, '"'), (12, '#'), (15, '#'), (16, 'm'), (19, 'm'),
     (20, '#'), (22, '#'), (25, 'm'), (27, '#'), (29, '"'), (30, 'm'), (31, 'm'), (32, 'm'), (33, 'm'), (34, '"'),
     (36, '#'), (37, 'm'), (38, '"'), (39, '"'), (40, '#'), (41, 'm'), (43, '#'), (44, '"'), (47, '#'), (50, '#'),
     (51, '"'), (53, '"'), (54, '#'), (57, '#'), (58, '"'), (60, '"'), (61, '#'), (64, '#'), (65, '"'), (67, '"'),
     (68, '#'), (73, '#')],
    [(1, '#'), (5, '#'), (8, '#'), (12, '#'), (16, '"'), (17, '"'), (18, '"'), (20, '#'), (22, '#'), (27, '#'),
     (29, '#'), (33, '"'), (34, '#'), (36, '#'), (41, '#'), (43, '#'), (44, '"'), (45, '"'), (46, '"'), (47, '"'),
     (50, '#'), (54, '#'), (57, '#'), (61, '#'), (64, '#'), (68, '#'), (73, '#')],
    [(1, '"'), (2, '#'), (3, 'm'), (4, '#'), (5, '#'), (8, '#'), (9, '#'), (10, 'm'), (11, '#'), (12, '"'), (15, '"'),
     (16, 'm'), (17, 'm'), (18, 'm'), (19, '"'), (23, '#'), (24, 'm'), (25, 'm'), (26, '#'), (29, '"'), (30, '#'),
     (31, 'm'), (32, 'm'), (33, 'm'), (34, '"'), (37, '#'), (38, 'm'), (39, 'm'), (40, '#'), (41, '"'), (43, '"'),
     (44, '#'), (45, 'm'), (46, 'm'), (47, '"'), (50, '#'), (51, '#'), (52, 'm'), (53, '#'), (54, '"'), (57, '#'),
     (58, '#'), (59, 'm'), (60, '#'), (61, '"'), (64, '#'), (65, '#'), (66, 'm'), (67, '#'), (68, '"'), (71, 'm'),
     (72, 'm'), (73, '#'), (74, 'm'), (75, 'm')], [], [], [],
    [(2, 'm'), (3, 'm'), (4, 'm'), (5, 'm'), (8, 'm'), (9, 'm'), (10, 'm'), (11, 'm'), (12, 'm'), (19, '#'), (24, 'm'),
     (25, 'm'), (26, 'm'), (29, '"'), (30, '"'), (31, 'm')],
    [(1, '#'), (2, '"'), (5, '"'), (6, 'm'), (8, '#'), (16, 'm'), (17, 'm'), (18, 'm'), (19, '#'), (22, 'm'), (23, '"'),
     (27, '"'), (31, '#')],
    [(1, '#'), (2, 'm'), (5, 'm'), (6, '#'), (8, '"'), (9, '"'), (10, '"'), (11, '"'), (12, 'm'), (13, 'm'), (15, '#'),
     (16, '"'), (18, '"'), (19, '#'), (22, '#'), (23, 'm'), (24, '"'), (25, '"'), (26, '#'), (27, 'm'), (31, '"'),
     (32, 'm'), (33, 'm')],
    [(2, '"'), (3, '"'), (4, '"'), (6, '#'), (13, '#'), (15, '#'), (19, '#'), (22, '#'), (27, '#'), (31, '#')],
    [(1, '"'), (2, 'm'), (3, 'm'), (4, 'm'), (5, '"'), (8, '"'), (9, 'm'), (10, 'm'), (11, 'm'), (12, '#'), (13, '"'),
     (15, '"'), (16, '#'), (17, 'm'), (18, '#'), (19, '#'), (23, '#'), (24, 'm'), (25, 'm'), (26, '#'), (27, '"'),
     (31, '#')], [(29, '"'), (30, '"')]]
temp = [' '] * 76
for line, data in enumerate(flag):
    if not data:
        print()
    else:
        for t in data:
            try:
                temp[t[0]] = t[1]
            except Exception:
                pass

    print(''.join(temp))

    temp = [' '] * 76
```

![在这里插入图片描述](./img/115-5.png)

## [DDCTF2018]第四扩展FS

得到一张`jpg`

![FS](./img/116-1.png)

详细信息里面有内容

![image-20231206140524620](./img/116-2.png)

`foremost`分离一下

![image-20231206140606147](./img/116-3.png)

根据详细信息中的备注作为密码,解压出一个文件

![image-20231206140737503](./img/116-4.png)

频次统计

```python
from collections import Counter

with open('./file.txt', 'r') as f:
    cont = f.read()
    res = Counter(cont)
    print(''.join(res.keys()))
```

![image-20231206141406795](./img/116-5.png)

组合一下即可

## [SCTF2019]Ready_Player_One

说是我在的电脑是虚拟机无法运行,干,看wp说是直接运行,一直按`w`就可以了

![在这里插入图片描述](./img/117-1.png)

## Beautiful_Side

`010editor`发现有隐藏的`png`图片,`binwalk`分不出来,使用`foremost`

发现半张二维码

![00000087](./img/118-1.png)

手撸补全即可

## [INSHack2018]42.tar.xz

解压递归的`.tar.xz`压缩包

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

## [BSidesSF2019]diskimage

给了我们一个`png`文件,用`zsteg`发现了一个文件

![image-20231206144248319](./img/119-1.png)

*用下面的命令导出镜像信息：*

```bash
zsteg -e 'b8,rgb,lsb,xy' attachment.png > disk.dat
```

用`testdisk`分析下导出的镜像，按图示操作即可

![image-20231206144617908](./img/119-2.png)

![image-20231206144646000](./img/119-3.png)

![image-20231206144712712](./img/119-4.png)

![image-20231206144757281](./img/119-5.png)

![image-20231206144832533](./img/119-6.png)

![image-20231206144851207](./img/119-7.png)

![image-20231206144942632](./img/119-8.png)

看到字节数较大的`_LAG.ICO`,按`c`然后再按`c`复制出来，得到`flag`。

![image-20231206145131789](./img/119-9.png)

## [INSHack2017]hiding-in-plain-sight

`foremost`分离即可获得`flag`

![00000000](./img/120-1.png)

## [INSHack2017]remote-multimedia-controller

搜索`flag`,然后查看字节流

![image-20231206150356220](./img/121-1.png)

![image-20231206150440517](./img/121-2.png)

似乎是`base64`

放到`cyberchef`解密

![image-20231206150509316](./img/121-3.png)

## [XMAN2018排位赛]AutoKey

`autokey`

https://github.com/WangYihang/UsbKeyboardDataHacker

![image-20231206152104983](./img/122-1.png)

去掉`CAP、DEL`，处理`AutoKey`密文时，在删除`DEL`的时候要把`DEL`前面的字符也删掉,得到`autokey`密文

```
mplrvffczeyoujfjkybxgzvdgqaurkxzolkolvtufblrnjesqitwahxnsijxpnmplshcjbtyhzealogviaaissplfhlfswfehjncrwhtinsmambvexpziz
```

https://www.cnblogs.com/LEOGG321/p/13735458.html

工具下架了

没办法继续做了

![img](./img/122-2.png)

```
HELLOBOYSANDGIRLSYOUARESOSMARTTHATYOUCANFINDTHEFLAGTHATIHIDEINTHEKEYBOARDPACKAGEFLAGISJHAWLZKEWXHNCDHSLWBAQJTUQZDXZQPF
```

`flag{JHAWLZKEWXHNCDHSLWBAQJTUQZDXZQPF}`

## [WMCTF2020]行为艺术

高度有点问题,修改高度

![image-20231206154858464](./img/123-1.png)

![image-20231206154934279](./img/123-2.png)

`50 4B 03 04`是压缩包

将其填入`hex`

![image-20231206155147233](./img/123-3.png)

有伪加密

![image-20231206155227334](./img/123-4.png)

`brainfuck`解密

![image-20231206155309189](./img/123-5.png)

## [QCTF2018]X-man-Keyword

![attachment](./img/124-1.png)

下载附件后，是一张图片，放到`010editor`以及`kali`后无果，然后将其放入`Stegsolve`，发现其`lsb`的头部有点东西，应该是`lsb`隐写，随后用`cloacked-pixel-master -> lsb`脚本解密可以得到`PVSF{vVckHejqBOVX9C1c13GFfkHJrjIQeMwf}`

![image-20231206155910667](./img/124-2.png)

*根据“hint1:把给出的keyword放到前面试试”的提示，从26个英文字母里把 “lovekfc”提出来放到前面做密钥。*

```
lovekfcabdghijmnpqrstuwxyz
```

*然后根据密钥替换密文中的字母解密（应该是Nihilist加密），这步用脚本来实现：*

```python
# -*- coding:utf-8 -*-
import string

ciphertext = 'PVSF{vVckHejqBOVX9C1c13GFfkHJrjIQeMwf}'
secretkey = 'lovekfcabdghijmnpqrstuwxyz'
plaintext = ''

for letter in ciphertext:
    if letter in string.ascii_lowercase:
        index = secretkey.lower().index(letter)
        plaintext += string.ascii_lowercase[index]
        continue
    if letter in string.ascii_uppercase:
        index = secretkey.upper().index(letter)
        plaintext += string.ascii_uppercase[index]
        continue
    plaintext += letter

print(plaintext)
```

![image-20231206160055025](./img/124-3.png)

## [INSHack2018]not so deep

![image-20231206161006741](./img/125-1.png)

`audacity`打开得到一半`flag`

`DeepSound2`

爆破密码脚本,`python3`

```python
#!/usr/bin/env python3
'''
deepsound2john extracts password hashes from audio files containing encrypted
data steganographically embedded by DeepSound (http://jpinsoft.net/deepsound/).

This method is known to work with files created by DeepSound 2.0.

Input files should be in .wav format. Hashes can be recovered from audio files
even after conversion from other formats, e.g.,

    ffmpeg -i input output.wav

Usage:

    python3 deepsound2john.py carrier.wav > hashes.txt
    john hashes.txt

This software is copyright (c) 2018 Ryan Govostes <rgovostes@gmail.com>, and
it is hereby released to the general public under the following terms:
Redistribution and use in source and binary forms, with or without
modification, are permitted.
'''

import logging
import os
import sys
import textwrap


def decode_data_low(buf):
  return buf[::2]

def decode_data_normal(buf):
  out = bytearray()
  for i in range(0, len(buf), 4):
    out.append((buf[i] & 15) << 4 | (buf[i + 2] & 15))
  return out

def decode_data_high(buf):
  out = bytearray()
  for i in range(0, len(buf), 8):
    out.append((buf[i] & 3) << 6     | (buf[i + 2] & 3) << 4 \
             | (buf[i + 4] & 3) << 2 | (buf[i + 6] & 3))
  return out


def is_magic(buf):
  # This is a more efficient way of testing for the `DSCF` magic header without
  # decoding the whole buffer
  return (buf[0] & 15)  == (68 >> 4) and (buf[2]  & 15) == (68 & 15) \
     and (buf[4] & 15)  == (83 >> 4) and (buf[6]  & 15) == (83 & 15) \
     and (buf[8] & 15)  == (67 >> 4) and (buf[10] & 15) == (67 & 15) \
     and (buf[12] & 15) == (70 >> 4) and (buf[14] & 15) == (70 & 15)


def is_wave(buf):
  return buf[0:4] == b'RIFF' and buf[8:12] == b'WAVE'


def process_deepsound_file(f):
  bname = os.path.basename(f.name)
  logger = logging.getLogger(bname)

  # Check if it's a .wav file
  buf = f.read(12)
  if not is_wave(buf):
    global convert_warn
    logger.error('file not in .wav format')
    convert_warn = True
    return
  f.seek(0, os.SEEK_SET)

  # Scan for the marker...
  hdrsz = 104
  hdr = None

  while True:
    off = f.tell()
    buf = f.read(hdrsz)
    if len(buf) < hdrsz: break

    if is_magic(buf):
          hdr = decode_data_normal(buf)
          logger.info('found DeepSound header at offset %i', off)
          break

    f.seek(-hdrsz + 1, os.SEEK_CUR)

  if hdr is None:
    logger.warn('does not appear to be a DeepSound file')
    return

  # Check some header fields
  mode = hdr[4]
  encrypted = hdr[5]

  modes = {2: 'low', 4: 'normal', 8: 'high'}
  if mode in modes:
    logger.info('data is encoded in %s-quality mode', modes[mode])
  else:
    logger.error('unexpected data encoding mode %i', modes[mode])
    return

  if encrypted == 0:
    logger.warn('file is not encrypted')
    return
  elif encrypted != 1:
    logger.error('unexpected encryption flag %i', encrypted)
    return

  sha1 = hdr[6:6+20]
  print('%s:$dynamic_1529$%s' % (bname, sha1.hex()))


if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser()
  parser.add_argument('--verbose', '-v', action='store_true')
  parser.add_argument('files', nargs='+', metavar='file',
    type=argparse.FileType('rb', bufsize=4096))
  args = parser.parse_args()

  if args.verbose:
    logging.basicConfig(level=logging.INFO)
  else:
    logging.basicConfig(level=logging.WARN)

  convert_warn = False

  for f in args.files:
    process_deepsound_file(f)

  if convert_warn:
    print(textwrap.dedent('''
    ---------------------------------------------------------------
    Some files were not in .wav format. Try converting them to .wav
    and try again. You can use: ffmpeg -i input output.wav
    ---------------------------------------------------------------
    '''.rstrip()), file=sys.stderr)
```

![image-20231206161820008](./img/125-2.png)

打开`DeepSound`输入密码

![image-20231206161916840](./img/125-3.png)

![image-20231206161947866](./img/125-4.png)

![image-20231206162036518](./img/125-5.png)

`INSA{Aud1o_st3G4n0_1s_4lwayS_Th3_S4me}`

## [MRCTF2020]寻找xxx

`拨号声音`

得到一个`wav`文件

听起来是拨号，用 `dtmf2num` 获取拨号内容 ：

![image-20231206162412105](./img/125-6.png)

提交到公众号不行，应该是有错误，分析[频谱图](https://so.csdn.net/so/search?q=频谱图&spm=1001.2101.3001.7020)：

 一个拨号音是由一个高频和一个低频组成，拨号频谱表如下：

![ ](./img/126-2.png)

用`sonic visualier`打开：

![image-20231206162649168](./img/126-3.png)

![ ](./img/126-4.png)

## 一路到底

给了一个`压缩包`,解压后发现有很多文件,文件内容比较类似

```
51728 : The next is d08299c283bf96c9e64439ceca8be04f.txt
```

猜测前面的是`16进制`信息,后面给的是下一个文件的文件名,且转为`16进制`长度不超过`4`,根据顺序读取,编写代码

```python
# 指定目录
import os
import binascii

dir = "/mnt/c/Users/cc/Downloads/38ff11ef-e3d3-4f8a-b163-3d300bc016ea/files"

hexdata = ''

with open(os.path.join(dir, 'start.txt'), 'r') as f:
    cont = f.read()
    # print(hex_data)
    hexdata += hex(int(cont.split(':')[0].strip()))[2:]
    next_file = cont.split(' ')[-1].strip()
    while True:
        path = os.path.join(dir, next_file)
        try:
            with open(path, 'r') as f:
                cont = f.read()
                hexdata += "{:04x}".format(int(cont.split(':')[0].strip()))
                next_file = cont.split(' ')[-1].strip()
        except:
            break

with open('flag.zip','wb') as f:
    f.write(binascii.unhexlify(hexdata))
```

![image-20231206163503186](./img/127-1.png)

发现压缩包有密码,也没有`伪加密`,爆破密码

![image-20231207095117175](./img/127-3.png)

解压后得到

![image-20231207095223281](./img/127-4.png)

![image-20231207095243702](./img/127-5.png)

文件头异常,应该时`jpg`文件,修改文件头`FF D8 DD E0`

![image-20231207095336355](./img/127-6.png)

## [INSHack2017]10-cl0v3rf13ld-lane-signal

题目给了后缀为`unk`的文件

![img](./img/129-1.png)

`010editor`打开,发现文件头时`jpg`

更改后缀为`jpg`

![find_me](./img/129-2.png)

没有什么东西,然后`010editor`继续看,发现了一个`png`的文件头,`binwalk`分离失败,使用`foremost`分离出一个文件

![00000075](./img/129-5.png)

左下角有一部分`morse`编码

![image-20231207092303321](./img/129-6.png)

发现不全

再去原文件看看,原文件目前可以分为`3部分` `jpg ` `png` `未知文件` 查看一下`png`文件末尾,发现`Ogg`特征,复制保存为`.ogg`文件后用`audacity`打开

![image-20231207092140011](./img/129-4.png)

![image-20231207092811638](./img/129-7.png)

最后手搓`摩斯编码`即可

## [羊城杯 2020]signin

给了我一个`txt`文件,内容为

```
BCEHACEIBDEIBDEHBDEHADEIACEGACFIBDFHACEGBCEHBCFIBDEGBDEGADFGBDEHBDEGBDFHBCEGACFIBCFGADEIADEIADFH
```

`hex`解码失败,说是有两个表,不知道知识点,看看`wp`

`Toy Cipher`: https://eprint.iacr.org/2020/301.pdf

![在这里插入图片描述](./img/130-1.png)

先将密文四个一组对照第二张表转换，简单Python处理

```python
cipherdic = {'M':'ACEG','R':'ADEG','K':'BCEG','S':'BDEG','A':'ACEH','B':'ADEH','L':'BCEH','U':'BDEH','D':'ACEI','C':'ADEI','N':'BCEI','V':'BDEI','H':'ACFG','F':'ADFG','O':'BCFG','W':'BDFG','T':'ACFH','G':'ADFH','P':'BCFH','X':'BDFH','E':'ACFI','I':'ADFI','Q':'BCFI','Y':'BDFI'}
ciphertext = ''
with open('signin.txt','r') as f:
    f = f.read()
    for i in range(0,len(f),4):
        block = f[i:i+4]
        for j in cipherdic:
            if block == cipherdic[j]:
                ciphertext += j
                #print('{}: {}'.format(block,j))
print(ciphertext)
```

得到如下字符

```
LDVUUCMEXMLQSSFUSXKEOCCG
```

再按照提示的意思，将第二张表倒序排列，再对比一次

```python
ciphertext = 'LDVUUCMEXMLQSSFUSXKEOCCG'

original_list = ['M','R','K','S','A','B','L','U','D','C','N','V','H','F','O','W','T','G','P','X','E','I','Q','Y']
reversed_list = original_list[::-1]

flag = ''
for char in ciphertext:
    for olist in original_list:
        if char == olist:
            oindex = original_list.index(olist)
            flag += reversed_list[oindex]

print(flag)
```

得到

```
GWHTTOYSAYGREENTEAISCOOL
```

```
GWHT{TOYSAYGREENTEAISCOOL}
```

[参考](https://blog.csdn.net/mochu7777777/article/details/116056136)

## [HDCTF2019]信号分析

给了个`wav`文件,用`audacity`打开

题目说信号分析

![img](./img/131-1.png)

只有这个波形图有内容，并且每段都是一样的

![img](./img/131-2.png)

![img](./img/131-3.png)

![img](./img/131-4.png)

![img](./img/131-5.png)

![img](./img/131-6.png)

一百零六题是根据这个01的地址码就是PT2242，这题是根据F0就是PT2262这种

![img](./img/131-7.png)

我们直接对应一下

FFFFFFFF0001

注意最后一个是停止码

![img](./img/131-8.png)

flag{FFFFFFFF0001}

```
一长一短：F
两短：0
两长：1
```

可以参考这篇文章

[https://unicorn.360.com/hackcube/forum.php?mod=viewthread&tid=13&extra=page%3D1](https://unicorn.360.com/hackcube/forum.php?mod=viewthread&tid=13&extra=page=1)

[参考](https://www.onctf.com/posts/d228f8e5.html#%E4%B8%80%E7%99%BE%E5%9B%9B%E5%8D%81%E4%B8%80%E3%80%81-MRCTF2020-%E6%91%87%E6%BB%9ADJ%EF%BC%88%E5%BB%BA%E8%AE%AE%E5%A4%A7%E5%A3%B0%E6%92%AD%E6%94%BE%EF%BC%89)

## [SUCTF2018]dead_z3r0

`trid`分析文件类型

![image-20231207111840270](./img/132-1.png)

没看懂是啥

再看看文件内容

![image-20231207111911253](./img/132-2.png)

看起来很像`pyc`文件

从`33 0D 0D 0A`开始分离,保存为`1.pyc`

使用`uncompyle6`转为`py`文件

```
uncompyle6.exe .\1.pyc > 1.py
```

```python
# uncompyle6 version 3.9.0
# Python bytecode version base 3.6 (3379)
# Decompiled from: Python 3.9.8 (tags/v3.9.8:bb3fdcf, Nov  5 2021, 20:48:33) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: cycle.py
# Compiled at: 2018-11-01 19:20:56
# Size of source mod 2**32: 622 bytes


def encryt(key, plain):
    cipher = ''
    for i in range(len(plain)):
        cipher += chr(ord(key[i % len(key)]) ^ ord(plain[i]))

    return cipher


def getPlainText():
    plain = ''
    with open('plain.txt') as (f):
        while True:
            line = f.readline()
            if line:
                plain += line
            else:
                break

    return plain


def main():
    key = 'LordCasser'
    plain = getPlainText()
    cipher = encryt(key, plain)
    with open('cipher.txt', 'w') as (f):
        f.write(cipher.encode('base_64'))


if __name__ == '__main__':
    main()
# okay decompiling .\1.pyc
```

解密其实就是处理异或

```python
import base64

key = 'LordCasser'

cipher = 'KTswVQk1OgQrOgUVODAKFikZJAUuKzwPCTUxMQE1Kxc8NxYYPjcgQwY7OxMhCzFDLyYFGBYjKwkXMDALAScZEycyJgooOigHEAoSDT42IEcBLCcdDiUxBi8mBRgoLBUKPgowBR04P1QnJj0cLyYFGBYjJBs5JywFL1wjHhkbMkI8KhoWFjAWXH55'


plaintext = ''

res =  base64.b64decode(cipher).decode()
for i, v in enumerate(res):
    plaintext += chr(ord(key[i % len(key)]) ^ ord(res[i]))

print(plaintext)
```

得到结果是一串`base64`编码

```
eTB1JTIwNHIzJTIwZjAwbDNkJTBBdGgxNSUyMDE1JTIwbjB0JTIwdGhhdCUyMHkwdSUyMHdhbnQlMEE5MCUyMDBuJTIwZHVkMyUwQWM0dGNoJTIwdGgzJTIwc3QzZzA1YXVydTU=
```

![image-20231207141152993](./img/132-3.png)

被耍了

`剑龙隐写`

![image-20231207235120171](./img/132-4.png)

## [watevrCTF 2019]Unspaellablle

![image-20231217144719537](./img/133-1.png)

是个电影台词,使用`bcompare`与原文对比,多出来的字母就是隐写的`flag`

## [NPUCTF2020]碰上彩虹，吃定彩虹！

解压出三个文件

```
total 32K
-rwxrwxrwx 1 c c 123 Apr 14  2020 lookatme.txt*
-rwxrwxrwx 1 c c 565 Apr 19  2020 maybehint.txt*
-rwxrwxrwx 1 c c 30K Apr 19  2020 secret*
```

首先`010editor`打开`lookatme.txt`

发现有换行和后面有数据

![image-20231217180123952](./img/134-1.png)

应该是`morse`码,`20`看作`.`,`09`看作`-`

```
.- ..- - --- -.- . -.--
```

`Morse`解密后为`AUTOKEY`

脚本爆破

![image-20231217181536343](./img/134-2.png)

得到结果` CONGRATULATIONSONFINDINGMYSECRETNOWIWILLGIVEYOUTHEPASSWORDITISIAMTHEPASSWD`

查看`maybehint.txt`

![image-20231217181734453](./img/134-3.png)

`零宽度字符隐写`

```python
import zwsp_steg

c = '​​​​​​‌​‍​‌​​​​​​‌‌​‌​​​​​​​​‌​‌‍​​​​​​‌‌‌​​​​​​​​​‌​‌‍​​​​​​‌​‍‍‍​​​​​​‌‌​​‍​​​​​​‌‌​‌​​​​​​​‌‌‌​‍​​​​​​​‌​‌‍​​​​​​​‍‍‍​​​​​​​‌​​‌​​​​​​​​‍‌‍‌​​​​​​‌​​​‍​​​​​​​‍‌​​'
    
print(zwsp_steg.decode(c, mode=zwsp_steg.MODE_ZWSP))
```

从`sublime`里复制到代码

```
do u know NTFS?
```

用`NtfsStreamEditor2`打开,注意要用`7zip`解压,不然找不到隐藏文件

![image-20231217202828459](./img/134-4.png)

一堆乱码且多次出现高频词,应该是词频分析

```python
from collections import Counter

with open('./demo.txt', 'r') as f:
    c = Counter(f.read())
    sorted_char_count = sorted(c.items(), key=lambda x: x[1], reverse=True)
    for res in sorted_char_count:
        print(res[0], end='')
```

运行结果

```
ZW5jcnlwdG8=
```

`base64`解码

`encrypto`

`010editor`分析`secret`文件，找了下文件头发现没有匹配的文件类型

到这边又有新东西了，`encrypto`加密

下载`encrypto`软件

对`1.txt`进行加密，会让你输入`hint`和`password`，加密后生成`1.crypto`文件

将`secret`后缀加上`crypto`即可打开

密钥为`iamthepasswd`

![image-20231217212227805](./img/134-5.png)

删除后重新输入即可

- 仔细观察图片可以发现，由五种不同颜色的横条分隔开的六块⻩色有略微深浅的差异， 用 `gimp` 或 `ps` 打开提取一下颜色

## [羊城杯 2020]TCP_IP

```
tshark -r .\attachment.pcap -T fields -e ip.id > data.txt
```

![ ](./img/135-1.png)

`16`进制解密

```
b'@iH<,{*;oUp/im"QPl`yR*ie}NK;.D!Xu)b:J[Rj+6KKM7P@iH<,{*;oUp/im"QPl`yR'
```

`base91`解码

```
flag{wMt84iS06mCbbfuOfuVXCZ8MSsAFN1GA}
```

## [BSidesSF2019]thekey

`USB`流量分析

![image-20231217213708998](./img/136-1.png)

## [INSHack2019]Passthru

被加密的`tls`流量

![image-20231217214013253](./img/137-1.png)

这场比赛的名字是`inshack`，`反过来`不就是`kcahsni`吗？会不会这里就是`flag`。多翻几条看看。

```
kcahsni=26cd07e1f71df3dcee9f
```

果然是不一样的。那就导出来！

tshark导出数据

tshark是个好东西。得好好研究一次。
先说从大神那里抄来的命令。

```
tshark -r fixed.pcap -o 'ssl.keylog_file:sslkey.log' -Y 'http contains "GET /searchbyimage"' -T fields -e http.request.uri.query.parameter > queries.txt
```

1. 要把sslkey.log放在同一目录下

2. 推荐使用kali

3. 参数解释：
   （1）-o 设置首选项值，这里导入key
   （2）-Y 过滤器，这里把目标GET条目过滤出来
   （3）-T 设置输出格式
   （4）-e 添加一个字段
   所以这个命令的效果就是

   ```
   image_url=http%3A%2F%2Frequestbin.net%2Fr%2Fzk2s2ezk%3Fid%3D82290383-7480-487c-b78b-77ac769c56cd%26kcahsni%3D9ef773fe97f56554a3b4,encoded_image=,image_content=,filename=,hl=fr
   image_url=http%3A%2F%2Frequestbin.net%2Fr%2Fzk2s2ezk%3Fid%3D8bd542b5-2056-489e-bc1c-4f028ef27894%26kcahsni%3D26cd07e1f71df3dcee9f,encoded_image=,image_content=,filename=,hl=fr
   image_url=http%3A%2F%2Frequestbin.net%2Fr%2Fzk2s2ezk%3Fid%3De76528cd-17d3-490a-be20-2d817ccee04e%26kcahsni%3D1eaf89725ab93968fc52,encoded_image=,image_content=,filename=,hl=fr
   image_url=http%3A%2F%2Frequestbin.net%2Fr%2Fzk2s2ezk%3Fid%3D491c01dd-f1a3-43c3-b3c8-30c4ab73ff4b%26kcahsni%3Df03c0a7d653539616433,encoded_image=,image_content=,filename=,hl=fr
   image_url=http%3A%2F%2Frequestbin.net%2Fr%2Fzk2s2ezk%3Fid%3Deeed4c5d-8a5f-4b8c-a12d-a2ef007e09e2%26kcahsni%3D66333861303164636130,encoded_image=,image_content=,filename=,hl=fr
   image_url=http%3A%2F%2Frequestbin.net%2Fr%2Fzk2s2ezk%3Fid%3Db69d43cd-ac86-4b20-acc6-6a441d94ae3e%26kcahsni%3D30663937353965366432,encoded_image=,image_content=,filename=,hl=fr
   image_url=http%3A%2F%2Frequestbin.net%2Fr%2Fzk2s2ezk%3Fid%3De56bc952-42c2-4631-96ee-e2e7cac51406%26kcahsni%3D30353331373634326335,encoded_image=,image_content=,filename=,hl=fr
   image_url=http%3A%2F%2Frequestbin.net%2Fr%2Fzk2s2ezk%3Fid%3Dece42ab1-a9d1-44df-a0b5-6b7e83aa9cd0%26kcahsni%3D34323166636461643033,encoded_image=,image_content=,filename=,hl=fr
   image_url=http%3A%2F%2Frequestbin.net%2Fr%2Fzk2s2ezk%3Fid%3D71ad1cf6-a31a-4694-812b-9ea5db6e3cad%26kcahsni%3D34656265373037376332,encoded_image=,image_content=,filename=,hl=fr
   image_url=http%3A%2F%2Frequestbin.net%2Fr%2Fzk2s2ezk%3Fid%3D1b3c7025-b1a8-477f-9d16-89c254af258a%26kcahsni%3D62646464343732627b41,encoded_image=,image_content=,filename=,hl=fr
   image_url=http%3A%2F%2Frequestbin.net%2Fr%2Fzk2s2ezk%3Fid%3D64ac599c-e5ac-43bc-a2e0-0447257cd5bc%26kcahsni%3D534e490b3295c3d06c24,encoded_image=,image_content=,filename=,hl=fr
   image_url=http%3A%2F%2Frequestbin.net%2Fr%2Fzk2s2ezk%3Fid%3Dd8af7f01-5b92-4ad3-8c80-c6af467eac30%26kcahsni%3Df2a8c7e8936667dbf7fe,encoded_image=,image_content=,filename=,hl=fr
   image_url=http%3A%2F%2Frequestbin.net%2Fr%2Fzk2s2ezk%3Fid%3D01b77323-6be9-4abd-b427-9f09d992a4df%26kcahsni%3Dce28456a0fd24ac21ec6,encoded_image=,image_content=,filename=,hl=fr
   image_url=http%3A%2F%2Frequestbin.net%2Fr%2Fzk2s2ezk%3Fid%3D3f3e4f2f-5d92-4d3a-8ce8-f11943b42df3%26kcahsni%3Da12e3efe4b,encoded_image=,image_content=,filename=,hl=fr
   ```

   得到

   ```
   ÷sþ—õeT£´&Íá÷óÜîŸ¯‰rZ¹9hüRð<
   }e59ad3f38a01dca00f9759e6d205317642c5421fcdad034ebe7077c2bddd472b{ASNI2•ÃÐl$ò¨Çè“fgÛ÷þÎ(EjÒJÂÆ¡.>þK
   ```

   其实我们应该是可以猜到（臭不要脸）是逆序的，直接上。

   ```
   Kþ>.¡ÆÂJÒjE(Îþ÷Ûgf“èÇ¨ò$lÐÃ•2INSA{b274dddb2c7707ebe430dadcf1245c246713502d6e9579f00acd10a83f3da95e}
   <ðRüh9¹Zr‰¯ŸîÜó÷áÍ&´£Teõ—þs÷ž
   ```

   ## [羊城杯 2020]逃离东南亚

   解压`日记1` 里面只有两个文件

   ![image-20231217214603501](./img/138-1.png)

修改了`img.png`的高度,发现压缩包密码

使用密码`wdnmd`解压`日记2`

![image-20231217215109807](./img/138-3.png)

前面加`++++++++`用`brainfuck`解密

![image-20231217215038782](./img/138-2.png)

![image-20231217215142394](./img/138-4.png)

`elf`文件执行

```
# ./flag
hei~what you want??
want a flag?
sorry~there is no flag
but maybe your can find something useful!
```

继续往下走，解压第三个密压缩包密码，会得到很多源码，看文本的提示就是里面有一些隐写具体是什么，得靠大家去猜想，这里其实是`tab`和`空格`的数据隐写。

脚本讲解：

🅰️因为涉及的文件很多我们不可能去一个一个文件寻找隐写的信息，需要使用脚本来判断隐写信息所在的文件位置，再使用脚本提取出来。
🅱️既然这里是使用的tab和空格来进行隐写，为了避免提取错误我们使用 \t \t来进行隐藏数据的提取。

```python
import os
import base64
import binascii

from numpy import binary_repr

def get_file_lists(dir_path):
    _file_list = os.listdir(dir_path)
    file_list = []
    for file_str in _file_list:
        new_dir_path = dir_path+'\\'+file_str
        if(os.path.isdir(new_dir_path)):
            file_list.extend(get_file_lists(new_dir_path))
        else:
            file_list.append(new_dir_path)
    return file_list

def important_file(path):
    FILE  =[]
    fiel_list = get_file_lists(path)
    for file in fiel_list:
        f =open(file,"r",encoding='utf-8')
        try:
            data = f.read()
            if " \t \t" in data:
                print(file)
                FILE.append(file)
        except:
            pass
    return FILE

def get_flag(f_list):
    result = ''
    for f in f_list:
        for data in open(f, 'r').readlines():
            data = data[:-1]
            if '}' in data:
                data = data.split('}')[-1]
                if '\t' in data:
                    data1 = data[::].replace('\t', '')
                    data1 = data1.replace(' ', '')
                    if not data1:
                        print([data])
                        result += data

    result = result.replace('\t', '1')
    result = result.replace(' ', '0')
    print(result)
    data = hex(int(result,2))[2:]
    data.encode('utf-8')
    str_bin = binascii.unhexlify(data)
    print(str_bin.decode('utf-8'))

if __name__ == "__main__":
    path = "./source_code"
    FILE = important_file(path)
    get_flag(FILE)
```

![image-20231217215618671](./img/138-5.png)

## [GKCTF 2021]0.03

`NtfsStreamEditor`发现隐藏文件

```
QAZ WSX EDC
RFV TGB YHN
UJM IKO LP/
```

`secret.txt`

```
do you believe that you get?

311223313313112122312312313311
```

解密后为

```
EBCCAFDDCE
```

成功挂载

![img](./img/138-6.png)

## [BSidesSF2020]barcoder

## [QCTF2018]picture

`lsb`隐写,密码为图片里`万物皆空 无欲无求`的首字母

`wwjkwywq`

![image-20231218171513781](./img/139-1.png)

```python
# _*_ coding:utf-8 _*_
 
ip = (58, 50, 42, 34, 26, 18, 10, 2,
 
      60, 52, 44, 36, 28, 20, 12, 4,
 
      62, 54, 46, 38, 30, 22, 14, 6,
 
      64, 56, 48, 40, 32, 24, 16, 8,
 
      57, 49, 41, 33, 25, 17, 9, 1,
 
      59, 51, 43, 35, 27, 19, 11, 3,
 
      61, 53, 45, 37, 29, 21, 13, 5,
 
      63, 55, 47, 39, 31, 23, 15, 7)
 
ip_1 = (40, 8, 48, 16, 56, 24, 64, 32,
 
        39, 7, 47, 15, 55, 23, 63, 31,
 
        38, 6, 46, 14, 54, 22, 62, 30,
 
        37, 5, 45, 13, 53, 21, 61, 29,
 
        36, 4, 44, 12, 52, 20, 60, 28,
 
        35, 3, 43, 11, 51, 19, 59, 27,
 
        34, 2, 42, 10, 50, 18, 58, 26,
 
        33, 1, 41, 9, 49, 17, 57, 25)
 
e = (32, 1, 2, 3, 4, 5, 4, 5,
 
     6, 7, 8, 9, 8, 9, 10, 11,
 
     12, 13, 12, 13, 14, 15, 16, 17,
 
     16, 17, 18, 19, 20, 21, 20, 21,
 
     22, 23, 24, 25, 24, 25, 26, 27,
 
     28, 29, 28, 29, 30, 31, 32, 1)
 
p = (16, 7, 20, 21, 29, 12, 28, 17,
 
     1, 15, 23, 26, 5, 18, 31, 10,
 
     2, 8, 24, 14, 32, 27, 3, 9,
 
     19, 13, 30, 6, 22, 11, 4, 25)
 
s = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 
      [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 
      [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
 
     [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 
      [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 
      [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
 
     [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 
      [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
 
     [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 
      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 
      [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
 
     [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 
      [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 
      [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
 
     [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 
      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 
      [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 
      [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
 
     [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 
      [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 
      [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
 
     [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 
      [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 
      [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 
      [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
 
pc1 = (57, 49, 41, 33, 25, 17, 9,
 
       1, 58, 50, 42, 34, 26, 18,
 
       10, 2, 59, 51, 43, 35, 27,
 
       19, 11, 3, 60, 52, 44, 36,
 
       63, 55, 47, 39, 31, 23, 15,
 
       7, 62, 54, 46, 38, 30, 22,
 
       14, 6, 61, 53, 45, 37, 29,
 
       21, 13, 5, 28, 20, 12, 4)
 
pc2 = (14, 17, 11, 24, 1, 5, 3, 28,
 
       15, 6, 21, 10, 23, 19, 12, 4,
 
       26, 8, 16, 7, 27, 20, 13, 2,
 
       41, 52, 31, 37, 47, 55, 30, 40,
 
       51, 45, 33, 48, 44, 49, 39, 56,
 
       34, 53, 46, 42, 50, 36, 29, 32)
 
d = (1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1)
 
__all__ = ['desdecode']
 
 
class DES:
    """解密函数，DES加密与解密的方法相差不大
        只是在解密的时候所用的子密钥与加密的子密钥相反
    """
 
    def __init__(self):
        pass
 
    def decode(self, string, key, key_len, string_len):
        output = ""
        num = 0
        # 将密文转换为二进制
        code_string = self._functionCharToA(string, string_len)
        # 获取字密钥
        code_key = self._getkey(key, key_len)
 
        # 如果密钥长度不是16的整数倍则以增加0的方式变为16的整数倍
        real_len = (key_len / 16) + 1 if key_len % 16 != 0 else key_len / 16
        trun_len = string_len * 4
        # 对每64位进行一次加密
        for i in range(0, trun_len, 64):
            run_code = code_string[i:i + 64]
            run_key = code_key[int(num % real_len)]
 
            # 64位明文初始置换
            run_code = self._codefirstchange(run_code)
 
            # 16次迭代
            for j in range(16):
                code_r = run_code[32:64]
                code_l = run_code[0:32]
 
                # 64左右交换
                run_code = code_r
 
                # 右边32位扩展置换
                code_r = self._functionE(code_r)
 
                # 获取本轮子密钥
                key_y = run_key[15 - j]
 
                # 异或
                code_r = self._codeyihuo(code_r, key_y)
 
                # S盒代替/选择
                code_r = self._functionS(code_r)
 
                # P转换
                code_r = self._functionP(code_r)
 
                # 异或
                code_r = self._codeyihuo(code_l, code_r)
 
                run_code += code_r
            num += 1
 
            # 32互换
            code_r = run_code[32:64]
            code_l = run_code[0:32]
            run_code = code_r + code_l
 
            # 将二进制转换为16进制、逆初始置换
            output += self._functionCodeChange(run_code)
        return output
 
    # 获取子密钥
    def _getkey(self, key, key_len):
 
        # 将密钥转换为二进制
        code_key = self._functionCharToA(key, key_len)
 
        a = [''] * 16
        real_len = (key_len / 16) * 16 + 16 if key_len % 16 != 0 else key_len
 
        b = [''] * int(real_len / 16)
        for i in range(int(real_len / 16)):
            b[i] = a[:]
        num = 0
        trun_len = 4 * key_len
        for i in range(0, trun_len, 64):
            run_key = code_key[i:i + 64]
            run_key = self._keyfirstchange(run_key)
            for j in range(16):
                key_l = run_key[0:28]
                key_r = run_key[28:56]
                key_l = key_l[d[j]:28] + key_l[0:d[j]]
                key_r = key_r[d[j]:28] + key_r[0:d[j]]
                run_key = key_l + key_r
                key_y = self._functionKeySecondChange(run_key)
                b[num][j] = key_y[:]
            num += 1
 
        return b
 
        # 异或
 
    def _codeyihuo(self, code, key):
        code_len = len(key)
        return_list = ''
        for i in range(code_len):
            if code[i] == key[i]:
                return_list += '0'
            else:
                return_list += '1'
        return return_list
 
    # 密文或明文初始置换
    def _codefirstchange(self, code):
        changed_code = ''
        for i in range(64):
            changed_code += code[ip[i] - 1]
        return changed_code
 
    # 密钥初始置换
    def _keyfirstchange(self, key):
        changed_key = ''
        for i in range(56):
            changed_key += key[pc1[i] - 1]
        return changed_key
 
    # 逆初始置换
    def _functionCodeChange(self, code):
        return_list = ''
        for i in range(16):
            list = ''
            for j in range(4):
                list += code[ip_1[i * 4 + j] - 1]
            return_list += "%x" % int(list, 2)
        return return_list
 
    # 扩展置换
    def _functionE(self, code):
        return_list = ''
        for i in range(48):
            return_list += code[e[i] - 1]
        return return_list
 
        # 置换P
 
    def _functionP(self, code):
        return_list = ''
        for i in range(32):
            return_list += code[p[i] - 1]
        return return_list
 
    # S盒代替选择置换
    def _functionS(self, key):
        return_list = ''
        for i in range(8):
            row = int(str(key[i * 6]) + str(key[i * 6 + 5]), 2)
            raw = int(str(key[i * 6 + 1]) + str(key[i * 6 + 2]) + str(key[i * 6 + 3]) + str(key[i * 6 + 4]), 2)
            return_list += self._functionTos(s[i][row][raw], 4)
 
        return return_list
 
    # 密钥置换选择2
    def _functionKeySecondChange(self, key):
        return_list = ''
        for i in range(48):
            return_list += key[pc2[i] - 1]
        return return_list
 
    # 将十六进制转换为二进制字符串
    def _functionCharToA(self, code, lens):
        return_code = ''
        lens = lens % 16
        for key in code:
            code_ord = int(key, 16)
            return_code += self._functionTos(code_ord, 4)
 
        if lens != 0:
            return_code += '0' * (16 - lens) * 4
        return return_code
 
    # 二进制转换
    def _functionTos(self, o, lens):
        return_code = ''
        for i in range(lens):
            return_code = str(o >> i & 1) + return_code
        return return_code
 
 
# 将unicode字符转换为16进制
def tohex(string):
    return_string = ''
    for i in string:
        return_string += "%02x" % ord(i)
    return return_string
 
 
def tounicode(string):
    return_string = ''
    string_len = len(string)
    for i in range(0, string_len, 2):
        return_string += chr(int(string[i:i + 2], 16))
    return return_string
 
 
# 入口函数
def desdecode(from_code, key):
    key = tohex(key)
 
    des = DES()
 
    key_len = len(key)
    string_len = len(from_code)
    if string_len % 16 != 0:
        return False
    if string_len < 1 or key_len < 1:
        return False
 
    key_code = des.decode(from_code, key, key_len, string_len)
    return tounicode(key_code)
 
 
# 测试
if __name__ == '__main__':
    print(desdecode('e3fab29a43a70ca72162a132df6ab532535278834e11e6706c61a1a7cefc402c8ecaf601d00eee72', 'mtqVwD4JNRjw3bkT9sQ0RYcZaKShU4sf'))
```

```
QCTF{eCy0AALMDH9rLoBnWnTigXpYPkgU0sU4}
```

## [*CTF2019]babyflash

使用`JPEXS Free Flash Decompiler`分解文件

首先用`Audacity`打开，就可以得到一部分`flag`

![image-20231222103939241](./img/140-1.png)

黑色作为黑色小块，白色作为白色小块

绘制二维码

```python
from PIL import Image
import os



path = 'C:/Users/cc/Downloads/images/'

images_fn_list = os.listdir(path)

images_fn_list.sort(key=lambda x: int(x.split('.')[0]))
# print(dir_list)

qr_data = ''

for image_name in images_fn_list:
    img = Image.open(os.path.join(path, image_name))
    im = img.load()
    if im[0, 0] == (0, 0, 0):   # 黑色
        qr_data += '1'
    elif im[0, 0] == (255, 255, 255):   # 白色
        qr_data += '0'
        
width = height = 21

new_image = Image.new('RGB', (width, height))
i = 0

for w in range(width):
    for h in range(height):
        if qr_data == '1':
            new_image.putpixel([w, h], (0, 0, 0))
        elif qr_data[i] == '0':
            new_image.putpixel([w, h], (255, 255, 255))
        i += 1
        
new_image.save('flag.png')
```

扫描二维码即可获得领一部分`flag`

## [b01lers2020]image_adjustments

`图像处理`

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

## [watevrCTF 2019]Polly

![image-20231222145721681](./img/141-1.png)

把`x=0`带入式子中得到`119`，转成符号就是`w`，而刚好这个比赛的`flag头`就是`w`，所以`x`要从`0`开始带入

```python
import sympy

flag = ''
x = sympy.symbols('x')
y = eval(open("attachment.txt","r").read())
for i in range(57):
    print(chr(y.subs(x, i)), end='')
```


# 面具下的flag

## 知识点

`vmdk`

`binwalk`

## 解题

打开照片,查看详细信息,没有什么东西

`010editor`查看一下

![image-20231125164007319](G:/CTFWriteUp/buuctf/Misc/img/16-2.png)

发现有文件拼接

`binwalk`分离一下,有一个`flag.vmdk`了

但是还是看看压缩包先

压缩包有加密,先看看是不是`伪加密`

![image-20231125164629347](G:/CTFWriteUp/buuctf/Misc/img/16-3.png)

确实是`伪加密`

![image-20231125165050463](G:/CTFWriteUp/buuctf/Misc/img/16-4.png)

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

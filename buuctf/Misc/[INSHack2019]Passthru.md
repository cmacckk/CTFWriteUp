# [INSHack2019]Passthru

## 知识点

`TLS加密流量`

## 解题

被加密的`tls`流量

![image-20231217214013253](./img/137-1.png)

这场比赛的名字是`inshack`，`反过来`不就是`kcahsni`吗？会不会这里就是`flag`。多翻几条看看。

```
kcahsni=26cd07e1f71df3dcee9f
```

果然是不一样的。那就导出来！

`tshark`导出数据

`tshark`是个好东西。得好好研究一次。
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

   是逆序的，

   ```
   Kþ>.¡ÆÂJÒjE(Îþ÷Ûgf“èÇ¨ò$lÐÃ•2INSA{b274dddb2c7707ebe430dadcf1245c246713502d6e9579f00acd10a83f3da95e}
   <ðRüh9¹Zr‰¯ŸîÜó÷áÍ&´£Teõ—þs÷ž
   ```

   
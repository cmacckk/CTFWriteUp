# greatescape

## 知识点

`FTP流量分析`

`TLS`

## 解题

找到`FTP`传的`ssc.key`

![image-20231205205624216](./img/99-1.png)

通过分析流量猜测，这应该在向`ftp`服务器传送私钥，我们得到了私钥，就可以解密`TLS`报文

`Edit->Preference->Protocols->TLS`，点击`Edit`，然后点击`+`添加`Key File`

![image-20231205205838804](./img/99-2.png)
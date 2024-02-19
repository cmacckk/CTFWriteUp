# [watevrCTF-2019]Cookie Store

## 知识点

`Cookie`

## 解题

在页面要求购买`Flag Cookie`给`flag`

![](./img/[watevrCTF-2019]Cookie Store-1.png)

但是我们余额不足,`Cookie`好像是用`base64`编码的,解码看一下

![](./img/[watevrCTF-2019]Cookie Store-2.png)





改余额后重新`base64`编码即可,更换`Cookie`就行

![](./img/[watevrCTF-2019]Cookie Store-3.png)
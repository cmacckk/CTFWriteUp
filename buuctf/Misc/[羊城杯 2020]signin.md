# [羊城杯 2020]signin

## 知识点

`toy cipher`

## 解题

给了我一个`txt`文件,内容为

```
BCEHACEIBDEIBDEHBDEHADEIACEGACFIBDFHACEGBCEHBCFIBDEGBDEGADFGBDEHBDEGBDFHBCEGACFIBCFGADEIADEIADFH
```

`hex`解码失败,说是有两个表,不知道知识点,看看`wp`

`Toy Cipher`: https://eprint.iacr.org/2020/301.pdf

![](./img/130-1.png)

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
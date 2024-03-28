# [ACTF新生赛2020]outguess

## 知识点

`outguess`

`社会主义核心价值观编码`

## 解题

在图片详细信息的备注里发现

`公正民主公正文明公正和谐`

`社会主义核心价值观解码`后为`abc`

```bash
outguess -r mmm.jpg -k abc res.txt
```

`res.txt`的内容即为`flag`
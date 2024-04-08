# [watevrCTF 2019]Polly

## 知识点

`python公式`

## 解题

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


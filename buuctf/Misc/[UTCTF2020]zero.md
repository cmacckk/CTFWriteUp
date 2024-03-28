# [UTCTF2020]zero

## 知识点

`零宽度字符隐写`

## 解题

> Lorem ipsum dolor ‌‌‌‌‍﻿‍‍sit amet‌‌‌‌‍﻿‍‌, consectetur adipiscing‌‌‌‌‍‬‍‬ elit.‌‌‌‌‍‬﻿‌‌‌‌‌‍‬‌‍ Phasellus quis tempus ante, nec vehicula mi. ‌‌‌‌‍‬‍﻿Aliquam nec‌‌‌‌‍﻿‬﻿ nisi ut neque interdum auctor.‌‌‌‌‍﻿‍﻿ Aliquam felis ‌‌‌‌‍‬‬‌orci, vestibulum ‌‌‌‌‍﻿‬‍sit amet ante‌‌‌‌‍‌﻿‬ at, consectetur‌‌‌‌‍‌﻿﻿ lobortis eros.‌‌‌‌‍‍‍‌ ‌‌‌‌‍‌‌‌Orci varius natoque ‌‌‌‌‍﻿‌﻿penatibus et ‌‌‌‌‍‬‌﻿magnis‌‌‌‌‌﻿‌‍‌‌‌‌‌﻿‌‍ dis ‌‌‌‌‍‍﻿﻿parturient montes, nascetur ridiculus ‌‌‌‌‌﻿‍‌‌‌‌‌‌﻿‬‍mus. In finibus‌‌‌‌‌﻿‌‬ magna‌‌‌‌‌﻿‍﻿ mauris, quis‌‌‌‌‍‬‌‍ auctor ‌‌‌‌‍‬‌‍libero congue quis. ‌‌‌‌‍‬‬‬Duis‌‌‌‌‍‬‌‬ sagittis consequat urna non tristique. Pellentesque eu lorem ‌‌‌‌‍﻿‌‍id‌‌‌‌‍‬‬﻿ quam vestibulum ultricies vel ac purus‌‌‌‌‌﻿‌‍.‌‌‌‌‌﻿‍‌‌‌‌‌‍﻿﻿‍

刚开始以为是字频分析,放到`qiupqiup`没发现什么

用`cat`打开,发现很多不可见字符

![image-20231129231602064](G:/CTFWriteUp/buuctf/Misc/img/68-1.png)

用`vim`打开

![image-20231129231628969](G:/CTFWriteUp/buuctf/Misc/img/68-2.png)

零宽度字符隐写：https://330k.github.io/misc_tools/unicode_steganography.html

![image-20231129231724473](G:/CTFWriteUp/buuctf/Misc/img/68-3.png)

[参考文章](https://blog.csdn.net/mochu7777777/article/details/109817723)
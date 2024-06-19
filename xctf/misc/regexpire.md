# regexpire

## 知识点

`正则计算匹配`

## 解题

python2

```python
import socket
import rstr

remoteip   = "61.147.171.105"
remoteport = 64650

def sock(remoteip, remoteport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((remoteip, remoteport))
    return s, s.makefile('rw', bufsize=0)

def read_until(f, delim='\n'):
    data = ''
    while not data.endswith(delim):
        data += f.read(1)
    return data

s, f = sock(remoteip, remoteport)

print read_until(f, "regexes?\n")

count = 0
while True:
	print "[+] Iter:", count
	target = read_until(f, "\n").strip()
	print "[+] Target:", target

	ans = rstr.xeger(target)
	while '\n' in ans:
		ans = rstr.xeger(target)
	print "[+] Answer:", ans
	s.send(ans+"\n")
	count += 1
	
s.close()
```


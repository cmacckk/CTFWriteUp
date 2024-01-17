c = ['\x1f', '\x12', '\x1d', '(', '0', '4', '\x01', '\x06', '\x14', '4', ',', 
 '\x1b', 'U', '?', 'o', '6', '*', ':', '\x01', 'D', ';', '%', '\x13']

flag = ''
l = len(c)

for i in range(l - 2, -1, -1):
    c[i] = chr(ord(c[i]) ^ ord(c[i + 1]))

for i in range(l):
    flag += chr((ord(c[i]) - i) % 128)

print(flag)
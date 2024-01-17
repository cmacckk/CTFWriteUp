domain = 'suctf'

res = ''

for v in domain:
    for j in range(0x7f, 0x10FFFF):
        try:
            if chr(j).encode('idna').decode('utf-8') == v:
                res += chr(j)
                break
        except:
            pass
print(res)
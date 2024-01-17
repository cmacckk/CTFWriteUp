f1 = 'GXY{do_not_'

f2 = ''
flag = ''

m_f2 = [0x7F, 0x66, 0x6F, 0x60, 0x67, 0x75, 0x63, 0x69][::-1]
for i, _ in enumerate(m_f2):
    if i % 2 == 1:
        s = chr(int(m_f2[i]) - 2)
    else:
        s = chr(int(m_f2[i]) - 1)
    print(s)
    flag += s

print(f1 + flag)
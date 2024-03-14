import itertools

string = "print_rscandir"

result2 = [0x8b, 0x9b, 0xa0, 0x9c, 0x8f, 0x91, 0x9e, 0xd1, 0x96, 0x8d, 0x8c]  # Original chars,11 total
result = result2[:9]  # to be deleted

hex_array = [ord(b) for b in string]
hex_array2 = hex_array[:9]


temp = []

for d in hex_array2:
    for a in hex_array:
        for b in hex_array:
            for c in hex_array:
                if (a ^ b ^ c == d):
                    if a == b == c == d:
                        continue
                    else:
                        print("%s,%s,c=%s,d=%s" % (hex(a), hex(b), hex(c), hex(d)))
                        if d not in temp:
                            temp.append(d)
print(len(temp), temp)

print(temp)
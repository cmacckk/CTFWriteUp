def en(s):
    return '%' + hex(ord(s) ^ 0xff)[2:]


p = list(set('printrscandir'))
for i in p:
    for j in p:
        for k in p:
            for m in p:
                if ord(j) ^ ord(k) ^ ord(m) == ord(i):
                    if(j == k or j == m or m == k):
                        continue
                    else:
                        print(i+' == '+j + '^' + k + '^'+m, end=' => ')
                        print('{:0>2} => {:0>2}^{:0>2}^{:0>2}"'.format(en(i), en(j), en(k), en(m)))
                        break
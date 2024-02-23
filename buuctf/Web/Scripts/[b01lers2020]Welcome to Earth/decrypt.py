from itertools import permutations


flag = ["{hey", "_boy", "aaaa", "s_im", "ck!}", "_baa", "aaaa", "pctf"]

data = permutations(flag)

for _, v in enumerate(data):
    res = ''.join(v)
    if res.startswith("pctf{hey") and res.endswith('ck!}'):
        print(res)
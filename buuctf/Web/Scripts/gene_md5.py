import hashlib
import string
import itertools


def gene_md5(plaintext: str):
    md5 =  hashlib.md5()
    md5.update(plaintext.encode())
    return md5.hexdigest()

def get_data():
    for i in range(10):
        print(f"[*] try gene {i}")
        combinations_with_replacement = list(itertools.combinations_with_replacement(string.ascii_letters, i))
        combinations_with_replacement_str = [''.join(combination) for combination in combinations_with_replacement]
        for data in combinations_with_replacement_str:
            tmp_md5 = gene_md5(data)
            if tmp_md5[0:6] == "6d0bc1":
                print(f"[+] {data}  ===> {tmp_md5}")
                exit(0)


if __name__ == "__main__":
    get_data()
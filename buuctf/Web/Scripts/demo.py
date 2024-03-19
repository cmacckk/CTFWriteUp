from collections import defaultdict


def get_mini_codes():
    """获取出现最少的url编码"""
    # 给定的字符串
    input_str = "(%ff%ff%ff%ff%ff%ff%ff^%8f%8d%96%91%8b%a0%8d)((%ff%ff%ff%ff%ff%ff%ff^%8c%9c%9e%91%9b%96%8d)((%ff^%d1)))"
    min_arr = []
    except_min_arr = []
    # 创建一个 defaultdict 以存储每个 URL 编码的计数
    url_encoding_counts = defaultdict(int)

    # 查找所有以 '%' 开头的两个字符的组合，并计数它们的出现次数
    for i in range(len(input_str) - 2):
        if (
            input_str[i] == "%"
            and input_str[i + 1].isalnum()
            and input_str[i + 2].isalnum()
        ):
            url_encoding = input_str[i : i + 3]
            url_encoding_counts[url_encoding] += 1

    min_count = min(url_encoding_counts.values())
    min_url_encodings = [
        encoding
        for encoding, count in url_encoding_counts.items()
        if count == min_count
    ]
    print(f"出现次数最少 (出现{min_count}次) 的编码为:")
    for encoding in min_url_encodings:
        print(f"{encoding} | ", end="")
        min_arr.append(encoding)
        
    except_min_url_encodings = [encoding for encoding, count in url_encoding_counts.items() if count != min_count]
    print("\n=============================\n出现次数除了最少之外的编码为:")
    for encoding in except_min_url_encodings:
        print(f"{encoding} | ", end="")
        except_min_arr.append(encoding)

    return min_arr, except_min_arr


def en(s):
    return '%' + hex(ord(s) ^ 0xFF)[2:]

from string import ascii_letters

def get_encoded():
        res = []

        p = list(ascii_letters)
        for i in p:
                for j in p:
                        for k in p:
                                for m in p:
                                        if ord(j) ^ ord(k) ^ ord(m) == ord(i):
                                                if j == k or j == m or m == k:
                                                        continue
                                                else:
                                                        # print(i + "==" + j + "^" + k + "^" + m, end="\t")
                                                        # print(
                                                        #     '{:0>2}  =>  ["{:0>2}","{:0>2}","{:0>2}"]'.format(
                                                        #         en(i), en(j), en(k), en(m)
                                                        #     )
                                                        # )
                                                        res.append([en(i), en(j), en(k), en(m)])
                                                        break

        return res


if __name__ == "__main__":
    mini_codes, except_mini_codes = get_mini_codes()
    all_codes = mini_codes + except_mini_codes
    coded = get_encoded()
    print("\n===================")
    for arr in coded:
        # print(arr)
        # if arr[0] in mini_codes and arr[1] in except_mini_codes and arr[2] in except_mini_codes and arr[3] in except_mini_codes:
        if arr[0] in all_codes and arr[1] in all_codes and arr[2] in all_codes and arr[3] in all_codes:
            print(f"{arr[0]} ==> {arr[1]}^{arr[2]}^{arr[3]}")
            all_codes.remove(arr[0])
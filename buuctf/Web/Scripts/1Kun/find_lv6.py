import requests

for i in range(1, 200):
    url = f"http://1d0b0ad0-f48f-4776-ae30-c47828cf6b31.node5.buuoj.cn:81/shop?page={i}"
    resp = requests.get(url)
    print(i, flush=True)
    if 'lv6.png' in resp.text:
        print(f"find -> {i}")
        break
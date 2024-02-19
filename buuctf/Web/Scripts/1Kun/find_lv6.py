import requests

for i in range(1, 200):
    url = f"http://2e51f033-2d85-4ae4-a843-33dd417500ef.node5.buuoj.cn:81/shop?page={i}"
    resp = requests.get(url)
    print(i, flush=True)
    if 'lv6.png' in resp.text:
        print(f"find -> {i}")
        break
"""
爬取美女图片
https://pic.netbian.com/4kmeinv/
"""

import requests
from bs4 import BeautifulSoup
import os

url = "https://pic.netbian.com/4kfengjing/"
r = requests.get(url)
r.encoding="gbk"
print(r.status_code)
html=r.text

soup = BeautifulSoup(html, "html.parser")
imgs = soup.find_all("img")
for img in imgs:
    src = img["src"]
    if "/uploads/" not in src:
        continue
    src = f"https://pic.netbian.com{src}"
    print(src)

    filename = os.path.basename(src)
    with open(f"aaa/{filename}", "wb") as f:
        r_img = requests.get(src)
        f.write(r_img.content)



import sys
import os
import qrcode
url = "https://www.youtube.com/watch?v=WR1ydijTx5E"
name = "qr"
directory = "./" #dir to save file at

for i, n in enumerate(sys.argv[1::]):
    if n == "-name":
        name = sys.argv[i+2]

    elif n == "-url":
        url = sys.argv[i+2]

    elif n == "-path":
        path = sys.argv[i+2]

os.makedirs(path, exist_ok=True)

img = qrcode.make(url)
img.save(os.path.join(path, f"{name}_qr.png"), "PNG")
from numpy import rint
import qrcode

import matplotlib.pyplot as plt

URL = "https://store.steampowered.com/app/1942120/"

qr_arr = qrcode.make(URL,border=0,box_size=1)

print(qr_arr.size)
x_size, y_size = qr_arr.size
print(x_size, y_size)
img_arr = []
for x in range(x_size):
    img_row = []
    for y in range(y_size):
        px = qr_arr.getpixel((x,y))
        #print(px)
        img_row.append(px // 255)
        print("X" if px == 0 else " ", end="")
    img_arr.append(img_row)
    print()

plt.imshow(img_arr)
plt.show()
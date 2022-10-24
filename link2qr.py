
import qrcode

# print two dimensional array
def print_arr(arr):
    for row in arr:
        for px in row:
            print(" " if px == 1 else "X", end="")
        print()

# convert url to qr arr
def url2arr(url):
    # convert url to Pil Image 
    qr_arr = qrcode.make(url, border=0, box_size=1)
    # get image size
    x_size, y_size = qr_arr.size
    img_arr = []
    for x in range(x_size):
        img_row = []
        for y in range(y_size):
            px = qr_arr.getpixel((x,y))
            px //= 255
            img_row.append(px)
        img_arr.append(img_row)

    return img_arr

# convert qr arr to openscad format string
def arr2openscad(arr):
    openscad_arr = "[\n"
    l = len(arr)
    for row_i in range(l):
        row = arr[row_i]
        openscad_arr += "[ {} ]".format(", ".join([str(el) for el in row]))
        openscad_arr += ",\n" if row_i != l-1 else "\n]; \n"
    return openscad_arr

# write an openscad array 'arr' to a file 'fn' as variable 'var_name'
def save_to_file(arr, var_name, fn):
    with open(fn, 'w') as f:
        f.writelines("{} = {}".format(var_name,arr))

# just a testing main
if __name__=="__main__":
    URL = "https://store.steampowered.com/app/1942120/"
    _arr = url2arr(URL)
    oscad_arr = arr2openscad(_arr)
    save_to_file(oscad_arr, "test_arr", "./qrs/test.scad-qr")
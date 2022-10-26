
import qrcode

# print two dimensional array
def print_arr(arr):
    for row in arr:
        for px in row:
            print(" " if px == 1 else "X", end="")
        print()

# convert url to qr arr
def url2qr(url):
    # convert url to Pil Image representing QR code
    qr_pil_img = qrcode.make(url, border=0, box_size=1)
    # get image size
    x_size, y_size = qr_pil_img.size
    qr_arr = []
    for x in range(x_size):
        img_row = []
        for y in range(y_size):
            px = qr_pil_img.getpixel((x,y))
            px //= 255
            img_row.append(px)
        qr_arr.append(img_row)

    return qr_arr

# convert qr arr to openscad format string
def qr2openscad(qr_arr):
    openscad_arr = "[\n"
    l = len(qr_arr)
    for row_i in range(l):
        row = qr_arr[row_i]
        openscad_arr += "[ {} ]".format(", ".join([str(el) for el in row]))
        openscad_arr += ",\n" if row_i != l-1 else "\n]; \n"
    return openscad_arr

# write an openscad array 'arr' to a file 'fn' as variable 'var_name'
def save_to_file(arr, var_name, fn):
    with open(fn, 'w') as f:
        f.writelines("{} = {}".format(var_name,arr))

# takes 'url' and save binary representation of QR code into 'file_name' in OpenSCAD array format as 'variable_name'
def process_url_to_file(url, file_name, variable_name):
    _arr = url2qr(url)
    oscad_arr = qr2openscad(_arr)
    save_to_file(oscad_arr, variable_name, file_name)

# just a testing main
if __name__=="__main__":
    URL = "https://store.steampowered.com/app/1942120/"
    _arr = url2qr(URL)
    oscad_arr = qr2openscad(_arr)
    save_to_file(oscad_arr, "test_arr", "./qrs/test.scad-qr")
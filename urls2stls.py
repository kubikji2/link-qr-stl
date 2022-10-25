import link2qr
import os

FN = "urls/urls.txt"

# load urls
def load_urls():
    short_urls = []
    with open(FN,'r') as f:
        for line in f.readlines():
            entries = line.strip().split("/")
            entries.pop(-2)
            new_url = "/".join(entries)
            short_urls.append(new_url)
    return short_urls

def process_url(url):
    #print(url)
    fn_base = url.split("/")[-2]
    print("Processing file: {}".format(fn_base))
    link2qr.save_to_file(link2qr.arr2openscad(link2qr.url2arr(url)), "qr_arr", "./qrs/qr-{}.scad-qr".format(fn_base))
    os.system("cp qrs/qr-{}.scad-qr qrs/qr.scad-qr".format(fn_base))
    scad_cmd = "openscad -o stls/{}-{}.stl qr2stls.scad -D is_qr={}".format(fn_base,"{}","{}")
    
    # first part
    cur_cmd = scad_cmd.format("false","false")
    print("EXECUTING: {}".format(cur_cmd))
    os.system(cur_cmd)
    
    # second part
    cur_cmd = scad_cmd.format("true","true")
    print("EXECUTING: {}".format(cur_cmd))
    os.system(cur_cmd)
    
if __name__=="__main__":
    
    for url in load_urls():
        process_url(url)
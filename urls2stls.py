import url2qr
import os

# load urls
def load_urls(urls_file):
    short_urls = []
    with open(urls_file,'r') as f:
        for line in f.readlines():
            entries = line.strip().split("/")
            entries.pop(-2)
            new_url = "/".join(entries)
            short_urls.append(new_url)
    return short_urls

def process_url(url):
    fn_base = url.split("/")[-2]
    fn_path = "./qrs/qr-{}.scad-qr".format(fn_base)
    var_name = "qr_arr"
    print("Processing file: {}".format(fn_base))
    url2qr.process_url_to_file(url, var_name, fn_path)

    os.system("cp {} qrs/qr.scad-qr".format(fn_path))
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

    FN = "urls/urls.txt"
    
    for url in load_urls(FN):
        process_url(url)
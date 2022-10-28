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

    # processing from url to qr-code file
    print("Processing file: {}".format(fn_base))
    url2qr.process_url_to_file(url, fn_path, var_name)

    # copy the qr-code openscad file to the file included by the main openscad-file
    os.system("cp {} qrs/qr.scad-qr".format(fn_path))

    # creating command to execute
    scad_cmd = "openscad -o stls/{}-{}.stl qr2stls.scad -D is_qr={}".format(fn_base,"{}","{}")
    
    # base part
    cur_cmd = scad_cmd.format("base","false")
    print("EXECUTING: {}".format(cur_cmd))
    os.system(cur_cmd)
    
    # qr-code part
    cur_cmd = scad_cmd.format("qr-code","true")
    print("EXECUTING: {}".format(cur_cmd))
    os.system(cur_cmd)
    
if __name__=="__main__":

    
    FN = "urls/urls.txt"
    
    for url in load_urls(FN):
        process_url(url)

    # testing on Rick Roll
    #URL = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ/'
    #process_url(URL)
#!/usr/bin/python3
import url2qr
import os, sys
import argparse

# load urls from the 'urls_file_path'
def load_urls(urls_file_path):
    urls = []
    try:
        # TODO will this work for binary files? Do I care about binary files?
        with open(urls_file_path,'r') as f:
            for line in f.readlines():
                new_url = line.strip().strip("/")
                urls.append(new_url)
    except:
        print("ERROR: '{}' is not path to readable file".format(urls_file_path),file=sys.stderr)
    return urls

def process_url(url):
    # composing a filename base
    # '-> in case of string, the space are replaced by underscrolls
    fn_base = url.split("/")[-1].replace(" ", "_")
    # path to qr array file
    qp_arr_path = "./qrs/qr-{}.scad-qr".format(fn_base)
    # variable name in 'qr_arr_path'
    var_name = "qr_arr"

    # processing from url/string to qr-code file
    print("Processing QR from file: {}".format(fn_base))
    url2qr.process_url_to_file(url, qp_arr_path, var_name)

    # copy the qr-code openscad file to the file included by the main openscad-file
    print("Updating QR array.")
    os.system("cp {} qrs/qr.scad-qr".format(qp_arr_path))

    # creating command-template
    scad_cmd = "openscad -o stls/{}-{}.stl qr2stl-wrapper.scad -D is_qr={}".format(fn_base,"{}","{}")
    
    # exporting the base part (white)
    cur_cmd = scad_cmd.format("base-white","false")
    print("Converting the base geometry.\n"+"EXECUTING: {}".format(cur_cmd))
    os.system(cur_cmd)
    
    # exporting the qr-code part (black)
    cur_cmd = scad_cmd.format("qr-black","true")
    print("Converting the qr-code geometry.\n"+"EXECUTING: {}".format(cur_cmd))
    os.system(cur_cmd)
    
if __name__=="__main__":

    parser = argparse.ArgumentParser(
                prog = '{}'.format(__file__),
                description = 'Convert url(s) or string(s) to 3D QR-code in `*.stl` format. User either provides file with new-line-separated urls/string, or a single url/string as an argument (see bellow).',
                epilog = 'See https://github.com/kubikji2 for more silly projects.')

    # adding file_path
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-p','--path2urls',  help="path to file with new-line-separated urls or strings.")
    group.add_argument('-u', '--url', help= "url or a string to be converted")
    
    # OpenSCAD arguments
    # TODO add those

    # handle the parse error   
    try:
        args = parser.parse_args()
    except SystemExit as err:
        if err.code == 2:
            print("'-> For more info see: {} -h.".format(__file__),file=sys.stderr)
        sys.exit(-1)
       
    # unify the strings to be converted
    urls = load_urls(args.path2urls) if args.url is None else [args.url]
    for url in urls:
        process_url(url)
    
    """
    # testing on Rick Roll
    URL = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ/'
    process_url(URL)
    """
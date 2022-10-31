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

def process_url(url, px_a=None, px_t=None, bs_t=None, qr_o=None):

    # Oh great Python, please forgive me this mess:
    openscad_param_names = ['px_a', 'px_t', 'bs_t', 'qr_o']
    openscad_params = [px_a, px_t, bs_t, qr_o]
    l = len(openscad_params)
    additional_params_str = " ".join(["-D {}={}".format(openscad_param_names[i],openscad_params[i]) for i in range(l) if not openscad_params[i] is None])
    print(additional_params_str)
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
    scad_cmd = "openscad -o stls/{}-{}.stl qr2stl-wrapper.scad -D is_qr={} {}".format(fn_base,"{}","{}", additional_params_str)
    
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
    group.add_argument('-u', '--url', help= "url or a string to be converted.")
    
    # OpenSCAD model arguments
    parser.add_argument('-px_a', '--pixel_size', help="size of the QR-code pixels in mm.", type=float)
    parser.add_argument('-px_t', '--pixel_thickness', help="thickness of the QR-code (pixels) in mm.", type=float)
    parser.add_argument('-bs_t', '--base_thickness', help="total thickness of the model in mm (including the `px_t`).", type=float)
    parser.add_argument('-qr_o', '--qr_code_offset', help="QR code offset (~ base corner radius) in mm.", type=float)
    parser.add_argument('-lh', '--layer_height', help="layer height presets in mm, overrides `ps_t` and `bs_t`", choices=['0.2', '0.3'])

    # handle the parse error   
    try:
        args = parser.parse_args()
    except SystemExit as err:
        if err.code == 2:
            print("'-> For more info see: {} -h.".format(__file__),file=sys.stderr)
        sys.exit(-1)
    
    # managing layer height present
    if not args.layer_height is None:
        if args.base_thickness or args.pixel_thickness:
            print("WARNING: `layer_height` present overrides `pixel_thickness` and `base_thickness`.",file=sys.stderr)
        args.pixel_thickness = float(args.layer_height)
        args.base_thickness = 0.2 + 0.6 + float(args.layer_height)

    # unify the strings to be converted
    urls = load_urls(args.path2urls) if args.url is None else [args.url]
    for url in urls:
        process_url(url, px_a=args.pixel_size, px_t=args.pixel_thickness, bs_t=args.base_thickness, qr_o=args.qr_code_offset)
    
    """
    # testing on Rick Roll
    URL = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ/'
    process_url(URL)
    """
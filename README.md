# Link-QR-STL

This repository is used for creating QR codes from URL links representing them as OpenSCAD arrays to create `stl` models using [Q++ OpenSCAD library](https://github.com/kubikji2/qpp-openscad-library).

## ROADMAP

- [x] link -> QR (Python part) realized in `url2qr.py`
  - [x] find lib for QR in python [qrcode](https://pypi.org/project/qrcode/)
  - [x] create QR code and save it as a list of lists in OpenSCAD
  - [ ] add argument parsing, so it can be run independently
- [x] QR -> stl (OpenSCAD part) realized in `qr2stl-src.scad` and `qr2stl-wrapper.scad`
  - [x] setup variables for customizing the QR-code models
  - [ ] make local variable part of module arguments
  - [ ] setup global variable in the `qr2stl-wrapper.stl`, so they can be customized through Python script
- [ ] link list -> QR stls (Python or bash part) realized in `urls2stls.py`
  - python script with customizable settings running `qr2stl-wrapper.stl`
  - IDEA:
    - For each link, create QR-code and save it to separate file using 
    - For each QR code, create symlink using the shell command in python and run the OpenSCAD with `-o` flag to automatically create the `stl` file. 
  - [ ] Load list of lists and include previous scripts
  - [ ] Propagate python settings into the scad.
- [ ] installation scripts
  - [ ] `requirements.txt`
  - [ ] OpenSCAD installation
  - [ ] Git submodule setup

# Link-QR-STL

This repository is used for creating QR codes from URL links representing them as [OpenSCAD](https://openscad.org/) arrays to create `stl` models using [Q++ OpenSCAD library](https://github.com/kubikji2/qpp-openscad-library).

## Installation (I am here to use it for a first time)

- It is assumed that `Python3` and `pip` are installed.

- For Ubuntu:
  - run: `./install.sh` it will setup submodules, `pip install` qrcode package and run install-script from [ubuntu-essentials-install repo](https://github.com/kubikji2/ubuntu-essentials-install) to install [OpenSCAD](https://openscad.org/)
- For other Linux distros:
  - run: `./install.sh` and pray. It should work since OpenSCAD is installed from [AppImage](https://appimage.org/), but I did not test it.
- For MacOS:
  - ???
- Windows:
  - GL&HF

## Usage (I am here to use)

- Two input options are possible:
  - run: `./urls2stls.py -p <path-to-txt-file>` to convert urls/strings on each line into separate qr-code
  - run: `./urls2stls.py -u <url-or-string-to-convert>` to convert single url/sting from terminal
- For more options run `./urls2stls.py -h`

- After successful execution, examine (TODO add a link to the separate repo?) for manufacturing tips out of the scope of this repository.

## How does it work (I am here to learn)

After running `./urls2stls.py`:

- The program arguments are processed using [argparse](https://docs.python.org/3/library/argparse.html) standard Python3 package
- Each url/string is: 
  - converted to QR-code using [qrcode](https://pypi.org/project/qrcode/) pip Python3 package
  - QR-code is converted from `Pil Image` ([see documentation](https://pillow.readthedocs.io/en/stable/reference/Image.html)) into a 2D array
  - the 2D array is saved (backed up) into `./qrs` directory in the format readable by OpenSCAD
  - then, the file is copied into master-file `./qrs/scad-qr`
  - the main OpenSCAD script (`qr2stl-wrapper.scad`) is executed twice with optional parameters overriding the default values within
    - the first run creates a base geometry with QR-code engraved into it and the second creates the QR-code itself.
- this process is repeated for each line of the text file

## ROADMAP (I want to come later)

- [ ] add argument parsing for `url2qr.py`, so it can be run independently 
  - [ ] possibly creates the option to export as `*.svg` or `*.png`


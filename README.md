# Link-QR-STL

This repository is used for creating QR codes from URL links representing them as [OpenSCAD](https://openscad.org/) arrays to create `stl` models using [Q++ OpenSCAD library](https://github.com/kubikji2/qpp-openscad-library).

## Installation (I am here to use it for the first time)

- It is assumed that `python3` and `pip` are installed.
  - Those can be installed from your favorite package manager such as `sudo apt install python3 python3-pip` for Ubuntu.

- For Ubuntu:
  - run: `./install.sh` it will setup submodules, `pip install` QRcode package and run install-script from [ubuntu-essentials-install repo](https://github.com/kubikji2/ubuntu-essentials-install) to install [OpenSCAD](https://openscad.org/)
- For other Linux distros:
  - run: `./install.sh` and pray. It should work since OpenSCAD is installed from [AppImage](https://appimage.org/), but I did not test it.
- For MacOS:
  - ???
- Windows:
  - GL&HF

## Usage (I am here to use)

- Two input options are possible:
  - run: `./urls2stls.py -p <path-to-txt-file>` to convert URLs/strings on each line into separate QRcode
  - run: `./urls2stls.py -u <url-or-string-to-convert>` to convert single URL/sting from terminal
- For more options run `./urls2stls.py -h`

- After successful execution, examine (TODO add a link to the separate repo?) for manufacturing tips out of the scope of this repository.

## How does it work (I am here to learn)

After running `./urls2stls.py`:

- The program arguments are processed using [argparse](https://docs.python.org/3/library/argparse.html) standard Python3 package for advanced argument parsing.
- Each URL/string is:
  - converted to QR-code using [QRcode](https://pypi.org/project/qrcode/) pip Python3 package
  - QR-code is transformed from `Pil Image` ([see documentation](https://pillow.readthedocs.io/en/stable/reference/Image.html)) into a binary 2D array
  - the 2D array is saved  into `./qrs` directory in the format readable by OpenSCAD
  - then, the file is copied into master-file `./qrs/qr.scad-qr`
  - the main OpenSCAD script (`qr2stl-wrapper.scad`) is executed twice with optional parameters overriding the default values
    - the first run creates a base geometry with QRcode engraved into it (white part) and the second creates the QRcode itself (black part).
- this process is repeated for each line of the text file

## What to do next (I want to print it)

Exported `*.stl` files can be printed in any multi-color 3D printer and the slicer of your choice.

However, QRcode `*.stl` files can also be printed using a SINGLE NOZZLE 3D printer using [Prusaslicer](https://www.prusa3d.com/page/prusaslicer_424/) and the following hack. Since PrusaSlicer allows modifying the 3D printer profiles, so you can easily trick PrusaSlicer to think that your 3D printer is in fact multi-color/multi-nozzle.

0. Install (*Configuration -> Configuration Wizzard ...*) and select your 3D printer. Turn on the *Expert mode*.
1. In the *Printer Settings* card, on the first page called *General*, locate the *Capabilities* tab and increase the number of extruders (at least 2).
2. On the second page called *Custom G-code*, locate *Tool change G-code* and insert the following line `M600 X10 Y15 Z55; Do filament change at X:10, Y:15, and Z:+55 from current`.
   - This g-code instruction interrupts the printing and ask user to manually change the filament. Then the printer continues the printing process with a new color.
   - NOTE: check whether your printer firmware support this instruction, since AFAIK it is only Marlin-flavor stuff. The printer flavor is shown on the *General* page in the *Firmware* tab.
3. OPTIONAL: save as a new profile and set extruder colors in the *Preview* tab on the page called *Extruder 1* and *Extruder 2* respectively.

In the `profiles` directory, there are exported *Printer Settings* for *Prusa i3 MK3S* and *Prusa MINI+* in a form of the configuration bundle with a physical printer. You are free to use them as is or to get inspiration from them. Select *File -> Import -> Import Config Bundle ...* to load configuration bundle profiles into the PrusaSlicer. 

## ROADMAP (I want to come later)

- [ ] add argument parsing for `url2qr.py`, so it can be run independently
  - [ ] possibly creates the option to export as `*.svg` or `*.png`

# Link-QR-STL

This repository is used for creating QR codes from URL links representing them as OpenSCAD arrays to create `stl` models.

## ROADMAP

- [x] link -> QR (python part)
  - [x] find lib for QR in python [qrcode](https://pypi.org/project/qrcode/)
  - [x] create QR code and save it as a list of lists in OpenSCAD
  - [ ] add more information about the QRs
- [x] QR -> stl (OpenSCAD part)
  - [x] setup variables for customizing the QR-code model
- [ ] link list -> QR stls
  - python script with customizable settings
  - IDEA:
    - For each link, create QR-code and save it to separate file
    - Create a single openscad file for execution. It contains:

      ```openscad
      include <cur.scad-qr>
      use<qr2stl.scad>
      qr_code(qr_arr);
      ```
    
    - For each QR code, create symlink using the shell command in python and run the OpenSCAD with `-o` flag to automatically create the `stl` file. 
  - [ ] Load list of lists and include previous scripts
  - [ ] OPTIONAL: propagate python settings into the stl.
- [ ] installation scripts
  - [ ] `requirements.txt`
  - [ ] OpenSCAD installation

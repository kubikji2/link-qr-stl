// include file with qr_arr 2D array
include <qrs/qr.scad-qr>
// use modules from the qr2stl scad
use <qr2stl-src.scad>

// create variables with default value, so it can be change from the terminal
// see: https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_OpenSCAD_in_a_command_line_environment
is_qr = false;  // -> is qr code (true) or base (false)
px_a = 1.2;     // -> QR code pixel xy dimensions
px_t = 0.3;     // -> QR-code (pixel) thickness
bs_t = 1.1;     // -> base total thickness including the QR-code grooving 
qr_o = 5;       // -> base corner radius ()

// create the geometry
qr_piece(qr_arr=qr_arr, is_qr=is_qr, px_a=px_a, px_t=px_t, bs_t=bs_t, qr_o=qr_o);

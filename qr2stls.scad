// include file with qr_arr 2D array
include <qrs/qr.scad-qr>
// use modules from the qr2stl scad
use <qr2stl.scad>

// create variable with default value, so it can be change from the terminal
// '-> see: https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_OpenSCAD_in_a_command_line_environment
is_qr = false;
// create the geometry
qr_piece(qr_arr=qr_arr,is_qr=is_qr);

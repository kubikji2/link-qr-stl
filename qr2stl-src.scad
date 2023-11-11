include <solidpp/solidpp.scad>

_eps = 0.001;


// module used to covert qr array to the physical model
module qr_code(qr_arr, is_qr, size=[1,1,1], off=0.01)
{
    x_size = len(qr_arr);
    y_size = len(qr_arr[0]);
    h = size[2];
    cube_size = [size[0]+2*off, size[1]+2*off, h];

    for(y=[0:y_size-1])
    {
        y_off = (y_size-y-1)*size[1] - off;
        for(x=[0:x_size-1])
        {
            x_off = x*size[0] - off;

            if (qr_arr[y][x] == 0)
            {
                translate([x_off,y_off,0])
                    color([0.2,0.2,0.2])
                        cube(cube_size);
            }
        }
    }
    
}


// module embeddint the qr array the the physical model including the base
module qr_piece(qr_arr, is_qr, px_a=1.2, px_t=0.3, bs_t=1.1, qr_o=5)
{
    _x = px_a*len(qr_arr) + 2*qr_o;
    _y = px_a*len(qr_arr[0])+ 2*qr_o;
    _size = [px_a, px_a, px_t + (is_qr ? 0 : _eps)];

    if(is_qr)
    {
        translate([qr_o, qr_o, bs_t])
            qr_code(qr_arr = qr_arr, size=_size, is_qr = is_qr, off=_eps);
    }
    else
    {  
        difference()
        {
            mod_list = [round_edges(qr_o)];
            cubepp([_x, _y, bs_t+px_t], mod_list=mod_list);

            translate([qr_o, qr_o, bs_t])
                qr_code(qr_arr = qr_arr, size=_size, is_qr = is_qr);
        }
    }
    
}

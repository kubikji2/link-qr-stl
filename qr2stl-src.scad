include <qpp-openscad-library/qpp_all.scad>

module qr_code(arr, is_qr, size=[1,1,1], off=0.01)
{
    x_size = len(arr);
    y_size = len(arr[0]);
    h = size[2];
    cube_size = [size[0]+2*off, size[1]+2*off, h];

    for(y=[0:y_size-1])
    {
        y_off = (y_size-y-1)*size[1] - off;
        for(x=[0:x_size-1])
        {
            x_off = x*size[0] - off;

            if (arr[y][x] == 0)
            {
                translate([x_off,y_off,0])
                    color([0.2,0.2,0.2])
                        cube(cube_size);
            }
        }
    }
    
}

module qr_piece(qr_arr, is_qr, px_a=1.2, px_t=0.3, bs_t=1.1, qr_o=5)
{
    _x = px_a*len(qr_arr) + 2*qr_o;
    _y = px_a*len(qr_arr[0])+ 2*qr_o;
    _size = [px_a, px_a, px_t + (is_qr ? 0 : qpp_eps)];

    if(is_qr)
    {
        translate([qr_o, qr_o, bs_t])
            qr_code(arr = qr_arr, size=_size, is_qr = is_qr, off=qpp_eps);
    }
    else
    {  
        difference()
        {
            qpp_cylindrocube([_x, _y, bs_t+px_t,qr_o]);
            translate([qr_o, qr_o, bs_t])
                qr_code(arr = qr_arr, size=_size, is_qr = is_qr);
        }
    }
    
}

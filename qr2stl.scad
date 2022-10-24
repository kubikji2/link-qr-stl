include <qrs/test.scad-qr>

module qr_code(arr, size=[1,1,1], off=0.01)
{
    x_size = len(arr);
    y_size = len(arr[0]);
    cube_size = [size[0]+2*off, size[1]+2*off, size[2]];
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

qr_code(test_arr);
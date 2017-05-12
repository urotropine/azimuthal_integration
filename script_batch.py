import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
import sys

for i in ['_529', 'I_626']:


    input_filename1 = "sampleXXII" + i + '_000.img'
    input_filename2 = "emptrycelll_405_000.img" 
    shape = (4096, 4096)
    dtype = np.dtype('u2')

    fid1 = open(input_filename1, 'rb')
    fid2 = open(input_filename2, 'rb')
    data1 = np.fromfile(fid1, dtype)
    data2 = np.fromfile(fid2, dtype)
    data = data1- data2
    data = data[256:] 
    gr_x = np.arange(0,4096)
    x = np.repeat(gr_x, 4096)
    gr_y = np.arange(0,4096)
    y = np.tile(gr_y, 4096)
    z = data

    image = data.reshape(shape)

    file_name = i + '.txt'
    sys.stdout = open(file_name, 'w')

    center_x = 2024
    center_y = 2984
    R1 = 1752
    R2 = 1802
    num = 6
    step = np.pi/num

    angle = np.arange(0, step+np.pi, step)
    for phi in angle:
    
        yi = np.linspace((center_x + R1 * np.cos(phi)),(center_x + R2 * np.cos(phi)),250)
        xi = np.linspace((center_y - R1 * np.sin(phi)),(center_y - R2 * np.sin(phi)),250)
        zi = griddata((x, y), z, (xi, yi), method = 'nearest')
        integral = np.sum(zi)
  
        print phi, integral

    sys.stdout.close()

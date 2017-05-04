import numpy as np
import matplotlib.pyplot as plt

def func(x, y):
    return x * (1 - x) * np.cos(4 * np.pi * x) * np.sin(4 * np.pi * y ** 2) ** 2

#grid_x, grid_y = np.mgrid[0:1:100j, 0:1:200j]
gr_x = np.linspace(0,1,100)
grid_x = np.repeat(gr_x, 200)
gr_y = np.linspace(0,1,200)
grid_y = np.tile(gr_y, 100)
value_grid = func(grid_x[:], grid_y[:])
#100*200 dots, with corresponding value
#repeat: abcd -> aabbccdd
#tile: abcd -> abcdabcd

#print len(value_grid)
#print len((grid_x, grid_y))

line_x = np.linspace(0, 1,40)
line_y = np.linspace(0.55,0.65,40)
#value_line = func(line_x[:], line_y[:]) 
#40 dots, with 40 corresponding values. 

from scipy.interpolate import griddata
#grid_z0 = griddata(points, value, (grid_x, grid_y), method= 'cubic')
line_z0 = griddata((grid_x, grid_y), value_grid, (line_x, line_y), method = 'cubic')

grid_x = grid_x.reshape(100,200)
grid_y = grid_y.reshape(100,200)

plt.subplot(121)  #1*2 subplot, the first one
plt.imshow(func(grid_x, grid_y).T, extent=(0,1,0,1), origin='lower')
#plt.plot(points[:,0], points[:,1], 'k.', ms=2)
plt.plot(line_x[:], line_y[:], 'o', ms = 2)
plt.title('original')

plt.subplot(122)
plt.plot(line_x, line_z0, '--', ms = 2)

#plt.subplot(122)  #1*2, the second one
#plt.imshow(grid_z0.T, extent = (0,1,0,1), origin = 'lower')
#plt.title('cubic')
plt.show()

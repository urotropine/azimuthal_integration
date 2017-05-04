import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
import sys

input_filename1 = "sampleXXIII_626_000.img"
input_filename2 = "emptrycelll_405_000.img" 
shape = (4096, 4096)
dtype = np.dtype('>u2')

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

sys.stdout = open('name_output.txt', 'w')

center_x =
center_y = 
R1 =
R2 =

angle = np.arange(0, np.pi/2, np.pi/180)
for phi in angle:
    
    xi = np.linspace((center_x + R1 * np.cos(phi)),(center_x + R2 * np.cos(phi)),500)
    yi = np.linspace((center_y + R1 * np.cos(phi)),(center_y + R2 * np.cos(phi)),500)
    zi = griddata((x, y), z, (xi, yi), method = 'nearest')
    integral = np.sum(zi)
  
    print phi, integral
    
sys.stdout.close()
'''
plt.subplot(211)
plt.imshow(image, cmap = "gray")
plt.plot(xi, yi, '-', ms = 2)
#plt.figure(figsize=(8,8))

plt.subplot(212)
plt.plot(xi, zi, '--', ms = 2)
plt.xlim(0,4096)
plt.figure(figsize=(15,5))
plt.show()
'''

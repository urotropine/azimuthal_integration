import matplotlib.pyplot as plt
import numpy as np

input_filename1 = "sampleXXIII_626_000.img"
input_filename2 = "emptrycelll_405_000.img" 
shape = (4096, 4096)
dtype = np.dtype('>u2')
#output_filename1 = "sampleXXIII_626_000.img"
#output_filename2 = "emptrycelll_405_000.img"

fid1 = open(input_filename1, 'rb')
fid2 = open(input_filename2, 'rb')
data1 = np.fromfile(fid1, dtype)
data2 = np.fromfile(fid2, dtype)
data = data1- data2
data = data[256:] 
#print(len(data))
image = data.reshape(shape)

plt.imshow(image, cmap = "gray")
#plt.savefig(output_filename)
plt.show()


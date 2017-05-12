import matplotlib.pyplot as plt
import numpy as np

input_filename = "sampleXXIII_626_000.img"
shape = (4096, 4096)
dtype = np.dtype('u2')
output_filename = "sampleXXIII_626_000.img"

fid = open(input_filename, 'rb')
data = np.fromfile(fid, dtype)
data = data[256:]
#print(len(data))
image = data.reshape(shape)

plt.imshow(image, cmap = "flag")
#plt.savefig(output_filename)
plt.show()


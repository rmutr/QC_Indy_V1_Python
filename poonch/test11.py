import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = mpimg.imread('LISA.png')
plt.subplot(1, 2, 1)
plt.imshow(image)

plt.subplot(1, 2, 2)
#plt.imshow(negative)
plt.show()
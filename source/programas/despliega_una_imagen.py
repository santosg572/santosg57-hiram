import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import funciones_imagenes as fun

img = fun.LeeIMG(13)

plt.imshow(img, cmap='gray')
plt.show()




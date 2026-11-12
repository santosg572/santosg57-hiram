import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import funciones_imagenes as fun

img = fun.LeeIMG(13)

imgn = img[350:, 700:]
plt.imshow(imgn, cmap='gray')
plt.show()




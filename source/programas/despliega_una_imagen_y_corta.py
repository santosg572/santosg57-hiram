import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import funciones_imagenes as fun

def Img_recortada(num=0):
   img = fun.LeeIMG(num)
   imgn = img[350:, 700:]
   return imgn

img = Img_recortada(20)

plt.imshow(img, cmap='gray')
plt.show()




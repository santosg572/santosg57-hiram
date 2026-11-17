import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

import funciones_imagenes as fun

def Img_recortada(num=0):
   img = fun.LeeIMG(num)
   imgn = img[350:, 700:]
   return imgn

img1 = Img_recortada(20)
img2 = Img_recortada(21)

ss = img1.shape

x1 = np.reshape(img1, ss[1]*ss[1])
print(ss)

'''
plt.imshow(img, cmap='gray')
plt.show()
'''



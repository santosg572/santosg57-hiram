import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

import funciones_imagenes as fun

def Filtro_Media(img=0):
  ss = img.shape
  print(ss)

  imgn = np.zeros(ss)

  for i in range(1,ss[0]-1):  
    for j in range(1,ss[1]-1):
      imgt = img[(i-1):(i+2), (j-1):(j+2)]
      res = np.mean(imgt)
      imgn[i,j] = res
  return imgn

def Filtro_Mediana(img=0):
  ss = img.shape
  print(ss)

  imgn = np.zeros(ss)

  for i in range(1,ss[0]-1):
    for j in range(1,ss[1]-1):
      imgt = img[(i-1):(i+2), (j-1):(j+2)]
      res = np.median(imgt)
      imgn[i,j] = res
  return imgn


#img = fun.LeeIMG(13)

#ss = img.shape
#print(ss)

#imgn = Filtro_Media(img)

#plt.imshow(imgn, cmap='gray')
#plt.show()




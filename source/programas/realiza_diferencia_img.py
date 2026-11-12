import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

import funciones_imagenes as fun
import Filtro_media as fmedia	

def Recorta_IMG(img=0):
  imgn = img[350:, 700:]
  return imgn

def Encuentra_matriz_Diferencia_IMG(img1 = 0, img2 = 0):
  imgc1 = fmedia.Filtro_Mediana(img1)
  imgc2 = fmedia.Filtro_Mediana(img2)
  
  imgd = np.abs(imgc1-imgc2)
  
  return imgd



def Encuentra_vector_Diferencia_IMG(img1 = 0, img2 = 0):
  imgc1 = fmedia.Filtro_Mediana(img1)
  imgc2 = fmedia.Filtro_Mediana(img2)

  imgd = imgc1-imgc2

  ss = imgd.shape

  dd = imgd.reshape(ss[0]*ss[1])
  dd = np.abs(dd)
  print(len(dd))

  #xm = np.mean(dd)
  #xm = np.max(dd)
  return dd

img1 = fun.LeeIMG(13)   
img2 = fun.LeeIMG(14)
img1 = Recorta_IMG(img1)
img2 = Recorta_IMG(img2)  

imgsif =

'''
dd =  Encuentra_vector_Diferencia_IMG(img1, img2)

xm = .9*np.max(dd)
ss = img1.shape

  
#i1 = 80000
i1 = 0
#i2 = 100000
i2 = ss[0]*ss[1]

x = np.linspace(0, i2-i1, num=i2-i1)
print(len(x))
y = dd[i1:i2]
print(len(y))

y2 = xm * np.ones(i2-i1)
print(len(y2))

plt.plot(x, y)
plt.plot(x, y2, 'r')

plt.show()
'''
#plt.imshow(imgn, cmap='gray')
#plt.show()




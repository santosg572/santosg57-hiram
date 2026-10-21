import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def corta_imagen(img=0, i1=0, i2=0, j1=0, j2=0):
  ''' hola como estas
   yo estoy bien
   --------------------------
  '''

  imgn = img[i1:i2, j1:j2]
  return imgn

def ConvierteIMG_una(img=0):
  imgn = img[:, :, 0]
  return imgn   

def despliega_img(imgB=''):
#  plt.ion()
  plt.imshow(imgB, cmap='gray')
#  plt.title(ns)
  #plt.axis("off")  # Oculta los ejes
#  plt.ioff()
  plt.show()

def LeeIMG_nombre(file=''):
    img = mpimg.imread(file)
    return img

def LeeIMG(n=0):
  print('549 imagenes')
  min = 15
  seg = 34
   
  print('tiempo inicial MIN, SEG: ' + str(min), ' : ', str(seg))

  if n < 10:
    ns = '00' + str(n+1)
  elif n < 100:
    ns = '0' + str(n+1)
  else:
    ns = str(n)

  file = "./imagenes/"+ "output_00" + ns + '.jpg'
  print(file)
  img = mpimg.imread(file)
  return img[:,:,0].copy()

def LeeIMG_corta(n):
  img = LeeIMG(n)
  img = corta_imagen(400, 700, 700, 1200, img)
  return img

def Une_2_imagenes_Vertical(img1=0, img2=0):
  ss1 = img1.shape
  ss2 = img2.shape

  ny = ss1[1]
  if ny < ss2[1]:
    ny = ss2[1]
  
  nx = ss1[0]+ss2[0]

  img = np.zeros((nx, ny))

  img[1:(ss1[0]+1), :] = img1
  img[(ss1[0]+1+1):(ss2[0]+2), :] = img2

  return img


import cv2
import numpy as np
import pylab as pl

pat = '../Hiram_datos/IMG_1952'

file = 'fotograma_0'

ni = 507

img = None

i1 = 250
i2 = 840
j1 = 310
j2 = 1900

filo = 'imgo_'

for i in range(390,ni):
    print(i)
    if i < 10:
      ss = '00'+str(i)
    elif i < 100:
      ss = '0'+str(i)
    else:
      ss = str(i)
    ff = pat+ '/' + file+ ss +'.png'
    im=pl.imread(ff)
    im[i1:(i1+2), :,0] = 0
    im[i2:(i2+2), :,0] = 0
    im[:, j1:(j1+2), 0] = 0
    im[:, j2:(j2+2), 0] = 0

    if img is None:
        img = pl.imshow(im)
        imgn = im[i1:i2, j1:j2,0]
        cv2.imwrite('ddddd' + '.jpg', imgn)
    else:
        img.set_data(im)
    pl.pause(.1)
    pl.draw()




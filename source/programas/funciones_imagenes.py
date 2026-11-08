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
  '''
  Lee una imagen donde:
  
  n - es el numero de archivos jpg que se va a leer
      n puede tomar valores de 1 a 27452
  |
  '''

  pat = '../../../temporal/'

  if n < 10:
    ns = '0000' + str(n)
  elif n < 100:
    ns = '000' + str(n)
  elif n < 1000:
    ns = '00' + str(n)
  elif n < 10000:
    ns = '0' + str(n)
  else:
    ns = str(n)

  file = pat + "output_" + ns + '.jpg'
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



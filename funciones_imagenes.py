import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def corta_imagen(i1=0, i2=0, j1=0, j2=0, img=0):
  imgn = img[i1:i2, j1:j2]
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



import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def despliega_img(file=''):
  img = mpimg.imread(file)
  i1 = 400
  i2 = 700
  j1 = 700
  j2 = 1200

  ii1 = 1
  ii2 = 50 
  jj1 = 200
  jj2 = 500

  imgB = np.zeros((i2-i1+ii2-ii1+2, j2-j1+jj2-jj1+2))

  img1 = img[ii1:ii2, jj1:jj2]
  img2 = img[i1:i2, j1:j2]

  imgB[1:(ii2-ii1+1),1:(jj2-jj1+1)] = img1[:,:,0]
  imgB[(ii2-ii1+2):(ii2-ii1+2)+(i2-i1)+1, (jj2-jj1+2):(jj2-jj1+2)+(j2-j1)+1] = img2[:,:,0]

  print(img.shape)

  plt.ion()
  plt.imshow(imgB)
  plt.title(ns)
  #plt.axis("off")  # Oculta los ejes
  plt.ioff()
#  plt.show()


print('549 imagenes')

min = 15
seg = 34

print('tiempo inicial: ' + str(seg))

while 1:
  print('en que tiempo deseas ver la imagen [0 - para terminar] :')

  n = int(input())

  if n > 0:
    if n < 10:
      ns = '00' + str(n+1)
    elif n < 100:
      ns = '0' + str(n+1)
    else:
      ns = str(n)

    file = "./imagenes/"+ "output_00" + ns + '.jpg'
 
    despliega_img(file)
  else:
    break

programas
=========

**crea_imagen_total.py**

.. code:: Python

   import numpy as np

   import funciones_imagenes as fun

   print(dir(fun))

   imgs = list()

   for i in range(25,37):
     img = fun.LeeIMG_nombre('cambios_detectados_'+ str(i) + '.jpg')
     imgs.append(img)

   ss = imgs[0].shape

   imgn = np.zeros((3*ss[0], 4*ss[1]))

   imgn[0:ss[0], 0:ss[1]] = imgs[0]
   imgn[0:ss[0], ss[1]:2*ss[1]] = imgs[1]
   imgn[0:ss[0], 2*ss[1]:3*ss[1]] = imgs[2]
   imgn[0:ss[0], 3*ss[1]:4*ss[1]] = imgs[3]

   imgn[ss[0]:2*ss[0], 0:ss[1]] = imgs[4]
   imgn[ss[0]:2*ss[0], ss[1]:2*ss[1]] = imgs[5]
   imgn[ss[0]:2*ss[0], 2*ss[1]:3*ss[1]] = imgs[6]
   imgn[ss[0]:2*ss[0], 3*ss[1]:4*ss[1]] = imgs[7]

   imgn[2*ss[0]:3*ss[0], 0:ss[1]] = imgs[4]
   imgn[2*ss[0]:3*ss[0], ss[1]:2*ss[1]] = imgs[5]
   imgn[2*ss[0]:3*ss[0], 2*ss[1]:3*ss[1]] = imgs[6]
   imgn[2*ss[0]:3*ss[0], 3*ss[1]:4*ss[1]] = imgs[7]


   fun.despliega_img(imgn)

**despliega_dos_imagen_y_corta_analiza.py**

.. code:: Python

   import numpy as np
   import matplotlib.pyplot as plt
   import matplotlib.image as mpimg

   def corta_imagen(i1=0, j1=0, img=0):
     i2 = 700 
     j2 = 1200
  
     ii1 = 1  
     ii2 = 50 
     jj1 = 200
     jj2 = 500
  
     imgB = np.zeros((i2-i1+ii2-ii1+2, j2-j1+jj2-jj1+2))
  
     img1 = img[ii1:ii2, jj1:jj2]
     img2 = img[i1:i2, j1:j2]
  
     imgB[1:(ii2-ii1+1),1:(jj2-jj1+1)] = img1
     imgB[(ii2-ii1+2):(ii2-ii1+2)+(i2-i1)+1, (jj2-jj1+2):(jj2-jj1+2)+(j2-j1)+1] = img2
     return imgB

   def despliega_imgN(imgB=''):
   #  plt.ion()
     plt.imshow(imgB, cmap='gray')
   #  plt.title(ns)
     #plt.axis("off")  # Oculta los ejes
   #  plt.ioff()
     plt.show()


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
   #  plt.title(ns)
     #plt.axis("off")  # Oculta los ejes
     plt.ioff()
   #  plt.show()


   print('549 imagenes')

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
     return img[:,:,0]

   img1 = LeeIMG(5)
   img1 = corta_imagen(400, 700, img1)

   img2 = LeeIMG(6)
   img2 = corta_imagen(400, 700, img2)

   ss = img1.shape

   i1 = ss[0]
   j1 = ss[1]

   imgn = np.zeros((2*i1+1, j1))
   imgn[1:(i1+1),:] = img1

   imgn[(i1+1):(i1+1+i1),:] = img2

   despliega_imgN(imgn)


**despliega_imagenes.py**



despliega_serie_imagenes.py
despliega_una_imagen.py
despliega_una_imagen_y_corta.py
existe_diferencia_01.py
funciones_imagenes.py
lee_image_corta_salva.py
porcentaje_de_similitud.py
porcentaje_de_similitud_2.py
programas.rst

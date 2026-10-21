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

.. code:: Python

   import matplotlib.pyplot as plt 
   import matplotlib.image as mpimg
   import time

   for i in range(1, 550):
     file = "output_00"
     if i < 10:  
       filen = file + "00" + str(i)
     elif i < 100:
       filen = file + "0" + str(i)
     else:
       filen = file + str(i)

     filen = "./imagenes/"+ filen + '.jpg'
     print(filen)
     img = mpimg.imread(filen)
     plt.imshow(img)
     plt.axis("off")  # Oculta los ejes
     plt.pause(1) 

**despliega_serie_imagenes.py**

.. code:: Python

   import numpy as np
   import pylab as pl

   pat = '../Hiram_datos/IMG_1952'

   file = 'fotograma_0'

   ni = 473

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
       else:
           img.set_data(im)
       pl.pause(.1)
       pl.draw()

**despliega_una_imagen.py**

.. code:: Python

   import cv2
   import matplotlib.pyplot as plt
   import matplotlib.image as mpimg

   import funciones_imagenes as fun

   def encuentra_diferencias_imagenes(img1=0, img2=0):
     diferencia = cv2.absdiff(img1, img2)

     # 2. Aplicar un umbral (Threshold) para binarizar los cambios importantes

     _, umbral = cv2.threshold(diferencia, 30, 255, cv2.THRESH_BINARY)

     # 3. Encontrar los contornos de las zonas que cambiaron

     contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

     # 4. Dibujar rectángulos sobre la imagen original donde se detectó cambio

     img_resultado = img1 #cv2.imread('imagen2.jpg')

     for c in contornos:
         if cv2.contourArea(c) > 500: # Filtrar ruido pequeño
             x, y, w, h = cv2.boundingRect(c)
             cv2.rectangle(img_resultado, (x, y), (x + w, y + h), (0, 0, 255), 2)
     return img_resultado

   print(dir(fun))

   for i in range(1,507):
     if i < 10:
       num = '00'+str(i)
     elif i < 100:
       num = '0'+str(i)
     else:
       num = str(i)
     file = 'output_0'
     file='temporal/' + file + num + '.jpg'

     fileon = 'cortadas_'
     fileon = 'temporal_cortadas/' + fileon + num + '.jpg'

     img = fun.LeeIMG_nombre(file)
     img = fun.ConvierteIMG_una(img)
     img = fun.corta_imagen(img, 50, 780, 500, 1750)
     cv2.imwrite(fileon, img)
     #fun.despliega_img(img)

   '''
   img1 = fun.LeeIMG_corta(13)

   file = 'cambios_detectados_'

   # 14,26
   # 26,38

   for i in range(24, 38):
     img2 = fun.LeeIMG_corta(i)
     img_resul = encuentra_diferencias_imagenes(img1, img2)
     cv2.imwrite(file+str(i-1)+'.jpg', img_resul)
     img1 = img2.copy()

   '''

**despliega_una_imagen_y_corta.py**

.. code:: Python

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

**existe_diferencia_01.py**

.. code:: Python

   from PIL import Image, ImageChops

   pat = 'temporal'
   file1 = 'output_0001.jpg'
   file2 = 'output_0001.jpg'


   # Cargar las dos imágenes JPG
   img1 = Image.open(pat + '/' + file1)
   img2 = Image.open(pat + '/' + file2)

   # Calcular la diferencia absoluta entre los píxeles
   diff = ImageChops.difference(img1, img2)

   # Comprobar si hay diferencias
   if diff.getbbox():
       print('Las imágenes son diferentes.')
       diff.show()  # Muestra la imagen resultante con los cambios
   else:
       print('Las imágenes son exactamente iguales.')

**funciones_imagenes.py**

.. code:: Python

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

**lee_image_corta_salva.py**

.. code:: Python

   # importing required libraries
   import matplotlib.pyplot as plt
   import matplotlib.image as img

   def lee_img_corta_salva(file='', fileout='', i1=0, i2=0, j1=0, j2=0):
     testImage = img.imread(file)

     im = testImage.copy()

     im = im[i1:i2, j1:j2]

     plt.imsave(fileout + '.jpg', im)


   pat = '../Hiram_datos/IMG_1952'

   i1 = 250
   i2 = 840
   j1 = 310
   j2 = 1900

   ni = 473

   file = 'fotograma_0'
   filo = 'xxxx_'

   for i in range(390,ni):
       print(i)
       if i < 10:
         ss = '00'+str(i)
       elif i < 100:
         ss = '0'+str(i)
       else:
         ss = str(i)
       ff = pat+ '/' + file+ ss +'.png'
       fileo = filo + ss 
       lee_img_corta_salva(ff, fileo, i1, i2, j1, j2)


   # displaying the image
   #plt.imshow(img)

   #plt.show()

**porcentaje_de_similitud.py**

.. code:: Python

   import cv2
   import matplotlib.pyplot as plt
   from skimage.metrics import structural_similarity as ssim

   # 1. Cargar las imágenes en escala de grises (SSIM lo requiere así)

   pat = 'temporal'
   file1 = 'output_0001.jpg'
   file2 = 'output_0002.jpg'

   img1 = cv2.imread(pat + '/' +  file1, cv2.IMREAD_GRAYSCALE)
   img2 = cv2.imread(pat + '/' +  file1, cv2.IMREAD_GRAYSCALE)

   # NOTA: Ambas imágenes deben tener exactamente las mismas dimensiones (Ancho x Alto)
   if img1.shape != img2.shape:
       # Si no miden lo mismo, redimensionamos la segunda imagen al tamaño de la primera
       img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

   # 2. Calcular SSIM (el argumento 'full=True' nos devuelve la imagen con las diferencias)
   score, diff = ssim(img1, img2, full=True)

   # El score va de -1 a 1, donde 1 significa que son idénticas
   porcentaje_similitud = score * 100
   print(f"Similitud entre imágenes: {porcentaje_similitud:.2f}%")

   # 3. Procesar la imagen de diferencia para resaltar los cambios
   # 'diff' está en formato float de 0 a 1; lo convertimos a un rango de 0 a 255 (entero)
   diff = (diff * 255).astype("uint8")

   # Aplicamos un umbral (threshold) para obtener una máscara blanca donde hay cambios
   _, thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

   # Encontrar los contornos de las zonas que cambiaron
   contornos, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

   # Cargar la imagen original a color para dibujar sobre ella los recuadros de diferencias
   img1_color = cv2.imread(pat + '/' +  file1)

   for c in contornos:
       # Filtrar ruidos pequeños (solo dibujar cajas si el área del cambio es significativa)
       if cv2.contourArea(c) > 20: 
           x, y, w, h = cv2.boundingRect(c)
           # Dibujar un rectángulo rojo alrededor de la diferencia
           cv2.rectangle(img1_color, (x, y), (x + w, y + h), (0, 0, 255), 2)

   # 4. Mostrar los resultados visualmente
   plt.figure(figsize=(10, 5))
   plt.subplot(1, 2, 1)
   plt.title(f"Similitud: {porcentaje_similitud:.2f}%")
   plt.imshow(cv2.cvtColor(img1_color, cv2.COLOR_BGR2RGB))
   plt.axis('off')

   plt.subplot(1, 2, 2)
   plt.title("Zonas con Cambios")
   plt.imshow(thresh, cmap='gray')
   plt.axis('off')

   plt.show()

**porcentaje_de_similitud_2.py**

.. code:: Python

   import cv2
   import matplotlib.pyplot as plt
   from skimage.metrics import structural_similarity as ssim

   # 1. Cargar las imágenes en escala de grises (SSIM lo requiere así)

   def similitud(file1='', file2=''):
     img1 = cv2.imread(pat + '/' +  file1, cv2.IMREAD_GRAYSCALE)
     img2 = cv2.imread(pat + '/' +  file2, cv2.IMREAD_GRAYSCALE)

     # NOTA: Ambas imágenes deben tener exactamente las mismas dimensiones (Ancho x Alto)
     if img1.shape != img2.shape:
       # Si no miden lo mismo, redimensionamos la segunda imagen al tamaño de la primera
       img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

     # 2. Calcular SSIM (el argumento 'full=True' nos devuelve la imagen con las diferencias)
     score, diff = ssim(img1, img2, full=True)

     # El score va de -1 a 1, donde 1 significa que son idénticas
     porcentaje_similitud = score * 100
     print(f"Similitud entre imágenes: {porcentaje_similitud:.2f}%")
     return diff

   pat = 'temporal'
   file1 = 'output_0001.jpg'
   file2 = 'output_0002.jpg'

   dd = similitud(file1, file2)

   def Grafica_diferencias(diff=''):
     # 3. Procesar la imagen de diferencia para resaltar los cambios
     # 'diff' está en formato float de 0 a 1; lo convertimos a un rango de 0 a 255 (entero)
     diff = (diff * 255).astype("uint8")

     # Aplicamos un umbral (threshold) para obtener una máscara blanca donde hay cambios
     _, thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

     # Encontrar los contornos de las zonas que cambiaron
     contornos, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

     # Cargar la imagen original a color para dibujar sobre ella los recuadros de diferencias
     img1_color = cv2.imread(pat + '/' +  file1)

     for c in contornos:
       # Filtrar ruidos pequeños (solo dibujar cajas si el área del cambio es significativa)
       if cv2.contourArea(c) > 20: 
           x, y, w, h = cv2.boundingRect(c)
           # Dibujar un rectángulo rojo alrededor de la diferencia
           cv2.rectangle(img1_color, (x, y), (x + w, y + h), (0, 0, 255), 2)

     # 4. Mostrar los resultados visualmente
     plt.figure(figsize=(10, 5))
     plt.subplot(1, 2, 1)
   #  plt.title(f"Similitud: {porcentaje_similitud:.2f}%")
     plt.imshow(cv2.cvtColor(img1_color, cv2.COLOR_BGR2RGB))
     plt.axis('off')

     plt.subplot(1, 2, 2)
     plt.title("Zonas con Cambios")
     plt.imshow(thresh, cmap='gray')
     plt.axis('off')

     plt.show()

   Grafica_diferencias(dd)


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




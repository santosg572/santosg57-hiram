import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import time

pat = '/Users/santosg/Hiram_datos/IMG_1952/'

prefijo = 'fotograma_0'

fig, ax = plt.subplots()
ax.axis('off')

for i in range(393,472):
  print(i)
  if i < 10:
    file = prefijo+'00'+str(i)+'.png'
  elif i < 100:
    file = prefijo+'0'+str(i)+'.png'
  else:
    file = prefijo+str(i)+'.png' 
  imgn = img.imread(pat+file)
  imgn = imgn[:,:,0]
  imgn = imgn[200:820,340:1900]
  fileo = prefijo+'O_'+str(i)+'.png'
  plt.imsave(fileo, imgn)
  ax.imshow(imgn, cmap='gray')
  plt.draw()       # Fuerza el redibujado de la figura
  plt.pause(1.0)   # Pausa el script por 1.0 segundos antes de la siguiente imagen
  ax.clear()       # Limpia el eje para evitar sobreponer imágenes

plt.close()





import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import time

pat = 'temporal/'

prefijo = 'fotograma_0O_'

fig, ax = plt.subplots()
ax.axis('off')

for i in range(393,472):
  print(i)
  file = prefijo+str(i)+'.png' 
  imgn = img.imread(pat+file)
  imgn = imgn[:,:,0]
  ax.imshow(imgn, cmap='gray')
  plt.draw()       # Fuerza el redibujado de la figura
  plt.pause(1.0)   # Pausa el script por 1.0 segundos antes de la siguiente imagen
  ax.clear()       # Limpia el eje para evitar sobreponer imágenes

plt.close()





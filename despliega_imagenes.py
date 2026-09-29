import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time

plt.ion()

file = 'output_00'
#file = file + '001'+'.jpg'

for i in range(1,550):
  if i < 10:
    filen = file + '00' + str(i) +'.jpg'
  elif i < 100:
    filen = file + '0' + str(i) +'.jpg'
  else:
    filen = file + str(i) +'.jpg'

  print(filen)

  img = plt.imread('./imagenes/'+filen)

  plt.imshow(img)
#  plt.axis('off') # Ocultar los ejes
#  plt.show()
  plt.show(block=False) # Mostrar sin bloquear el código    
  print('hola')
  time.sleep(2) # Pausa en segundos

  plt.close() # Cerrar la imagen actual para la siguiente




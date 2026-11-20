import numpy as np
import matplotlib.pyplot as plt

import funciones_imagenes as fun

k1 = 1
k2 = 60
del1 = 10

while k1+del1 < 27452:
  k2 = k1+del1
  img1 = fun.LeeIMG_corta(k1)
  img1 = fun.Filtro_Media(img1)

  img2 = fun.LeeIMG_corta(k2)
  img2 = fun.Filtro_Media(img2) 

  dif_img = img1-img2

  ss = dif_img.shape

  #print(ss)

  vec = np.abs(dif_img.reshape(ss[0]*ss[1]))

  min = np.min(vec)
  max = np.max(vec)

  #print('min, max: ' , min, max)
  umbral = .9*max

  suma = np.sum(vec > umbral)
  print(suma)

  #print('longitud del vector: ', len(vec))
  k1 = k1+del1

'''
plt.plot(vec)
plt.plot([0, len(vec)], [umbral, umbral])

plt.show()
'''

#fun.despliega_img(img)

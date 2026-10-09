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




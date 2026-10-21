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



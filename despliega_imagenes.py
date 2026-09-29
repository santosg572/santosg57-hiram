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

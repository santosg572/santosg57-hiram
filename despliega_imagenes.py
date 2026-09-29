import matplotlib.pyplot as plt
import matplotlib.image as mpimg

file = 'output_00'
#file = file + '001'+'.jpg'

fig, axes = plt.subplots(1, 549, figsize=(15, 5))

for i in range(1,550):
  if i < 10:
    filen = file + '00' + str(i) +'.jpg'
  elif i < 100:
    filen = file + '0' + str(i) +'.jpg'
  else:
    filen = file + str(i) +'.jpg'

  img = plt.imread(filen)

  axes[i].imshow(img)
  axes[i].set_title(str(i)) # Título opcional
  axes[i].axis('off')                     # Ocultar los ejes de coordenadas
  plt.tight_layout()
  plt.show()




import matplotlib.pyplot as plt
import matplotlib.image as mpimg

file = "./imagenes/"+ "output_00210.jpg"
img = mpimg.imread(file)
plt.imshow(img)
plt.axis("off")  # Oculta los ejes
plt.show()


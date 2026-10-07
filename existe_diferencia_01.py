from PIL import Image, ImageChops

pat = 'temporal'
file1 = 'output_0001.jpg'
file2 = 'output_0001.jpg'


# Cargar las dos imágenes JPG
img1 = Image.open(pat + '/' + file1)
img2 = Image.open(pat + '/' + file2)

# Calcular la diferencia absoluta entre los píxeles
diff = ImageChops.difference(img1, img2)

# Comprobar si hay diferencias
if diff.getbbox():
    print('Las imágenes son diferentes.')
    diff.show()  # Muestra la imagen resultante con los cambios
else:
    print('Las imágenes son exactamente iguales.')



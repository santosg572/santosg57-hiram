
import cv2
import os

# Ruta de la carpeta con la secuencia de imágenes

carpeta_imagenes = 'temporal'

archivos = sorted(os.listdir(carpeta_imagenes))

if len(archivos) < 2:
    print('Se necesitan al menos dos imágenes.')
    exit()

# Cargar la primera imagen como base
img1_path = os.path.join(carpeta_imagenes, archivos[0])
fondo_gris = cv2.cvtColor(cv2.imread(img1_path), cv2.COLOR_BGR2GRAY)
fondo_gris = cv2.GaussianBlur(fondo_gris, (21, 21), 0)

for i in range(1, len(archivos)):
    img_path = os.path.join(carpeta_imagenes, archivos[i])
    imagen = cv2.imread(img_path)
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    gris = cv2.GaussianBlur(gris, (21, 21), 0)

    # Calcular la diferencia absoluta entre el fondo y la imagen actual
    delta_frame = cv2.absdiff(fondo_gris, gris)
    _, umbral = cv2.threshold(delta_frame, 25, 255, cv2.THRESH_BINARY)
    umbral = cv2.dilate(umbral, None, iterations=2)

    # Encontrar contornos del movimiento
    contornos, _ = cv2.findContours(umbral.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#    print(contornos)

    print(f'Imagen {archivos[i]}: se encontraron {len(contornos)} zonas con movimiento.')

    # Opcional: actualizar el fondo o mantener el inicial
    fondo_gris = gris


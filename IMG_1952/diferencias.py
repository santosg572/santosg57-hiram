import cv2
from skimage.metrics import structural_similarity as ssim

# 1. Cargar las dos imágenes en escala de grises

pat = '/Users/santosg/Hiram_datos/IMG_1952/'
prefijo = 'fotograma_0'

i = 393
file1 = prefijo+str(i)+'.png'
file2 = prefijo+str(i+1)+'.png'

imagen1 = cv2.imread(pat+file1)
imagen2 = cv2.imread(pat+file2)

gris1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2GRAY)
gris2 = cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)

# 2. Calcular el SSIM (puntuación entre -1 y 1) y la imagen de diferencia
puntaje, diferencia = ssim(gris1, gris2, full=True)
print(f"Índice de Similitud Estructural (SSIM): {puntaje:.4f}")

# La diferencia está en valores de [0, 1], la convertimos a uint8 [0, 255]
diferencia = (diferencia * 255).astype("uint8")

# 3. Aplicar un umbral para destacar zonas con cambios significativos
_, umbral = cv2.threshold(diferencia, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

# 4. Encontrar contornos de las áreas diferentes
contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 5. Dibujar rectángulos alrededor de las diferencias en la imagen original
resultado = imagen1.copy()
for c in contornos:
  if cv2.contourArea(c) > 50:  # Filtrar ruido pequeño
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(resultado, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Mostrar o guardar la imagen resultante
cv2.imwrite("diferencias_detectadas.png", resultado)



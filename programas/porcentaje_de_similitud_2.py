import cv2
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

# 1. Cargar las imágenes en escala de grises (SSIM lo requiere así)

def similitud(file1='', file2=''):
  img1 = cv2.imread(pat + '/' +  file1, cv2.IMREAD_GRAYSCALE)
  img2 = cv2.imread(pat + '/' +  file2, cv2.IMREAD_GRAYSCALE)

  # NOTA: Ambas imágenes deben tener exactamente las mismas dimensiones (Ancho x Alto)
  if img1.shape != img2.shape:
    # Si no miden lo mismo, redimensionamos la segunda imagen al tamaño de la primera
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

  # 2. Calcular SSIM (el argumento 'full=True' nos devuelve la imagen con las diferencias)
  score, diff = ssim(img1, img2, full=True)

  # El score va de -1 a 1, donde 1 significa que son idénticas
  porcentaje_similitud = score * 100
  print(f"Similitud entre imágenes: {porcentaje_similitud:.2f}%")
  return diff

pat = 'temporal'
file1 = 'output_0001.jpg'
file2 = 'output_0002.jpg'

dd = similitud(file1, file2)

def Grafica_diferencias(diff=''):
  # 3. Procesar la imagen de diferencia para resaltar los cambios
  # 'diff' está en formato float de 0 a 1; lo convertimos a un rango de 0 a 255 (entero)
  diff = (diff * 255).astype("uint8")

  # Aplicamos un umbral (threshold) para obtener una máscara blanca donde hay cambios
  _, thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

  # Encontrar los contornos de las zonas que cambiaron
  contornos, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # Cargar la imagen original a color para dibujar sobre ella los recuadros de diferencias
  img1_color = cv2.imread(pat + '/' +  file1)

  for c in contornos:
    # Filtrar ruidos pequeños (solo dibujar cajas si el área del cambio es significativa)
    if cv2.contourArea(c) > 20: 
        x, y, w, h = cv2.boundingRect(c)
        # Dibujar un rectángulo rojo alrededor de la diferencia
        cv2.rectangle(img1_color, (x, y), (x + w, y + h), (0, 0, 255), 2)

  # 4. Mostrar los resultados visualmente
  plt.figure(figsize=(10, 5))
  plt.subplot(1, 2, 1)
#  plt.title(f"Similitud: {porcentaje_similitud:.2f}%")
  plt.imshow(cv2.cvtColor(img1_color, cv2.COLOR_BGR2RGB))
  plt.axis('off')

  plt.subplot(1, 2, 2)
  plt.title("Zonas con Cambios")
  plt.imshow(thresh, cmap='gray')
  plt.axis('off')

  plt.show()

Grafica_diferencias(dd)


import cv2
import numpy as np

# Inicializar la captura de video (0 para cámara web o ruta de un archivo de video)
cap = cv2.VideoCapture(0)

# Leer el primer fotograma como referencia

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
  # 1. Calcular la diferencia absoluta entre dos fotogramas consecutivos
  diff = cv2.absdiff(frame1, frame2)

  # 2. Convertir a escala de grises y aplicar un desenfoque para reducir ruido
  gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray, (5, 5), 0)

  # 3. Aplicar umbralización (binarización) para obtener zonas blancas de movimiento
  _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

  # 4. Dilatar la imagen umbralizada para rellenar huecos
  dilated = cv2.dilate(thresh, None, iterations=3)

  # 5. Encontrar los contornos del movimiento con cv2.findContours
  contours, _ = cv2.findContours(
      dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
  )

  # Crear una imagen negra del mismo tamaño para dibujar solo las zonas de movimiento
  zona_movimiento = np.zeros_like(frame1)

  for contour in contours:
    # Filtrar contornos pequeños por área (ejemplo: área menor a 500 píxeles se ignora)
    if cv2.contourArea(contour) < 500:
      continue

    # Dibujar el contorno o un rectángulo delimitador en la imagen de zonas
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.drawContours(zona_movimiento, [contour], -1, (0, 255, 0), thickness=cv2.FILLED)

  # Mostrar las ventanas de resultado
  cv2.imshow('Detección en Video', frame1)
  cv2.imshow('Zonas de Movimiento (Binario/Contornos)', zona_movimiento)

  # Actualizar los fotogramas
  frame1 = frame2
  ret, frame2 = cap.read()

  # Salir con la tecla 'ESC'
  if cv2.waitKey(10) & 0xFF == 27:
    break

cap.release()
cv2.destroyAllWindows()



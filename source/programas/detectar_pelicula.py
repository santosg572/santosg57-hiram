import cv2
from ultralytics import YOLO
#import pati

# 1. Cargar el modelo pre-entrenado de YOLO (yolov8n.yaml / yolov8n.pt es rápido y ligero)
model = YOLO("yolov8n.pt")

# 2. Ruta a tu archivo de video o película
video_path = 'pelicula_recortada_recuadro.mp4' # "ruta/a/tu/pelicula.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error al abrir el video. Verifica la ruta.")
    exit()

# 3. Procesar el video fotograma por fotograma
while cap.isOpened():
    success, frame = cap.read()

    if success:
        # Realizar la inferencia (detección de objetos) en el frame actual
        results = model(frame)

        # Dibujar los resultados (cajas y etiquetas) sobre el frame
        annotated_frame = results[0].plot()

        # Mostrar el fotograma resultante en una ventana
        cv2.imshow("Deteccion de Objetos - Pelicula", annotated_frame)

        # Presiona la tecla 'q' para salir antes de que termine el video
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()



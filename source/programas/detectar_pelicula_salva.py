import cv2
from ultralytics import YOLO

# 1. Cargar el modelo YOLO
model = YOLO("yolov8n.pt")

# 2. Configurar rutas de video
video_path = "pelicula_recortada_recuadro.mp4"
output_path = "pelicula_recortada_recuadro_procesada.mp4"  # Nombre del video guardado

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error al abrir el video original. Verifica la ruta.")
    exit()

# 3. Obtener propiedades del video original para el archivo de salida
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# 4. Configurar el guardado del video (Codec mp4v para formato .mp4)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(
    output_path, fourcc, fps, (frame_width, frame_height)
)

print("Procesando y guardando video... Presiona 'q' para detener.")

# 5. Bucle de procesamiento
while cap.isOpened():
    success, frame = cap.read()

    if success:
        # Detectar objetos en el fotograma actual
        results = model(frame)

        # Dibujar las cajas y etiquetas
        annotated_frame = results[0].plot()

        # Escribir el fotograma anotado en el nuevo archivo de video
        out.write(annotated_frame)

        # Mostrar en pantalla el progreso en tiempo real
        cv2.imshow("Guardando Detecciones", annotated_frame)

        # Salir si se presiona 'q'
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# 6. Liberar todos los recursos de manera correcta
cap.release()
out.release()
cv2.destroyAllWindows()
print(f"¡Proceso terminado! El video se guardó en: {output_path}")



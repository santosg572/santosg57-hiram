dame un programa en python para detectar objetos que estan en un movie
=====================================================================

Para detectar objetos en una película o video usando Python, la herramienta más rápida y potente actual es YOLO (en su 
versión YOLOv8 de Ultralytics) combinada con OpenCV para leer y mostrar los fotogramas del video.

**Requisitos previos**

Primero, instala las librerías necesarias en tu terminal:

.. code:: Bash

   pip install ultralytics opencv-python


**Código en Python**

Crea un archivo llamado **detectar_pelicula.py** y pega el siguiente código:

.. code:: Python

   import cv2
   from ultralytics import YOLO

   # 1. Cargar el modelo pre-entrenado de YOLO (yolov8n.yaml / yolov8n.pt es rápido y ligero)
   model = YOLO("yolov8n.pt")

   # 2. Ruta a tu archivo de video o película
   video_path = "ruta/a/tu/pelicula.mp4"
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


**Explicación rápida**

• YOLO("yolov8n.pt"): Descarga automáticamente un modelo liviano entrenado con el conjunto de datos COCO (capaz de detectar 80 clases comunes como personas, coches, sillas, teléfonos, etc.).

• cap.read(): Lee la película cuadro por cuadro.

• results[0].plot(): Dibuja automáticamente los recuadros (bounding boxes), la clase detectada y el porcentaje de confianza.

• cv2.imshow(): Abre una ventana de reproducción mostrando lo que la inteligencia artificial va detectando en tiempo real.

Puedes ver un ejemplo práctico de cómo se implementa y ejecuta este proceso usando YOLOv8 en Python:

**guardar el video procesado**

Para guardar el video procesado con las detecciones integradas, necesitamos añadir cv2.VideoWriter. Esta herramienta toma las 
dimensiones y los fotogramas por segundo (FPS) del video original para exportar el resultado con la misma velocidad y tamaño.

Aquí tienes el código actualizado:

.. code:: Python

   import cv2
   from ultralytics import YOLO

   # 1. Cargar el modelo YOLO
   model = YOLO("yolov8n.pt")

   # 2. Configurar rutas de video
   video_path = "ruta/a/tu/pelicula.mp4"
   output_path = "pelicula_procesada.mp4"  # Nombre del video guardado

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


**¿Qué cambió en esta versión?**

• cv2.VideoWriter: Configura un contenedor que escribe los fotogramas modificados en el disco duro.
• cap.get(...): Extrae automáticamente el ancho, alto y la velocidad (FPS) de tu video para que el archivo final no se vea acelerado, lento o deformado.
• out.write(annotated_frame): Guarda cuadro por cuadro la imagen ya dibujada por la inteligencia artificial antes de pasar al siguiente frame.

Si necesitas seguir refinando el script, cuéntame:

• ¿El video procesado se reproduce a la velocidad correcta o notas algún desfase?
• ¿Te gustaría ocultar las etiquetas de texto para dejar solo los recuadros de color y que se vea más limpio?




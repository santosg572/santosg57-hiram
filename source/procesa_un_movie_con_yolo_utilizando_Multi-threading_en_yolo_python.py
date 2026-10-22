procesa un movie con yolo utilizando Multi-threading en yolo python
====================================================================


Procesar un video utilizando Ultralytics YOLO con hilos (threading) en Python requiere una regla de oro fundamental: no 
compartas una misma instancia del modelo YOLO entre varios hilos. Debido al diseño de PyTorch y a las condiciones de carrera, 
cada hilo debe inicializar o poseer su propia instancia del modelo (o bien usar un mecanismo de bloqueo/mutex).
Para videos, la arquitectura más eficiente suele separar las tareas: un hilo/proceso lee los fotogramas (VideoCapture), y 
otros hilos procesan los lotes o fragmentos. Aquí tienes un ejemplo práctico usando threading y queue con Ultralytics YOLO:

Código de ejemplo con Multithreading y YOLO

.. code:: Python

   import queue
   import threading
   import cv2 
   from ultralytics import YOLO

   # Rutas de configuración
   VIDEO_PATH = 'ruta/al/video.mp4'
   OUTPUT_PATH = 'ruta/al/video_procesado.mp4'
   MODEL_PATH = 'yolov8n.pt'  # O tu modelo personalizado
   NUM_THREADS = 2

   # Colas para comunicación segura entre hilos
   frame_queue = queue.Queue(maxsize=30)
   result_queue = queue.Queue(maxsize=30)


   def worker_inferencia(worker_id):
     """
       Función que ejecuta cada hilo. 
       IMPORTANTE: Se instancia el modelo YOLO DENTRO del hilo para garantizar seguridad de hilos (thread-safety).
       """
     print(f'[Hilo {worker_id}] Cargando modelo YOLO...')
     model = YOLO(MODEL_PATH)

     while True:
       data = frame_queue.get()
       if data is None:  # Señal para terminar
         frame_queue.task_done()
         break

       frame_idx, frame = data

       # Realizar inferencia con la instancia local del hilo
       results = model(frame, verbose=False)
       annotated_frame = results[0].plot()
 
       result_queue.put((frame_idx, annotated_frame))
       frame_queue.task_done()

 
   def procesar_video_multihilo():
     cap = cv2.VideoCapture(VIDEO_PATH)
     if not cap.isOpened():
       print('Error al abrir el video.')
       return

     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
     fps = cap.get(cv2.CAP_PROP_FPS)
     total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

     out = cv2.VideoWriter(
         OUTPUT_PATH, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height)
     )

     # Iniciar los hilos de inferencia
     threads = []
     for i in range(NUM_THREADS):
       t = threading.Thread(target=worker_inferencia, args=(i,))
       t.daemon = True
       t.start()
       threads.append(t)

     # Hilo lector: lee el video y alimenta la cola
     frame_idx = 0
     read_thread_active = True

     # Bucle para enviar frames a la cola
     def lector_frames():
       nonlocal frame_idx, read_thread_active
       while True:
         ret, frame = cap.read()
         if not ret:
           break
         frame_queue.put((frame_idx, frame))
         frame_idx += 1
       read_thread_active = False

     t_lector = threading.Thread(target=lector_frames)
     t_lector.start()

     # Diccionario y contador para reordenar los frames si fuera necesario
     # (con threading simple los frames pueden salir desordenados)
     procesados = 0
     buffer_resultados = {}
     siguiente_a_escribir = 0

     t_lector.join()

     # Esperar a que la cola de entrada se vacíe
     frame_queue.join()

     # Detener los hilos de inferencia enviando None
     for _ in range(NUM_THREADS):
       frame_queue.put(None)

     for t in threads:
       t.join()

     # Recoger y ordenar resultados de la cola
     while not result_queue.empty():
       idx, ann_frame = result_queue.get()
       buffer_resultados[idx] = ann_frame

     # Escribir en orden en el archivo de salida
     for i in range(frame_idx):
       if i in buffer_resultados:
         out.write(buffer_resultados[i])

     cap.release()
     out.release()
     print('¡Procesamiento de video completado!')


   if __name__ == '__main__':
     procesar_video_multihilo()


Consulta más detalles sobre la ejecución segura en la Guía de Inferencia Segura para Subprocesos de Ultralytics o revisa las 
opciones para seguimiento en la documentación de Ultralytics YOLO para el seguimiento de objetos.

Visualiza una explicación comparativa entre multiprocessing y multithreading en Python para tareas pesadas como visión 
artificial:



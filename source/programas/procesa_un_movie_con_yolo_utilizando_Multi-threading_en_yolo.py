import queue
import threading
import cv2
from ultralytics import YOLO

# Rutas de configuración
VIDEO_PATH = 'pelicula_recortada_recuadro.mp4'
OUTPUT_PATH = 'pelicula_recortada_recuadro_procesada_2.mp4'
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


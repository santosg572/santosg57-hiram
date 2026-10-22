 recorta el recuadro de un video
================================

Para recortar el recuadro o los bordes negros (letterbox/pillarbox) de un video en Python, la herramienta más eficiente y 
utilizada es ffmpeg-python (o usar subprocess con FFmpeg de forma directa). También puedes hacerlo cuadro por cuadro con 
OpenCV, aunque es más lento para videos largos.

Aquí tienes las dos mejores opciones según lo que necesites:



**Opción 1: Usando FFmpeg (Recomendada - Rápida y sin pérdida de calidad)**

Esta es la mejor opción porque no decodifica y vuelve a codificar todo el video de forma pesada, sino que aplica un filtro 
directo.

Requisitos:

Primero, instala la librería en tu terminal:

.. code:: Bash

   pip install ffmpeg-python

.. code:: Python

   import ffmpeg

   def recortar_video(video_entrada, video_salida, x, y, ancho, alto):
       """
       x, y: Coordenadas de la esquina superior izquierda del recuadro que quieres conservar.
       ancho, alto: Dimensiones del recuadro que vas a recortar.
       """
       (
           ffmpeg
           .input(video_entrada)
           .crop(x, y, ancho, alto)
           .output(video_salida, vcodec='libx264', acodec='copy')
           .run(overwrite_output=True)
       )

   # Ejemplo de uso: Recortar un recuadro de 1280x720 empezando desde la coordenada (100, 50)
   recortar_video('mi_pelicula.mp4', 'pelicula_recortada.mp4', x=100, y=50, ancho=1280, alto=720)


**Opción 2: Usando OpenCV (Ideal si quieres analizar o procesar los fotogramas)**

Si necesitas procesar los cuadros uno a uno o automatizar el recorte detectando los bordes negros, OpenCV es una excelente 
opción.

Requisitos:

.. code:: Bash

   pip install opencv-python

.. code:: Python

   import cv2

   # 1. Cargar el video
   cap = cv2.VideoCapture('mi_pelicula.mp4')

   # 2. Definir las coordenadas del recuadro a recortar [y_min:y_max, x_min:x_max]
   # Ajusta estos números a las dimensiones de tu video
   x, y, ancho, alto = 100, 50, 1280, 720

   # 3. Configurar el archivo de salida
   fps = int(cap.get(cv2.CAP_PROP_FPS))
   fourcc = cv2.VideoWriter_fourcc(*'mp4v')
   out = cv2.VideoWriter('pelicula_recortada.mp4', fourcc, fps, (ancho, alto))

   while cap.isOpened():
       ret, frame = cap.read()
       if not ret:
           break
    
       # Recortar usando el indexado de matrices de NumPy [filas, columnas]
       recorte = frame[y:y+alto, x:x+ancho]
    
       # Guardar el cuadro recortado
       out.write(recorte)

   # Liberar recursos
   cap.release()
   out.release()
   cv2.destroyAllWindows()
   print("¡Recorte finalizado con éxito!")



**¿Cómo saber qué coordenadas (x, y, ancho, alto) usar?**

Si no estás seguro de las dimensiones exactas, una forma rápida con FFmpeg en la terminal es usar su detector automático de 
bordes negros:

.. code:: Bash

   ffmpeg -i mi_pelicula.mp4 -t 30 -vf cropdetect -f null -

Esto analizará los primeros 30 segundos y te arrojará en la consola una línea como: crop=1280:720:100:50 (que corresponde a 
ancho:alto:x:y).


Si lo deseas, dime:

• ¿Quieres eliminar bordes negros automáticos o recortar una zona específica (ej. una esquina)?
• ¿Conoces las dimensiones actuales de tu video?

Te puedo ayudar a programar un script que detecte y elimine las franjas negras automáticamente.






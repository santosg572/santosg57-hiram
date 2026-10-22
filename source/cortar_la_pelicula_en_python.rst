Para cortar o recortar una película o archivo de video en Python, la forma más común y sencilla es utilizar la biblioteca 
MoviePy o bien FFmpeg mediante la librería subprocess si buscas mayor velocidad sin recodificar todo el archivo.
Aquí tienes las dos mejores opciones:

**Opción 1: Cortar un video usando MoviePy (Más fácil)**

Primero debes instalar la librería en tu terminal:

.. code:: Bash

   pip install moviepy

Luego, utiliza el siguiente código en Python:

.. code:: Python

   from moviepy.editor import VideoFileClip

   # 1. Cargar el archivo de video (ej. "pelicula.mp4")
   video = VideoFileClip("pelicula.mp4")

   # 2. Definir el tiempo de inicio y fin en segundos (ej. del segundo 10 al segundo 45)
   tiempo_inicio = 10 
   tiempo_fin = 45
   cortado = video.subclip(tiempo_inicio, tiempo_fin)

   # 3. Guardar el fragmento en un nuevo archivo
   cortado.write_videofile("pelicula_cortada.mp4", codec="libx264", audio_codec="aac")

https://ellibrodepython.com/moviepy-python


**Opción 2: Cortar un video usando FFmpeg desde Python (Más rápido sin perder calidad)**

Si la película es muy larga, MoviePy puede tardar porque vuelve a procesar y renderizar los fotogramas. Usar FFmpeg 
directamente desde Python es mucho más rápido:

.. code:: Python

   import subprocess

   # Comando de FFmpeg para recortar desde el minuto/segundo de inicio (-ss) con una duración (-t)
   # Ejemplo: cortar desde 00:01:00 (1 minuto) un fragmento de 30 segundos
   comando = [
       'ffmpeg',
       '-ss', '00:01:00',  # Tiempo de inicio (HH:MM:SS o segundos)
       '-i', 'pelicula.mp4',  # Archivo de entrada
       '-t', '30',  # Duración del clip en segundos
       '-c', 'copy',  # Copiar streams sin recodificar (súper rápido)
       'pelicula_cortada.mp4'
   ]

   subprocess.run(comando)









import subprocess
import pati

filein = pati.File()

# Comando de FFmpeg para recortar desde el minuto/segundo de inicio (-ss) con una duración (-t)
# Ejemplo: cortar desde 00:01:00 (1 minuto) un fragmento de 30 segundos
comando = [
    'ffmpeg',
    '-ss', '00:00:13',  # Tiempo de inicio (HH:MM:SS o segundos)
    '-i', filein, #'pelicula.mp4',  # Archivo de entrada
    '-t', '4',  # Duración del clip en segundos
    '-c', 'copy',  # Copiar streams sin recodificar (súper rápido)
    'pelicula_cortada.mp4'
]

subprocess.run(comando)


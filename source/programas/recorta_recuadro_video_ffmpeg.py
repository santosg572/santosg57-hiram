import ffmpeg

filein  = 'pelicula_cortada.mp4'


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
recortar_video(filein, 'pelicula_recortada_recuadro.mp4', x=400, y=200, ancho=1520, alto=600)



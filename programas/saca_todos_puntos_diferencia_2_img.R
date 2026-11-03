source('Lee_IMG.R')
source('saca_tamano.R')
source('display_raster_funcion.R')
source('diferencia_2_img.R')
source('saca_puntos_diferencia_2_img.R')

i1 = 1
i2 = 27452
ff = .10

xt = c()
yt = c()

npn = c()
for (i in i1:i2){
#  print(i)
  mat_dif = diferencia_2_img(i)
  xy = saca_puntos_diferencia_2_img(ff, mat_dif)
  ix = xy[[1]]
  iy = xy[[2]]
  np1 = length(ix)
#  print(paste('num puntos: ', np1))
  npn = c(npn, np1)
}
  
plot(npn)


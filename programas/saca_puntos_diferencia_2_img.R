source('Lee_IMG.R')
source('saca_tamano.R')
source('display_raster_funcion.R')
source('diferencia_2_img.R')

saca_puntos_diferencia_2_img <- function(ff=0, mat_dif=0){
  k = 0
  ss = dim(mat_dif)
  xx = c()
  yy = c()
  for (i in 1:ss[1]){  
    for (j in 1:ss[2]){
      if (mat_dif[i,j] > ff){
        xx = c(xx, i)
        yy = c(yy, j)
        k = k+1
      }
    }
  }
#  print(k)
  res = list(xx,yy)
}




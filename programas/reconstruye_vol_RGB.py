source('Lee_IMG.R')
source('saca_tamano.R')
source('display_raster_funcion.R')
source('diferencia_2_img.R')
source('saca_puntos_diferencia_2_img.R')

i1 = 1
i2 = 10
ff = .10

xt = c()
yt = c()

for (i in i1:i2){
  print(i)
  mat_dif = diferencia_2_img(i)
  xy = saca_puntos_diferencia_2_img(ff, mat_dif)
  ix = xy[[1]]
  iy = xy[[2]]
  np1 = length(ix)
  print(paste('num puntos: ', np1))
  if (np1 > 0){
    xt = c(xt, ix)
    yt = c(yt, iy)
  }
}
  
img = Lee_IMG(i1)

ss = dim(img)

vol = rep(0, ss[1]*ss[2]*3)
dim(vol) = c(ss[1], ss[2], 3)

verde = rep(0, ss[1]*ss[2])
dim(verde) = c(ss[1], ss[2])

ff = .10
del1 = 5
rojo = img

ix = xt
iy = yt	
np1 = length(ix)
print(np1)

if (np1 > 0){
  for (k in 1:np1){
    i = ix[k]
    j = iy[k]
    if (1 < i-del1 & i+del1 < ss[1] & 1 < j-del1 & j+del1 < ss[2]){
      rojo[(i-del1):(i+del1),(j-del1):(j+del1)] = 0
      verde[(i-del1):(i+del1),(j-del1):(j+del1)] = 1
    }
  }
} else {
  print('np1 fue igual a cero')
}

vol[,,1] = rojo
vol[,,2] = verde

display_raster_funcion(vol)







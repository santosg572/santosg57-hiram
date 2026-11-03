source('saca_tamano.R')
source('diferencia_2_img.R')
source('saca_puntos_diferencia_2_img.R')

dif = diferencia_2_img(9)

ss = dim(dif)

dim(dif) = c(ss[1]*ss[2])

print(ss)

plot(dif)







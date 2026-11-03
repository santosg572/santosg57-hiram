source('Lee_IMG.R')
source('saca_tamano.R')

diferencia_2_img <- function(i=0){
  img1 = Lee_IMG(i)
  img2 = Lee_IMG(i+1)

  dif = abs(img1 - img2)

  ret = dif
}
 
ss = saca_tamano()

img = diferencia_2_img(1)
x = img
dim(x) = c(ss[1]*ss[2])



plot(x)






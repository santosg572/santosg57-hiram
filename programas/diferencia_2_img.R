source('Lee_IMG.R')

diferencia_2_img <- function(i=0){
  img1 = Lee_IMG(i)
  img2 = Lee_IMG(i+1)

  dif = abs(img1 - img2)

  ret = dif
}




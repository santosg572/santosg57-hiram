source('Lee_IMG.R')

diferencia_2_img <- function(i=0){
  img1 = Lee_IMG(i)
  img2 = Lee_IMG(i+1)

  x = img1
  y = img2

  ss = dim(x)
#  print(ss)

  dim(x) = c(ss[1]*ss[2])
  dim(y) = c(ss[1]*ss[2])

  dif = abs(x-y)

  ret = max(dif)
}

n = 27451
dd = rep(0,n)

ma = 0
for (i in 1:27451){
  x = diferencia_2_img(i)
  if (x > ma){
    ma = x
  }
  dd[i] = x
}

print(ma)
plot(dd, ylim=c(0,2))






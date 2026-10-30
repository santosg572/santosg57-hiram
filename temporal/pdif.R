library(jpeg)

source('saca_tamano.R')

ss = saca_tamano()

Lee_IMG <- function(ide = 0){
  pref = 'output_'
  i = ide
  #  print(i)
  if (i < 10){
     file = paste(pref, '0000', i, '.jpg', sep='')
  } else if (i < 100){
    file = paste(pref, '000', i, '.jpg', sep='')
  } else if (i < 1000){
     file = paste(pref, '00', i, '.jpg', sep='')
  } else if (i < 10000){
     file = paste(pref, '0', i, '.jpg', sep='')
  } else {
     file = paste(pref, i, '.jpg', sep='')
  }

  print(file)
  img <- readJPEG(file)
  res = img
} 

x <- Lee_IMG(1)
x = x[,,1]
y <- Lee_IMG(2)
y = y[,,1]
ss = dim(x)
print(ss)

dim(x) = c(ss[1] * ss[2])
dim(y) = c(ss[1] * ss[2])

xy = abs(x-y)

mxy = mean(xy)
sxy = sd(xy)

print(mxy)
print(sxy)


plot(xy, type='l')



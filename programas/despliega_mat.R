library(jpeg)

source('saca_tamano.R')

saca_MAT <- function(inx=0){
   ss = saca_tamano()

   nx = ss[1]
   ny = ss[2]
   nn = 27452
   mat = matrix(rep(0,nn*ny), nrow=nn)

   pref = 'output_'
   i = 1
   while (i < nn){
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

   #  print(paste(i, '-', file))
     img <- readJPEG(file)
     mat[i,] = img[nx-inx,,1]
     i = i+1
   } 
   ret = mat
}

mati = saca_MAT(100)
y = mati[1,]
plot(y, ylim=c(0,10), type='l')

print(dim(mati))
nn2 = 27452

for (i in 2:nn2){
  print(i)
  y = mati[i,]  
  points(y, ylim=c(0,10), type='l')
}



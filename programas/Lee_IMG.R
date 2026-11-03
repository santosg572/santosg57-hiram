library(jpeg)

Lee_IMG <- function(i=0){
   pat='../../temporal/'
   pref = 'output_'
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
   file = paste(pat,file,sep='')
#   print(file)
   mat <- readJPEG(file)
   ret = mat[,,1]
}

#img = Lee_IMG(5)

#image(img)








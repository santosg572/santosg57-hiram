library(jpeg)

saca_tamano <- function(){
  pref = 'output_'
  i = 1
  file = paste(pref, '0000', i, '.jpg', sep='')
  img <- readJPEG(file)
  print(file)
  ret = dim(img)
}

#ss = saca_tamano()
#print(ss)




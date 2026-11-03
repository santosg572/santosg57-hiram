library(raster)

nx = 256

template = rep(0,nx*nx)
dim(template) = c(nx, nx)

rojo = template
rojo[1:128,] = 1

verde = template
verde[128:256,1:128] = 1

azul = template
azul[128:256,129:256] = 1

vol = rep(0, nx*nx*3)
dim(vol) = c(nx, nx, 3)

vol[,,1] = rojo
vol[,,2] = verde
vol[,,3] = azul

grid::grid.newpage()
grid::grid.raster(vol)




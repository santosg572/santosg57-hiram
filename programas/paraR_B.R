
#3. El enfoque moderno: El ecosistema future y furrr

#Si trabajas habitualmente con herramientas de Tidyverse y utilizas funciones de la librería purrr (como map), el paquete 
#furrr es la opción ideal y más limpia

# Instalación previa si no los tienes:
# install.packages(c("future", "furrr"))

library(furrr)

# Configurar R para que procese en paralelo en segundo plano (multicore es nativo en Mac)
plan(multicore, workers = detectCores() - 1)

# Usar future_map en lugar de map para distribuir el procesamiento
resultados <- future_map(1:1000, function(x) {
  Sys.sleep(0.01)
  print(sqrt(x))
})



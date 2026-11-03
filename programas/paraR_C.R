#4. El enfoque tradicional robusto: foreach y doParallel

#Si prefieres estructuras similares a los ciclos for, puedes combinar foreach con doParallel.


# install.packages(c("foreach", "doParallel"))

library(foreach)
library(doParallel)

# Registrar los núcleos en el sistema

num_cores <- detectCores() - 1
registerDoParallel(cores = num_cores)

# Ejecutar el bucle mapeando la salida directamente a un vector combinado (.combine = c)

resultados <- foreach(i = 1:1000, .combine = c) %dopar% {
  print(sqrt(i))
}

# Al finalizar, es buena práctica cerrar las conexiones paralelas

stopImplicitCluster()





#2. El método nativo y más rápido: mclapply

#La forma más directa en Mac de paralelizar un bucle clásico (lapply) es usando mclapply del paquete interno parallel.

library(parallel)



# 1. Definir cuántos núcleos usar (se aconseja dejar al menos uno libre para el sistema)
num_cores <- detectCores() - 1

# 2. Tu vector o lista de datos
datos <- 1:1000

# 3. Tu función costosa (ejemplo simple: calcular una raíz cuadrada con una pausa)
funcion_costosa <- function(x) {
  Sys.sleep(0.01) # Simula procesamiento
  return(sqrt(x))
}

# 4. Ejecución en paralelo usando los núcleos asignados
resultados <- mclapply(datos, funcion_costosa, mc.cores = num_cores)

print(resultados)




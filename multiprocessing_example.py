"""
 GIL: Global Interpreter Lock
 Es un tipo de lock especial que permite que solo un hilo se ejecute en Python.
 Esto es necesario porque la administración de memoria en Python no es thread-safe.
 Hay implementación y wrappers en Python que ayudan a sobrepasar estas limitaciones.

 Proceso: Instancia de un programa.
 Cada proceso es independiente de otros.
 La memoria no se comparte entre los procesos.
 Cada proceso puede quedar en un core diferente.
 El proceos es lento de iniciar en comparación con los hilos.
 Son útiles para evitar las limitaciones del GIL, se crea un GIL por cada proceso.
 La comunicación es mas complicada que entre hilos.
 Los procesos se pueden interrumpir.
"""

from multiprocessing import Process
import os
import platform


# Esta es la función que se ejecuta en cada proceso
def funcion(numero):
    print(os.getpid())
    for n in range(10):
        valor = n*n+n
        print (valor, "--->", numero)
             

# Para observar la ejecución debemos de ejecutar en una consola y colocamos el main para facilitar todo

if __name__ == '__main__':
    procesos =[]

    # Se obtiene cantidad de cores:
    cores = os.cpu_count()
    print('Tienes ', cores, 'cores')

    print ('------ Instanciar')
    # Se crean los procesos, uno por cada core

    for n in range(cores):
        # Creamos la instancia
        # Asignamos al función a ejecutar y cualquier parámetro necesario
        proceso= Process(target=funcion, args=(n,))
        # Lo adicionamos a la lista de procesos

        procesos.append(proceso)

    print('----- Ejecutar')

    # Ahora que ya están instanciados, se ejecutan

    for proceso in procesos:
        proceso.start()

    print('----- Espera')        
    for proceso in procesos:
        proceso.join()

    print('Regreso a la ejecución inicial')
    a = input('Presione cualquier tecla para termina...')



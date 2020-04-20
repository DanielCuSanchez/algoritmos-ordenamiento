import sys

array = [50, 23, 15, 20, 10]
print(len(array))

# Buscar el menor numero en mi array
# Crear dos subarrays para llevar el control del algoritmo
# Imprimir el resultado del ordenamiento


def selectionSort(array):
    # Recorre todo el array
    for i in range(len(array)):
        print(array)
        # Encontrar el valor minimo dentro del array desordenando
        idxDes = i
        for j in range(i+1, len(array)):
            if array[idxDes] > array[j]:
                idxDes = j

        # Ya que encontramos el minimo lo vamos a cambiar por el primer valor
        # de nuestro array desordenado
        array[i], array[idxDes] = array[idxDes], array[i]

selectionSort(array)
print(array)
for i in range(len(array)):
    print("%d"%array[i])
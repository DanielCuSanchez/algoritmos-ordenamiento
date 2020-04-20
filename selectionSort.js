let lista = [999, 333, 1, 31, 34, 3, 2, 1]

function selectionSort(lista) {
    let index
    let aux
    for (let i = 0; i < lista.length; i++) {
        index = i
        for (let j = i + 1; j < lista.length; j++) {
            if (lista[index] > lista[j]) {
                index = j
            }
        }
        aux = lista[i]
        lista[i] = lista[index]
        lista[index] = aux
    }
}

selectionSort(lista)
console.log(lista)
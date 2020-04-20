let numeros = [1, 80, 2, 65, 2, 85, 96, 10]
console.log(numeros.length)
for (let i = 0; i < numeros.length; i++) {
    // console.log("i = ",i)
    for (let j = 0; j < numeros.length - i - 1; j++) {
        console.log(i, j)
        if (numeros[j] > numeros[j + 1]) {

            let aux
            aux = numeros[j]
            numeros[j] = numeros[j + 1]
            numeros[j + 1] = aux
        }
    }
}
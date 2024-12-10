// bucle que sume los numeros del 1 al 100
let i=1
let resultado=0
while(i<=100){
resultado+=i
i++
}
console.log(resultado)

// pares de 1 a 50

for(j=0;j<=50;j++){
    if(j%2!=0){
        continue
    }
    console.log(j)
}

//imprimir los nombres de un array de nombres

let nombres = ["juan","andres","felipe"]

for (let nombre of nombres) {
    console.log(nombre)
}

//contar vocales de un texto

let vocales=["a","e","i","o","u"]
const palabra="parangaraturimicaro"
let contadorvocales=0
for (let letra of palabra) {
    for(let vocal of vocales){
        if(letra==vocal){
            contadorvocales++
            break
        }
    }
}
console.log(contadorvocales)

//multiplicar numeros de un array

let numeros=[1,2,3,4,5]
let tamaño=numeros.length
resultado=1
i=0
do {
    resultado*=numeros[i]
   i++ 
} while (i<tamaño);
console.log(resultado)

//tabla de multiplicar del 5

for(j=0;j<11;j++){
    console.log("5 * ",j," = ",5*j)
}

// invertir un texto
let nuevapalabra="-"
tamaño=(palabra.length)
for (j=tamaño-1;j>=0;j--) {
    nuevapalabra+=palabra[j]
}
nuevapalabra=nuevapalabra.replace("-","")
console.log(nuevapalabra)
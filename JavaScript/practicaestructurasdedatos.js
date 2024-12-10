
//crear una rray con 5 animales

let animales=["Perro","Gato","chiguiro","Raton","Leopardo"]

// agrega dos animales uno al principio y otro al final
let libros = new Set(["libro1","libro2","libro3","libro4","libro5"])

let meses = new Map([
    [1,"Enero"],
    [2,"Febrero"],
    [3,"Marzo"],
    [4,"Abril"],
    [5,"Mayo"],
    [6,"June"],
    [7,"Jule"],
    [8,"Augost"],
    [9,"Septomber"],
    [10,"October"],
    [11,"November"],
    [12,"Dicember"]
])

if (meses.has(5)){
    console.log(meses.get(5))
}

meses.set("verano",["Mayo","June","Jule","Augost"])
console.log(meses.values())

let animalesset = new Set(animales)

meses.set("animales",animalesset)
console.log(meses.values())

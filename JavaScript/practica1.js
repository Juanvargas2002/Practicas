//Este es un comentario de una linea

/* 
Este es un comentario de varias lineas
*/

//declara una variable de cada tipo
let numero=10
let string="soy un string"
let boleano=true
let bigint=BigInt(1848888884840000000000000000000000000000000)
let simbolo=Symbol("soy un simbolo")
let undefine
let nulo=null
//imprime el valor de las variables
console.log(numero)
console.log(string)
console.log(boleano)
console.log(bigint)
console.log(simbolo)
console.log(undefine)
console.log(nulo)
//imprime el tipo de las variables
console.log(typeof numero)
console.log(typeof string)
console.log(typeof boleano)
console.log(typeof bigint)
console.log(typeof simbolo)
console.log(typeof undefine)
console.log(typeof nulo)
//modifica los valores de las variables por otros del mismo tipo
numero=11
string="soy otro string"
boleano=false
bigint=BigInt(1212121212121212121212121212121212)
simbolo=Symbol("soy el mismo simbolo con otro valor")
undefine=""
nulo=null

console.log(numero)
console.log(string)
console.log(boleano)
console.log(bigint)
console.log(simbolo)
console.log(undefine)
console.log(nulo)
//imprime el tipo de las variables
console.log(typeof numero)
console.log(typeof string)
console.log(typeof boleano)
console.log(typeof bigint)
console.log(typeof simbolo)
console.log(typeof undefine)
console.log(typeof nulo)
//modifica los valores por otros de diferente tipo
numero="antes era un numero"
string=35
boleano=Symbol("antes era booleano")
bigint=null
simbolo=
undefine=BigInt(21379812738972131283791238193)
nulo=true
//declara constantes
const numero2=10
const string2="soy un string"
const boleano2=true
const bigint2=BigInt(10000000000000000000000000000000)
const simbolo2=Symbol("soy un simbolo")
const undefine2=""
const nulo2=null
//modifica las constanetes

//todas estas daran error porque las constates no se pueden cambiar
/*
numero2=12
string2="soy otro string"
boleano2=false
bigint2=BigInt(1123123213413510510053015010510500000000000000000000)
simbolo2=Symbol("soy otro simbolo")
undefine2=""
nulo2=null
*/
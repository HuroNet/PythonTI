// empezamos 
const sumarElementosObjeto=(objeto)=>{
  let valores = Object.values(objeto);
  let sum=0;
  // for(let valor of valores){
  //   sum=valor+sum
  // }
  // for(let i=0;i<valores.length;i++){
  //   sum+=valores[i]
  // }
  valores.forEach(value => sum+=value)
  return sum
}
// console.log(sumarElementosObjeto({a: 1, b: 2, c: 3}))
// Entrada: {a: 1, b: 2, c: 3}
// console.log(sumar_elementos({a: 1, b: 2, c: 3}))
// Salida: 6

//Invertir una cadena
const invertirCadena = (cadena) =>{
  const result = cadena.split("").reverse().join("")
  return result
}

// console.log(invertirCadena("hola mundo"))

// Entrada: "hola"
// console.log(invertir_cadena("hola mundo"))
// Salida: "aloh"

//
// 3. Encontrar el número más grande en un arreglo
const numeroMasGrande = (array) =>{
  const arr = array.sort((a,b)=>(b-a))
  return arr[0]
}
console.log(numeroMasGrande([1, 3, 7, 0, 5]))


// Entrada: [1, 3, 7, 0, 5]
// console.log(numero_mas_grande([1, 3, 7, 0, 5]))
// Salida: 7


// 4. Contar cuántas veces se repite un valor en un arreglo



// Entrada: [1, 2, 3, 1, 2, 1], 1
// console.log(repeticiones_valor([1,2,3,1,3,1],1))
// Salida: 3
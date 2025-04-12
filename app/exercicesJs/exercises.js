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
// console.log(numeroMasGrande([1, 3, 7, 0, 5]))


// Entrada: [1, 3, 7, 0, 5]
// console.log(numero_mas_grande([1, 3, 7, 0, 5]))
// Salida: 7


// 4. Contar cuántas veces se repite un valor en un arreglo
const repeticionDeNumeros=(array, target)=>{
  let total=0
  for(valor of array){
    if (target == valor){
      total+=1
    }
  }
  return total
}
// Entrada: [1, 2, 3, 1, 2, 1], 1
// console.log(repeticionDeNumeros([1,2,2,1,3,1,3,1],1))
// Salida: 3

// ejercicio de contar cuantas veces apracen los numero en un array 

const conteoDeNumeros=(array)=>{
  let obj={}
  for(let i=0;i<array.length;i++){
    if (obj[array[i]]){
      obj[array[i]]+=1
    }
    else{
      obj[array[i]]=1
    }
  }
  return obj;
}

// console.log(conteoDeNumeros([1,2,2,1,3,1,3,1]))

//
//ELiminar Duplicados
// Entrada: [1, 2, 2, 3, 3, 4]
// console.log(eliminar_duplicados([1, 2, 2, 3, 3, 4]))
// Salida: [1, 2, 3, 4]
 
const eliminarDuplicados = (array) =>{
  const newList = []
  array.forEach(element => {
    newList.includes(element)?
    null:
    newList.push(element)
  })
  return newList
}

// console.log(eliminarDuplicados([1, 2, 2, 3, 3, 4]))

//invertir una cadena
const invertirCadena2 = (cadena)=>{
  return 0
}

console.log()

// Entrada: "hola"
// console.log(invertir_cadena("hola mundo"))
// Salida: "aloh"
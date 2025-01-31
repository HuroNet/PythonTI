
// Sumar los elementos en un objeto de números

const sumar_elementos = (objeto) => {
    // const total = Object.values(objeto).reduce((acc,valores) => acc + valores, 0);//primera 
    let total=0;
    // for(let value in objeto){
    //     total = total + objeto[value]
    // }

    //object.keys
    
    // const keys = Object.keys(objeto);
    // for(let i=0;i <  keys.length;i++){
    //     total += objeto[keys[i]]
    // }

    // //foreach
    // Object.values(objeto).forEach(value => {
    //     total+=value       
    // });


    // for
    // for(let value of Object.values(objeto)){
    //     total+=value
    // }

    return total
}

// Entrada: {a: 1, b: 2, c: 3}
// console.log(sumar_elementos({a: 1, b: 2, c: 3}))
// Salida: 6



// 1. Invertir una cadena
const invertir_cadena = (cadena) =>{
    const resultado = cadena.split('').reverse().join('')
    return resultado
}

// Entrada: "hola"
// console.log(invertir_cadena("hola mundo"))
// Salida: "aloh"

// 3. Encontrar el número más grande en un arreglo
const numero_mas_grande = (array) =>{
    const ordenar = array.sort((a,b)=>a-b);
    const resultado = ordenar[ordenar.length - 1]

    return resultado
}
// Entrada: [1, 3, 7, 0, 5]
// console.log(numero_mas_grande([1, 3, 7, 0, 5]))
// Salida: 7

// 4. Contar cuántas veces se repite un valor en un arreglo
const repeticiones_valor = (array,num) => {
    let resultado = 0
    // for (let value of array){
    //     if(value===num){
    //         resultado += 1;
    //     }
    // }
    // array.forEach(values => {
    //     values === num?
    //     resultado+=1: 
    //     null
    // });
    // for (let i=0;i<array.length;i++){
    //     console.log(array[i])
    // }
    
    // resultado = array.reduce((count, value)=>
    // (value===num? count + 1: count),0)


    return resultado
}
 
// Entrada: [1, 2, 3, 1, 2, 1], 1
// console.log(repeticiones_valor([1,2,3,1,3,1],1))
// Salida: 3

// 5. Eliminar duplicados de un arreglo
const eliminar_duplicados = (array) =>{
    // const resultado = [...new Set(array)]
    const resultado = [];
    // for(let valor of array){
    //     if(resultado.includes(valor)){
    //         console.log('si esta')
    //     }
    //     else{
    //         resultado.push(valor)
    //     }
    // }
    
    // array.forEach(element => {
    //     resultado.includes(element)?
    //     null:
    //     resultado.push(element)
    // });

 
}
// Entrada: [1, 2, 2, 3, 3, 4]
// console.log(eliminar_duplicados([1, 2, 2, 3, 3, 4]))
// Salida: [1, 2, 3, 4]

// 6. Verificar si una palabra es un palíndromo
const palindro = (palabra) =>{
    const minusculas = palabra.toLowerCase().split('')
    if(minusculas === minusculas.reverse() ){
        return true
    }else{
        return false
    }
}
// Entrada: "madam"
// console.log(palindro("madaM"))
// Salida: true

// 7. Reemplazar un valor en un arreglo por otro
const remplazar = (array, pos, valor) => {
    if (pos >= 0 && pos < array.length) {
        array[pos] = valor;
    }
    return array;
}

// Entrada: [1, 2, 3, 4], 2, 5
// console.log(remplazar([1, 2, 3, 4], 2, 5))
// Salida: [1, 5, 3, 4]

// 8. Sumar los elementos en un objeto de números
const suma_elementos = (objeto) => {
    const  valores = Object.values(objeto);
    let total=0
    // for(let valor of valores){
    //      total += valor
    // }
    // valores.forEach(element => {
    //     total += element        
    // });

    // total =  valores.reduce((acc,elementos)=>acc+elementos)

    return total
}
// Entrada: {a: 1, b: 2, c: 3}
// console.log(suma_elementos({a: 1, b: 2, c: 3}))
// Salida: 6x

// 9. Encontrar el índice de un valor en un arreglo

const index_array = (array,target) => {
    // return array.indexOf(target)
    for (let i = 0; i < array.length; i++) {
        if(array[i] === target){
            return i
        }
    }
}

// Entrada: [10, 20, 30, 40], 30
// console.log(index_array([10, 20, 30, 40], 30))
// Salida: 2

// 10. Comprobar si un número es primo
const es_primo = (num) => {
    if(num <=1){
        return false
    }
    for (let i = 2; i < num; i++) {
        if (num % i === 0) {
            return false; // Si el número es divisible por cualquier número en el rango, no es primo
        }
    }
    return true

}
// Entrada: 7
// console.log(es_primo(8))
// Salida: true

// 11. Contar la cantidad de caracteres en una cadena
const contar_caracteres = (caracteres) =>{
    let total=0
    const arrayCaracteres = caracteres.split('')
    return caracteres.length
}
// Entrada: "javascript"
// console.log(contar_caracteres("javaScript"))
// Salida: 10

// 12. Fibonacci Recursivo
const fibo = (num) =>{
    let secuencia = [0,1];
    for(let i=2;i<num;i++){
        secuencia.push(secuencia[i - 1] + secuencia[i - 2]); 
    }
    return secuencia
}
// Entrada: 5
// console.log(fibo(5))
// Salida: 5?

// 16. Verificar si un número es perfecto
const numero_perfecto = (numero) =>{
    let total = 0
    for (let i=0;i<numero;i++){
        if(numero%i===0 ){
            total+=i;
        }
    }

    return total===numero
}

// Entrada: 6
// console.log(numero_perfecto(6))
// Salida: true

// 17. Convertir una cadena a un número entero
const cadena_a_numero = (cadena) =>{
    // return Number(cadena)
    return parseInt(cadena)
}
// Entrada: "123"
// console.log(cadena_a_numero("123"))
// Salida: 123

// 18. Crear un arreglo con los múltiplos de un número
const multiplos = (numero,limite)=>{
    let resultado = []
    // for(let i=1;i<limite +1;i++){
    //     resultado.push(numero*i);
    //     // console.log(i)
    // }
    // return resultado

    //while
    let i=1;
    while (i <= limite){
        resultado.push(numero*i);
        i++
    }
    return resultado
}
// Entrada: 3, 5
// console.log(multiplos(3,5))
// Salida: [3, 6, 9, 12, 15]

// 19. Contar las vocales en una cadena
const contar_vocales = (cadena)=>{
    // const vocales = ["a","e","i","o","u"];
    // const arrayPalabra = cadena.toLowerCase().split('');
    let resultado=0

    // arrayPalabra.forEach(element => {
    //     if(vocales.includes(element)){
    //         resultado+=1
    //     }
    // });
    // for (let i=0;i<arrayPalabra.length;i++){
    //     if(vocales.includes(arrayPalabra[i])){
    //         resultado+=1
    //     }
    // }


    return resultado
}

// Entrada: "javascript"
// console.log(contar_vocales("javascript"))
// Salida: 3

//objetos

const objetos = (objeto) =>{
  const resultado = {}
  objeto.forEach(element => {
    if (!resultado[element.category]) {
        resultado[element.category]={}
    }
    if (resultado[element.category][element.name]) {
        resultado[element.category][element.name] += element.quantity;
    } 
    else {
        resultado[element.category][element.name] = element.quantity;
    }
  });
  return resultado;
};

// console.log(objetos([
//     { name: 'doll', quantity: 5, category: 'toys' },
//     { name: 'car', quantity: 3, category: 'toys' },
//     { name: 'ball', quantity: 2, category: 'sports' },
//     { name: 'car', quantity: 2, category: 'toys' },
//     { name: 'racket', quantity: 4, category: 'sports' }
//   ]))

// 20. Filtrar los números pares de un arreglo
const numerosPares = (array) =>{
    let numPares = []
    array.forEach(element => {
        if (element %2 === 0){
            numPares.push(element)
        }
    });
    return numPares
}
// Entrada: [1, 2, 3, 4, 5, 6]
// console.log(numerosPares([1, 2, 3, 4, 5, 6]))
// Salida: [2, 4, 6]

// 22. Obtener los elementos comunes entre dos arreglos
const elementosComunes = (array1,array2) =>{
    const comunes=[]
    for(let val1 of array1){
        for (let val2 of array2){
            if (val1 === val2){
                comunes.push(val1)
            }
        }
    }
    const comunesFilter = array1.filter(element=>array2.includes(element))
    return comunesFilter
}
// Entrada: [1, 2, 3, 4], [3, 4, 5, 6]
// console.log(elementosComunes([1, 2, 3, 4], [3, 4, 5, 6]))
// Salida: [3, 4]

// 23. Contar cuántas veces aparece un carácter en una cadena
const contarVeces = (cadena,letra) =>{
    const arrayCadena = cadena.toLowerCase().split('');
    const filtraLetra = arrayCadena.filter(element => element === letra)
    console.log(filtraLetra)

    return 0
}
// Entrada: "banana", "a"
// console.log(contarVeces("banana", "a"))
// Salida: 3

// 27. Crear un arreglo con los primeros n números de Fibonacci
const fibonacciSerie = (number) =>{
    const inicio = [0,1]
    for(let i=2;i<number;i++){
        inicio[i] = inicio[i-1]+inicio[i-2]
    }

    return inicio
}

// Entrada: 5
// console.log(fibonacciSerie(5))
// // Salida: [0, 1, 1, 2, 3]

// 29. Revertir el orden de los elementos en un arreglo
const revertirArreglo = (array) =>{
    const result = array.sort((a,b) => b-a)
    const result2 = array.reverse()
    return result
}
// Entrada: [1, 2, 3, 4]
// console.log(revertirArreglo([1,2,3,4]))
// Salida: [4, 3, 2, 1]

// 33. Crear un arreglo con los divisores de un número
const divisores = (numero) =>{
    let resultado=[]
    for(let i=0;i<numero+1;i++){
        if(numero % i === 0){
            resultado.push(i)
        }
    }
    return resultado
}

// Entrada: 6
// console.log(divisores(6))
// Salida: [1, 2, 3, 6]

// 37. Encontrar el valor máximo en un objeto con claves numéricas
const valorMaxObject = (object) =>{
    let maximo = 0
    Object.values(object).forEach(element=>{
        // console.log(element)
        if(element>maximo){
            console.log(maximo)
            maximo=element
        }
    })
    return maximo
} 
// Entrada: {1: 5, 2: 10, 3: 2}
// console.log(valorMaxObject({1: 5, 2: 11 ,3: 20}))
// Salida: 10

// 41. Obtener la longitud de la palabra más larga en un arreglo
const logPalabra = (array) =>{
    const maximo = 0
    for(let i=0;i<array.length;i++){
        console.log(array[i])
        if(array[i].length > maximo){
            maximo=array[i].length
        }
    }
    return maximo
}
// Entrada: ["apple", "banana", "kiwi"]
// console.log(logPalabra(["apple", "banana", "kiwi"]))
// Salida: 6



// Las claves del objeto serán las categorías de juguetes.
// Los valores serán objetos que tienen como claves los nombres de los juguetes y como valores las cantidades totales de cada juguete en esa categoría.
// Si hay juguetes con el mismo nombre en la misma categoría, debes sumar sus cantidades.
// Si el array está vacío, la función debe devolver un objeto vacío {}.

const organizeInventory = (inventory) =>{
    const resultado ={}
    
    const resultado2 ={}
    inventory.forEach(element => {
        if (!resultado[element.category]) {
            resultado[element.category]={}
            
            resultado2[element.category]={}
        }
        if(!resultado[element.category][element.name]){
            resultado[element.category]=1;
            resultado2[element.category][element.quantity]=2
        }
        
    });
    return { resultado, resultado2 };
}

const inventory = [
{ name: 'doll', quantity: 5, category: 'toys' },
{ name: 'car', quantity: 3, category: 'toys' },
{ name: 'ball', quantity: 2, category: 'sports' },
{ name: 'car', quantity: 2, category: 'toys' },
{ name: 'racket', quantity: 4, category: 'sports' }
]
// console.log(organizeInventory(inventory))


const emparejamiento = (shoes) =>{
    let lista_shoes =[]
    shoes.forEach(element => {
        
    });
    return lista_shoes
}


const shoes = [
    { type: 'I', size: 38 },
    { type: 'R', size: 38 },
    { type: 'R', size: 42 },
    { type: 'I', size: 41 },
    { type: 'I', size: 42 }
  ]

// console.log(emparejamiento(shoes))



//mas ejerciciso "
// 8. Eliminar duplicados en un arreglo

const eliminarDuplicados = (array) =>{
    const resultado = new Set(array)
    return resultado
}

// console.log(eliminarDuplicados([1, 2, 2, 3, 4, 4, 5]))

// 9. Encontrar la longitud de la palabra más larga en un arreglo
const longitudMasLarga = (array) =>{
    let resultado = 0
    array.forEach(element => {
        resultado=Math.max(resultado,element.length)
    });
    return resultado
} 

// console.log(longitudMasLarga(["perro", "gato", "elefante"]))


// Contar la frecuencia de cada elemento en un arreglo

//     Entrada: [1, 2, 2, 3, 3, 3]
//     Salida: {1: 1, 2: 2, 3: 3}
const contarFrecuencia = (array) =>{
    let dic = {}
    for(let dato of array){
      if(dic[dato]){
        dic[dato]+=1
      }
      else{
        dic[dato]=1
      }
    }
    return dic;
  }
//   console.log(contarFrecuencia([1, 2, 2, 3, 3, 3]))

// Rotar un arreglo hacia la derecha por k posiciones



//     Entrada: ([1, 2, 3, 4, 5], 2)
// console.log(rotarDerecha([1, 2, 3, 4, 5], 2))
//     Salida: [4, 5, 1, 2, 3]

// Invertir Palabras en una Cadena
const invertirPalabra = (cadena) =>{
    const separar = cadena.split(" ")
    let resultado = separar[0] + separar[1]
    return resultado
}

// console.log(invertirPalabra("hola mundo"))
//     Entrada: "hola mundo"
//     Salida: "mundo hola"


const contar = (cadena) =>{
    const arrayCadena = cadena.split(" ")
    let resultado={}
    for(let valor of arrayCadena){
        if(resultado[valor]){
            resultado[valor]+=1
        }
        else{
            resultado[valor]=1
        }
    }
    return resultado
}

// // console.log(contar("el sol brilla el sol"))

// Ordenar una lista de objetos por una propiedad
const ordenar = (array,propiedad) =>{
    console.log(array[propiedad])
    const ordenar = array.sort((a,b)=>{
        if(a[propiedad]<b[propiedad]){
            console.log(a[propiedad])
        }
    })
    return 0
}
//  . Ejemplo: [{name: "Juan", age: 28}, {name: "Ana", age: 22}], propiedad: "age"
//      [{name: "Ana", age: 22}, {name: "Juan", age: 28}]
console.log(ordenar([{name: "Juan", age: 28}, {name: "Ana", age: 22}],"age"))
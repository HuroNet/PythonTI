// ejercios:
// Sumar ambos números y devolver el resultado.

const sumaDosNumeros = (a, b) => {
  let total = a + b;
  return total;
};
// console.log(sumaDosNumeros(5,7))

// 🔹 2. Número par o impar
//     Input: n = 4
//     Output: "Par"
//     Explicación: Usar el oper

const numeroParImpar = (number) => {
  if (number % 2 === 0) {
    return `par`;
  } else {
    return `inpar`;
  }
};

// 🔹 3. Palíndromo
//     Input: "oso"
//     Output: True
//     Explicación: Comprobar si la cadena se lee igual al derecho y al revés.
const palindromo = (string) => {
  const minusculas = string.toLowerCase();
  const invertida = minusculas.split("").reverse().join("");
  return minusculas === invertida;
};
// console.log(palindromo("ahsAd"))

// 4. Factorial de un número
// Input: n = 5
// Output: 120
// Explicación: Calcular 5 * 4 * 3 * 2 * 1.

const factorial = (numero) => {
  // let total = numero
  // for(let i = numero -1; i>0;i--){
  //   total = total * i
  // }
  // return total
  // uso del while
  // let total = 1
  // let start = 1
  // while (start <= numero){
  //   total = start * total;
  //   start ++
  // }
  // return total
};
// 🔹 5. FizzBuzz

//     Input: n = 15

//     Output: "FizzBuzz"

//     Explicación: Si es múltiplo de 3 y 5, devuelve "FizzBuzz", si solo de 3 "Fizz", si solo de 5 "Buzz".

const FizzBuzz = (numero) => {
  if (numero % 3 === 0 && numero % 5 === 0) {
    return "FizzBuzz";
  } else if (numero % 3 === 0) {
    return "fizz";
  } else if (numero % 5 === 0) {
    return "buzz";
  } else {
    return numero;
  }
};

// console.log(FizzBuzz(15))

// 🔹 6. Número primo

//     Input: n = 7

//     Output: True

//     Explicación: Verifica que solo tenga dos divisores: 1 y él mismo.
const numerosPrimos = (numero) => {
  for (let i = 2; i < numero; i++) {
    if (numero % i === 0) {
      return false;
    }
  }
  return true;
};

// 7. Revertir una cadena

//     Input: "hola"

//     Output: "aloh"

//     Explicación: Usar slicing o un bucle para invertir la cadena.

const revertirCadena = (cadena) => {
  string = cadena.split("").reverse();
  return string.join("");
};

// console.log(revertirCadena("carlitos"))

// 8. Contar vocales

// Input: "ingeniería"

// Output: 6

// Explicación: Recorrer la cadena y contar las letras a, e, i, o, u.

const contarVocales = (string) => {
  const vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"];
  const array = string.split("");
  let result = 0;
  for (let letra of array) {
    if (vocales.includes(letra)) {
      result += 1;
    }
  }

  return result;
};

// 9. Longitud de la palabra más larga

// Input: "El zorro marrón salta"

// Output: 6

// Explicación: Separar las palabras y hallar la más larga.

const longitudPalabraLarga = (string) => {
  const array = string.split(" ");
  let maxLongiitud = 0;
  for (let palabra of array) {
    if (palabra.length > maxLongiitud) {
      maxLongiitud = palabra.length;
    }
  }
  return maxLongiitud;
};

// 🔹 10. Suma de los dígitos de un número

//     Input: 1234

//     Output: 10

//     Explicación: 1 + 2 + 3 + 4 = 10

const sumaDigitos = (digitos) => {
  const numeros = digitos.toString().split("");

  let total = 0;
  numeros.forEach((element) => {
    total += Number(element);
  });
  return total;
};

// console.log(sumaDigitos(1234))
// 🔹 11. Eliminar duplicados en una lista

//     Input: [1, 2, 2, 3]

//     Output: [1, 2, 3]

//     Explicación: Usar set() o lógica para mantener solo elementos únicos.

const eliminarDuplicados = (array) => {
  const result = [...new Set(array)];

  return result;
};
// console.log(eliminarDuplicados([1,2,3,2,3]))

// 1. Invertir una cadena

// Input: "developer"
// Output: "repoleved"

const invertir_string = (string) => {
  const array = string.split("");
  let result = [];
  for (let letra of array) {
    result.unshift(letra);
  }
  return result;
};
// console.log(invertir_string("developer"))

// 2. Comprobar si una palabra es palíndromo

// Input: "racecar"
// Output: true

const comprobarPalindormo = (string) => {
  const reverse = string.split("").reverse().join("");
  if (reverse === string) {
    return true;
  } else {
    return false;
  }
};

// 4. Repetir una cadena N veces

// Input: "abc", 3
// Output: "abcabcabc"

const repetirCadenaNVeces = (string, target) => {
  let resultado = "";
  for (let i = 0; i < 3; i++) {
    resultado += string;
  }
  // return resultado
  return string.repeat(target);
};

// console.log(repetirCadenaNVeces('abc',3))
// 5. Encontrar el número más grande en un arreglo

// Input: [3, 19, 8, 5]
// Output: 19

const numeroMasGrande = (array) => {
  let array1 = array.sort();
  return array1[0];
};
// onsole.log(numeroMasGrande([3,19,8,5]))

// 6. Ordenar arreglo sin usar .sort()

// Input: [4, 2, 7, 1]
// Output: [1, 2, 4, 7]

const bubbleSort = (array) => {
  let size = array.length;
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size - 1; j++) {
      if (array[j] > array[j + 1]) {
        let temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
      }
    }
  }
  return array;
};

// console.log(bubbleSort([4,2,6,31,22]))

// 7. Eliminar duplicados en arreglo

// Input: [1, 2, 2, 3, 1]
// Output: [1, 2, 3]

const eliminar_Duplicados = (array) => {
  // let result = [...new Set(array)]
  let result = [];
  for (element of array) {
    if (result.includes(element)) {
      result.push(element);
    }
  }
  return result;
};
// console.log(eliminarDuplicados([1,2,2,3,3,1,1]))
// 8. Suma de elementos de un arreglo

// Input: [1, 2, 3, 4]
// Output: 10

const sumaElementos = (array) => {
  let result = 0;
  for (element of array) {
    result += element;
  }
  return result;
};

// console.log(sumaElementos([1,2,3,42]))

// 9. Convertir primera letra de cada palabra a mayúscula

// Input: "hola mundo cruel"
// Output: "Hola Mundo Cruel"
const primeraMayuscula = (string) => {
  const arregloDeString = string.split(" ");
  const result = [];
  for (const element of arregloDeString) {
    const palabra = element;
    if (palabra) {
      const primera = palabra.charAt(0).toUpperCase();
      const demas = palabra.slice(1);
      result.push(primera + demas);
    }
  }

  return result.join(" ");
};

// console.log(primeraMayuscula("hola mundo cruel"));
// 11. Rotar arreglo hacia la derecha

// Input: [1, 2, 3, 4], 1
// Output: [4, 1, 2, 3]
const rotarDerecha = (array, value) => {
  for (let i = 0; i < value; i++) {
    const ultimo = array.pop();
    array.unshift(ultimo);
  }
  return array;
};

// console.log(rotarDerecha([1,2,3,4],3))
// 12. Contar ocurrencias de un elemento

// Input: [1,2,3,2,2,4], 2
// Output: 3

const ocurrencias = (array, value) => {
  let result = {};
  let contador = 0;
  for (element of array) {
    if (result[element]) {
      contador += 1;
      result[element] += 1;
    } else {
      result[element] = 1;
    }
  }
  return result;
};
// console.log(ocurrencias([1,2,3,2,2,4], 2))
// 20. Filtrar solo palabras largas

// Input: ["hola", "desarrollador", "web"], min = 5
// Output: ["desarrollador"]

const filtradoPalabrasLargas = (array, min) => {
  for (element of array) {
    if (element.length >= 5) {
      return element;
    }
  }
};
// console.log(filtradoPalabrasLargas( ["hola", "desarrollador", "web"], 5))
// 21. Fusionar dos arreglos sin duplicados

// Input: [1,2,3], [3,4,5]
// Output: [1,2,3,4,5]

const fucionarArrays = (array1, array2) => {
  let union = array1;
   for (const elemento of array2) {
    if (!union.includes(elemento)) {
      console.log(elemento)
    }
  }
  return union;
};

// 22. Encontrar el número que falta

// Input: [1, 2, 4, 5]
// Output: 3
const numeroFaltante = (array) =>{
  
}

console.log(numeroFaltante([1,2,4,5]))
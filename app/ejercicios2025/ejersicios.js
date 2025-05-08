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
  let maxLongiitud = 0
  for (let palabra of array){
    console.log(palabra)
  }
  return maxLongiitud;
};

console.log(longitudPalabraLarga("EL zorro marron salta"));

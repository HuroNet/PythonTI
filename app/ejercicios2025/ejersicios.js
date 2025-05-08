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

console.log(factorial(5));

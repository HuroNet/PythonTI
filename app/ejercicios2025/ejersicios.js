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
// console.log(numeroParImpar(5));

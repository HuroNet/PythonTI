// Referencia a los elementos del DOM
const entrada = document.getElementById("cash"); // Campo donde el usuario ingresa el dinero
const btnCompra = document.getElementById("purchase-btn"); // Botón para hacer la compra
const resultado = document.getElementById("change-due"); // Área donde se muestra el resultado

// Precio del producto que se compra
let price = 19.5;

// Fondo de caja (cid) con las denominaciones disponibles y su cantidad
let cid = [
  ['PENNY', 1.01], // Monedas de 1 centavo
  ['NICKEL', 2.05], // Monedas de 5 centavos
  ['DIME', 3.1], // Monedas de 10 centavos
  ['QUARTER', 4.25], // Monedas de 25 centavos
  ['ONE', 90], // Billetes de 1 dólar
  ['FIVE', 55], // Billetes de 5 dólares
  ['TEN', 20], // Billetes de 10 dólares
  ['TWENTY', 60], // Billetes de 20 dólares
  ['ONE HUNDRED', 100] // Billetes de 100 dólares
];

// Objeto que mapea el nombre de la moneda/billete a su valor en dólares
const denominaciones = {
  "PENNY": 0.01,
  "NICKEL": 0.05,
  "DIME": 0.1,
  "QUARTER": 0.25,
  "ONE": 1,
  "FIVE": 5,
  "TEN": 10,
  "TWENTY": 20,
  "ONE HUNDRED": 100
};

// Función principal que se ejecuta cuando se hace clic en el botón de compra
const comprar = () => {
  // Obtener el valor ingresado por el usuario y convertirlo a un número flotante
  const cash = parseFloat(entrada.value.trim());
  // Calcular cuánto cambio se necesita
  const changeRequired = (cash - price).toFixed(2); // .toFixed(2) para asegurarnos de que tenga dos decimales

  // Si el cliente no tiene suficiente dinero, mostrar un mensaje de error
  if (changeRequired < 0) {
    alert("Customer does not have enough money to purchase the item.");
    return; // Detener la ejecución si no tiene suficiente dinero
  }

  // Si el cambio es exactamente cero, indicar que no hay cambio
  if (changeRequired === "0.00") {
    resultado.textContent = "No change due - customer paid with exact cash.";
    return;
  }

  // Calcular el cambio que se debe devolver
  const resultadoCambio = calcularCambio(changeRequired);

  // Si el cambio no es posible con el fondo de caja, mostrar mensaje de fondos insuficientes
  if (resultadoCambio.status === "INSUFFICIENT_FUNDS") {
    resultado.textContent = "Status: INSUFFICIENT_FUNDS";
  } else {
    // Si el cambio es posible, mostrar el estado y el desglose de las denominaciones de cambio
    resultado.textContent = `Status: ${resultadoCambio.status} ${resultadoCambio.change.join(", ")}`;
  }
};

// Función para calcular el cambio
const calcularCambio = (changeRequired) => {
  let cambio = []; // Aquí se almacenarán las denominaciones de cambio
  let change = parseFloat(changeRequired); // Convertimos el cambio necesario en un número

  // Calcular el total de dinero en el fondo de caja
  let totalEnCaja = cid.reduce((sum, [denom, amount]) => sum + amount, 0).toFixed(2);

  // Si el cambio necesario es mayor que lo que hay en la caja, no se puede dar el cambio
  if (change > totalEnCaja) {
    return { status: "INSUFFICIENT_FUNDS", change: [] };
  }

  // Iterar sobre las denominaciones en orden descendente (de mayor a menor)
  for (let i = cid.length - 1; i >= 0; i--) {
    let [denom, amount] = cid[i]; // Obtener el nombre y la cantidad de cada denominación
    let value = denominaciones[denom]; // Obtener el valor en dólares de la denominación
    let cantidadDeDenom = 0; // Contador para la cantidad de esa denominación que se va a usar

    // Mientras el cambio restante sea mayor o igual al valor de la moneda y haya suficiente cantidad en la caja
    while (change >= value && amount > 0) {
      change -= value; // Restamos el valor de la denominación al cambio
      change = parseFloat(change.toFixed(2)); // Redondeamos para evitar problemas de precisión
      amount -= value; // Restamos la cantidad disponible de la denominación
      cantidadDeDenom += value; // Sumamos el valor de la denominación utilizada
    }

    // Si hemos usado alguna cantidad de esa denominación, la añadimos al cambio
    if (cantidadDeDenom > 0) {
      cambio.push(`${denom}: $${cantidadDeDenom.toFixed(2)}`);
    }
  }

  // Si después de procesar todas las denominaciones aún queda cambio por devolver, significa que no se puede dar el cambio
  if (change > 0) {
    return { status: "INSUFFICIENT_FUNDS", change: [] };
  }

  // Si hemos devuelto todo el cambio correctamente, devolvemos el estado "OPEN" y el desglose del cambio
  return { status: "OPEN", change: cambio };
};

// Asignar un evento al botón de compra para que ejecute la función comprar cuando se haga clic
btnCompra.addEventListener("click", comprar);

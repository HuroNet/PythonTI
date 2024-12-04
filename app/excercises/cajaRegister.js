const entrada = document.getElementById("cash");
const btnCompra = document.getElementById("purchase-btn");
const resultado = document.getElementById("change-due");

// Precio del producto
let price = 19.5;

// Fondo de caja
let cid = [
  ['PENNY', 1.01],
  ['NICKEL', 2.05],
  ['DIME', 3.1],
  ['QUARTER', 4.25],
  ['ONE', 90],
  ['FIVE', 55],
  ['TEN', 20],
  ['TWENTY', 60],
  ['ONE HUNDRED', 100]
];

// Denominaciones
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

// Función principal para manejar la compra
const comprar = () => {
  const cash = parseFloat(entrada.value.trim());
  const changeRequired = (cash - price).toFixed(2); // Cambio necesario

  if (changeRequired < 0) {
    alert("Customer does not have enough money to purchase the item.");
    return;
  }

  if (changeRequired === "0.00") {
    resultado.textContent = "No change due - customer paid with exact cash.";
    return;
  }

  // Calcular cambio
  const resultadoCambio = calcularCambio(changeRequired);

  if (resultadoCambio.status === "INSUFFICIENT_FUNDS") {
    resultado.textContent = "Status: INSUFFICIENT_FUNDS";
  } else {
    resultado.textContent = `Status: ${resultadoCambio.status} ${resultadoCambio.change.join(", ")}`;
  }
};

// Función para calcular el cambio
const calcularCambio = (changeRequired) => {
  let cambio = [];
  let change = parseFloat(changeRequired); // Cambio necesario como número
  let totalEnCaja = cid.reduce((sum, [denom, amount]) => sum + amount, 0).toFixed(2);

  if (change > totalEnCaja) {
    return { status: "INSUFFICIENT_FUNDS", change: [] };
  }

  for (let i = cid.length - 1; i >= 0; i--) {
    let [denom, amount] = cid[i];
    let value = denominaciones[denom];
    let cantidadDeDenom = 0;

    while (change >= value && amount > 0) {
      change -= value;
      change = parseFloat(change.toFixed(2)); // Evitar problemas con decimales
      amount -= value;
      cantidadDeDenom += value;
    }

    if (cantidadDeDenom > 0) {
      cambio.push(`${denom}: $${cantidadDeDenom.toFixed(2)}`);
    }
  }

  if (change > 0) {
    return { status: "INSUFFICIENT_FUNDS", change: [] };
  }

  return { status: "OPEN", change: cambio };
};

// Asignar evento al botón de compra
btnCompra.addEventListener("click", comprar);

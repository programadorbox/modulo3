// Validador de tarjetas de crédito con Node.js

const readline = require('readline');

// Crear interfaz para leer input desde la consola
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Función de Luhn
function luhnCheck(cardNum) {
  const digits = cardNum.split('').reverse().map(Number);

  for (let i = 1; i < digits.length; i += 2) {
    digits[i] *= 2;
    if (digits[i] > 9) {
      digits[i] -= 9;
    }
  }

  const totalSum = digits.reduce((acc, val) => acc + val, 0);
  return totalSum % 10 === 0;
}

// Preguntar al usuario
rl.question('Ingresa el número de tarjeta para verificar: ', (cardNum) => {
  if (luhnCheck(cardNum)) {
    console.log('✅ El número ES válido (pasa el algoritmo de Luhn).');
  } else {
    console.log('❌ El número NO es válido (no pasa el algoritmo de Luhn).');
  }
  rl.close();
});

//node luhn.js
// hay que tener instalado node para hacerlo correr

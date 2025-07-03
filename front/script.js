// Algoritmo de Luhn en JS para navegador

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

// Manejar click del botón
document.getElementById('validateBtn').addEventListener('click', () => {
  const cardNum = document.getElementById('cardNumber').value.trim();
  const result = document.getElementById('result');

  if (cardNum === '') {
    result.textContent = 'Por favor ingresa un número.';
    result.style.color = 'orange';
    return;
  }

  if (!/^\d+$/.test(cardNum)) {
    result.textContent = 'Solo se permiten números.';
    result.style.color = 'red';
    return;
  }

  if (luhnCheck(cardNum)) {
    result.textContent = '✅ Número válido (pasa Luhn).';
    result.style.color = 'green';
  } else {
    result.textContent = '❌ Número inválido (no pasa Luhn).';
    result.style.color = 'red';
  }
});

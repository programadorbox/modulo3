# validador de tarjetas de credito
# invertir el orden de los numeros, despues se multiplica por 2 cada segundo digito, desde el primero
#si dan 2 digitos se suman esos digitos, si la suma es redondeada es que es valida 
def luhn_check(card_num):
    digits = [int(x) for x in str(card_num)][::-1]
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    total_sum = sum(digits)
    return total_sum % 10 == 0

# Versión interactiva
card_input = input("Ingresa el número de tarjeta para verificar: ")

if luhn_check(card_input):
    print("✅ El número ES válido (pasa el algoritmo de Luhn).")
else:
    print("❌ El número NO es válido (no pasa el algoritmo de Luhn).")

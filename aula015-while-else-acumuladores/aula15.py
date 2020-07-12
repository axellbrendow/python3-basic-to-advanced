"""
while / else
* Contadores
* Acumuladores
"""

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador += contador
    contador += 1

else:  # Só cai no else se a condição do looping der False alguma vez.
    print('Cheguei no else.')

print('Final')

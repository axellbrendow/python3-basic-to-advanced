"""
While
Utilizado para realizar ações enquanto
uma condição for verdadeira.

Requisitos: Entender condições e operadores.
"""

x = 0

while x < 5:
    print(x)
    x += 1

print('Acabou !')

#############

x = 0

while x < 5:
    if x == 3:
        x += 1
        continue  # Se x é 3, incrementa-o e volta à condição do while

    print(x)
    x += 1

print('Acabou !')

#############

x = 0

while x < 5:
    if x == 3:
        x += 1
        break  # Se x é 3, incrementa-o e sai condição do while

    print(x)
    x += 1

print('Acabou !')

#############

x = 0
y = 0

while x < 10:
    y = 0

    while y < 5:
        print(f'({x}, {y})')
        y += 1

    x += 1

print('Acabou !')

#############

while True:
    print()

    num1 = input('Informe o 1º número: ')
    num2 = input('Informe o 2º número: ')
    operador = input('Informe o operador: ')
    resultado = None

    if not num1.isnumeric() or not num2.isnumeric():
        print('Informe números inteiros')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        resultado = num1 + num2

    elif operador == '-':
        resultado = num1 - num2

    elif operador == '*':
        resultado = num1 * num2

    elif operador == '/':
        resultado = num1 / num2

    else:
        print('Operador inválido')

    if resultado:
        print(f'{num1} {operador} {num2} = {resultado}')

    if input('Deseja sair ? [s]im ou [n]ão: ') == 's':
        break

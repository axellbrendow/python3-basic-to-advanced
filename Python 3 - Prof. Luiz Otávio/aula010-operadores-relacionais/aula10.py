"""
Operadores relacionais
== > >= < <= !=
"""

value1 = 2
value2 = '2'
value3 = (value1 == value2)  # False

print(value3)

value2 = 2
value3 = (value1 > value2)
print(value3)

value3 = (value1 >= value2)
print(value3)

value3 = (value1 < value2)
print(value3)

value3 = (value1 <= value2)
print(value3)

value3 = (value1 != value2)
print(value3)

nome = input('Qual é o seu nome ? ')
idade = int(input('Qual a sua idade ? '))

idade_menor = 20
idade_maior = 30

if idade_menor <= idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')

else:
    print(f'{nome} NÃO pode pegar o empréstimo.')
    print(f'Idade mínima: {idade_menor}.')
    print(f'Idade máxima: {idade_maior}.')

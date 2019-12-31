"""
Entrada de dados
"""

# A função input sempre retorna strings
nome = input('Qual é o seu nome ? ')
idade = input('Qual é a sua idade ? ')

ano_nascimento = 2019 - int(idade)

print()
print(f'O usuário digitou {nome} e o tipo da variável é {type(nome)}')
print(f'{nome} tem {idade} anos. {nome} nasceu em {ano_nascimento}.')

# Calculadora que faz soma
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

print(num1 + num2)

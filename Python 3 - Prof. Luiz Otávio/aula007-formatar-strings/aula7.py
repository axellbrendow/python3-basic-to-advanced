"""
Breve introdução à formatação de strings
"""

nome = 'Luiz'
idade = 32
altura = 1.80
maior_de_idade = idade > 18
peso = 80
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos de idade e seu imc é: {imc:.2f}')
print('{2} {0} {0} tem {1} anos e seu imc é: {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos e seu imc é: {im:.2f}'.format(n=nome, i=idade, im=imc))

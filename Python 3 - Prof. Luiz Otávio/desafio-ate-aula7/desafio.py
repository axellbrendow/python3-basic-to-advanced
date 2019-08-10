"""
* Criar variáveis para nome (str), idade (int), altura (float) e
peso (float) de uma pessoa.
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Luiz'
idade = 32
altura = 1.8
peso = 80
ano_atual = 2019
ano_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nascimento}.')

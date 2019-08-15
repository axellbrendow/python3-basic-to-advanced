"""
Filter - Percorre os elementos de um iterável, cria cópias deles e aplica uma
função que decide se o elemento deve ou não ir para a nova coleção.
"""

from dados import carrinho, pessoas, lista

print('lista')
print(lista)

# O map cria cópias dos elementos e aplica a lambda nelas
nova_lista = list(filter(lambda item: item > 5, lista))
print(nova_lista)

nova_lista = [item for item in lista if item > 5]
print(nova_lista)

print('\ndicionario produtos')

for produto in carrinho:
    print(produto)

print('\npegando preços')

precos = list(filter(lambda produto: produto['preco'] > 70, carrinho))
print(precos)

print('\ndicionario pessoas')

for pessoa in pessoas:
    print(pessoa)

print('\nfiltrando idades')

def filtrar_idade(pessoa):
    return pessoa['idade'] < 18

novas_pessoas = list(filter(filtrar_idade, pessoas))

for pessoa in pessoas:
    print(pessoa)
print('######')
for pessoa in novas_pessoas:
    print(pessoa)

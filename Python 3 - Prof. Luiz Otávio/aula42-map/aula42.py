"""
Map - Percorre os elementos de um iterável, cria cópias deles e aplica uma função.
"""

from dados import carrinho, pessoas, lista

print('lista')
print(lista)

# O map cria cópias dos elementos e aplica a lambda nelas
nova_lista = list(map(lambda item: item * 2, lista))
print(nova_lista)

nova_lista = [item * 2 for item in lista]
print(nova_lista)

print('\ndicionario produtos')

for produto in carrinho:
    print(produto)

print('\npegando preços')

precos = list(map(lambda produto: produto['preco'], carrinho))
print(precos)

print('\naumentando preços')

def aumentar_preco(produto):
    produto['preco'] = round(produto['preco'] * 1.05, 2)
    return produto

novo_carrinho = map(aumentar_preco, carrinho)

for produto in novo_carrinho:
    print(produto)

print('\ndicionario pessoas')

for pessoa in pessoas:
    print(pessoa)

print('\naumentando idades')

def aumentar_idade(pessoa):
    pessoa['nova_idade'] = round(pessoa['idade'] * 1.05, 2)
    return pessoa

novas_pessoas = map(aumentar_idade, pessoas)

for pessoa in pessoas:
    print(pessoa)
print('######')
for pessoa in novas_pessoas:
    print(pessoa)

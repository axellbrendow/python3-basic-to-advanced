"""
Reduce(lambda valor_acumulado, item_atual: novo_valor_acumulado, iterable, valor_inicial)
- Consome os itens de um iterável executando uma função sobre eles que recebe dois
parâmetros: valor_acumulado que é o último valor retornado por essa função e item_atual
que é o item atual do iterável. Ela deve retornar o novo_valor_acumulado.
"""

from dados import carrinho, pessoas, lista
from functools import reduce

print('lista')
print(lista)

print('somando lista')
soma_list = reduce(lambda acumulado, item_atual: acumulado + item_atual, lista, 0)
print(soma_list)

print('\ndicionario produtos')

for produto in carrinho:
    print(produto)

print('\nsomando preços')

precos = reduce(lambda acumulado, produto: acumulado + produto['preco'], carrinho, 0)
print(precos)

print('\ndicionario pessoas')

for pessoa in pessoas:
    print(pessoa)

print('\nsomando idades')

def somar_idade(acumulado, pessoa):
    return acumulado + pessoa['idade']

media = reduce(somar_idade, pessoas, 0) / len(pessoas)
print(media)

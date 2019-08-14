"""
Geradores, Iteradores e Iteráveis
"""

import sys
import time

lista = list(range(10))
lista = iter(lista)  # Transforma a lista num iterador

# Iteradores têm o método __next__
print(hasattr(lista, '__next__'))

print('Itera sobre o iterador da lista')
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

print('Tamanho em bytes da lista')
print(sys.getsizeof(lista))

print('Inicia geradores')

def gerar():
    listagerar = []

    for n in range(50):
        listagerar.append(n)
        time.sleep(0.1)  # Simulando uma função com alto custo

    return listagerar

listagerada = gerar()

for value in listagerada:
    print(value)

print('Criando uma função geradora')

def gerar():
    for n in range(50):
        yield n
        time.sleep(0.1)  # Simulando uma função com alto custo

gerador = gerar()

for value in gerador:
    print(value)

print(hasattr(gerador, '__iter__'))  # É iterável
print(hasattr(gerador, '__next__'))  # É iterador

lista2   = [x for x in range(1000)]
gerador2 = (x for x in range(1000))  # Criando um gerador
print(type(lista2))
print(type(gerador2))
print(sys.getsizeof(lista2))
print(sys.getsizeof(gerador2))

"""
Expressões lambda - Funções anônimas
"""

def funcao(arg, arg2):
    return arg * arg2

print(funcao(2, 3))

anonima = lambda x, y: x * y

print(anonima(2, 3))

print('#######################')

lista = [
    ['p1', 13],
    ['p2', 6],
    ['p3', 7],
    ['p4', 50],
    ['p5', 8],
]

copia = [ *lista ]

# Recebe o item da lista e retorna a 2ª chave dele que é um valor comparável
def func(item):
    return item[1]

# Usar a função sorted caso a lista original deva ficar intacta
lista.sort(key=func)
copia.sort(key=lambda item: item[1])

print(lista)
print(copia)

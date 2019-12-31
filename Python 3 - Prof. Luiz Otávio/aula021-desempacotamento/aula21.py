"""
Desempacotamento de listas
"""

lista = ['Luiz', 'João', 'Maria', 'a', 'b', 'c']

n1, n2, *outra_lista, ultimo_valor = lista

print(n1, n2, outra_lista, ultimo_valor)

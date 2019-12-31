"""
Tuplas
"""

tupla1 = (1, 2, 3, 'a', 'Luiz Otávio')
tupla2 = 1, 2, 'a', 'b'
tupla3 = 1,  # Tupla de uma elemento precisa ter a vírgula
tupla4 = tupla1 + tupla2
tupla5 = tupla3 * 10
lista1 = list(tupla5)
lista1[0] = 0

v1, v2, v3, *_, last = tupla4

print(tupla1[2:])
print(tupla2)
print(tupla3)
print(tupla4)
print(f'\nv1 = {v1}\nv2 = {v2}\nv3 = {v3}\n_ = {_}\nlast = {last}')
print(tupla5)
print(lista1)
print(tuple(lista1))

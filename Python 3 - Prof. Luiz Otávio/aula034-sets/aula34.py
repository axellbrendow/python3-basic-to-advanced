"""
Sets - Conjuntos

add, update, clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (União menos interseção)
"""

s1 = { 1, 2, 3, 4, 5 }

for v in s1:
    print(v)

s1.add(6)
print(s1)

s1.discard(4)
print(s1)

s1.update('Python')  # update itera sobre o parâmetro. Strings são iteráveis.
print(s1)

print('\nRemovendo elementos repetidos')
l1 = [1, 2, 1, 3, 4, 5, 6, 6, 6, 6, 6, 6, 6, 'Luiz', 'Luiz']
print(l1)
l1 = set(l1)
print('Convertendo para set')
print(l1)

print('\nUnião')
print(s1)
print(l1)
print(s1 | l1)

print('\nInterseção')
print(s1)
print(l1)
print(s1 & l1)

print('\nDiferença (apenas elementos do primeiro set)')
print(s1)
print(l1)
print(s1 - l1)

print('\nOu-exclusivo (união - interseção)')
print(s1)
print(l1)
print(s1 ^ l1)

"""
Combinations, Permutations, Product
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""

from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

print('Combinações:')
for group in combinations(pessoas, 2):  # Combina em grupos de 2 elementos
    print(group)

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

print('\nPermutações:')
for group in permutations(pessoas, 2):  # Combina em grupos de 2 elementos
    print(group)

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

print('\nPermutações com repetição:')
for group in product(pessoas, repeat=2):  # Combina em grupos de 2 elementos
    print(group)

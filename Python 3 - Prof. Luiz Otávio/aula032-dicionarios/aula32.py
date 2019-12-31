"""
Dicionários - { chave: valor }
"""

import copy

print('\nCriando dicionários e alterando chaves e valores...')
dicionario1 = {'chave1': 'valor da chave'}
print(dicionario1)

dicionario1['chave2'] = 'valor da nova chave'
print(dicionario1)
print(dicionario1['chave2'])

# Outra forma de criar dicionário
dicionario2 = dict(chave1='valor da chave', chave2='valor da nova chave')
print(dicionario2)

print('\nCriando chaves de diferentes tipos e acessando/atualizando valores...')
# Dicionários aceitam qualquer tipo de dado imutável como chave
dicionario3 = {
    'str': [ 'valor', 'valor2' ],
    123: 'outro valor',
    (1, 2, 3, 4): 'tupla'
}

print(dicionario3)

# Checa se o dicionário tem a tupla como chave
if (1, 2, 3, 4) in dicionario3:
    print( dicionario3[(1, 2, 3, 4)] )

print(dicionario3)
dicionario3.update( { (1, 2, 3, 4): 'tupla-update' } )
print(dicionario3)
print('\ntupla-update' in dicionario3.keys())  # Acessar os valores do dicionário
print('\ntupla-update' in dicionario3.values())  # Acessar os valores do dicionário

# Iterando sobre o dicionário
print('\nIterando sobre as chaves do dicionário...')
for key in dicionario3:
    print(key)
    
print('\nIterando sobre os valores do dicionário...')
for value in dicionario3.values():
    print(value)
    
print('\nIterando sobre as chaves e os valores do dicionário...')
for key, value in dicionario3.items():
    print(key, value)

# Usar a função .copy() para fazer uma shallow copy (cópia rasa) do dicionário
print('\nFazendo uma cópia rasa do dicionário 3')
dicionario4 = dicionario3.copy()
dicionario4[123] = 'outro valor4'
dicionario4['str'][0] = 'valor-str'

print(dicionario3)
print(dicionario4)

# Usar a função deepcopy() do módulo copy para fazer uma deep copy (cópia profunda)
print('\nFazendo uma cópia profunda do dicionário 3')
dicionario4 = copy.deepcopy(dicionario3)
dicionario4['str'][0] = 'valor----'

print(dicionario3)
print(dicionario4)

# Conversão de listas e tuplas em dicionários
print('\nConvertendo listas e tuplas em dicionários')

lista = [
    ['p1', 13],
    ['p2', 6],
    ['p3', 7],
    ['p4', 50],
    ['p5', 8],
]

print(lista)
print(dict(lista))

# Removendo pares de um dicionário
print('\nRemovendo pares de um dicionário')

dicionario5 = dict(lista)
print(dicionario5)

dicionario5.pop('p4')
print(dicionario5)
dicionario5.popitem()
print(dicionario5)

# Concatenando dicionários
print('\nConcatenando dicionários')

dicionario6 = {
    'novachave1': 'nc1',
    'novachave2': 'nc2',
}

print(dicionario6)

dicionario5.update(dicionario6)
print(dicionario5)

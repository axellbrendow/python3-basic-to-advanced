import os

filename = 'abc.txt'
file = open(filename, 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

# 2º parâmetro (whence = de onde) 0 - inicio, 1 - atual, 2 - fim
file.seek(0, 0)
print('Lendo o arquivo inteiro')
print(file.read())

file.seek(0, 0)
print('Lendo linha a linha')

print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')

file.seek(0, 0)
print('\nLendo todas as linhas para uma lista')
print(file.readlines())

file.close()

print('\n############################\n')

# Usando gerenciadores de contexto.
# Ele já fecha o arquivo no final da execução e também cuida de exceções.
with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')
    file.seek(0, 0)
    print(file.read())

os.remove(filename)

import json

pessoas = [{'nome': 'Luiz'      , 'idade': 12},
           {'nome': 'André'     , 'idade': 43},
           {'nome': 'Eduardo'   , 'idade': 65},
           {'nome': 'Letícia'   , 'idade': 14},
           {'nome': 'Fabrício'  , 'idade': 17},
           {'nome': 'Rose'      , 'idade': 19},
           {'nome': 'Joana'     , 'idade': 25},
           {'nome': 'Júlia'     , 'idade': 32},
           {'nome': 'Felipe'    , 'idade': 23},
           {'nome': 'Lucas'     , 'idade': 59},]

with open(filename, 'w+') as file:
    file.write(json.dumps(pessoas, indent=True))
    file.seek(0, 0)
    pessoas_json = file.read()
    pessoas = json.loads(pessoas_json)
    print([pessoa for pessoa in pessoas if pessoa['idade'] >= 59])

os.remove(filename)

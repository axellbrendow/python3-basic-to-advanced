"""
Groupby

Agrupa elementos de acordo com propriedades comuns.
É obrigatório que o conjunto esteja ordenado pela propriedade escolhida.
"""

from itertools import groupby

alunos = [
    {'nome': 'Luiz'     , 'nota': 'A'},
    {'nome': 'Letícia'  , 'nota': 'B'},
    {'nome': 'Fabrício' , 'nota': 'A'},
    {'nome': 'Rosemary' , 'nota': 'C'},
    {'nome': 'Joana'    , 'nota': 'D'},
    {'nome': 'João'     , 'nota': 'A'},
    {'nome': 'Eduardo'  , 'nota': 'B'},
    {'nome': 'André'    , 'nota': 'A'},
    {'nome': 'Anderson' , 'nota': 'C'},
    {'nome': 'José'     , 'nota': 'B'},
]

nota = lambda aluno: aluno['nota']

print('Ordena por nota')
alunos.sort(key=nota)

for aluno in alunos:
    print(aluno)

print('\nAgrupa por nota')
alunos_agrupados = groupby(alunos, nota)  # Notas devem estar ordenadas !!
lista_aluno = list()

for nota, grupo in alunos_agrupados:
    print(f'Nota: {nota}, grupo:')
    lista_aluno = list(grupo)

    for aluno in lista_aluno:
        print(f'\t{aluno}')

    print(f'\tQuantidade de alunos: {len(lista_aluno)}\n')

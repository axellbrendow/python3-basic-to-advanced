"""
zip e zip_longest - unindo iteráveis

zip e zip_longest unem dois conjuntos iteráveis em uma tupla e retornam um
iterador preguiçoso sobre as tuplas.
"""

from itertools import zip_longest, count

indice = count()  # Cria um iterador sobre numeros infinitos
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']
# cidades_estados_zip = zip(cidades, estados)  # Joga fora 'Monte Belo'

# Não joga fora 'Monte Belo', completa o array de estados com fillvalue=None
# Como o iterador count() é infinito, zip_longest irá ficar em looping infinito
# ao ser iterado
cidades_estados_zip_longest = zip_longest(
    indice,
    cidades,
    estados,
    fillvalue='Estado'
)

for valor in cidades_estados_zip_longest:
    print(valor)

# print(cidades)
# print(estados)
# print(list(cidades_estados_zip))
# print(list(cidades_estados_zip_longest))

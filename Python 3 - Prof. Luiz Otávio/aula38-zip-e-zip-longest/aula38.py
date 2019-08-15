"""
zip e zip_longest - unindo iteráveis
"""

from itertools import zip_longest, count

indice = count()  # Cria um gerador de numeros
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']
#cidades_estados_zip = zip(cidades, estados)  # Joga fora 'Monte Belo'
# Não joga fora 'Monte Belo', completa o array de estados com fillvalue=None
cidades_estados_zip_longest = zip_longest(
    indice,
    cidades,
    estados,
    fillvalue='Estado'
)

for indice, estado, cidade in cidades_estados_zip_longest:
    print(indice, estado, cidade)

#print(cidades)
#print(estados)
#print(list(cidades_estados_zip))
#print(list(cidades_estados_zip_longest))

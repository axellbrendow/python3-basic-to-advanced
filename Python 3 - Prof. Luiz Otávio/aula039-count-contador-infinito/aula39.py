"""
count - itertools
"""

from types import GeneratorType

variavel = zip('Alo', 'Alo')

# Geradores são instâncias de GeneratorType
print(isinstance(variavel, GeneratorType))

variavel = (x for x in zip('Alo', 'Alo'))

# Geradores são instâncias de GeneratorType
print(isinstance(variavel, GeneratorType))

from itertools import count

contador = count(start=9, step=-0.05)

for valor in contador:
    print(round(valor, 2))  # round arredonda para 2 casas decimais

    if valor >= 10 or valor <= -10:
        break  # Forma de parar um iterador

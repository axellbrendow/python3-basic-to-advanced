# Mutabilidade de alguns tipos:
# Mutável: listas, dicionários
# Imutável: tuplas, strings, números, booleanos, None


def juntar(clientes, clientes_acumulados=[]):
    clientes_acumulados.extend(clientes)

    return clientes_acumulados


clientes1 = juntar(['A', 'B', 'C'])
clientes2 = juntar(['D', 'E'])
clientes3 = juntar(['F'])

print(clientes1)
print(clientes2)
print(clientes3)
# Todas as variáveis apontam para a mesma lista porque o interpretador do Python
# só avalia uma única vez o cabeçalho da função juntar(), aí ele cria apenas uma
# vez a lista vazia do parâmetro clientes_acumulados. Como esse parâmetro é
# retornado, todos esses retornos são a mesma lista.

print('\nTratando o problema\n')

# A forma de contornar o problema é dar um valor padrão que seja imutável e
# tratar isso dentro do código da função.


def juntar(clientes, clientes_acumulados=None):
    if clientes_acumulados is None:
        clientes_acumulados = []

    clientes_acumulados.extend(clientes)

    return clientes_acumulados


clientes1 = juntar(['A', 'B', 'C'])
clientes2 = juntar(['D', 'E'], ['Z', 'W'])
clientes3 = juntar(['F'])

print(clientes1)
print(clientes2)
print(clientes3)

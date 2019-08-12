"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
"""

def funcao1(funcao):
    return funcao()

def funcao2():
    return 11 * 3

print(funcao1(funcao2))

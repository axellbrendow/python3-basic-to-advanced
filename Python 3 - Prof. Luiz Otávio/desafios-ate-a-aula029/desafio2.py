"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2
executada. Faça a função1 executar duas funções que recebam um número diferente de
argumentos.
"""

def funcao1(funcao_1, funcao_2):
    return funcao_1(1, 2, 3, 4, multiplicador = 2) + funcao_2(9, 8, 7, 6, multiplicador = -2)

# O * desempacota listas, já o ** desempacota dicionários
def funcao_1(*args, **kwargs):
    sum = 0
    print(f'sum = {sum}')

    for i in range(0, len(args), 2):
        sum += args[i] + args[i + 1]
        print(f'args[{i}] + args[{i + 1}] = {args[i]} + {args[i + 1]}, sum = {sum}')
    
    multiplicador = kwargs['multiplicador']
    ret_value = sum * multiplicador

    print(f'multiplicador = {multiplicador}, return = {ret_value}')

    return ret_value

def funcao_2(*args, **kwargs):
    sum = 0
    print(f'sum = {sum}')

    for i in range(0, len(args), 2):
        sum += args[i] - args[i + 1]
        print(f'args[{i}] - args[{i + 1}] = {args[i]} - {args[i + 1]}, sum = {sum}')
    
    multiplicador = kwargs['multiplicador']
    ret_value = sum * multiplicador

    print(f'multiplicador = {multiplicador}, return = {ret_value}')

    return ret_value

print('soma =', funcao1(funcao_1, funcao_2))

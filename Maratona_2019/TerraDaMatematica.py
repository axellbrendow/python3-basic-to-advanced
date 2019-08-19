# x != 0, y != 0, x >= y
# (x + y) * y = p
#   x * y + y * y = p (I)
#
# |x - y| * x = q:
#   x * x - y * x = q (II) ou
#   -x * x + y * x = q (III)
#
# Somando (I) e (II):
#   x * x + y * y = p + q, como x * x + y * y > 0, p + q > 0  ->  p > -q
#
# Subtraindo (III) de (I):
#   x * x + y * y = p - q, como x * x + y * y > 0, p - q > 0  ->  p > q
#
# Como x >= y, x - y sempre será positivo, portanto, a equação (III) é inválida.
# Ou seja, é obrigatório que x * x + y * y = p + q
#
# Obs.: dar prioridade às soluções com x menor.

from itertools import combinations
# from functools import reduce
import math


def gerar_quadrados_perfeitos_menores_ou_iguais_a(valor: int):
    valor_base = quadrado_perfeito = 1
    quadrados_perfeitos = []

    while quadrado_perfeito <= valor:
        quadrados_perfeitos.append(quadrado_perfeito)
        valor_base += 1
        quadrado_perfeito = valor_base * valor_base

    return quadrados_perfeitos


numero_de_entradas = int(input())

for i in range(numero_de_entradas):
    print(f'Case {i + 1}:')
    p, q = [int(x) for x in input().split()]

    if p > -q:
        quadrados_perfeitos = gerar_quadrados_perfeitos_menores_ou_iguais_a(p + q)

        # Gera pares ordenados com as supostas raízes da equação ao quadrado
        raizes_a_2 = combinations(quadrados_perfeitos, 2)

        # Pega os pares que solucionam a equação, x² + y² = p + q
        raizes_a_2 = filter(lambda par: par[0] + par[1] == p + q, raizes_a_2)

        # Tira a raiz quadrada dos pares para obter as raízes de fato
        raizes = ( ( int(math.sqrt(x2)), int(math.sqrt(y2)) ) for y2, x2 in raizes_a_2 )

        # raizes_finais = reduce(lambda raizes_atuais, proximas:
        #                        proximas if proximas[2] < raizes_atuais[2] else raizes_atuais,
        #                        raizes)

        try:
            x, y = min(raizes, key=lambda par: par[0])
            print(x, y)

        except:
            print('Impossible.')

    else:
        print('Impossible.')

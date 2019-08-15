from functools import reduce
import math

PI = math.pi


def dobra_lista(lista):
    return [x * 2 for x in lista]


def multiplica(lista):
    return reduce(lambda acumulado, prox_item: acumulado * prox_item, lista, 1)


# Checa se esse arquivo é o que está sendo executado e não importado.
if __name__ == '__main__':
    lista = list(range(1, 6))
    print(lista)
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)

    # Caso o módulo seja importado em outro, __name__ será calculos, senão, será __main__
    print('Nome do módulo:', __name__)

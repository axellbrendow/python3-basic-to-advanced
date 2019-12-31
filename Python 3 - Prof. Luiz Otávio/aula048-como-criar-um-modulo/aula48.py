import calculos

# Caso o módulo seja importado em outro, __name__ será calculos, senão, será __main__
print('Nome do módulo:', __name__)

print(calculos.PI)

lista = [2, 4]
print(calculos.multiplica(lista))

from calculos import multiplica, dobra_lista, PI

print(lista)
print('from calculos import multiplica:', multiplica(lista))
print('from calculos import dobra_lista:', dobra_lista(lista))
print('from calculos import PI:', PI)

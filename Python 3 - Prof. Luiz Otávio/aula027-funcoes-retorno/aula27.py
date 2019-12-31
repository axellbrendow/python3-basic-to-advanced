"""
Funções - def
return
"""

# Funções sem return retornam None


def divisao(num1, num2):

    return num1 / num2 if num2 != 0 else None


resultado = divisao(8, 0)

if resultado:
    print(f'resultado = {resultado}')

else:
    print('Informe um divisor diferente de zero.')

print('#########################')


def f(var):
    print(var)


def dumb():
    return f


var = dumb()
var('Chamando uma função retornada por outra.')

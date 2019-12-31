"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne Fizz. Se ele for
divisível por 5, retorne Buzz. Se o parâmetro da função for divisível por 5 e por 3,
retorne FizzBuzz, caso contrário, retorne o número enviado.
"""

def fizzbuzz(numero):
    resultado = ''

    if numero % 2 == 0:
        resultado = 'Fizz'

    elif numero % 5 == 0:
        resultado = 'Buzz'

        if numero % 3 == 0:
            resultado = 'Fizz' + resultado

    else:
        resultado = numero

    return resultado

print(fizzbuzz(0))
print(fizzbuzz(1))
print(fizzbuzz(15))
print(fizzbuzz(5))

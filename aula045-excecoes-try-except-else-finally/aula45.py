"""
try, except, else, finally
"""

try:
    # print(a)  # NameError
    # list()[0]  # IndexError
    # dict()[0]  # KeyError
    a = 1/0  # ZeroDivisionError

except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')

except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')

except Exception as erro:
    print('Ocorreu um erro inesperado:', type(erro))

else:  # O else só é executado senao houver except, ou seja, se tudo correr bem
    print('Seu código foi executado com sucesso!')
    print(a)

finally:  # O finally sempre é executado
    print('Finalmente')

print('Bora continuar...')

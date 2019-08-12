"""
Escopos local e global
"""

variavel = 'valor'

def func():
    print(variavel)

def func2():
    # Por padrão variáveis referenciadas dentro de uma função são locais
    variavel = 'outro valor'  # variavel é uma variável local da função com o mesmo nome
    print(variavel)

# def func2():
#     global variavel
#     variavel = 'outro valor'
#     print(variavel)

func()
func2()

print(variavel)

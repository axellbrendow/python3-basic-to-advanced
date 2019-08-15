"""
Funções decoradoras recebem uma função como parâmetro e decoram/modificam ela
retornando uma nova a ser usada no lugar.
"""


def decorar(funcao):  # Exemplo de uma função decoradora de funções

    # Geralmente, ao decorar uma função, deseja-se substituí-la por outra.
    # E esta abaixo irá substituir a recebida como parâmetro acima
    def funcao_decorada(*args, **kwargs):
        print('############')
        funcao(*args, **kwargs)
        print('############')

    return funcao_decorada


def printar(valor):
    for i in range(3):
        print(valor)


nova_printar = decorar(printar)
nova_printar(9)


# Forma mais usual de decorar uma função
@decorar
def printar(valor):
    for i in range(3):
        print(valor)


printar(7)

# Criando um decorador para cronometrar o tempo de execução de uma função:
import time

def cronometrar(funcao):

    def nova_funcao(*args, **kwargs):
        start = time.time()
        funcao(*args, **kwargs)
        duracao = (time.time() - start) * 1000

        print(f'A função "{funcao.__name__}" gastou {duracao:.2f}ms.')

    return nova_funcao

@cronometrar
def minhafuncao():
    for i in range(5):
        print(i)
        time.sleep(1)


minhafuncao()
